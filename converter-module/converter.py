import os
import pika
import json
import subprocess

# RabbitMQ parameters
RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'localhost')
RABBITMQ_QUEUE = 'video_tasks'

# Message processing function
def callback(ch, method, properties, body):
    task = json.loads(body)
    video_path = task['video_path']
    audio_path = task['audio_path']

    # Convert video to audio
    subprocess.run(['ffmpeg', '-i', video_path, audio_path])
    print(f"Converted {video_path} to {audio_path}")

    ch.basic_ack(delivery_tag=method.delivery_tag)

# Start message consumer
def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST))
    channel = connection.channel()
    channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=RABBITMQ_QUEUE, on_message_callback=callback)
    print(' [*] Waiting for messages...')
    channel.start_consuming()

if __name__ == '__main__':
    main()
