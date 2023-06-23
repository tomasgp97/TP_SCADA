from flask import Flask, abort, request, jsonify
import database as db_connection
from datos import Datos
from bson.objectid import ObjectId
from flask_apscheduler import APScheduler
from flask_cors import CORS
# import serial, time
from datetime import datetime


app = Flask(__name__)
CORS(app)
db = db_connection.db_connection()
collection = db['test']



#sensor stuff
# port = '/dev/cu.usbmodem1101'
port = 'COM3'
baudrate = 9600  
timeout = 10
# ser = serial.Serial(port, baudrate=baudrate, timeout=timeout)

@app.post('/data')
def update_data():
    sensor_values = []

    while len(sensor_values) <= 10:
        # sensorValue = ser.readline().decode().strip()
        sensorValue = 1500
        timestamp = datetime.now().strftime("%I:%M:%S")

        try:
            sensor_values.append({'value':sensorValue, 'timestamp': timestamp})
            print('inserted:', sensorValue)

            
        except ValueError:
            print('Invalid data received:', sensorValue)
    

    result = collection.insert_many(sensor_values).inserted_ids
    for i in range (len(result)):
        result[i] = str(result[i])
    return jsonify(result)


# @app.post('/data')
# def update_data():
#     sensor_values = []

#     while len(sensor_values) <= 10:
#         sensorValue = ser.readline().decode().strip()
#         # sensorValue = 200
#         timestamp = datetime.now().strftime("%I:%M:%S")

#         try:
#             sensor_values.append({'value':sensorValue, 'timestamp': timestamp})
#             print('inserted:', sensorValue)

            
#         except ValueError:
#             print('Invalid data received:', sensorValue)
    

#     result = collection.insert_many(sensor_values).inserted_ids
#     for i in range (len(result)):
#         result[i] = str(result[i])
#     return jsonify(result)

@app.get('/data')
def get_all_data():
    data = list(db['test'].find())
    for datum in data:
        datum['_id'] = str(datum['_id'])
    return data



# @app.post('/datos')
# def post_datos():
#     data = request.get_json()
#     print(data)

#     try:
#         datos = Datos(**data)
#         print()
#         result = db['datos'].insert_one(datos.to_db_collection())
#         response = {
#             **datos.to_db_collection(),
#             'id': str(result.inserted_id),
#         }
#         return jsonify(response)
#     except TypeError:
#         abort(400)


@app.route('/ping')
def ping():
    return 'pong'


if __name__ == '__main__':
    app.run(port=5000)


# @app.get('/players/club/<club>/')
# def get_player_by_club(club):
#     players = list(db['players'].find({'club': club}))
#     for player in players:
#         player['_id'] = str(player['_id'])

#     return players


# @app.get('/players/country/<country>/')
# def get_player_by_country(country):
#     players = list(db['players'].find({'country': country}))
#     for player in players:
#         player['_id'] = str(player['_id'])

#     return players


# @app.get('/players/<id>/')
# def get_player_by_id(id):
#     player = db['players'].find_one({'_id': ObjectId(id)})
#     if player is None:
#         abort(404)
#     player['_id'] = str(player['_id'])
#     return player


# @app.get('/players')
# def get_players():
#     players = list(db['players'].find())
#     for player in players:
#         player['_id'] = str(player['_id'])

#     return players



# @app.put('/players/<id>/')
# def update_club(id):
#     data = request.get_json()
#     if 'club' not in data or data['club'] == '':
#         abort(400)
#     db['players'].update_one({'_id': ObjectId(id)}, {'$set': {'club': data['club']}})
#     return {}


# @app.delete('/players/<id>/')
# def delete_player_by_id(id):
#     db['players'].delete_one({'_id': ObjectId(id)})
#     return {}
