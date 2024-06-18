#!/bin/sh
# Run after changing the flows in node red, or dashboards in grafana via the UI
# get currently deployed node red flows:
rsync -Cavz raspberrypi:/home/thomasboltze/.node-red/flows.json ansible/nodered/
# get currently deployed grafana dashboards
curl http://admin:admin@raspberrypi-2.local:3000/api/dashboards/uid/bc778dee-454c-4dd6-ab8f-bbf4867f2b23 > ansible/grafana/solar-dashboard.json

curl http://admin:admin@raspberrypi.local:3000/api/dashboards/uid/f3f7b237-0c72-4a75-a493-4f451fb64bbb > ansible/grafana/neohub-dashboard.json
