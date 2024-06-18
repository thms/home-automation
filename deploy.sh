#!/bin/sh
rsync -Cavz models/*.py raspberrypi:/home/thomasboltze/solar/models/
rsync -Cavz lib/* raspberrypi:/home/thomasboltze/solar/lib/
rsync -Cavz *.py raspberrypi:/home/thomasboltze/solar/
