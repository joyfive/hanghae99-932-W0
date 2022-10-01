from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://joyfive:whdlvkdlqm999@cluster0.omhyorx.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta
#mongodb+srv://joyfive:<password>@cluster0.omhyorx.mongodb.net/?retryWrites=true&w=majority

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


db.netflix.insert_one(
{
            'title': '더 크라운',
            'desc': '엘리자베스 2세의 이야기와 그녀의 통치에 영향을 준 수많은 정치적, 개인적 사건들을 담은 역사 기반의 시리즈.',
            'img': "https://occ-0-3077-993.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABWaMdRz9_lijyEH7AR9On8PWREx3N1DX3_3A7ZxzVD3dolRNgNVzkidNqi7RqbCaTDt6iZrK9SzP9fNW-XimLlIIdG9RB6jo4amGKc1pabSiDayTdsCQu6L3ewdVOsN7qnqr.jpg?r=8eb",

            # 'tag': ['음악','뮤지션'],
            'like': 0,
        }
)

db.netflix.insert_one(
    {
        'title': '리모델링 임파서블',
        'desc': '전광석화처럼 빠르게 일을 처리하는 리모델링 전문 팀이 위험을 무릅쓰고 심혈을 기울여 계획을 세운다. 참가 가족의 집을 단 12시간 안에 지붕부터 바닥까지 몽땅 뜯어고치기 위해서.',
        'img': "https://occ-0-3077-993.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABUMagNGm4wXOiTdP1w5nuovFO2wIzvk1jl-92-eK3y7bxs1M5bXTYB_VJEScf-xrKu5AMBINBT2fS3GAURO_jO78rEiNrSGhsDW52iv_w1JZZF_1NR2bQrQgsQd4k3GjwIN5.jpg?r=168",

        # 'tag': ['코미디', '블랙코미디'],
        'like': 0,
    }
)
db.netflix.insert_one(
    {
        'title': '슬기로운 의사생활',
        'desc': '99학번 의예과 동갑내기 친구들, 이젠 내 환자 보기에도 24시간이 부족한 40대 의사가 되었다. 각자 방식으로 살아가던 다섯 명의 친구들에게 한 통의 전화가 걸려오는데!',
        'img': "https://occ-0-3077-993.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABZmSmJsdmHoWsTsDnC3afQxPn470IR5osSI4sC2ctblHLWtt1nD8_8QJdUbIGJz09dsotijzyzeWZ61n0Ss7nE7iQ5mqFx4ITK4.webp?r=32e",

        # 'tag': ['로맨스', '웹드라마'],
        'like': 0,
    }
)

db.netflix.insert_one(
    {
        'title': '개와 함께',
        'desc': '그 어떤 어려운 상황에서도, 사랑하는 마음은 변치 않는다. 서로를 돌보고, 서로를 닮아간다. 특별한 유대 관계를 맺은 인간과 개의 가슴 뭉클한 동행. 세계 곳곳의 따뜻한 이야기를 만난다.',
        'img': "https://occ-0-3077-993.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABZLyXAWpG2jvET4E3MEA2NzD-96s-WNfFks-iDozqTqAFaTxUCkfAL0jQIvFH9Pz1LK1HiiQc1se9DbqAYI5MVxAqLXrqabJET38H4VaukTwmh4dWrTqc0gGZ_lkx7lH7wO1.jpg?r=e24",

        # 'tag': ['어두운', '독립영화'],
        'like': 0,
    }
)
db.netflix.insert_one(
    {
        'title': '사랑의 불시착',
        'desc': '뜻밖의 돌풍은 행운일까, 불운일까. 패러글라이딩 사고로 북한에 불시착한 재벌 딸. 그곳에서 깐깐한 북한군 장교를 만난다. 이 와중에 피어오르는 낯선 감정은 뭐지?',
        'img': "https://occ-0-3077-993.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABVJBN9qIx9eZPkct9lnKXQPgHb6BKx40A2HLbiQL1xNYqVVDpgIgs2z96km9P0fQ7bNJtSKN4Q-Q96nclkqcwFcI4de9DdLsKqU.webp?r=b44",

        # 'tag': ['로맨틱코미디', '웹드라마'],
        'like': 0,
    }
)


db.netflix.insert_one(
    {
        'title': '고양이는 왜 고양이일까?',
        'desc': '와락 달려들었다가도 획 돌아서는 고양이. 전문가들이 고양이의 수수께끼 같은 마음속으로 파고들어 이들의 진정한 능력을 밝혀본다. 고양이에 대한 매혹적이고 사랑스러운 다큐멘터리.',
        'img': "https://occ-0-3077-993.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABWvZB8xl6szE6p86uURlY_3huePiyeqCLXTSrE13ibAN8ckcuBb_P0lRamkQdRI2oBgGjSTbKrsg2zfGQZBaeNs0HbEZMI3JvpFfj5sozADvPBEe-uW3taEeIY0uyE_X_BUS.jpg?r=8f7",

        # 'tag': ['공포', '무서운'],
        'like': 0,
    }
)
db.netflix.insert_one(
    {
        'title': '사내맞선',
        'desc': '친구를 대신해 맞선 자리에 나간 하리. 남자가 겁을 먹고 퇴짜를 놓게 할 작정이다. 하지만 맞선남이 하리가 다니는 회사의 CEO로 드러나며 계획은 엉망이 된다. 게다가 그가 청혼을 하다니.',
        'img': 'https://occ-0-3077-993.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABe9BxHZ3xKYa-a9pqMOFSr7b3LtXfaYFKoWMjhh4DHyt-vNb8FjB5fwyimVLAKlwtaf-8YdkNGAi-IEO4m6gVWhR4vhTC_jMaC0.webp?r=db4',

        # 'tag': ['드라마', '중국'],
        'like': 0
    }
)

db.netflix.insert_one(
    {
        'title': '나의 아저씨',
        'desc': '순리대로 살지만 소년의 순수성과 어른의 지혜를 갖춘 아저씨가 있다. 그런데 이상한 애가 그를 흔든다. 거친 인생을 살아온 무모한 스물한 살 그녀가. 어느덧 우정이 움트고, 둘은 서로에게 안식처가 된다. 이 차가운 세상에서.',
        'img': 'https://occ-0-3077-993.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABWU6NvzMQHPEeUmo58s8jJbuk2aEqLyOUeDIJSjeeUVEvSfMWZ7eGLR1FqAc54RGzxPm-0VBUCQftKOF847mCye3pWvQZ9XHtxo.webp?r=7ad',

        # 'tag': ['다큐멘터리', '요리'],
        'like': 0
    }
)

db.netflix.insert_one(
    {
        'title': '굿플레이스',
        'desc': '살아생전 자기밖에 모르던 그녀. 착하게 살아야 천당 간다더니 그 반대가 돼버렸다! 사후 세계의 ‘굿 플레이스’에 남기 위한, 악녀의 개과천선 프로젝트 하나 둘 셋!',
        'img': 'https://occ-0-3077-993.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABa3hJWTH-8a2swv9NpuRLmx3WfXXWrAXpinWFsbolSOUX9H3Et0dmUpzObwKI8Ro5Fr7MAsejiZB6yeTiUTYTTBX9qbpp81l6Lc3SrTWahOCxo63eHJiNN3_Ooyd8pBZqlCD.jpg?r=944',

        # 'tag': ['코미디', '중국'],
        'like': 0
    }
)


db.netflix.insert_one(
    {
        'title': '나의 해방일지',
        'desc': '어른이 된 후 매일매일 되풀이되는 단조로운 일상에 지친 세 남매. 한없이 평범한 삶 속에서 특별한 성취와 자유를 찾아 나선다.',
        'img': 'https://occ-0-3077-993.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABb_E9ieBpnDiswAj598psNieNIx1H-mAde89yEOdzq-Lg3CH-7aPiOKJSRbJ-Wi3SwJxieZhzthacDiniwxAgOAQVqOhwwfBllg.webp?r=e93',

        # 'tag': ['SF', '미국'],
        'like': 0
    }
)
db.netflix.insert_one(
    {
        'title': '오징어게임',
        'desc': '빚더미에 짓눌린 중년 남자 기훈. 그가 일확천금을 노리고 의문의 게임에 뛰어든다. 그런데 게임이 시작되자마자 눈 앞에 펼쳐진 것은, 보고도 믿기 힘든 경악과 공포의 현장.',
        'img': 'https://occ-0-3077-993.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABbwRr6Ki3jguaITXzt2lxEr1CuskuhySNuyl2k0GcM4l6VkB2lYD8X06Pztx2ULqcZHdt5QsdnKarG8TnjIT8z39w61lEuxCwnhoFwL9kxS2c2GrwI1IgaaA-RbEUbA-dfHmPfGBydICoXx0U0gEpkeOjltgZvtVa6WGItEGp5ehnrW4NYkTYyDvouzocAs.jpg?r=b9a',

        # 'tag': ['코미디', '웹드라마'],
        'like': 0
    }
)
db.netflix.insert_one(
    {
        'title': '셰프의 테이블:피자',
        'desc': '유명 셰프들의 손에서 탄생한 전 세계 곳곳의 피자를 소개합니다. 열정과 독창성을 가득 담아 구워낸 최고의 한 조각. 정성을 기울인 만큼 맛있다!',
        'img': 'https://occ-0-3077-993.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABa5zRNomHo-2UXcAzTvHf4DlqPhow4KSHbqfFaxE575WLDr6caCFjcNYg6jLlStiHN3oURPiDpvZXIuwVDjgTKt1LJo-B1LTkED4k64ofMIIFpJ7qOmV3OEw8QnDwA27VuG-.jpg?r=065',

        # 'tag': ['범죄', '한국'],
        'like': 0
    }
)
db.netflix.insert_one(
    {
        'title': '브리저튼',
        'desc': '모두가 보는 앞에서 왕자의 선물을 받은 다프네. 이대로 그녀를 놓쳐도, 사이먼은 정말 괜찮은 걸까. 레이디 휘슬다운을 동경하던 엘로이즈는 그녀를 만나기로 마음먹는다.',
        'img': 'https://occ-0-3077-993.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABYOvOgg7ADDOL96QlFX-Dod2neS8rjp-YMQnZdGsbrUuiESceYn8eCA_YdvadjZ888jfmnP11ocBDOWjcm54f6o7bopmv3Rx66AbKfmzZcr-COWkihd3RsQA1NhIxd3m0f_l.jpg?r=b08',

        # 'tag': ['로맨스', '대만'],
        'like': 0
    }
)
db.netflix.insert_one(
    {
        'title': '우리들의 블루스',
        'desc': '사랑은 달콤하면서도 씁쓸하고, 인생은 좋을 때도 슬플 때도 있는 법. 바쁘게 돌아가는 섬 제주에서 하루하루 살아가는 우리들의 이야기가 펼쳐진다.',
        'img': 'https://occ-0-3077-993.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABZDtbYX_EfpD8rd1a2CQTNxxS2us6IGfRcPZJph8FOi-6FpFho4YnCNuX0s_bU8xQuy_vbgawJem5NH-bZpUaRI6Eskz5FcptcE.webp?r=f62',

        # 'tag': ['애니메이션', '학원물'],
        'like': 0
    }
)
db.netflix.insert_one(
    {
        'title': '샌드맨',
        'desc': '오랜 세월 감금당한 채 지내온 꿈의 군주 모르페우스. 그가 여러 세계를 가로지르는 새로운 여정을 시작한다. 빼앗긴 것들과 잃어버린 힘을 되찾기 위해.',
        'img': 'https://occ-0-3077-993.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABf90aojFm91JdlUejYnAmQLAPpCPr_6INUU0glfS_ksfWMw4aOAlilwg-_TjhGOoNfMdxizsE4bztpuBNVbRHZEaOgcguT4DdmRqyqmdlaHdY5dCJVKbo9MDjd6-i4vB5BmFlZEAx9PwmoXHnK3lIUgEm4yhiTCnH1BG2gJ6sWwW0aJ5sp8oykmh5W1WS69B-BEUqK0nIT_XIwDVHHvMqtZF4qIfLv2EB3spKflrcO6YhjF9JhiUVqrEes_TTnFKMzaUFTtg4z3Kd9e1GQcf91m84qFzx8ZqQfFaYuDc.jpg?r=df7',

        # 'tag': ['미스터리', '추리'],
        'like': 0
    }
)
db.netflix.insert_one(
    {
        'title': '내일',
        'desc': '사고로 반은 인간, 반은 영혼이 된 남자. 저승사자가 운영하는 지하세계 회사에 채용되고, 특별한 임무를 수행하러 나선다.',
        'img': 'https://occ-0-3077-993.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABYmSIloZOKn6lx_0XKyMjeqN9vEUcfE4g8JCD86Ol1As69kC5tC6B-Vze0g4xUYgw-ACyO_s29PCkciqwsYGhDs5qi1vHOZTETU.webp?r=25c',

        # 'tag': ['로맨스', '중국'],
        'like': 0
    }
)
db.netflix.insert_one(
    {
        'title': '굿닥터',
        'desc': '자폐증과 서번트 증후군을 앓는 외과 레지던트. 우여곡절 끝에 병원에 채용되어 시험대에 오른다. 자격을 증명하거나, 즉각 해고되거나. 주어진 시간은 단 6개월. 운명의 주사위가 던져진다!',
        'img': 'https://occ-0-3077-993.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABQukrmAM5mNa9TnnN1BsvrbzTf7o1gT4Xl68z66atFHnaRiVxFjIFUoPDfgsOojffKIHghuyFAR1oyyDlTF-STOzpN-PyuwriVE.webp?r=c3d',

        # 'tag': ['', '사랑'],
        'like': 0
    }
)

db.netflix.insert_one(
    {
        'title': '빨간 머리 앤',
        'desc': '빨간 머리에 고집 센 눈동자, 꿈 많고 당찬 아이 앤. 이 소녀가 초록지붕집의 마릴라와 매슈 남매에게 온다. 뜻밖의 운명으로. 루시 모드 몽고메리의 소설이 원작인 작품.',
        'img': 'https://occ-0-3077-993.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABSe_VjJJRNJoo69doC8aFFHDP-rOv0rKfVFv2WibD03x5ZJdPX8h8hXdbSdzqBz6CCue3bTNnVN10haVPbu4EEHkkHz-htBJO8MY3Xfs6iW88lRT8Jii5SNL4HI9hbWm2H_-.jpg?r=ffa',

        # 'tag': ['드라마', '옴니버스'],
        'like': 0
    },
)
db.netflix.insert_one(
    {
        'title': '그 해 우리는',
        'desc': '고등학교 시절 촬영한 다큐멘터리가 역주행하며 화제가 됐다. 서로 안 좋게 헤어졌건만, 어쩔 수 없이 다시 카메라 앞에 선 두 사람. 그렇게 서로의 삶에 다시 모습을 드러내기 시작한다.',
        'img': 'https://occ-0-3077-993.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABWNAwXbUtAoDg8vLK_B6Mm2RuV9wd6nsXaYCPMs4cPJaX0O9YQQjbgPbw8WPpA1vJLJoVK-11COzueTEVC5Og0LCDFrR-Sfjnww.webp?r=f58',
        # 'tag': ['전기', '미국'],
        'like': 0
    }
)
db.netflix.insert_one(
    {
        'title': '글로우 업',
        'desc': '명성을 얻고 싶다, 최고가 되고 싶다. 야심에 불타는 메이크업 아티스트들이 다채로운 과제를 헤쳐나간다. 끝까지 살아남으면, 꿈에 그리던 기회를 잡을 수 있다.',
        'img': 'https://occ-0-3077-993.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABRrJo8dGvMJUVAi1vSwOhzaa_eG8uTObp44bmbst-wZiZztjffF4vy-Uv9zo-refxUvKPzGh3OHX6PnlyEysmAk8rLjD1P_UIDRnYWeiGTlCx2xbCr-abud0fB8b8TaLnuQqGnT3x3wZsQj3GusgDP2eAu2Tq8Dmjqwbj7BfIqSUysRNkPni9stUDEqOyTVjvlEMXSZWUdGwAbiVMiDqTzpkka0USQBFBybNHIDgL6nqTLylPqLJUYnyASKOFAQnlpRxOpjaVTrKh6Jh6vYpONglvaqE3yHE.jpg?r=bd0',
        # 'tag': ['범죄', '미국'],
        'like': 0
    }
)