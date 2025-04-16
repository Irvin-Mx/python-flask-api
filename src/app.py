from flask import Flask,jsonify,request
app = Flask(__name__)

todos = [{"label":"My first taskt","done":False}, {"label":"My second taskt","done":False}]

@app.route('/todos', methods=['GET'])
def hello_world():

    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json

    todos.append(request_body)

    print("Incomming request with the following body", request_body )
    return jsonify(todos)

@app.route('/todos/<int:position>',methods=["DELETE"])
def delete_todo(position):

    deletedItem = todos.pop(position)
    print("This is the position to delete:", position)
    #print("deleted item id",deletedItem)
    return jsonify(todos)


if(__name__ == '__main__'):
    app.run(host='0.0.0.0', port=3245 , debug=True)