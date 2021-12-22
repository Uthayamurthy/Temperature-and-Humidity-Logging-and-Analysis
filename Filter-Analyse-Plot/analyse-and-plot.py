from collections import Counter, OrderedDict
from matplotlib import pyplot as plt
import csv
import os

os.chdir('Data/')
def gen_analysis(): # Conducts a general analysis of data.
    with open('data_filtered.csv', 'r') as data_file:
        csv_reader = csv.reader(data_file)
        next(csv_reader)
        temp_counter = Counter()
        hum_counter = Counter()
        temp_list = []
        hum_list = []
        for line in csv_reader:
            temp_list.append(float(line[2]))
            hum_list.append(float(line[3]))
    temp_counter.update(temp_list)
    hum_counter.update(hum_list)
    print(f'Temperature Counter : \n {temp_counter.most_common(10)}')
    print(f'Humidity Counter : \n {hum_counter.most_common(10)}')
    print('-'*25)
    print(f'Average Temperature : {sum(temp_list)/len(temp_list)}')
    print(f'Average Humidity : {sum(hum_list)/len(hum_list)}')
    print('-'*25)
    print(f'Maximum Temperature : {max(temp_list)}')
    print(f'Minimum Temperature : {min(temp_list)}')
    print(f'Maximum Humidity : {max(hum_list)}')
    print(f'Minimum Humidity : {min(hum_list)}')

def hourly_analysis(): # Conducts a Hourly Analysis of Data
    with open('data_filtered.csv', 'r') as data_file:
        csv_reader = csv.reader(data_file)
        next(csv_reader)
        hourly_readings_temp = OrderedDict()
        hourly_readings_hum = OrderedDict()
        hour_list = []
        for line in csv_reader:
            hour = line[1].split(':')[0]
            if hour not in hour_list:
                hour_list.append(hour)

            # Sort the temperature according to hour
            if hour not in hourly_readings_temp:
                hourly_readings_temp[hour] = [float(line[2])]
            else:
                hourly_readings_temp[hour].append(float(line[2]))

            # Sort the humidity according to hour
            if hour not in hourly_readings_hum:
                hourly_readings_hum[hour] = [float(line[3])]
            else:
                hourly_readings_hum[hour].append(float(line[3]))
        # Calulate Average Hourly Temperature and Humidity.
        hourly_avg_temp = OrderedDict()
        hourly_avg_hum = OrderedDict()
        for hour in hour_list:
            hourly_avg_temp[hour] = round(sum(hourly_readings_temp[hour])/len(hourly_readings_temp[hour]), 2)
            hourly_avg_hum[hour] = round(sum(hourly_readings_hum[hour])/len(hourly_readings_hum[hour]), 2)
        return hourly_avg_temp, hourly_avg_hum

def plot_avg_temp(temp):
    plt.style.use('ggplot')
    
    hour_x = temp.keys()
    temp_y = temp.values()

    plt.plot(hour_x, temp_y)

    plt.xlabel('Time(in 24:hrs)')
    plt.ylabel('Temperature (in *C)')
    plt.title('Average Hourly Tempearature from 21/12/21 (10pm) to 22/12/21 (7am)')

    plt.tight_layout()
    plt.show()


def plot_avg_hum(hum):
    plt.style.use('ggplot')
    
    hour_x = hum.keys()
    hum_y = hum.values()

    plt.plot(hour_x, hum_y)

    plt.xlabel('Time(in 24:hrs)')
    plt.ylabel('Humidity (%)')
    plt.title('Average Hourly Humidity from 21/12/21 (10pm) to 22/12/21 (7am)')

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    gen_analysis()
    temp, hum = hourly_analysis()
    # Run any one of following to plot the graph.
    # Plots Average Hourly Temperature Graph
    plot_avg_temp(temp)
    # Plots Average Hourly Humidity Graph
    # plot_avg_temp(hum)
