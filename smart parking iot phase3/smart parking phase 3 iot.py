Import serial 
Import requests 
Import time 
 
# Set your ThingSpeak API key and ThingSpeak channel URL 
Api_key = “your_api_key” 
Thing_speak_url = https://api.thingspeak.com/update 
 
# Set the COM port for your Arduino Uno 
Arduino_port = ‘COM3’ 
 
# Initialize serial communication with Arduino Uno Try: 
    Arduino = serial.Serial(arduino_port, 9600) Except serial.SerialException: 
    Print(f”Failed to connect to {arduino_port}. Check your COM port and connections.”) 
    Exit() 
Def read_sensor_data(): 
    Try: 
        # Read data from the Arduino via serial communication 
        Arduino.write(b’R’)  # Signal Arduino to send sensor data 
        Sensor_data = arduino.readline().decode().strip() 
        Return sensor_data 
    Except Exception as e: 
Print(f”Failed to read sensor data: {str€}”) 
        Return None 
 
Def send_to_thingspeak(data): 
    Payload = {“api_key”: api_key, “field1”: data}
    Try: 
Response = requests.post(thing_speak_url, params=payload)
If response.status_code == 200: 
            Print(“Data sent to ThingSpeak successfully”)
            Else: 
            Print(“Failed to send data to ThingSpeak”)
            Except Exception as e: 

Print(f”Error sending data to ThingSpeak: {str€}”) 
 
If __name__ == “__main__”: 
    Try: 
        While True: 
            Sensor_data = read_sensor_data()
            If sensor_data is not None: 
                Print(“Sensor Data:”, sensor_data) 

Send_to_thingspeak(sensor_data)
Time.sleep(60)  # Adjust the interval as needed     Except KeyboardInterrupt: 
        Print(“Exiting the program.”) 
        Arduino.close() 
 
