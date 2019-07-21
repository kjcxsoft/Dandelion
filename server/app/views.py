from flask import request
from flask_jwt import jwt_required, current_identity

from app import app, db
from app.models import Response, Code, User


@app.route('/register', methods=['POST'])
def register():
    resp = check_mime()
    if resp.code.value:
        return resp.build()
    username, password = request.json['username'], request.json['password']
    if not all([username, password]):
        return Response(Code.InvalidRequest, error='请求数据缺少用户名或密码！').build()
    user = User.query.filter_by(username=username).scalar()
    if user:
        return Response(Code.UsernameRegistered, error='用户名已被注册！').build()
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return Response(Code.OK, data=f'{user}').build()


@app.route('/t')
@jwt_required()
def test():
    return f'identity: {current_identity}'


def check_mime():
    if not request.is_json:
        return Response(Code.InvalidRequest, error='请求数据格式必须为 JSON！')
    else:
        return Response(Code.OK)
