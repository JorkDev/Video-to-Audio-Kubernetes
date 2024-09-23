import os
import pika
import json

# RabbitMQ connection parameters
RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'localhost')
RABBITMQ_QUEUE = 'notification_tasks'

def callback(ch, method, properties, body):
    task = json.loads(body)
    user_id = task['user_id']
    message = task['message']
    
    # Notify user (can be extended to email/SMS service)
    print(f"Notification for User {user_id}: {message}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST))
    channel = connection.channel()
    channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=RABBITMQ_QUEUE, on_message_callback=callback)
    print(' [*] Waiting for notification messages...')
    channel.start_consuming()

if __name__ == '__main__':
    main()
