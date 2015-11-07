#!/usr/bin/python
# import matplotlib.pyplot as plt
# import sqlite3 as lite
# import sys, getopt
# from math import log,fabs
# import datetime
# import matplotlib
# import numpy as np
# import cPickle
# from googlemaps.roads import snap_to_roads as sr
# from googlemaps.directions import directions as directions
# import googlemaps
# gmaps = googlemaps.Client(key='AIzaSyCyLJ81ZkZOFVyXVEkXfKbOGZLwiwPxpl4')


from db_handler import *
from jumper_backend.settings_local import *
from visual import *
from interpolation import *
import cPickle
from jumper_backend.settings import BASE_DIR
from maps_inputs import *
from merge_rides import *
import cPickle


database_name = CURRENT_DATABASE
table_name = CURRENT_DB_TABLENAME


datatype = "acc_z"
runopt=0
ride_num=9

if runopt==0:
	db_data = fetchdata_db_ride(database_name,table_name,ride_num)
	gps_lat_list = collect_columndata_timestamp(db_data,"gps_lat")
	gps_long_list = collect_columndata_timestamp(db_data,"gps_long")
	for elem in gps_lat_list:
		print elem
	for elem in gps_long_list:
		print elem
	