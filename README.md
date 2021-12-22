# Temperature and Humidity - Logging and Analysis
## Powered by Raspberry pi

> This repo contains code that was quickly written, so it is not optimised.

### Hardware Used -
- Raspberry pi - 3
- DHT-22 [Temperature and Humidity Sensor]

![Harware Image](/Images/hardware.jpg)

### Directory Structure of this Repository -
- **Data** - Contains the Raw as well as Filtered Data
- **Logger** - Contains the program to log temperature every one hour. Must be run in Raspberry Pi.
- **Filter-Analysis-Plot** - Contains Programs to filter, analyse and plot the data. Can be run on pi or your pc.

> Data from only 10pm to 7am are analysed and plotted.

### Final Graph Plots -

- **Temperature Graph -**

![Temperature Plot Image](/Images/avg_temp.png)

- **Humidity Graph -**

![Humidity Plot Image](/Images/avg_hum.png)
