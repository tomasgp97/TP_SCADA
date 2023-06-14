from extensions import scheduler
from extensions import db
# from extensions import sensor
from flask import jsonify
from datetime import datetime


@scheduler.task('interval', id='do_job_1', seconds=10, misfire_grace_time=900)
def read_line():
        with scheduler.app.app_context():
            print('Starting job read_line')
            try:
                timestamp = datetime.now().strftime("%I:%M:%S")
                print("epoch is:", timestamp)
                
                
                # line = sensor.readline().decode().strip()
                # sensorValue = int(line)
                line = 'a'
                sensorValue = 21
                # datos = Datos(sensorValue)

                # result = db['clavos'].insert_one(datos.to_db_collection())
                result = db['sensor_values'].insert_one({'weight': sensorValue, 'timestamp': timestamp})
                response = {
                    # **sensorValue.to_db_collection(),
                    'id': str(result.inserted_id),
                }
                print(jsonify(response))

            except ValueError:
                print('Invalid data received:', line)