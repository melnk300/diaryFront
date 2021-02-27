from flask import Flask, request, jsonify
import datetime as dt
from exceptions import Login_Error
from flask_cors import CORS
import psycopg2 as psql
from models import User_Web, Task
from cfg import DevConfig as cfg
app = Flask(__name__)
CORS(app)


@app.route('/api/reg', methods=["GET", "POST"])
def register_user():
    payload = request.get_json()
    user = User_Web()
    return user.register_user(payload)


@app.route('/api/reg_education', methods=["GET", "POST"])
def reg_education():
    user = User_Web()
    payload = request.get_json()
    return user.register_education(payload)


@app.route('/api/log_check', methods=["GET", "POST"])
def log_check():
    try:
        user = User_Web()
        payload = request.get_json()
        res = user.login_check(payload)
        return res
    finally:
        return '401'


@app.route('/api/get_task', methods=["GET", "POST"])
def get_task():
    try:
        user = User_Web()
        req = request.get_json()
        user.login_check(req['user'])
        task = Task()
        return task.get_task(req['payload'], user)
    except Login_Error:
        return '401'


@app.route('/api/add_task', methods=["GET", "POST"])
def add_task():
    try:
        req = request.get_json()
        user = User_Web()
        user.login_check(req['user'])
        task = Task()
        return task.add_task(req['payload'], user)
    except Login_Error:
        return '401'


@app.route('/api/delete_task', methods=["GET", "POST"])
def delete_task():
    try:
        req = request.get_json()
        user = User_Web()
        user.login_check(req['user'])
        task = Task()
        return task.delete_task(req['payload'], user)
    except Login_Error:
        return '401'


if __name__ == '__main__':
    app.run(cfg.beyound_host, debug=True)
