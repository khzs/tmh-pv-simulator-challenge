from pika import BasicProperties
from tqdm import tqdm
from commonpvs import connection, channel, QUEUE_NAME

if __name__ == '__main__':
    STOP_TIME = 24 * 60 * 60

    for i in tqdm(range(0, STOP_TIME, 5), desc='Sending meter values'):  # every 5 seconds of one full day
        channel.basic_publish(exchange = '',
                              routing_key = QUEUE_NAME,
                              body = f'{i}',
                              properties = BasicProperties(delivery_mode = 2))

    connection.close()
