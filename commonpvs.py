import pika

QUEUE_NAME = 'meter'

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue = QUEUE_NAME, auto_delete = True)
