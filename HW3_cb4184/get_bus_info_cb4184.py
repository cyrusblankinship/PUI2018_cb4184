from __future__ import print_function
import sys
import json
import csv
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

if not len(sys.argv) == 4:
    print("Invalid number of arguments. Run as: python  get_bus_info_cb4184.py <APIKEY> <BUSNAME> <BUSNAME>.csv")
    sys.exit()

"""Query the MTA BusTime vehicle monitoring API for locations"""
key = sys.argv[1]
bus = sys.argv[2]
busCSV = sys.argv[3]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&LineRef=%s" % (key, bus)
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

item = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

with open(busCSV, 'w', newline='') as csvfile:
    RowWriter = csv.writer(csvfile, delimiter=',')
    RowWriter.writerow(['Latitude', 'Longitude', 'Stop', 'Distance'])
    for i in item:
        lat = i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        long = i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        dist = i['MonitoredVehicleJourney']['MonitoredCall']['Extensions']['Distances']['PresentableDistance']
        stop = i['MonitoredVehicleJourney']['MonitoredCall']['StopPointName']
        RowWriter.writerow([lat, long, stop, dist])