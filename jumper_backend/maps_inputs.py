import datetime

def basic_maps_input(gps_lat_list,gps_long_list):
	ans = {}
	markers = []
	markers_green = []
	RouteCoordinates = []
	if len(gps_lat_list) == len(gps_long_list):
		for ii in range(len(gps_lat_list)):
			cur_time = datetime.datetime.fromtimestamp(int(gps_lat_list[ii][1]/1000))
			markers.append([str(cur_time),gps_lat_list[ii][0],gps_long_list[ii][0],'red'])

	ans['markers'] = markers
	ans['markers_green'] = markers_green
	ans['RouteCoordinates'] = RouteCoordinates

	return ans		

