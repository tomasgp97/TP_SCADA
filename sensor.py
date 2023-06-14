# import serial


# def sensor_connection():
#     try:
#         port = '/dev/cu.usbmodem1101'
#         baudrate = 9600  
#         timeout = 10
#         ser = serial.Serial(port, baudrate=baudrate, timeout=timeout)
#         return ser
#     except ConnectionError as e:
#         print('Error connecting to the sensor')
#         raise e

# sensor_connection()