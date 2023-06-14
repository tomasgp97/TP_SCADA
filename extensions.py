import database as db_connection
from flask_apscheduler import APScheduler
# from sensor import sensor_connection

scheduler = APScheduler()
db = db_connection.db_connection()
# sensor = sensor_connection() 

