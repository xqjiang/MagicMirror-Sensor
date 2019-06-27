from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io
from flask import Flask, render_template, send_file, make_response, request
app = Flask(__name__)
import sqlite3
import datetime

conn = sqlite3.connect('pirData.db')
curs = conn.cursor()

# request last data from database
def getLastData():
	for row in curs.execute("SELECT * FROM pir_data ORDER BY timestamp DESC LIMIT 1"):
		time = str(row[0])
		dist = row[1]
	#conn.close()
	return time, dist

# get data that is within the designated range, which is # seconds 
# before the current time
def getHistData(numberSeconds):
	#nowTime = datetime.datetime.now()
	#priorTime = nowTime - datetime.timedelta(seconds = numberSeconds)
	#nowTimeSQL = Datetime(nowTime.strftime('%Y-%m-%d %H:%M:%S'))
	#priorTimeSQL = Datetime(priorTime.strftime('%Y-%m-%d %H:%M:%S'))
	
	#print(nowTimeSQL,priorTimeSQL)
	#curs.execute("SELECT * FROM pir_data WHERE timestamp >priorTimeSQL and timestamp <nowTimeSQL")
	curs.execute("SELECT * FROM pir_data ORDER BY timestamp DESC LIMIT "+str(numberSeconds))
	data = curs.fetchall()
	dates = []
	dists =[]
	for row in reversed(data):
		dates.append(row[0])
		dists.append(row[1])
	return dates, dists

def maxRowsTable():
	for row in curs.execute("SELECT COUNT(timestamp) FROM pir_data"):
		maxNumberRows = row[0]
	return maxNumberRows

global numSamples
numSamples = maxRowsTable()
if (numSamples > 101):
	nmSamples = 100

# main route
@app.route("/")
def index():
	time, dist = getLastData()
	templateData ={
		'time' : time, 
		'dist' : dist
		#'numSamples' : numSamples
	}
	return render_template('index.html', **templateData)

@app.route('/', methods =['POST'])
def my_form_post():
	global numSamples
	numSamples  = int(request.form['numSamples'])
	numMaxSamples = maxRowsTable()
	if(numSamples > numMaxSamples):
		numSamples = (numMaxSamples -1)
	time, dist = getLastData()
	templateData ={
		'time' : time,
		'dist' : dist,
		'numSamples' : numSamples
	}
	return render_template('index.html', **templateData)

# plotting graph
@app.route('/plot/dist')
def plot_dist():
	times, dists = getHistData(numSamples)
	
	ys = dists
	#print(ys)
	#print("FINISH!!!!!!")
	fig = Figure()
	axis = fig.add_subplot(1,1,1)
	axis.set_title("Sensor Sensing")
	axis.set_xlabel("Time")
	axis.set_ylabel("ON/OFF State")
	axis.grid(True)
	xs = range(numSamples)
	#print(xs)
	#print("xs FINISH!!!")
	axis.plot(xs, ys)
	canvas = FigureCanvas(fig)
	output = io.BytesIO()
	canvas.print_png(output)
	response = make_response(output.getvalue())
	response.mimetype ='image/png'
	return response



if __name__ == "__main__":
	app.run(host ='0.0.0.0',port = 82, debug =False)
