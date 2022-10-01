from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://joyfive:whdlvkdlqm999@cluster0.omhyorx.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta
#mongodb+srv://joyfive:<password>@cluster0.omhyorx.mongodb.net/?retryWrites=true&w=majority

db.watcha.find().forEach(function(obj){
    if (obj.hasOwnProperty('like')) {
        obj.like = "" + obj.like;
    }
    db.watcha.save(obj);
});