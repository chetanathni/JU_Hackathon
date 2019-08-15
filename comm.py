import firebase
from firebase.firebase import FirebaseApplication
firebase=firebase.firebase.FirebaseApplication('https://cabdetails-2e8a0.firebaseio.com/')   #using a Realtime Database
print("Successfully Established connection. Now sending data.");
print("Hit the escape sequence to exit");
import serial   #To obtain serial input from the Arduino
ser=serial.Serial('COM6',115200,timeout=0)   #defining the COM port where the Arduino has been connected



while 1:
	
	anValue=ser.readline()
	anValue=anValue.decode("utf-8")
	if len(anValue)==21:
			vals=list(anValue.split(' '))
			result = firebase.put('https://cabdetails-2e8a0.firebaseio.com/','AlcoholDetected',vals[0][-1])
			if vals[2][5]=='1': 
				result = firebase.put('https://cabdetails-2e8a0.firebaseio.com/','CrashDetected','1')
				print("DONE")
				break
	else:
		continue