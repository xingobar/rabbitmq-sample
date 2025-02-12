import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672)
)

channel = connection.channel()

# create queue name with hello
channel.queue_declare(queue='hello')

# publish message to hello queue
channel.basic_publish(
    exchange='',
    routing_key='hello',
    body='Hello World!',
)

connection.close()