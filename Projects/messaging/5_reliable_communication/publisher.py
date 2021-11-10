import pika
import sys
import random

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

# Set a confirmation that the exchange received the message
channel.confirm_delivery()

# durable = True makes sure the exchange won't lose the configurantion when is down
channel.exchange_declare(exchange = 'logs_exchange', exchange_type='direct', durable=True)

severity = ["Error", "Warning", "Info", "Other"]
messages = ["EMsg", "WMsg", "IMsg", "OMsg"]

for i in range(10):
    randomNum = random.randint(0, len(severity)-1)
    message = messages[randomNum]
    rk = severity[randomNum]
    try:
        channel.basic_publish(exchange='logs_exchange',
                              routing_key=rk,
                              body=message,
                              properties=pika.BasicProperties(
                                  delivery_mode=2 # Make Message Persistent
                                  )
                              )
        print("[x] sent %r" %message)
    except pika.exceptions.ChannelClosed:
        print("Channel Closed")
    except pika.exceptions.ConnectionClosed:
        print("Connection Closed")




channel.exchange_delete(exchange='logs_exchange', if_unused=False)

connection.close()





