from flask import Flask, jsonify, render_template, request
import json


app = Flask(__name__)
jData = json.loads(open('./restuarants.json').read())
data=jData["Restuarants"]

# Intial request Ex: localhost:5000
@app.route('/')
def route_main():
    return "RESTful Webservice Started. Request data with proper URL"

# Returns JSON which containes all restuarants
@app.route('/getrestuarants/')
def restuarants_all():
    return render_template("index.html",items=data)

# Returns restuarants JSON which matches the id
@app.route('/getrestuarants/<string:id>/')
def restuarants_by_id(id=''):
    myList=[]
    for element in data:
        if element["id"] == id:
            myList.append(element)
    return render_template("index.html",items=myList)

# Returns the restuarants JSON with particualr food type
@app.route('/getrestuarants/type/<string:type_of_food>/')
def restuarants_by_type(type_of_food=''):
    myList=[]
    for element in data:
        if element["type_of_food"].lower() == type_of_food.lower():
            myList.append(element)
    return render_template("index.html",items=myList)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')