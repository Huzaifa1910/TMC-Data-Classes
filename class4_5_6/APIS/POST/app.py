from flask import Flask, request, jsonify
import mysql.connector #pip install mysql-connector
from datetime import datetime 
app = Flask(__name__)

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tmc_hr_prod"
)

@app.route('/attendanceApp/employee/attendance/add', methods=['POST'])
def post_data():
    try:
        data = request.get_json()
        name = data['name']
        email = data['email']
        type = data['type']
        remoteType = data['remote_type']
        latitude = 31.4703872
        longitude = 74.3079936
        timestamp = datetime.now()
        remarks = ""
        mycursor = mydb.cursor()
        sql = "INSERT INTO hr_time_attendance (app_time_stamp,latitude,longitude,remarks,remote_type,type,user_email, user_name) VALUES (%s, %s,%s, %s,%s, %s,%s, %s)"
        val = (timestamp,latitude,longitude,remarks,remoteType,type,email,name)
        mycursor.execute(sql, val)
        mydb.commit()
        return jsonify({"status": "success"})
    except Exception as e:
        print(e)

if __name__ == '__main__':
    app.run(debug=True)