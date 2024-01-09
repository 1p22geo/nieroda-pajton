from flask import Flask, request
import json
import sort
from database import Database, DatabaseIndexException

app = Flask("app")

data = Database()

@app.route('/sorted/<ix>', methods=['GET'])
def sorted_route(ix): 
    fn = lambda x: x[ix]
    return (json.dumps(
        {
            "data": sort.fnsort(data.get(), fn)
        }
    ))

@app.route('/data', methods=['POST', 'GET'])
def data_route(): 
    if request.method == 'GET':
        return (json.dumps(
            {
                "data": data.get()
            }
        ))
    if request.method == 'POST':
        return {'inserted_id':  data.insert(request.get_json(force=True))}
    
@app.route('/data/<int:id>', methods=['POST', 'GET'])
def data_id_route(id): 
    if request.method == 'GET':
        try:
            return (json.dumps(
                {
                    "data": data.get(id),
                    "id":id
                }
            ))
        except DatabaseIndexException as de:
            return f"No such index in database: {id}"
    if request.method == 'POST':
        return {'inserted_id': data.insert(request.get_json(force=True), id)}
    