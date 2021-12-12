import pika, sys, os


def main():

    connection = pika.BlockingConnection(pika.ConnectionParameters(host = "localhost"))
    
    channel = connection.channel()
    
    channel.queue_declare(queue="hello")
    
    # Function which will be linked to the queue to consume the messages.
    def callback(ch, method, properties, body):
        print(f'[x] received {body}')

    # Create the link between the function and the queue
    channel.basic_consume(queue="hello", on_message_callback=callback, auto_ack = True)

    print(" [*] waiting for the messages. To exit press Ctrl-C")

    # Start the process of consuming the messages. It is a loop.
    channel.start_consuming()

# When we have more than one consumer to the same queue,
# the messages will be distributerd in a round-robin manner(to the next)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

