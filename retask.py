import firebase_admin
from firebase_admin import db
import flask

app = flask.Flask(__name__)

firebase_admin.initialize_app(options={
    'databaseURL': 'https://<DB_NAME>.firebaseio.com'
})
TASK = db.reference('task')

@app.route('/texts', methods=['POST'])
def create_task():
    req = flask.request.json
    text = TASK.push(req)
    return flask.jsonify({'id': text.key}), 201

@app.route('/texts/<id>')
def read_text(id):
    return flask.jsonify(_ensure_text(id))

@app.route('/texts/<id>', methods=['PUT'])
def update_text(id):
    _ensure_text(id)
    req = flask.request.json
    TASK.child(id).update(req)
    return flask.jsonify({'success': True})

@app.route('/texts/<id>', methods=['DELETE'])
def delete_text(id):
    _ensure_text(id)
    TASK.child(id).delete()
    return flask.jsonify({'success': True})

def _ensure_text(id):
    text = TASK.child(id).get()
    if not text:
        flask.abort(404)
    return text