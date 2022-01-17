from flask import Blueprint, request, jsonify,redirect,make_response
import requests
import hashlib
import jwt
import datetime as dt
from team_project2 import client
import os
SECRET_KEY = os.environ.get("SECRET_KEY")
SECRET_KEY_GITHUB = os.environ.get("SECRET_KEY_GITHUB")

bp = Blueprint('auth',__name__,)
db = client.team_project2

def get_user():
    token_receive = request.cookies.get('token')
    user_info = jwt.decode(token_receive, SECRET_KEY , algorithms=['HS256'])
    user = db.user.find_one({'email': user_info['email']})
    return user


# 중복확인
@bp.route('/join/api/email', methods=['POST'])
def emailKakunin():
    email = request.form['email']
    user = db.user.find_one({'email':email})
    if user:
        return jsonify({'fail':'email is alreay taken'})
    return jsonify('ok')

# 회원가입
@bp.route('/join/api', methods=['POST'])
def join():
    email = request.form['email']
    name = request.form['name']
    pw = request.form['pw']
    pw_hashed = hashlib.sha256(pw.encode('utf-8')).hexdigest()
    db.user.insert_one({'email':email,'name':name,'password':pw_hashed,'social_only': False})
    return jsonify({'result': 'success', 'msg': '아이디를 성공적으로 생성하였습니다.'})
# 로그인
@bp.route('/login/api', methods=['POST'])
def login_api():
    email = request.form['email']
    pw = request.form['pw']
    pw_hashed = hashlib.sha256(pw.encode('utf-8')).hexdigest()
    user = db.user.find_one({'email':email})
    if not user:
        return jsonify({'not': 'user is not'})

    if pw_hashed != user['password']:
        return jsonify({'fail':'password is not correct'})


    payload = {
        'email' : user['email'],

    }
    token = jwt.encode(payload, SECRET_KEY , algorithm='HS256')
    return jsonify({'result': 'success', 'token': token})





@bp.route('/login/kakao')
def login_kakao():
    code = request.args.get('code')
    redirect_uri = 'http://localhost:5000/login/kakao'
    client_id = '7f535c9ad05fa8ee370a9eb9318421c7'
    url="https://kauth.kakao.com/oauth/token"
    headers = {'Content-type': 'application/x-www-form-urlencoded'}

    resp = requests.post(
        url=url,
        headers=headers,
        data={'grant_type':"authorization_code",'client_id':client_id,'redirect_uri':redirect_uri,'code':code}
    )
    #토큰 얻어옴

    access_token = resp.json()['access_token']
    url = 'https://kapi.kakao.com/v2/user/me'
    headers.update({'Authorization': f'Bearer {access_token}'})
    resp = requests.post(
        url=url,
        headers=headers,
    )
    #토큰을 바탕으로 유저정보 얻어옴
    user_info = resp.json()
    print(user_info)
    is_it = db.user.find_one({'email':user_info['id']})
    #아이디가 존재하면 아이디 생략 x
    if not is_it:
        db.user.insert_one({'email': user_info['id'], 'name': user_info['properties']['nickname'],'social_only': True} )
    #토큰 생성후 쿠키 부여
    payload = {'email': user_info['id']}
    token = jwt.encode(payload,SECRET_KEY , algorithm='HS256')
    resp = make_response(redirect('/'))
    resp.set_cookie('token',token)
    return resp

@bp.route('/login/github')
def login_github():
    code = request.args.get('code')
    url ='https://github.com/login/oauth/access_token'
    client_secret = str(SECRET_KEY_GITHUB)
    client_id = '94debc0ee29ed22a1f74'
    headers = {'Accept': 'application/json'}

    resp = requests.post(
        url=url,
        headers=headers,
        data={'client_id': client_id, 'client_secret': client_secret,'code': code}
    )
    access_token = resp.json()['access_token']

    url = 'https://api.github.com/user'
    headers = {'Authorization': f'token {access_token}'}
    resp = requests.get(
        url=url,
        headers=headers,
    )
    url = 'https://api.github.com/user/emails'
    resp2 = requests.get(
        url=url,
        headers=headers,
    )
    user_info = resp.json()
    user_info2 = resp2.json()
    for i in user_info2:
        if i['email'] and i['primary']:
            email = i['email']
    is_it = db.user.find_one({'email': email})

    if not is_it:
        db.user.insert_one(
            {'email': email, 'name':user_info['name'] ,'social_only': True})

    payload = {'email': email}
    token = jwt.encode(payload, SECRET_KEY , algorithm='HS256')
    resp = make_response(redirect('/'))
    resp.set_cookie('token', token)
    return resp

@bp.route('/cat/comment',methods=['POST'])
def comment():
    user = get_user()
    user_id = str(user['_id'])
    user_name = user['name']
    if user['face'] == 'cat':
        face = '😺 고양이상'
    else:
        face = '🐶 강아지상'
    now = dt.datetime.now().strftime('%Y년 %m월 %d일 %H시 %M분 %S초')
    print(now)
    comment = request.form['comment']
    db.comments.insert_one({'content':comment,'author_id':user_id,'author_name':user_name ,'created_time': now, 'face':face})

    return jsonify({'result':'okay'})