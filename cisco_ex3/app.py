from flask import Flask, request, jsonify, make_response, current_app
from flask_sqlalchemy import SQLAlchemy
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
app = Flask(__name__)


app.config['SECRET_KEY'] = 'thesecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'

db = SQLAlchemy(app)


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)

class Sys_details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ipaddress = db.Column(db.String(50))
    hostname = db.Column(db.String(50))
    user_id = db.Column(db.Integer)

@app.route('/user', methods=['GET'])
def get_all_users():

    users = User.query.all()

    output = []

    for user in users:
        user_data = {}
        user_data['public_id'] = user.public_id
        user_data['name'] = user.name
        user_data['password'] = user.password
        user_data['admin'] = user.admin
        output.append(user_data)
    return jsonify({'users': output})

@app.route('/user/<public_id>', methods=['GET'])
def get_one_user(public_id):
    user = User.query.filter_by(public_id=public_id).first()
    if not user:
        return jsonify({'message': 'no user found'})
    user_data = {}
    user_data['public_id'] = user.public_id
    user_data['name'] = user.name
    user_data['password'] = user.password
    user_data['admin'] = user.admin
    return jsonify({'user': user_data})

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()

    hashed_password = generate_password_hash(data['password'], method='sha256')

    new_user = User(public_id=str(uuid.uuid4()), name=data['name'], password=hashed_password, admin=False)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'New user create!'})

@app.route('/user/<public_id>', methods=['PUT'])
def promote_user(public_id):
    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message': 'No user found!'})
    user.admin = True
    db.session.commit()
    return jsonify({'message': 'user promoted'})

@app.route('/user/<public_id>', methods=['DELETE'])
def delete_user(public_id):
    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message': 'user not found!'})
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message':'user deleted'})

@app.route('/login')
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response('could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})
    user = User.query.filter_by(name=auth.username).first()
    if not user:
        return make_response('could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})
    if check_password_hash(user.password, auth.password):
        token = jwt.encode({'public_id': user.public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])

        return jsonify({'token' : token})
    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

@app.route('/sysdetail', methods=['GET'])
def get_all_sysdetails():
    sysdetails = Sys_details.query.filter_by(user_id=user_id).all

    output = []
    for sysdetails in sysdetails:
        sysdetails_data = {}
        sysdetails_data['id'] = sysdetails.id
        sysdetails_data['ipaddress'] = sysdetails.ipaddress
        sysdetails_data['hostname'] = sysdetails.hostname
        sysdetails_data['user_id'] = sysdetails.user_id
        output.append(sysdetails_data)

    return jsonify({'sysdetails': output})

@app.route('/sysdetail/<ipaddress>', methods=['GET'])
def get_one_sysdetails(ipaddress):
    sysdetails = Sys_details.query.filter_by(id=ipaddress, user_id=user_id).first()
    if not sysdetails:
        return jsonify({'message':'no record found'})

    sysdetails_data = {}
    sysdetails_data['id'] = sysdetails.id
    sysdetails_data['ipaddress'] = sysdetails.ipaddress
    sysdetails_data['hostname'] = sysdetails.hostname
    sysdetails_data['user_id'] = sysdetails.user_id

    return jsonify({sysdetails_data})

@app.route('/sysdetail', methods=['POST'])
def create_sysdetails():
    data = request.json()
    new_sysdetails = Sys_details(ipaddress=data['text'], hostname=data['text'], user_id=user_id.id)
    db.session.add(new_sysdetails)
    db.session.commit()
    return jsonify({'message':'sysip inserted'})

@app.route('/sysdetail', methods=['PUT'])
def update_sysdetails():
    sysdetails = Sys_details.query.filter_by(id=ipaddress, user_id=current_user).first()
    if not sysdetails:
        return jsonify({'message': 'no record found'})
    new_sysdetails = Sys_details(ipaddress=data['text'])
    sysdetails.ipaddress = db.session.add(new_sysdetails)
    db.session.commit()
    return jsonify({'message':'new record updated'})

@app.route('/sysdetail/<ipaddress>', methods=['DELETE'])
def delete_sysdetails():
    sysdetails = Sys_details.query.filter_by(id=ipaddress, user_id=user_id).first()
    if not sysdetails:
        return jsonify({'message': 'no record found'})
    db.session.delete(sysdetails)
    db.session.commit()
    return jsonify({'message':'sysdetails item deleted'})


if __name__ == '__main__':
    app.run(debug=True)