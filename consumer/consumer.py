import pika
import time

time.sleep(35) 

def callback(ch, method, properties, body):
    print(" [x] Received in consumer %r" % body) 

credentials = pika.PlainCredentials('pika', 'pika')
parameters = pika.ConnectionParameters('rabbitmq-service',
                                    5672,
                                    'pika_vhost',
                                    credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_consume('hello', callback)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()