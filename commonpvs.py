from pika import BlockingConnection, ConnectionParameters

START_TIME = 0
RESOLUTION = 60 * 60
STOP_TIME = 24 * RESOLUTION
INTERVAL = 5

QUEUE_NAME = 'meter'

connection = BlockingConnection(ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue = QUEUE_NAME, auto_delete = True)
