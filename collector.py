import serial,time

# Configuración de la comunicación serial con Arduino
port = '/dev/cu.usbmodem1101'  # Cambiar al puerto adecuado // este es el de mas lejos de la pantalla
baudrate = 9600  # Must match the baud rate in the Arduino sketch
timeout = 10  # Timeout for serial communication (in seconds)

# Open the serial port
ser = serial.Serial(port, baudrate=baudrate, timeout=timeout)

# Create an empty array to store the values
sensor_values = []

while True:
    # Read a line from the serial port
    line = ser.readline().decode().strip()

    # Parse the line as an integer value
    try:
        sensorValue = int(line)
        print('Numero de clavos:', sensorValue)

        # Append the value to the array
        sensor_values.append(sensorValue)

    except ValueError:
        print('Invalid data received:', line)

# Close the serial port
ser.close()