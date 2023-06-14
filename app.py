from flask import Flask, g
import logging
from datos import Datos
from bson.objectid import ObjectId
from extensions import scheduler
# from flask_apscheduler import APScheduler
# import sensor as sensor_connection
# import database as db_connection


def create_app():
    """Create a new app instance."""

    app = Flask(__name__)
    scheduler.init_app(app)

    logging.getLogger("apscheduler").setLevel(logging.INFO)

    with app.app_context():
        import tasks  
        import events

        
        scheduler.start()
        # from routes import web  
        # app.register_blueprint(web.web_bp)

        return app

app = create_app()


if __name__ == "__main__":
    app.run()

#scheduler stuff
# scheduler = APScheduler()
# scheduler.api_enabled = True
# scheduler.init_app(app)
# scheduler.start()
# global timestamp
#sensor stuff
# ser = sensor_connection.sensor_connection()

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


# if __name__ == '__main__':
#     app.run(port=5000)