from pika import BlockingConnection, ConnectionParameters

QUEUE_NAME = 'meter'

connection = BlockingConnection(ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue = QUEUE_NAME, auto_delete = True)
