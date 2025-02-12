import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672))

channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

tag = channel.basic_consume(
    queue='hello',
    auto_ack=True,
    on_message_callback=callback,
)

print(f"consumer tag: {tag}")

channel.start_consuming()