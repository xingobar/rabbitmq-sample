import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672)
)

channel = connection.channel()

channel.queue_declare(queue='task', durable=True)

def callback(ch, method, properties, body):
    print(f"[x] Received {body}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(
    queue='task',
    on_message_callback=callback
)

channel.start_consuming()