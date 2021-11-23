from flaskapp import app,request
from service import getUser,postUser,putUser,deleteUser

@app.route('/user',methods=['GET'])
@app.route('/user/<id>',methods=['GET'])
def read_user(id=None):
    return getUser(id)

@app.route('/user',methods=['POST'])
def insert_user():
    return postUser(request.data)

@app.route('/user',methods=['PUT'])
def update_user():
    return putUser(request.data)

@app.route('/user/<id>',methods=['DELETE'])
def delete_user(id):
    return deleteUser(id)
    
if __name__ == '__main__':
    # app.run(host="0.0.0.0", port=5000,debug = True) docker
    app.run(debug = True)