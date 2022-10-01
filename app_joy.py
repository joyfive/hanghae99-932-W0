from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://joyfive:whdlvkdlqm999@cluster0.omhyorx.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta
#mongodb+srv://joyfive:<password>@cluster0.omhyorx.mongodb.net/?retryWrites=true&w=majority

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route("/watcha")
def watchapage():
    return render_template('watcha.html')


@app.route("/watcha/api", methods=["GET"])
def watcha_get():
    watcha_list = list(db.watcha.find({}, {'_id': False}))
    return jsonify({'watchas': watcha_list})

@app.route("/watcha/like", methods=["POST"])
def like_post():
    title_receive = request.form["title_give"]
    db.watcha.update_one({'title': title_receive},{'$set': {'like': 1}})
    return jsonify({'msg': '좋아요 완료❤️'})

@app.route("/watcha/dislike", methods=["POST"])
def dislike_post():
    title_receive = request.form["title_give"]
    db.watcha.update_one({'title': title_receive},{'$set': {'like': 0}})
    return jsonify({'msg': '좋아요가 취소 되었습니다🥲'})

@app.route("/netflix")
def netflixpage():
    return render_template('netflix.html')

@app.route("/netflix/api", methods=["GET"])
def netflix_get():
    netflix_list = list(db.netflix.find({}, {'_id': False}))
    return jsonify({'netflixs': netflix_list})

@app.route("/netflix/like", methods=["POST"])
def like_post_n():
    title_receive = request.form["title_give"]
    db.netflix.update_one({'title': title_receive},{'$set': {'like': 1}})
    return jsonify({'msg': '좋아요 완료❤️'})

@app.route("/netflix/dislike", methods=["POST"])
def dislike_post_n():
    title_receive = request.form["title_give"]
    db.netflix.update_one({'title': title_receive},{'$set': {'like': 0}})
    return jsonify({'msg': '좋아요가 취소 되었습니다🥲'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)