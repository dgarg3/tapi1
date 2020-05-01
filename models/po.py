
from db import db
class PoModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    cust_id = db.Column(db.Integer , db.ForeignKey('cust.id'))
    customer = db.relationship('CustModel')


    def __init__(self,name,price,cust_id):
        self.name = name
        self.price = price
        self.cust_id = cust_id

    def json_t(self):
        return {'name':self.name,'price':self.price}

    @classmethod
    def find_by_name(cls,name):
        # conn = sqlite3.connect('tb.db')
        # cursor = conn.cursor()
        # query = "select * from items where name = ?"
        # results = cursor.execute(query, (name,))
        # row = results.fetchone()
        # conn.close()
        #
        # if row:
        #     return cls(*row)

        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def del_from_db(self):
        db.delete(self)
        db.session.commit()

    # def insert_item(self):
    #     # conn = sqlite3.connect('tb.db')
    #     # cursor = conn.cursor()
    #     # query = "insert into items values(?,?)"
    #     # cursor.execute(query, (self.name, self.price))
    #     # conn.commit()
    #     # conn.close()
    #     db.session.add(self)
    #     db.session.commit()
    #
    #
    # def update(self):
    #     conn = sqlite3.connect('tb.db')
    #     cursor = conn.cursor()
    #     query = "update items set price = ? where name = ?"
    #     cursor.execute(query, (self.name, self.price))
    #     conn.commit()
    #     conn.close()

