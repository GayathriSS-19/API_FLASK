#Understading GET Method

from flask import Flask,jsonify,make_response,abort
#Flask provides jsonify function to convert list,dictionaries to json(language of API)

#create a flask application
app=Flask(__name__)
#some dummy entries

tasks =[{'id':1,
        'title':'Buy Groceries',
         'Description':'Milk,Cheese,Bread,Fruits',
         'done':False},
         {'id':2,
        'title':'Buy Books',
         'Description':'Ikigai,Atomic Habits,Wings of Fire',
         'done':False}]

@app.route('/',methods=['GET'])
def get_tasks():
    """To get the information of tasks"""
    return jsonify({'tasks':tasks})

@app.route('/tasks/<int:task_id>',methods=['GET'])
def get_task(task_id):
    task=[task for task in tasks if task['id']==task_id]
    if len(task)==0:
        abort(404)
    return jsonify({'task':task[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'There is an error':'Recheck again'}),404)

if __name__=='__main__':
    app.run(debug=True)
