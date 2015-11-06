import cPickle
import numpy as np

def get_pixel_num(cur_lat,cur_long,dict_extremes,lat_blocks,long_blocks):
    lat_block_size = float (dict_extremes['max_lat'] - dict_extremes['min_lat']) / float (lat_blocks)
    long_block_size = float (dict_extremes['max_long'] - dict_extremes['min_long']) / float (lat_blocks)


    lat_number =  int ((cur_lat - dict_extremes['min_lat'])/ lat_block_size)
    long_number =  int ((cur_long - dict_extremes['min_long'])/ long_block_size)
    ans = {}
     

    if lat_number < 0 or long_number < 0 or lat_number > lat_blocks or long_number > long_blocks:
        print "JIHAAD"
        import sys
        sys.exit(1)
    elif lat_number == lat_blocks:
        lat_number = lat_blocks - 1
    elif long_number == long_blocks:
        long_number = long_blocks - 1    

    # print lat_number, long_number  
    ans['lat_number'] = lat_number
    ans['long_number'] = long_number

    return ans    


def get_latlng(lat_number,long_number,dict_extremes,lat_blocks,long_blocks):
    ans = {}
    lat_size = float (dict_extremes['max_lat'] - dict_extremes['min_lat']) / float (lat_blocks)
    long_size = float (dict_extremes['max_long'] - dict_extremes['min_long']) / float (lat_blocks)
    ans['lat'] = dict_extremes['min_lat'] + lat_number*lat_size
    ans['long'] = dict_extremes['min_long'] + long_number*long_size
    return ans


def basic_merge_alldata(interpolated_data):
        
        lat_vec_int = []
        long_vec_int = []
        acc_vec_int = []
        time_vec_int = []
        cnt = 0
        for ride_data in interpolated_data:
                for elem in ride_data:
                    lat_vec_int.append(elem[0])
                    long_vec_int.append(elem[1])
                    acc_vec_int.append(elem[2])
                    time_vec_int.append(elem[3])
                

        min_lat = min(lat_vec_int)
        max_lat = max(lat_vec_int)

        min_long = min(long_vec_int)
        max_long = max(long_vec_int)



        PIXEL = []
        PIXEL_AVG = []
        lat_blocks = 100
        long_blocks = 100


        for ii in range(lat_blocks):
            PIXEL.append([])
            PIXEL_AVG.append([])
            for jj in range(long_blocks):
                PIXEL[ii].append([])
                PIXEL_AVG[ii].append(float('NaN'))

        count_me = 0 

        dict_extremes = {}

        dict_extremes['min_lat'] = min_lat
        dict_extremes['max_lat'] = max_lat
        dict_extremes['min_long'] = min_long
        dict_extremes['max_long'] = max_long



        for ii in range(len(acc_vec_int)):
            if count_me > -1:
                cur_lat = lat_vec_int[ii]
                cur_long = long_vec_int[ii]
                cur_acc = acc_vec_int[ii]
                pm = get_pixel_num(cur_lat,cur_long,dict_extremes,lat_blocks,long_blocks)
                PIXEL[pm['lat_number']][pm['long_number']].append(cur_acc)
            count_me = count_me + 1

        for ii in range(lat_blocks):
            for jj in range(long_blocks):
                tmp = PIXEL[ii][jj]
                if len(tmp) > 0:
                    PIXEL_AVG[ii][jj] = float (sum(tmp)) / float(len(tmp))
            
        val_vec = []
        for elem_x in PIXEL_AVG:
            for elem_xy in elem_x:
                if str(elem_xy) != "nan":            
                    val_vec.append(elem_xy)
        f_avg = sum(val_vec)/len(val_vec)
        f_std = np.std(np.array(val_vec))


        ans = {}
        markers = []
        markers_green = []
        RouteCoordinates = []
        
        iii=0
        for elem_x in PIXEL_AVG:
            jjj = 0
            for elem_xy in elem_x:
                tmp_latlng = get_latlng(iii,jjj,dict_extremes,lat_blocks,long_blocks)
                if str(elem_xy) != "nan":
                    if elem_xy - f_avg > f_std:   
                        markers.append([str(elem_xy),tmp_latlng['lat'],tmp_latlng['long'],'red']) 
                    else:
                        markers_green.append([str(elem_xy),tmp_latlng['lat'],tmp_latlng['long'],'green']) 
                 
                jjj+=1
            iii+=1
            
        ans['markers'] = markers 
        ans['markers_green'] = markers_green
        ans['RouteCoordinates'] = RouteCoordinates  

        return ans 
                   
