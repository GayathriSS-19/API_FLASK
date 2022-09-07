#First flask application

from flask import Flask
from flask_ngrok import run_with_ngrok  #connect to a wifi not lan
app=Flask(__name__) #creating a flask application object which contains data about applications and methods
#and also methods that tell application to do certain task

#run_with_ngrok(app)
#@app.route('/Gayathri')  #this is called routing
@app.route('/') 
def greeting():
	"""My first flask application"""
	return "First flask Application"

@app.route('/<name>')  #<variable name>
def displayname(name):
	"""passing a argument"""
	return f'your name is {name}'

if __name__ =='__main__':
	#app.run(debug=True)  #no need to write once ngrok is introduced
	app.run()