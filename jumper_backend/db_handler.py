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

