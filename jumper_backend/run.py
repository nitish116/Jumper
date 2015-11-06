#!/usr/bin/python
import matplotlib.pyplot as plt
import sqlite3 as lite
import sys, getopt
from math import log,fabs
import datetime
import matplotlib
import numpy as np
import cPickle
from googlemaps.roads import snap_to_roads as sr
from googlemaps.directions import directions as directions
import googlemaps
gmaps = googlemaps.Client(key='AIzaSyCyLJ81ZkZOFVyXVEkXfKbOGZLwiwPxpl4')
