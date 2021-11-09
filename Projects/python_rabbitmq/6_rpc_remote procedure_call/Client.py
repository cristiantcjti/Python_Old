import pika
import uuid

class FactRPCClient:
    def __init__(self):
        self.connection = \
            pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()

        self.queue_name = 'rpc_client_queue'
        self.server_queue_name = 'rpc_server_queue'
        self.channel.queue_declare(queue=self.queue_name, exclusive=True)


        self.channel.basic_consume(queue=self.queue_name,
                                   on_message_callback= self.on_response,
                                   auto_ack= True)

    def on_response(self, ch, method, props, body):
        if(self.correlation_id == props.correlation_id):
            self.response = body

    def call(self, n):
        self.response = None
        self.correlation_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key=self.server_queue_name,
                                   properties=pika.BasicProperties(
                                       reply_to=self.queue_name,
                                       correlation_id= self.correlation_id,
                                   ),
                                   body=str(n),
                                   )
        while(self.response is None):
            self.connection.process_data_events()
        return(int(self.response))


fact_rpc = FactRPCClient()
print("Check the n! of a number.")
n = input("Insert a number:")
print("Requesting Fact(", n, ")")
response = fact_rpc.call(n)
print("Got the response ", response)