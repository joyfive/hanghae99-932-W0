from pymongo import MongoClient
import certifi

caw = certifi.where()

wclient = MongoClient('mongodb+srv://joyfive:whdlvkdlqm999@cluster0.omhyorx.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=caw)
wdb = wclient.dbsparta
#mongodb+srv://joyfive:<password>@cluster0.omhyorx.mongodb.net/?retryWrites=true&w=majority

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route("/watcha", methods=["GET"])
def watcha_get():
    watcha_list = list(wdb.watcha.find({}, {'_id': False}))
    print(watcha_list)