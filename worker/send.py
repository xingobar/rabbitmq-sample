import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672)
)

channel = connection.channel()

channel.queue_declare(queue='task', durable=True)

channel.basic_publish(
    exchange='',
    routing_key='task',
    body='Hello World!',
    properties=pika.BasicProperties(
        delivery_mode=pika.DeliveryMode.Persistent
    )
)

connection.close()