import time
import RPi.GPIO as GPIO
import sqlite3
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26, GPIO.IN)
GPIO.setup(24, GPIO.OUT)

dbname ='pirData.db'
sampleFrequency = 2 # take in data every 2 seconds

#  get data from the sensor
def getData():
	while True:
		conn = sqlite3.connect(dbname)
		curs = conn.cursor()
		state = GPIO.input(26)
		print( "state is", state)
		if state == True:
			curs.execute("Insert into pir_data values(datetime('now'),1)")
			GPIO.output(24, True)
		else: 
			curs.execute("Insert into pir_data values(datetime('now'),0)")
		conn.commit()
		time.sleep(2) # to stablize 
		GPIO.output(24, False)
		#GPIO.cleanup()

def logData(dist):
	conn = sqlite3.connect(dbname)
	curs = conn.cursor()
	curs.execute("INSERT INTO pir_data values(datetime('now'), (?))",(dist))
	conn.commit()
	conn.close()

#display database data
def displayData():
	conn = sqlite3.connect(dbname)
	curs = conn.cursor()
	print("\Entire database contents:\n")
	for row in curs.execute("SELECT * FROM pir_data"):
		print(row)
	conn.close()


def main():
	for i in range (0,10):
		getData()
	displayData()

# Execute Program
main()
