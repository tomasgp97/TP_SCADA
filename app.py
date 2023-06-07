from flask import Flask, abort, request, jsonify
import database as db_connection
from datos import Datos
from bson.objectid import ObjectId
from flask_apscheduler import APScheduler
import serial, time


app = Flask(__name__)
db = db_connection.db_connection()
collection = db['sensor_values']

#scheduler stuff
scheduler = APScheduler()
scheduler.api_enabled = True
scheduler.init_app(app)
scheduler.start()
timestamp = 0

#sensor stuff
port = '/dev/cu.usbmodem1101'  
baudrate = 9600  
timeout = 10
# ser = serial.Serial(port, baudrate=baudrate, timeout=timeout)


@scheduler.task('interval', id='do_job_1', seconds=10, misfire_grace_time=900)
def read_line():
        with scheduler.app.app_context():
            print('Starting job read_line')
            timestamp += 10
            try:

                # line = ser.readline().decode().strip()
                # sensorValue = int(line)
                line = 'a'
                sensorValue = 21
                # datos = Datos(sensorValue)

                # result = db['clavos'].insert_one(datos.to_db_collection())
                result = collection.insert_one({'weight': sensorValue, 'timestamp': timestamp})
                response = {
                    # **sensorValue.to_db_collection(),
                    'id': str(result.inserted_id),
                }
                print(jsonify(response))

            except ValueError:
                print('Invalid data received:', line)




@app.post('/datos')
def post_datos():
    data = request.get_json()
    print(data)

    try:
        datos = Datos(**data)
        print()
        result = db['datos'].insert_one(datos.to_db_collection())
        response = {
            **datos.to_db_collection(),
            'id': str(result.inserted_id),
        }
        return jsonify(response)
    except TypeError:
        abort(400)


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
