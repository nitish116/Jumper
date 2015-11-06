import matplotlib.pyplot as plt
import sys
from utils import *
from jumper_backend.settings_local import *

#assumption : vt_list is a list of 2-tuples, 0 - value and 1- hardware timestamp
#time_axis is in increasing order
#time_axis values are in the order pow(10,17)
def main_plotter(vt_list,plot_type,fig_savepath):
    time_axis = []
    value_axis = []

    for elem in vt_list:
        if len(elem) != 2:
            print "main_plotter in visual.py"
            print "Length of the tuple is not 2"
            sys.exit()
        tmp_time = int(elem[1])    
        value_axis.append(elem[0])
        time_axis.append(tmp_time)
        
        if len(str(tmp_time)) != TIME_ORDER:
            print len(str(elem[1]))
            print "main_plotter in visual.py"
            print "time_axis values should be of order "+str(TIME_ORDER)+", check the input"
            sys.exit()


    if not non_decreasing(time_axis):
        print "main_plotter in visual.py"
        print "time_axis is not non decreasing, check the input"
        sys.exit()


    if plot_type == 'time_plot':
        plt.plot(time_axis,value_axis)
    if plot_type == 'histogram_time': # bins are as many as the number of seconds
        nbins =  int(float(max(time_axis) - min(time_axis))/pow(10,3))
        plt.hist(time_axis,nbins)
    if plot_type == 'histogram_value': # bins are as many as the number of seconds
        plt.hist(value_axis)

    plt.savefig(fig_savepath)    
    plt.clf()
