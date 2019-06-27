import RPi.GPIO as GPIO
from flask import Flask, render_template
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
senPIR = 26
senPIRSts = GPIO.LOW

# set PIR sensor pins a an input
GPIO.setup(senPIR, GPIO.IN)

@app.route("/")
def index():
	# read sensors status
	senPIRSts = GPIO.input(senPIR)
	templateData ={
		'title': 'GPIO input Status!',
		'senPIR': senPIRSts
	}
	return render_template('index.html', **templateData)

if __name__ =="__main__":
	app.run(host='0.0.0.0', port =81, debug =True)
