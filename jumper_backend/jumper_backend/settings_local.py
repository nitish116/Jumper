from settings import BASE_DIR

DATA_FOLDER_PATH = BASE_DIR + "/DATA"

# This is assuming we are dealing with one database.
#But when daily updation happens , we need to screen for addition of new folders, datewise folders inside which folders for each user would be present. Select each database, all tables inside that and run the code
CURRENT_DATABASE = DATA_FOLDER_PATH + "/20151017/JumperDB"
CURRENT_DB_TABLENAME = "SensorValues"


# GOOGLE MAPS 
# WARNING : make sure you don't push this into settings_sample.py
GOOGLE_API_KEY = "AIzaSyCyLJ81ZkZOFVyXVEkXfKbOGZLwiwPxpl4"


#In the function collect_columndata_timestamp in visual.py , if len==19 we are correcting to 13
TIME_ORDER = 13



