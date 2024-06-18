# Purpose
Connect to Sofar Solar and pull the data in to a database, from where we can run grafana dashboard and more.

## Grafana dashboard
on OSX: 
brew install grafana
  grafana-server --config=/usr/local/etc/grafana/grafana.ini --homepath /usr/local/share/grafana --packaging=brew cfg:default.paths.logs=/usr/local/var/log/grafana cfg:default.paths.data=/usr/local/var/lib/grafana cfg:default.paths.plugins=/usr/local/var/lib/grafana/plugins

grafana run on port 3000 by default
plugin for sqlite:
expects timestamps in seconds since epoch, that works nicely

https://grafana.com/tutorials/install-grafana-on-raspberry-pi/
(inludes instructions of how to set up the pi for headless)
Has adapter for sqlite
grafana-cli plugins install frser-sqlite-datasource
use sudo on the rapsberry pi

find the dashboard
curl http://admin:admin@raspberrypi.local:3000/api/search
dump out the dashboard
curl http://admin:admin@raspberrypi.local:3000/api/dashboards/uid/bc778dee-454c-4dd6-ab8f-bbf4867f2b23 > solar-dashboard.json

### Install on PI
https://grafana.com/tutorials/install-grafana-on-raspberry-pi/

## Use the imager to set ssh and wireless, that worked the first time, vs the file method which never worked
creates firstrun.sh
ssh username: thomasboltze
ssh password: password
ip address: 192.168.188.112

ssh access via key
https://www.raspberrypi.com/documentation/computers/remote-access.html


## Node-red
Graphical environment for doing flow based stuff, not really needed, can just use cron....
OSX: npm install -g node-red
start: node-red
http://127.0.0.1:1880/

PI
sudo systemctl enable nodered.service

## CAN Hat
https://www.waveshare.com/wiki/RS485_CAN_HAT?Amazon
12Mhz version

## Solar calc

## Inverter
Uses ModBus protocal over RS485
pip install minimalmodbus


## Shutting down
sudo shutdown -h now


## sqlite integration
That'll do
sudo apt install sqlite3

## Python version
3.9.2

## Prometheus and node_exporter
wget https://github.com/prometheus/node_exporter/releases/download/v1.6.1/node_exporter-1.6.1.linux-armv7.tar.gz
tar xcvf node_exporter-1.6.1.linux-armv7.tar.gz
sudo cp node_exporter-1.6.1.linux-armv7/node_exporter /usr/local/bin/
sudo useradd -m -s /bin/bash node_exporter
sudo mkdir /var/lib/node_exporter
sudo chown -R node_exporter:node_exporter /var/lib/node_exporter
nano /etc/systemd/system/node_exporter.service
sudo systemctl daemon-reload 
sudo systemctl enable node_exporter.service
sudo systemctl start node_exporter.service

wget https://github.com/prometheus/prometheus/releases/download/v2.47.0-rc.0/prometheus-2.47.0-rc.0.linux-armv7.tar.gz
tar xzvf prometheus-2.47.0-rc.0.linux-armv7.tar.gz
sudo mv prometheus-2.47.0-rc.0.linux-armv7 /opt/prometheus
sudo useradd -m -s /bin/bash prometheus
sudo chown prometheus:prometheus -R /opt/prometheus
sudo systemctl daemon-reload 
sudo systemctl enable prometheus.service
sudo systemctl start prometheus.service

## Weather
weatherapi.com
API Key: 0416816d4ab64e3f9c5134047232308

https://github.com/weatherapicom/python

GET http://api.weatherapi.com/v1/current.json?key=0416816d4ab64e3f9c5134047232308&q=richmond,uk&aqi=no

{
    "location": {
        "name": "Richmond",
        "region": "Richmond upon Thames, Greater London",
        "country": "United Kingdom",
        "lat": 51.46,
        "lon": -0.3,
        "tz_id": "Europe/London",
        "localtime_epoch": 1692798511,
        "localtime": "2023-08-23 14:48"
    },
    "current": {
        "last_updated_epoch": 1692798300,
        "last_updated": "2023-08-23 14:45",
        "temp_c": 26.0,
        "temp_f": 78.8,
        "is_day": 1,
        "condition": {
            "text": "Sunny",
            "icon": "//cdn.weatherapi.com/weather/64x64/day/113.png",
            "code": 1000
        },
        "wind_mph": 5.6,
        "wind_kph": 9.0,
        "wind_degree": 210,
        "wind_dir": "SSW",
        "pressure_mb": 1019.0,
        "pressure_in": 30.09,
        "precip_mm": 0.0,
        "precip_in": 0.0,
        "humidity": 34,
        "cloud": 0,
        "feelslike_c": 25.9,
        "feelslike_f": 78.6,
        "vis_km": 10.0,
        "vis_miles": 6.0,
        "uv": 7.0,
        "gust_mph": 3.4,
        "gust_kph": 5.4
    }
}

## Mopidy audio server
sudo apt install python3-pip

## backups
database needs to be done nightly to the NAS
dashboards should be in git and deployed from there
node red flows should be in git an deployed from there - or just use cron ...

## Need to redoe this whole thing with ansible/terraform, so I can just reinstall when needed
# applying ansible playbooks:
ansible-playbook backup.yml -i hosts 

# main playbook has the items in order
cd ansible
ansible-playbook main.yml -i hosts 


