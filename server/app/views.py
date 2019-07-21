from flask import request
from flask_jwt import jwt_required, current_identity

from app import app, db
from app.models import Response, Code, User


@app.route('/register', methods=['POST'])
def register():
    resp = check_mime()
    if resp.code.value:
        return resp.build()
    username, password = request.json.get('username'), request.json.get('password')
    if not all([username, password]):
        return Response(Code.InvalidRequest, error='请求数据缺少用户名或密码！').build()
    user = User.query.filter_by(username=username).scalar()
    if user:
        return Response(Code.UsernameRegistered, error='用户名已被注册！').build()
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return Response(Code.OK, data='成功注册！').build()


@app.route('/push', methods=['POST'])
@jwt_required()
def push():
    resp = check_mime()
    if resp.code.value:
        return resp.build()
    user = User.query.filter_by(id=current_identity.id).scalar()
    if not user:
        return Response(Code.InternalError, error='无Token对应用户，但是Token有效，用户可能已被删除，请重新注册！').build()
    user.record = str(request.json)
    db.session.add(user)
    db.session.commit()
    return Response(Code.OK, data=f'成功更新 {user.username} 的通讯录！').build()


@app.route('/pull', methods=['GET'])
@jwt_required()
def pull():
    user = User.query.filter_by(id=current_identity.id).scalar()
    if not user:
        return Response(Code.InternalError, error='无Token对应用户，但是Token有效，用户可能已被删除，请重新注册！').build()
    return Response(Code.OK, data=user.record).build()


def check_mime():
    if not request.is_json:
        return Response(Code.InvalidRequest, error='请求数据格式必须为 JSON！')
    else:
        return Response(Code.OK)
