import sqlite3 as lite


def fetchdata_db_ride(database_path,table_name,ride_num=0):
    con = lite.connect(database_path)
    cur = con.cursor()
    cur.execute("PRAGMA table_info("+table_name+")")
    table_info = cur.fetchall()
    cur.execute("select * from "+table_name+ " where exp_id="+str(ride_num))
    data = cur.fetchall()
    ans = {}
    ans['table_info'] = table_info
    ans['data'] = data
    return ans


def fetchdata_db_all(database_path,table_name):
    con = lite.connect(database_path)
    cur = con.cursor()
    cur.execute("PRAGMA table_info("+table_name+")")
    table_info = cur.fetchall()
    cur.execute("select * from "+table_name)
    data = cur.fetchall()
    ans = {}
    ans['table_info'] = table_info
    ans['data'] = data
    return ans


#collect column data and hardware timestamp
def collect_columndata_timestamp(AllData,datatype):
    data = AllData['data']
    table_info = AllData['table_info']

    vt_list = []

    # This is in case the column names of the db change in future
    column_dict = {}
    for elem in table_info:
        column_dict[elem[1]] = elem[0]

    for elem in data:
        if elem[column_dict['type']] == datatype:
            h_time = int (elem[column_dict['hardware_timestamp']])
            cur_value = elem[column_dict['value']]
            if len(str(h_time)) == 19:
                    h_time = float(h_time)/pow(10,6)
            elif len(str(h_time)) == 13:
                h_time = float(h_time)
            else:
                h_time = float(h_time)
            vt_list.append((cur_value,h_time))    
            
    return vt_list  

def dc_latlong2path(gps_lat_list,gps_long_list):
    path = []
    for ii in range(len(gps_lat_list)):
        path.append((gps_lat_list[ii][0],gps_long_list[ii][0]))
    return path    


def dc_srout2path(snapped_path):
    ans = []
    for elem in snapped_path:
        ans.append((elem['location']['latitude'],elem['location']['longitude']))
    return ans    


def dc_tuple2lists(snapped_path):
    gps_lat_list = []
    gps_long_list = []
    for elem in snapped_path:
        gps_lat_list.append((elem[0],0))
        gps_long_list.append((elem[1],0))
    return {'lat_list':gps_lat_list,'long_list':gps_long_list}    



