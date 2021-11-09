import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='logs_exchange', exchange_type='direct')

result = channel.queue_declare(queue='', exclusive=True)

queue_name = result.method.queue

#print("Subscriber queue_name =", queue_name)

severity = ["Error", "Warning", "Info"]

channel.queue_bind(exchange='logs_exchange', queue=queue_name, routing_key="Warning")

print('[*] waiting for the messages')

def callback(ch, method, properties, body):
    print(f'[x] Writing to File:::: {body}')

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()