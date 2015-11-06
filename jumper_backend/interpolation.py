import numpy as np
from db_handler import *


def basic_interpolation(acc_list,gps_lat_list,gps_long_list):
    t_lat = []
    lat_vec = []
    for elem in gps_lat_list:
        t_lat.append(elem[1])
        lat_vec.append(elem[0])

    t_long = []
    long_vec = []
    for elem in gps_long_list:
        t_long.append(elem[1])
        long_vec.append(elem[0])

    t_acc = []
    acc_vec = []
    for elem in acc_list:
        t_acc.append(elem[1])
        acc_vec.append(elem[0])

    

    if t_lat == t_long:
        lat_vec_int = np.interp(t_acc,t_lat,lat_vec)
        long_vec_int = np.interp(t_acc,t_long,long_vec)
    else:
        print "basic_interpolation function in interpolation.py"
        print "t_lat not equal to t_long, please check the database"
        sys.exit()

    
    ans = []
    for ii in range(len(t_acc)):
        ans.append((lat_vec_int[ii],long_vec_int[ii],acc_vec[ii],t_acc[ii]))

    return ans  

    





    

