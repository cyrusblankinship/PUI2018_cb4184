import sys
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib


"""Query the MTA BusTime vehicle monitoring API for locations"""
key = sys.argv[1]
bus = sys.argv[2]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&LineRef=%s" % (key, bus)
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

item = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

print('Bus Line: ', bus)
print('Number of Active Buses: %d' % (len(item)))

for i in item:
    busNum = i['MonitoredVehicleJourney']['VehicleRef'].split('_')[1]
    lat = i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    long = i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    print('Bus %s is at latitude %s and longitude %s' % (busNum, lat, long))
