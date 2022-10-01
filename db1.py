from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://joyfive:whdlvkdlqm999@cluster0.omhyorx.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta
#mongodb+srv://joyfive:<password>@cluster0.omhyorx.mongodb.net/?retryWrites=true&w=majority

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


db.watcha.insert_one(
{
            'title': '인사이드 리릭스',
            'desc': 'TV프로그램, 12세 이용가',
            'img': "https://an2-img.amz.wtchn.net/image/v2/SoHRCHxGLWfj7R342hKUsQ.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5ETXllRFkwTUhFNE1DSmRMQ0p3SWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk5qQTJNVGMwTXprd056YzVNak16TnpVaWZRLkRrZlEzMnZqM3ViRmFJZi0wWXZROElXbFhBQmZrS3ZOYVgwQ0V5bjBLZE0",

            # 'tag': ['음악','뮤지션'],
            'like': '0',
        }
)

db.watcha.insert_one(
    {
        'title': '메이드 포 러브',
        'desc': 'TV프로그램, 15세 이용가',
        'img': "https://an2-img.amz.wtchn.net/image/v2/hIRH_AjGj97Vxnfzlj4YSw.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5ETXllRFkwTUhFNE1DSmRMQ0p3SWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk5qQXhNREV6TkRFd01qRTFOamd5T0RRaWZRLmxFejVaWE5wNTlnTFowSEVsMTFlaS02N0I4dGpkYTY0UnU3X2Q0TGxtblE",

        # 'tag': ['코미디', '블랙코미디'],
        'like': '0',
    }
)
db.watcha.insert_one(
    {
        'title': '정서원나요가애 : 귀여운 프로그래머',
        'desc': 'TV프로그램, 15세 이용가',
        'img': "https://an2-img.amz.wtchn.net/image/v2/PWrUa22gr9JVqpYIUY4qEg.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5ETXllRFkwTUhFNE1DSmRMQ0p3SWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk5qRTFNRFF6TmpRNU9EUTJORGMyTmpnaWZRLkNjZFBCUkdCWFlONU4wY1NickI0YVBwUFNqdmRsRmxmcG1zV1V4ckhITkk",

        # 'tag': ['로맨스', '웹드라마'],
        'like': '0',
    }
)

db.watcha.insert_one(
    {
        'title': '송곳니',
        'desc': '영화, 19세 이용가',
        'img': "https://an2-img.amz.wtchn.net/image/v2/VzKtYIFY2Mm1E7lk-hhwbQ.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5ETXllRFkwTUhFNE1DSmRMQ0p3SWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk5qRXhORGszTnpNM01qTXpNalF3TlRVaWZRLks3SERvdEpRNjhIQ3AwVVlvOFdrb05WQ0s1R2Y3WnRsRnlBeHlBNkpKc3c",

        # 'tag': ['어두운', '독립영화'],
        'like': '0',
    }
)
db.watcha.insert_one(
    {
        'title': '주아대면적소가가 : 달달한 이웃',
        'desc': 'TV 프로그램, 15세 이용가',
        'img': "https://an2-img.amz.wtchn.net/image/v2/1iNQQb4OPdKE0dmijvmvuw.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5ETXllRFkwTUhFNE1DSmRMQ0p3SWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk5qRTNORGt5TkRFeU9Ua3pOemd6TmpNaWZRLi03VmU1aVlqRTczSHl2LVZuQ1hMcFdXV0t5bHZ6V0w5bzNybGo4R2Rkcmc",

        'tag': ['로맨틱코미디', '웹드라마'],
        'like': '0',
    }
)


db.watcha.insert_one(
    {
        'title': '기담',
        'desc': '영화, 15세 이용가',
        'img': "https://an2-img.amz.wtchn.net/image/v2/XOv9wvlcEnMaFRtlR1Kfkg.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5ETXllRFkwTUhFNE1DSmRMQ0p3SWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk5qQTRNREkwTkRjNU1qQXhNVGM1TmpraWZRLmpSMW5IMXBCcmNBUmdNa1BFWnk0UVZZLVFPYmR2Nll5ZzNlQ2poajNqZDg",

        # 'tag': ['공포', '무서운'],
        'like': '0',
    }
)
db.watcha.insert_one(
    {
        'title': '여과성음유기억 : 소리의 기억',
        'desc': 'TV 프로그램, 15세 이용가',
        'img': 'https://an2-img.amz.wtchn.net/image/v2/3Vo3TiQwhyrcs9x3qlpPnA.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5ETXllRFkwTUhFNE1DSmRMQ0p3SWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk5qRTNOVEkzTVRRNE16TTROREUwTVRraWZRLkVKWUdqQU9RSWFXd2hpY2w5RnZYZkl5cml3Y2N6MXFkTS01WjJzY3RJUkE',

        'tag': ['드라마', '중국'],
        'like': '0'
    }
)

db.watcha.insert_one(
    {
        'title': '완벽한 도쿄의 맛',
        'desc': '영화, 전체 이용가',
        'img': 'https://an2-img.amz.wtchn.net/image/v2/SPfgs0qLR2rc2BvZY1wbwg.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5ETXllRFkwTUhFNE1DSmRMQ0p3SWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk5qRXlNemcwTkRRd05EVTJPRFk1TURBaWZRLnJneml0MTVGMjhfWExxWlNXaXliU1pOUXJCb0dxaV96ZEtwMTRpdG9FblU',

        # 'tag': ['다큐멘터리', '요리'],
        'like': '0'
    }
)

db.watcha.insert_one(
    {
        'title': '청풍랑월',
        'desc': 'TV 프로그램, 15세 이용가',
        'img': 'https://an2-img.amz.wtchn.net/image/v2/X2EHORtDW0kjQNP92zdxrg.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5ETXllRFkwTUhFNE1DSmRMQ0p3SWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk5qRTNOVFF6TmpRM05qRTROalV5TkRBaWZRLmJTMHQyLWJreWVKZEd1ZUszemNNSk5HN1lrU0ZKWl9KVVgyRGlqd05FM2c',

        # 'tag': ['코미디', '중국'],
        'like': '0'
    }
)


db.watcha.insert_one(
    {
        'title': '듀얼 : 나를 죽여라',
        'desc': '영화, 15세 이용가',
        'img': 'https://an2-img.amz.wtchn.net/image/v2/MgH4Los_RlS_JQF7UwiCwQ.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5ETXllRFkwTUhFNE1DSmRMQ0p3SWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk5UZzVNREF4TVRNd056VXpOVEE1TnpraWZRLjliT2tjRDFrbTAwZlRtaUpHWjVCQjlMOXk5RTlrNFV0SFRlSXNod2gwX2c',

        # 'tag': ['SF', '미국'],
        'like': '0'
    }
)
db.watcha.insert_one(
    {
        'title': '허순순적다화운',
        'desc': 'TV 프로그램, 15세 이용가',
        'img': 'https://an2-img.amz.wtchn.net/image/v2/9fScmImaXbYYxCIoFewcuA.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5ETXllRFkwTUhFNE1DSmRMQ0p3SWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk5qRTNOVFV6TnpJek5qTXhOVEF5T0RFaWZRLjRhTHJmOGxnd3U3Y2JrMGRhb0RaN2ZmNUY4MHpaUXhtcXcza2U3aXR1N3c',

        # 'tag': ['코미디', '웹드라마'],
        'like': '0'
    }
)
db.watcha.insert_one(
    {
        'title': '보이스',
        'desc': '영화, 15세 이용가',
        'img': 'https://an2-img.amz.wtchn.net/image/v2/b2O4HRp5Bkm_qfPf1DzgGQ.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5ETXllRFkwTUhFNE1DSmRMQ0p3SWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk5UUTROVEU0TURrME9EWTNNakl6TnpBaWZRLkZRWDlhLTlORE10QkMxLTJrVXM0c0VLZ3M3N2ZmR3IzV3htYklCR0pVSG8',

        # 'tag': ['범죄', '한국'],
        'like': '0'
    }
)
db.watcha.insert_one(
    {
        'title': '정부지간 - Plus&Minus',
        'desc': 'TV 프로그램, 15세 이용가',
        'img': 'https://an2-img.amz.wtchn.net/image/v2/h7--eFNWdMlQRBBtI1j8rA.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5ETXllRFkwTUhFNE1DSmRMQ0p3SWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk5qQTRPVEUxTVRReU1USXpOemsxTWpRaWZRLmtSbDJ0UHYtS25aTXVac1JKanJGbkxjajJZbFRMZUpUTWsxRlFOUFk2a2s',

        'tag': ['로맨스', '대만'],
        'like': '0'
    }
)
db.watcha.insert_one(
    {
        'title': '사사키와 미야노',
        'desc': 'TV 프로그램, 15세 이용가',
        'img': 'https://an2-img.amz.wtchn.net/image/v2/KNkDfZGwtFl6wFnwaxMMtw.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5ETXllRFkwTUhFNE1DSmRMQ0p3SWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk5qQTRPVE00TlRJME1UZ3lOemN5TlRFaWZRLlhrUW5zUVRVTFlEQU84bmhaTkh4aElQUEJRVy1tZU1tZmlPLXpsSzJiTTQ',

        # 'tag': ['애니메이션', '학원물'],
        'like': 0
    }
)
db.watcha.insert_one(
    {
        'title': '오키테가미 쿄코의 비망록',
        'desc': 'TV 프로그램, 15세 이용가',
        'img': 'https://an2-img.amz.wtchn.net/image/v2/ZZU2OGSzdxVSXe5IUacfeg.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5ETXllRFkwTUhFNE1DSmRMQ0p3SWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk5qQTRPVFF6TWpRNE9ERTJNVFkyTXpjaWZRLnFiMFFaR1FwTGFaNkotRXdwa1lCWUw0TlJqXzZCaXhQWjhqbnJJQUV3ZmM',

        # 'tag': ['미스터리', '추리'],
        'like': 0
    }
)
db.watcha.insert_one(
    {
        'title': '하선생적연연불망',
        'desc': 'TV 프로그램, 15세 이용가',
        'img': 'https://an2-img.amz.wtchn.net/image/v2/IU64VwkPCkZwPKBu-QoWRA.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5ETXllRFkwTUhFNE1DSmRMQ0p3SWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk5qQTJNekV5TkRJM01qWTRNVGc1TURBaWZRLjdiUndDMk1leV90VXd0bFJxNVBqYkF6TTBQMU1PSzJNNVFHNEdNaE9fX0U',

        # 'tag': ['로맨스', '중국'],
        'like': '0'
    }
)
db.watcha.insert_one(
    {
        'title': '마릴린 먼로와 함께한 일주일',
        'desc': '영화, 15세 이용가',
        'img': 'https://an2-img.amz.wtchn.net/image/v2/J-GcRdNqN0Ebv1kzVAl6zg.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5ETXllRFkwTUhFNE1DSmRMQ0p3SWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk5qQTNPVEF5TVRnek9UY3dOVGd5TlRZaWZRLmZqdnRfdzNfTkQwRGU5MG1ycmpfSU4tNkR6UnBiUWZTeG5ZQkNUS2QwaGM',

        # 'tag': ['', '사랑'],
        'like': '0'
    }
)

db.watcha.insert_one(
    {
        'title': '우연과 상상',
        'desc': '영화, 15세 이용가',
        'img': 'https://an2-img.amz.wtchn.net/image/v2/r0y_C9Ye-HVe_iso_2_VBQ.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5ETXllRFkwTUhFNE1DSmRMQ0p3SWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk5UZ3pPRFF3TURjMk56YzBOREUwTURnaWZRLl9iWFh6RzNFLUtaTU1hY2tseEl4eFF2T2NrTkR2QldQdmhpblo2MTVwVkU',

        # 'tag': ['드라마', '옴니버스'],
        'like': '0'
    },
)
db.watcha.insert_one(
    {
        'title': '퍼스트 레이디',
        'desc': 'TV 프로그램, 12세 이용가',
        'img': 'https://an2-img.amz.wtchn.net/image/v2/vl1qYK9zzXL_JlLkeqiGlA.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5ETXllRFkwTUhFNE1DSmRMQ0p3SWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk5Ua3pORFEyT1RNNE9EWTVNVFF6TURraWZRLnphVEtiMktlR2JJUXpUNTVlaXpGYVVpMWdpR0lsMzYtM1NYUUs2UWlhVDg',
        # 'tag': ['전기', '미국'],
        'like': '0'
    }
)
db.watcha.insert_one(
    {
        'title': '스틸워터',
        'desc': '영화, 15세 이용가',
        'img': 'https://an2-img.amz.wtchn.net/image/v2/dJDii7P9ASVHw9VbY1du0g.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5ETXllRFkwTUhFNE1DSmRMQ0p3SWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk5UUTNOalV3T0RjME5qazJPVFF3TXpjaWZRLjZoTTlpbUN6bWZWbmVGSmpJS25ycndXc04zMGVJem9GeVpnTXhZRlBReUk',
        # 'tag': ['범죄', '미국'],
        'like': '0'
    }
)