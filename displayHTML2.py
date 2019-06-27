from flask import Flask, render_template, request
app = Flask(__name__)
import sqlite3

# retrieve data from database
def getData():
	conn = sqlite3.connect('pirData.db')
	curs = conn.cursor()
	for row in curs.execute("SELECT * FROM pir_data ORDER BY timestamp DESC LIMIT 1"):
		time = str(row[0])
		output = row[1]
	conn.close()
	return time, output

# main route
@app.route("/")
def index():
	time, output = getData()
	templateData ={
		'time': time,
		'output':output
	}
	return render_template('index.html', **templateData)

if __name__ == "__main__":
	app.run(host ='0.0.0.0', port = 82, debug = True)
