from csv import writer
from random import uniform
from scipy.interpolate import InterpolatedUnivariateSpline

from commonpvs import *

graph_points = [(0, 0),
                (1, 0),
                (2, 0),
                (3, 0),
                (4, 0),
                (6, 0.1),
                (8, 0.4),
                (12, 2.7),
                (14, 3.2),
                (16, 3),
                (20, 0.1),
                (21, 0),
                (22, 0),
                (23, 0),
                (24, 0)
                ]

x = [i[0] * resolution for i in graph_points]  # time converted from hour to timestamp format
y = [i[1] * 1000 for i in graph_points]  # power converted from kW to W
interpolation_function = InterpolatedUnivariateSpline(x, y)


def simulator(timestamp):
    reading = interpolation_function(int(timestamp))
    noise = uniform(-1, 1) * (reading * 0.05)
    return max(0, round(reading + noise, 2))  # cannot generate negative power


def process_data(chan, method, properties, body):
    timestamp, formatted_time, meter_value = str(body)[2:-1].split(',')  # [2:-1] selects b'<.....>'
    meter_value = float(meter_value)
    pvs_value = simulator(timestamp)
    if int(timestamp) % resolution == 0:
        print(timestamp, formatted_time, meter_value, pvs_value)
    with open('output.csv', 'a') as file:
        wr = writer(file, delimiter = ',')
        wr.writerow([timestamp, formatted_time, meter_value,  # these already come formatted from the queue
                     '{:.2f}'.format(pvs_value),
                     '{:.2f}'.format(meter_value + pvs_value),
                     '{:.2f}'.format(meter_value - pvs_value)])


if __name__ == '__main__':
    with open('output.csv', 'w') as file:
        wr = writer(file)
        wr.writerow(['Timestamp', 'Formatted Time', 'Meter Consumption (W)', 'PV Simulator output (W)', 'Sum (W)',
                     'Diff (W)'])

    channel.basic_consume(queue = queue_name,
                          on_message_callback = process_data)
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
        connection.close()
