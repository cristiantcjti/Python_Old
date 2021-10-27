import pika

# Create a connection 
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

# Create a channel
channel = connection.channel()

# Create a queue
channel.queue_declare(queue="hello")

# Publish a message
channel.basic_publish(exchange="", routing_key="hello", body="hello_world 2")
print("[x] Sent Hello World")

# Close the connection
connection.close()
