from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
​
from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.0pziqjw.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('comment.html')

@app.route('/comment', methods=['GET'])
def comment_get():
    comment_list = list(db.comment.find({}, {'_id': False}))

    return jsonify({'comment': comment_list})

@app.route('/comment', methods=['POST'])
def comment_post():

    comment_list = list(db.comment.find({}, {'_id': False}))
    count = len(comment_list) + 1

    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'num': count,
        'name': name_receive,
        'comment': comment_receive,
        'done': 0
    }
    db.comment.insert_one(doc)
​
    return jsonify({'msg': '댓글 등록 완료'})
​
@app.route("/comment/del", methods=["POST"])
def comment_del():
    num_receive = request.form['num_give']
​
    db.comment.update_one({'num': int(num_receive)}, {'$set': {'done': 1}})
    db.comment.delete_one({'done': 1})
    return jsonify({'msg': '삭제 완료'})
​
if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)