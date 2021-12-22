# Filters the data that has abnormal values (such as humidity > 100%)
# Filters data from 10pm to 7am

import csv
import os

os.chdir('Data/')
with open('data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    with open('data_filtered.csv', 'w') as filtered_file:
        csv_writer = csv.writer(filtered_file)
        header = next(csv_reader)
        csv_writer.writerow(header)
        print(f'Header : {header}')
        for line in csv_reader:
            if float(line[3]) > 100:
                continue
            hour = int(line[1].split(':')[0])
            if hour <= 7 and hour >= 0:
                print(line)
                csv_writer.writerow(line)
            if hour >= 22:
                print(line)
                csv_writer.writerow(line)
    print('Done filtering !')