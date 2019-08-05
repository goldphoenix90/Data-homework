import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

app = Flask(__name__)

@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return (
        f"Thinking of going to Hawaii?</br>"
        f"Check out these API routes to find out about precipitation and temperature the past year.</br>"
        f"Latest reading is dated 2017-08-23.</br>"
        f"Please write the start and end dates in yyyy-mm-dd format</br>"
        f"/api/v1.0/precipitation</br>"
        f"/api/v1.0/stations</br>"
        f"/api/v1.0/tobs</br>"
        f"/api/v1.0/start</br>"
        f"/api/v1.0/start/end")


@app.route("/api/v1.0/precipitation")
def precip():
    print("Server received request for 'Precipitation' page...")
    session = Session(engine)
    results = session.query(Measurement.date, Measurement.prcp).all()
    Precipitation = []
    for date, precipitation in results:
        precip_dict = {}
        precip_dict["date"] = date
        precip_dict["prcp"] = precipitation
        Precipitation.append(precip_dict)

    return jsonify(Precipitation)


@app.route("/api/v1.0/stations")
def station():
    print("Server received request for 'Stations' page...")
    session = Session(engine)
    results = session.query(Station.name).group_by(Station.name).all()
    station_list = list(np.ravel(results))
    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def temp():
    print("Server received request for 'Temperatures' page...")
    session = Session(engine)
    results = session.query(Measurement.date, Measurement.tobs).\
                                filter(Measurement.date > '2016-08-23').\
                                filter(Measurement.date < '2017-08-23').\
                                order_by(Measurement.date).all()
    temp_last_year=[]
    for date, temperature in results:
        temp_dict={}
        temp_dict["date"] = date
        temp_dict["tobs"] = temperature
        temp_last_year.append(temp_dict)
    return jsonify(temp_last_year)

@app.route("/api/v1.0/<start>")
def start(start):
    print("Server received request for 'Temperature Start' page...")
    session = Session(engine)
    # start=start_date
    summary=[]
    min_temp = session.query(func.min(Measurement.tobs)).filter(Measurement.date > start).all()
                                
    max_temp = session.query(func.max(Measurement.tobs)).filter(Measurement.date > start).all()
                                
    avg_temp = session.query(func.avg(Measurement.tobs)).filter(Measurement.date > start).all()
                           
    summary.append(min_temp)
    summary.append(max_temp)
    summary.append(avg_temp)

    return jsonify(summary)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    print("Server received request for 'Temperatures Start End' page...")
    session = Session(engine)
    summary=[]
    min_temp = session.query(func.min(Measurement.tobs)).filter(Measurement.date > start).\
                                filter(Measurement.date < end).all()                    
    max_temp = session.query(func.max(Measurement.tobs)).filter(Measurement.date > start).\
                                filter(Measurement.date < end).all()                         
    avg_temp = session.query(func.avg(Measurement.tobs)).filter(Measurement.date > start).\
                                filter(Measurement.date < end).all()            
    summary.append(min_temp)
    summary.append(max_temp)
    summary.append(avg_temp)

    return jsonify(summary)

if __name__ == "__main__":
    app.run(debug=True)