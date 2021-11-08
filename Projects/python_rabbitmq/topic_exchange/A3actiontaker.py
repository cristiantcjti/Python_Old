import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='system_exchange', exchange_type='topic')

result = channel.queue_declare(queue='', exclusive=True)

queue_name = result.method.queue

#print("Subscriber queue_name =", queue_name)

channel.queue_bind(exchange='system_exchange', queue=queue_name, routing_key="#.A3.#")

print('[*] waiting for the messages')

def callback(ch, method, properties, body):
    print(f'[x] :::: {body}')

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()




