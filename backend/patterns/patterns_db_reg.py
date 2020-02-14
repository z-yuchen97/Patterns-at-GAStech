from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import pymysql
from datetime import datetime
from dateutil.parser import parse
import config_patterns

# connection with mysql database
app = Flask(__name__)
app.config.from_object(config_patterns)
db = SQLAlchemy(app)


class Cc_data(db.Model):
    __tablename__ = 'cc_data'
    autoid = db.Column(db.Integer, primary_key = True, autoincrement = True)
    timestamp = db.Column(db.String(255))
    location = db.Column(db.String(255))
    price = db.Column(db.String(255))
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))

class Car_assignments(db.Model):
    __tablename__ = 'car_assignments'
    autoid = db.Column(db.Integer, primary_key = True, autoincrement = True)
    lastname = db.Column(db.String(255))
    firstname = db.Column(db.String(255))
    carid = db.Column(db.String(255))
    currentemploymenttype = db.Column(db.String(255))
    currentemploymenttitle = db.Column(db.String(255))

class Gps(db.Model):
    __tablename__ = 'gps'
    autoid = db.Column(db.Integer, primary_key = True, autoincrement = True)
    timestamp = db.Column(db.String(255))
    id = db.Column(db.String(255))
    latitude = db.Column(db.String(255))
    longtitude = db.Column(db.String(255))

class Loyalty_data(db.Model):
    __tablename__ = 'loyalty_data'
    autoid = db.Column(db.Integer, primary_key = True, autoincrement = True)
    timestamp = db.Column(db.String(255))
    location = db.Column(db.String(255))
    price = db.Column(db.String(255))
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))

db.create_all()


class PatternsInit():
    def __init__(self):
        pass

    def select_cc(self):
        # Open database connection
        db = pymysql.connect(user = "root", password = "Root2021@",
                            host = "127.0.0.1",
                            database = "patterns_origin" )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        sql = """select * from cc_data"""
        cursor.execute(sql)
        creditcard_record_list = cursor.fetchall()
        db.close()
        return creditcard_record_list

    def select_car(self):
        # Open database connection
        db = pymysql.connect(user = "root", password = "Root2021@",
                            host = "127.0.0.1",
                            database = "patterns_origin" )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        sql = """select * from car_assignments"""
        cursor.execute(sql)
        car_record_list = cursor.fetchall()
        db.close()
        return car_record_list

    def select_gps(self):
        # Open database connection
        db = pymysql.connect(user = "root", password = "Root2021@",
                            host = "127.0.0.1",
                            database = "patterns_origin" )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        sql = """select * from gps"""
        cursor.execute(sql)
        gps_record_list = cursor.fetchall()
        db.close()
        return gps_record_list

    def select_loyalty(self):
        # Open database connection
        db = pymysql.connect(user = "root", password = "Root2021@",
                            host = "127.0.0.1",
                            database = "patterns_origin" )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        sql = """select * from loyalty_data"""
        cursor.execute(sql)
        loyalty_record_list = cursor.fetchall()
        db.close()
        return loyalty_record_list


def init_cc_data():
    creaditcard_record_list = PatternsInit().select_cc()
    for cc_record in creaditcard_record_list:
        timestamp = parse(cc_record[1])
        patterns_cc_data = Cc_data(
                    timestamp = timestamp,
                    location = cc_record[2],
                    price = cc_record[3],
                    firstname = cc_record[4],
                    lastname = cc_record[5])
        db.session.add(patterns_cc_data)
        db.session.commit()

def init_car_assigments():
    car_record_list = PatternsInit().select_car()
    for car_record in car_record_list:
        patterns_car_assigments = Car_assignments(
                    lastname = car_record[1],
                    firstname = car_record[2],
                    carid = car_record[3],
                    currentemploymenttype = car_record[4],
                    currentemploymenttitle = car_record[5])
        db.session.add(patterns_car_assigments)
        db.session.commit()

def init_gps():
    gps_record_list = PatternsInit().select_gps()
    for gps_record in gps_record_list:
        timestamp = parse(gps_record[1])
        patterns_gps = Gps(
                    timestamp = timestamp,
                    id = gps_record[2],
                    latitude = gps_record[3],
                    longtitude = gps_record[4])
        db.session.add(patterns_gps)
        db.session.commit()

def init_loyalty_data():
    loyalty_record_list = PatternsInit().select_loyalty()
    for loyalty_record in loyalty_record_list:
        timestamp = parse(loyalty_record[1])
        patterns_loyalty_data = Loyalty_data(
                    timestamp = timestamp,
                    location = loyalty_record[2],
                    price = loyalty_record[3],
                    firstname = loyalty_record[4],
                    lastname = loyalty_record[5])
        db.session.add(patterns_loyalty_data)
        db.session.commit()


if __name__ == "__main__":
    # initialize patterns data
    # init_cc_data()
    init_car_assigments()
    init_gps()
    init_loyalty_data()
    