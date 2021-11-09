import pika



def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)

def on_request(ch, method, props, body):

    reply_queue_name = props.reply_to
    corr_id = props.correlation_id
    n = int(body)
    print("called fact(", n, ")")

    response = fact(n)


    ch.basic_publish(exchange='', routing_key=reply_queue_name,
                     properties=pika.BasicProperties(
                         correlation_id= corr_id
                     ),
                     body = str(response)
                     )
    ch.basic_ack(delivery_tag= method.delivery_tag)


########## Main Program #################
connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))

channel = connection.channel()

queue_name = "rpc_server_queue"
result = channel.queue_declare(queue=queue_name,
                               #exclusive=True,
                               durable=True)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=queue_name,
                      on_message_callback=on_request
                      #, auto_ack=True
                     )

print("Awaiting RPC requests")
channel.start_consuming()

