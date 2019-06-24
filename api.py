from flask import Flask,jsonify,request
from flask_pymongo import PyMongo
app=Flask(__name__)

app.config['MONGO_DBNAME']='waterdep'
app.config['MONGO_URI'] = 'mongodb://Vandit:password123@ds040489.mlab.com:40489/waterdep'

mongo = PyMongo(app)

@app.route('/api/getPressureData', methods=['GET'])
def get_all_data():
    data = mongo.db.PressureSensor 

    output = []
    #deviceID = int(did,10)
    for j in data.find():
        output.append({'Time' : j['Time'], 'Pressure' : j['Pressure'], 'DeviceID' : j['Device ID']})

    return jsonify({'result' : output})


@app.route('/api/getPressureDataWithDeviceID/<did>', methods=['GET'])
def get_all_data_with_device_id(did):
    data = mongo.db.PressureSensor 
    output = []
    deviceID = int(did,10)
    for j in data.find({'Device ID': deviceID}):
        output.append({'Time' : j['Time'], 'Pressure' : j['Pressure'], 'DeviceID' : j['Device ID']})
    
    
    return jsonify({'result' : output})


if __name__ == '__main__':
    app.run()