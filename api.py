from flask import Flask,jsonify,request
from flask_pymongo import PyMongo
from flask_cors import CORS
app=Flask(__name__)
CORS(app)

app.config['MONGO_DBNAME']='waterdep'
app.config['MONGO_URI'] = 'mongodb://Vandit:password123@ds040489.mlab.com:40489/waterdep'

mongo = PyMongo(app)

@app.route('/api/getPressureData', methods=['GET'])
def get_all_data():
    data = mongo.db.pressure 

    output = []
    #deviceID = int(did,10)
    for j in data.find():
        output.append({'Time' : j['Time'], 'Pressure' : j['Pressure'], 'DeviceID' : j['DeviceID']})

    return jsonify({'result' : output})


@app.route('/api/getPressureData/<did>', methods=['GET'])
def get_all_data_with_device_id(did):
    data = mongo.db.pressure
    output = []
    deviceID = int(did,10)
    for j in data.find({'DeviceID': deviceID}).sort('Time',1):
        output.append({'Time' : j['Time'], 'Pressure' : j['Pressure'], 'DeviceID' : j['DeviceID']})
    
    
    return jsonify({'result' : output})

@app.route('/api/getWaterLevelData', methods=['GET'])
def get_all_water_level_data():
    data = mongo.db.waterLevel 
    output = []
    for j in data.find():
        output.append({'Time' : j['Time'], 'Water Level' : j['Water Level'], 'DeviceID' : j['DeviceID']})
    
    
    return jsonify({'result' : output}) 

@app.route('/api/getWaterLevelDatas/<did>', methods=['GET'])
def get_all_water_level_data_with_device_id(did):
    data = mongo.db.waterLevel 
    output = []
    deviceID = int(did,10)
    for j in data.find({'DeviceID': deviceID}).sort('Time',1):
        output.append({'Time' : j['Time'], 'Water Level' : j['Water Level'], 'DeviceID' : j['DeviceID']})
    
    
    return jsonify({'result' : output})

@app.route('/api/getWaterQualityData', methods=['GET'])
def get_all_water_quality_data():
    data = mongo.db.waterQuality 
    output = []
    for j in data.find():
        output.append({'Time' : j['Time'], 'Water Quality' : j['Water Quality'], 'DeviceID' : j['DeviceID']})
    
    
    return jsonify({'result' : output}) 

@app.route('/api/getWaterQualityData/<did>', methods=['GET'])
def get_all_water_quality_data_with_device_id(did):
    data = mongo.db.waterQuality 
    output = []
    deviceID = int(did,10)
    for j in data.find({'DeviceID': deviceID}).sort('Time',1):
        output.append({'Time' : j['Time'], 'Water Quality' : j['Water Quality'], 'DeviceID' : j['DeviceID']})
    
    
    return jsonify({'result' : output})



@app.route('/api/getWaterUnits', methods=['GET'])
def get_all_water_units_data():
    data = mongo.db.waterUnits 
    output = []
    for j in data.find():
        output.append({'Time' : j['Time'], 'Water Units' : j['WaterUnits'], 'DeviceID' : j['DeviceID']})
    
    
    return jsonify({'result' : output}) 

@app.route('/api/getWaterUnits/<did>', methods=['GET'])
def get_all_water_units_data_with_device_id(did):
    data = mongo.db.waterUnits
    output = []
    deviceID = int(did,10)
    for j in data.find({'DeviceID': deviceID}).sort('Time',1):
        output.append({'Time' : j['Time'], 'Water Units' : j['WaterUnits'], 'DeviceID' : j['DeviceID']})
    
    
    return jsonify({'result' : output})


if __name__ == '__main__':
    app.run()