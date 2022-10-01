import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://joyfive:whdlvkdlqm999@cluster0.omhyorx.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

wclient = MongoClient('mongodb+srv://test:sparta@cluster0.l7wrk04.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
cclient = MongoClient('mongodb+srv://test:sparta@cluster0.0pziqjw.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
wdb = wclient.dbsparta
cdb = cclient.dbsparta

#mongodb+srv://joyfive:<password>@cluster0.omhyorx.mongodb.net/?retryWrites=true&w=majority

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)








headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://flixpatrol.com/calendar/popular/tv-shows/netflix/', headers=headers)
data2 = requests.get('https://pedia.watcha.com/ko-KR', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
soup2 = BeautifulSoup(data2.text, 'html.parser')

nmovies = soup.select('body > div:nth-child(3) > div.card.-mx-content > div > table > tbody > tr')
wmovies = soup2.select('#root > div > div.css-1xm32e0 > section > div > section > div:nth-child(3) > div.css-1qq59e8 > div > div.css-9dnzub > div > div > ul > li')

# body > div:nth-child(3) > div.card.-mx-content > div > table > tbody > tr:nth-child(1) > td.table-td.w-24.text-right.md\:whitespace-nowrap
# body > div:nth-child(3) > div.card.-mx-content > div > table > tbody > tr:nth-child(1) > td.table-td.w-full.md\:w-2\/3 > a > div:nth-child(2) > div.group-hover\:underline
# body > div:nth-child(3) > div.card.-mx-content > div > table > tbody > tr:nth-child(1) > td.table-td.w-full.md\:w-2\/3 > a > div.table-poster-2 > div > picture > img

# root > div > div.css-1xm32e0 > section > div > section > div:nth-child(2) > div.css-1qq59e8 > div > div.css-9dnzub > div > div > ul > li:nth-child(1) > a > div.css-1qmeemv > div.css-unzuzl-StyledLazyLoadingImage.ezcopuc0 > img
# root > div > div.css-1xm32e0 > section > div > section > div:nth-child(2) > div.css-1qq59e8 > div > div.css-9dnzub > div > div > ul > li:nth-child(1) > a > div.css-1qmeemv > div.css-unzuzl-StyledLazyLoadingImage.ezcopuc0 > img
# root > div > div.css-1xm32e0 > section > div > section > div:nth-child(2) > div.css-1qq59e8 > div > div.css-9dnzub > div > div > ul > li:nth-child(1) > a > div.css-1qmeemv > div.css-10hm9rg
# root > div > div.css-1xm32e0 > section > div > section > div:nth-child(2) > div.css-1qq59e8 > div > div.css-9dnzub > div > div > ul > li:nth-child(2) > a > div.css-1qmeemv > div.css-unzuzl-StyledLazyLoadingImage.ezcopuc0 > img
# root > div > div.css-1xm32e0 > section > div > section > div:nth-child(2) > div.css-1qq59e8 > div > div.css-9dnzub > div > div > ul > li:nth-child(2) > a > div.css-1qmeemv > div.css-10hm9rg
# root > div > div.css-1xm32e0 > section > div > section > div:nth-child(2) > div.css-1qq59e8 > div > div.css-9dnzub > div > div > ul > li:nth-child(1) > a > div.css-1qmeemv > div.css-10hm9rg
# root > div > div.css-1xm32e0 > section > div > section > div:nth-child(2) > div.css-1qq59e8 > div > div.css-9dnzub > div > div > ul > li:nth-child(1) > a
# root > div > div.css-1xm32e0 > section > div > section > div:nth-child(2) > div.css-1qq59e8 > div > div.css-9dnzub > div > div > ul > li:nth-child(1) > a > div.css-1qmeemv > div.css-10hm9rg
# root > div > div.css-1xm32e0 > section > div > section > div:nth-child(2) > div.css-1qq59e8 > div > div.css-9dnzub > div > div > ul > li:nth-child(2) > a > div.css-1qmeemv > div.css-10hm9rg
# body > div:nth-child(3) > div.card.-mx-content > div > table > tbody > tr:nth-child(1) > td.table-td.w-full.md\:w-2\/3 > a > div.table-poster-2 > div > picture > source
# body > div:nth-child(3) > div.card.-mx-content > div > table > tbody > tr:nth-child(1) > td.table-td.w-full.md\:w-2\/3 > a > div.table-poster-2 > div > picture > img


for nmovie in nmovies:
    a = nmovie.select_one('td.table-td.w-full.md\:w-2\/3 > a > div.table-poster-2 > div > picture > source')
    nname = nmovie.select_one('td.table-td.w-full.md\:w-2\/3 > a > div:nth-child(2) > div.group-hover\:underline').text.strip()
    nrank = nmovie.select_one('td.table-td.w-24.text-right.md\:whitespace-nowrap').text.strip()
    nnrank = nrank.strip('.')
    nimg = a['srcset']
    nnimg = nimg.replace("72","350")
    if wdb.netflix.find_one({'rank':nnrank}):
        wdb.netflix.delete_one({'rank':nnrank})
        doc = {
            'rank': nnrank,
            'title': nname,
            'img': nnimg
        }
        wdb.netflix.insert_one(doc)
    else:
        doc = {
            'rank': nnrank,
            'title': nname,
            'img': nnimg
        }
        wdb.netflix.insert_one(doc)




for wmovie in wmovies:
    a = wmovie.select_one('a > div.css-1qmeemv > div.css-unzuzl-StyledLazyLoadingImage.ezcopuc0 > img')
    wname = wmovie.select_one('a')['title']
    wimg = a['src']
    wrank = wmovie.select_one('a > div.css-1qmeemv > div.css-csn5n', ).text
    if wdb.watcha.find_one({'rank': wrank}):
        wdb.watcha.delete_one({'rank': wrank})
        doc = {
            'rank': wrank,
            'title': wname,
            'img': wimg
        }
        wdb.watcha.insert_one(doc)
    else:
        doc = {
            'rank': wrank,
            'title': wname,
            'img': wimg
        }
        wdb.watcha.insert_one(doc)
        print(wimg)



# ---------------------------


@app.route('/comment', methods=['GET'])
def comment_get():
    comment_list = list(cdb.comment.find({}, {'_id': False}))

    return jsonify({'comment': comment_list})


@app.route('/comment', methods=['POST'])
def comment_post():

    comment_list = list(cdb.comment.find({}, {'_id': False}))
    count = len(comment_list) + 1

    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'num': count,
        'name': name_receive,
        'comment': comment_receive,
        'done': 0
    }
    cdb.comment.insert_one(doc)

    return jsonify({'msg': '댓글 등록 완료'})

@app.route("/comment/del", methods=["POST"])
def comment_del():
    num_receive = request.form['num_give']

    cdb.comment.update_one({'num': int(num_receive)}, {'$set': {'done': 1}})
    cdb.comment.delete_one({'done': 1})
    return jsonify({'msg': '삭제 완료'})


# ------------------------------

@app.route('/')
def home():
   return render_template('index_3.html')


@app.route("/wnetflix", methods=["GET"])
def wnetflix_get():
    norders_list = list(wdb.netflix.find({}, {'_id': False}))
    return jsonify({'norders': norders_list})


@app.route("/wwatcha", methods=["GET"])
def wwatcha_get():
    worders_list = list(wdb.watcha.find({}, {'_id': False}))
    return jsonify({'worders': worders_list})


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
    app.run('0.0.0.0', port=5000, debug=True)



