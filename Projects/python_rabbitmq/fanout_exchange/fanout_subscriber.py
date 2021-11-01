import pika


# Create a connection say CN
connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))

# Create a channel in CN, say CH
channel = connection.channel()

# Create the exchange (will not affect if exchange is already there)
channel.exchange_declare(exchange='br_exchange', exchange_type='fanout')

# Create the temporary queue, if it does not exist already and associate it with the channel CH exclusively
result = channel.queue_declare(queue='', exclusive=True)

# Bind the queue with the exchange
queue_name = result.method.queue

print("Subscriber queue_name =", queue_name)

# Associate a call-back function with the message queue
channel.queue_bind(exchange='br_exchange', queue=queue_name)

print('[*] waiting for the messages')

def callback(ch, method, properties, body):
    print('[x] %r' %body)

# Parameterize the consume behaviour
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)


# Start consuming the messages
channel.start_consuming()

