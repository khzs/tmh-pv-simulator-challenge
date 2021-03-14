from pika import BasicProperties
from random import uniform
from time import strftime, gmtime
from tqdm import tqdm

from commonpvs import *

if __name__ == '__main__':

    for timestamp in tqdm(range(START_TIME, STOP_TIME, INTERVAL), desc= 'Sending meter values'):
        multiplier = (60 * 60) / RESOLUTION  # gmtime() is optimized to 24 * 60 * 60, hence the multiplier
        formatted_time = strftime("%H:%M:%S", gmtime(timestamp * multiplier))
        consumption = '{:.2f}'.format(uniform(0.0, 9000.0))

        channel.basic_publish(exchange = '',
                              routing_key = QUEUE_NAME,
                              body = f'{timestamp},{formatted_time},{consumption}',
                              properties = BasicProperties(delivery_mode = 2))

    connection.close()
