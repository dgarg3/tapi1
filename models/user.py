import sqlite3
from db import db
class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))


    def __init__(self,username,password):

        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def json_t(self):
        return {'username created': self.username}

    @classmethod
    def find_by_username(cls,username):

        # conn = sqlite3.connect('tb.db')
        # cursor = conn.cursor()
        # sql = "select * from users where username = ? "
        # result = cursor.execute(sql,(username,))
        # row = result.fetchone()
        # if row:
        #     user = cls(*row)
        # else:
        #     user = None
        # conn.close()
        #return user
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        # conn = sqlite3.connect('tb.db')
        # cursor = conn.cursor()
        # sql = "select * from users where id = ? "
        # result = cursor.execute(sql, (_id,))
        # row = result.fetchone()
        # if row:
        #     user = cls(*row)
        # else:
        #     user = None
        # conn.close()
        # return user
        return cls.query.filter_by(id=_id).first()