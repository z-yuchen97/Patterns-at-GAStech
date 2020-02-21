from flask import Flask, url_for, redirect, render_template
from flask import request
from flask import jsonify
from flask_cors import CORS

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from dateutil.parser import parse
from datetime import datetime

# website backend bulid up
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
patterns_conn = "mysql+pymysql://root:Root2021@@127.0.0.1:3306/patterns"

@app.route('/init_person', methods=['GET'])
def init_person():
    engine = create_engine(patterns_conn)
    Base = automap_base()
    Base.prepare(engine, reflect = True)
    db = sessionmaker(bind = engine)()
    Gps = Base.classes.gps
    Car_assignments = Base.classes.car_assignments
    result_list = db.query(Car_assignments).filter(Car_assignments.carid.isnot(None))
    personal_info_list = []
    for result in result_list:
        personal_info = {"carid": result.carid,
                    "firstname" : result.firstname,
                    "lastname" : result.lastname}
        personal_info_list.append(personal_info)
    return jsonify(personal_info_list)


@app.route('/init_time', methods=['GET'])
def init_time():
    date = []
    hour = []
    minute = []
    for d in range(6, 20): date.append(d)
    for h in range(0, 24): hour.append(h)
    for m in range(0, 60): minute.append(m)
    time = {"date" : date, "hour" : hour, "minute" : minute}
    return jsonify(time)


@app.route('/search_gps', methods=['GET','POST'])
def search_gps():
    # load data from frontend post request
    firstname = request.args.get("firstname")
    lastname = request.args.get("lastname")
    time_start = request.args.get("time_start")
    time_end = request.args.get("time_end")
    time_start = datetime.strptime(time_start, "%y-%m-%d %H:%M")
    time_end = datetime.strptime(time_end, "%y-%m-%d %H:%M")
    # start engine in sql datbase
    engine = create_engine(patterns_conn)
    Base = automap_base()
    Base.prepare(engine, reflect = True)
    db = sessionmaker(bind = engine)()
    Gps = Base.classes.gps
    Car_assignments = Base.classes.car_assignments
    # trigger search condition
    if (firstname == "Truck Drivers") :
        result_list = db.query(Gps).filter(Gps.id > 35).filter(Gps.timestamp.between(time_start, time_end))
        gps_record_list = []
        for result in result_list:
            gps_record = {"timestamp" : result.timestamp,
                        "firstname" : "Truck",
                        "lastname" : "Drivers",
                        "latitude" : float(result.latitude), 
                        "longtitude" : float(result.longtitude)}
            gps_record_list.append(gps_record)
    elif((len(firstname) != 0 ) and (len(lastname) != 0)) :
        result_list = (db.query(Car_assignments, Gps)
                    .join(Car_assignments, Car_assignments.carid == Gps.id)
                    .filter_by(firstname = firstname)
                    .filter_by(lastname = lastname)
                    .filter(Gps.timestamp.between(time_start, time_end)))
        gps_record_list = []
        for result in result_list:
            gps_record = {"timestamp" : result.gps.timestamp,
                        "firstname" : result.car_assignments.firstname,
                        "lastname" : result.car_assignments.lastname,
                        "latitude" : float(result.gps.latitude), 
                        "longtitude" : float(result.gps.longtitude)}
            gps_record_list.append(gps_record)
    else:
        result_list = (db.query(Car_assignments, Gps)
                    .join(Car_assignments, Car_assignments.carid == Gps.id)
                    .filter(Gps.timestamp.between(time_start, time_end)))
        gps_record_list = []
        for result in result_list:
            gps_record = {"timestamp" : result.gps.timestamp,
                        "firstname" : result.car_assignments.firstname,
                        "lastname" : result.car_assignments.lastname,
                        "latitude" : float(result.gps.latitude), 
                        "longtitude" : float(result.gps.longtitude)}
            gps_record_list.append(gps_record)
    return jsonify(gps_record_list)


@app.route('/search_card', methods=['GET','POST'])
def search_card():
    # load data from frontend post request
    firstname = request.args.get("firstname")
    lastname = request.args.get("lastname")
    time_start = request.args.get("time_start")
    time_end = request.args.get("time_end")
    time_start = datetime.strptime(time_start, "%y-%m-%d %H:%M")
    time_end = datetime.strptime(time_end, "%y-%m-%d %H:%M")
    # start engine in sql datbase
    engine = create_engine(patterns_conn)
    Base = automap_base()
    Base.prepare(engine, reflect = True)
    db = sessionmaker(bind = engine)()
    Car_assignments = Base.classes.car_assignments
    Cc_data = Base.classes.cc_data
    Loyalty_data = Base.classes.loyalty_data

    if((len(firstname) != 0 ) and (len(lastname) != 0)):
        # search for cc_data
        result_list = (db.query(Car_assignments, Cc_data)
                        .join(Car_assignments, (Car_assignments.firstname == Cc_data.firstname) 
                        & (Car_assignments.lastname == Cc_data.lastname))
                        .filter_by(firstname = firstname)
                        .filter_by(lastname = lastname)
                        .filter(Cc_data.timestamp.between(time_start, time_end)))
        cc_record_list = []
        for result in result_list:
            cc_record = {"type": "credit",
                        "location": result.cc_data.location,
                        "name": result.cc_data.firstname + " " + result.cc_data.lastname,
                        "timestamp" : result.cc_data.timestamp,
                        "price": result.cc_data.price}
            cc_record_list.append(cc_record)
        # search for loyalty_data
        result_list = (db.query(Car_assignments, Loyalty_data)
                        .join(Car_assignments, (Car_assignments.firstname == Loyalty_data.firstname) 
                        & (Car_assignments.lastname == Loyalty_data.lastname))
                        .filter_by(firstname = firstname)
                        .filter_by(lastname = lastname)
                        .filter(Loyalty_data.timestamp.between(time_start, time_end)))
        loyalty_record_list = []
        for result in result_list:
            loyalty_record = {"type": "loyalty",
                        "location": result.loyalty_data.location,
                        "name": result.loyalty_data.firstname + " " + result.loyalty_data.lastname,
                        "timestamp" : result.loyalty_data.timestamp,
                        "price": result.loyalty_data.price}
            loyalty_record_list.append(loyalty_record)
    else:
        # search for cc_data
        result_list = (db.query(Car_assignments, Cc_data)
                        .join(Car_assignments, (Car_assignments.firstname == Cc_data.firstname) 
                        & (Car_assignments.lastname == Cc_data.lastname))
                        .filter(Cc_data.timestamp.between(time_start, time_end)))
        cc_record_list = []
        for result in result_list:
            cc_record = {"type": "credit",
                        "location": result.cc_data.location,
                        "name": result.cc_data.firstname + " " + result.cc_data.lastname,
                        "timestamp" : result.cc_data.timestamp,
                        "price": result.cc_data.price}
            cc_record_list.append(cc_record)
        # search for loyalty_data
        result_list = (db.query(Car_assignments, Loyalty_data)
                        .join(Car_assignments, (Car_assignments.firstname == Loyalty_data.firstname) 
                        & (Car_assignments.lastname == Loyalty_data.lastname))
                        .filter(Loyalty_data.timestamp.between(time_start, time_end)))
        loyalty_record_list = []
        for result in result_list:
            loyalty_record = {"type": "loyalty",
                        "location": result.loyalty_data.location,
                        "name": result.loyalty_data.firstname + " " + result.loyalty_data.lastname,
                        "timestamp" : result.loyalty_data.timestamp,
                        "price": result.loyalty_data.price}
            loyalty_record_list.append(loyalty_record)
    shop_record_list = cc_record_list + loyalty_record_list
    shop_record_list = sorted(shop_record_list, key = lambda i: i['timestamp']) 
    return jsonify(shop_record_list)  


@app.route('/search_hist', methods=['GET','POST'])
def search_hist():
    time_start = request.args.get("time_start")
    time_start = time_start.split(" ", 1)[0]
    time_mstone0 = datetime.strptime(time_start + " " + "0:0", "%y-%m-%d %H:%M")
    time_mstone1 = datetime.strptime(time_start + " " + "2:0", "%y-%m-%d %H:%M")
    time_mstone2 = datetime.strptime(time_start + " " + "4:0", "%y-%m-%d %H:%M")
    time_mstone3 = datetime.strptime(time_start + " " + "6:0", "%y-%m-%d %H:%M")
    time_mstone4 = datetime.strptime(time_start + " " + "8:59", "%y-%m-%d %H:%M")
    time_mstone5 = datetime.strptime(time_start + " " + "10:0", "%y-%m-%d %H:%M")
    time_mstone6 = datetime.strptime(time_start + " " + "12:0", "%y-%m-%d %H:%M")
    time_mstone7 = datetime.strptime(time_start + " " + "14:0", "%y-%m-%d %H:%M")
    time_mstone8 = datetime.strptime(time_start + " " + "16:0", "%y-%m-%d %H:%M")
    time_mstone9 = datetime.strptime(time_start + " " + "18:0", "%y-%m-%d %H:%M")
    time_mstone10 = datetime.strptime(time_start + " " + "20:0", "%y-%m-%d %H:%M")
    time_mstone11 = datetime.strptime(time_start + " " + "22:0", "%y-%m-%d %H:%M")
    time_mstone12 = datetime.strptime(time_start + " " + "23:59", "%y-%m-%d %H:%M")
    # start engine in sql datbase
    engine = create_engine(patterns_conn)
    Base = automap_base()
    Base.prepare(engine, reflect = True)
    db = sessionmaker(bind = engine)()
    Gps = Base.classes.gps
    # search for time_range data
    track1 = db.query(Gps).filter(Gps.timestamp.between(time_mstone0, time_mstone1)).count()
    track2 = db.query(Gps).filter(Gps.timestamp.between(time_mstone1, time_mstone2)).count()
    track3 = db.query(Gps).filter(Gps.timestamp.between(time_mstone2, time_mstone3)).count()
    track4 = db.query(Gps).filter(Gps.timestamp.between(time_mstone3, time_mstone4)).count()
    track5 = db.query(Gps).filter(Gps.timestamp.between(time_mstone4, time_mstone5)).count()
    track6 = db.query(Gps).filter(Gps.timestamp.between(time_mstone5, time_mstone6)).count()
    track7 = db.query(Gps).filter(Gps.timestamp.between(time_mstone6, time_mstone7)).count()
    track8 = db.query(Gps).filter(Gps.timestamp.between(time_mstone7, time_mstone8)).count()
    track9 = db.query(Gps).filter(Gps.timestamp.between(time_mstone8, time_mstone9)).count()
    track10 = db.query(Gps).filter(Gps.timestamp.between(time_mstone9, time_mstone10)).count()
    track11 = db.query(Gps).filter(Gps.timestamp.between(time_mstone10, time_mstone11)).count()
    track12 = db.query(Gps).filter(Gps.timestamp.between(time_mstone11, time_mstone12)).count()
    track_list = [{"slot": 2, "number" : int(track1)},{"slot": 4, "number" : int(track2)},
                {"slot": 6, "number" : int(track3)},{"slot": 8, "number" : int(track4)},
                {"slot": 10, "number" : int(track5)},{"slot": 12, "number" : int(track6)},
                {"slot": 14, "number" : int(track7)},{"slot": 16, "number" : int(track8)},
                {"slot": 18, "number" : int(track9)},{"slot": 20, "number" : int(track10)},
                {"slot": 22, "number" : int(track11)},{"slot": 24, "number" : int(track12)}]
    return jsonify(track_list)


if __name__ == "__main__":
	app.run(host = "0.0.0.0", debug = True)
	
