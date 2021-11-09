import pika
import random
import time


subId = random.randint(1, 100)
print("Subscriber Id = ", subId)


connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='logs_exchange', exchange_type='direct', durable=True)

queue_name = "task_queue"
result = channel.queue_declare(queue=queue_name,
                               # If excluse is true, when the subscriber is down the queue dies 
                               #exclusive=True,
                               # durable=True ensures the queue keeps the configuration
                               durable=True)

severity = ["Error", "Warning", "Info", "Other"]

for s in severity:
    channel.queue_bind(exchange='logs_exchange', queue=queue_name, routing_key=s)

print('[*] waiting for the messages')

def callback(ch, method, properties, body):
    print('[x] Received message:::: %r' %body)
    #randomSleep = random.randint(1, 5)
    randomSleep = 5
    print("Working for ", randomSleep, "seconds")
    while randomSleep > 0:
        print(".", end="")
        time.sleep(1)
        randomSleep -= 1
    print("!")
    #delivery_tag=method.delivery_tag sends back to the queue a confirmation 
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=queue_name,
                      on_message_callback=callback
                      #auto_ack=True
                      )

channel.start_consuming()

