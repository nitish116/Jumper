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


database_name = CURRENT_DATABASE
table_name = CURRENT_DB_TABLENAME

ride_num = 4
datatype = "acc_z"

# db_data = fetchdata_db_ride(database_name,table_name,ride_num)

# acc_z_list = collect_columndata_timestamp(db_data,datatype)
# gps_lat_list = collect_columndata_timestamp(db_data,"gps_lat")
# gps_long_list = collect_columndata_timestamp(db_data,"gps_long")

# # markers_ds = basic_maps_input(gps_lat_list,gps_long_list)
# # cPickle.dump(markers_ds,open(BASE_DIR+"/tmp.dat","w"))


ride_list = range(3,8)
AllData_interpolated = []
for ride_num in ride_list:
	db_data = fetchdata_db_ride(database_name,table_name,ride_num)
	acc_z_list = collect_columndata_timestamp(db_data,datatype)
	gps_lat_list = collect_columndata_timestamp(db_data,"gps_lat")
	gps_long_list = collect_columndata_timestamp(db_data,"gps_long")
	interpolated_data = basic_interpolation(acc_z_list,gps_lat_list,gps_long_list)
	AllData_interpolated.append(interpolated_data)

marker_ds = basic_merge_alldata(AllData_interpolated)
cPickle.dump(marker_ds,open(BASE_DIR+"/tmp.dat","w"))


	

