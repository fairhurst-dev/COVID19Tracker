# reference https://github.com/suarez605/SpainRentalHeatMaps

import os
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import pandas as pd
import folium
from folium.plugins import HeatMap

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'COVID_DATA'

mysql = MySQL(app)

app.secret_key = 'Veritas'

@app.route('/', methods=['GET', 'POST'])
def display_intro():
    msg =''
    if request.method == 'POST' and 'first' in request.form and 'last' in request.form and 'zip' in request.form and 'DOB' in request.form and 'household' in request.form :
        first_name = request.form['first']
        last_name = request.form['last']
        zip_code = request.form['zip']
        date_of_birth = request.form['DOB']
        household_size = request.form['household']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        print(first_name + last_name)

        if not re.match(r'[A-Za-z]+', first_name):
            msg = 'First name must contain only characters!'
        elif not re.match(r'[A-Za-z]+', last_name):
            msg = 'Last name must contain only characters!'
        elif not re.match(r'[0-9]', zip_code):
            msg = 'Zip code must contain only numbers!'
        elif not re.match(r'[0-9]', date_of_birth):
            msg = 'Date of birth must contain only numbers in MMDDYYYY format!'
        elif not first_name or not last_name or not zip_code or not date_of_birth:
            msg = 'Please fill out the form!'
        else:
            cursor.execute('INSERT INTO Collected_Data (FIRST_NAME, LAST_NAME) VALUES ( %s, %s)',
                           (first_name, last_name))

            mysql.connection.commit()
            msg = 'You have successfully completed entering the data!'
            cursor.close()
            msg= 'You have entered all baseline data'


    elif request.method == 'POST':
        msg = 'Please fill out the form!'


    return render_template('index.html', msg=msg)

@app.route('/emergency_symptoms', methods=['GET','POST'])
def display_emergency_symptoms():
    if request.method == 'POST':
        emergency = []
        emergency = request.form.getlist('emergency')
        print(emergency)
    return render_template('emergency_symptoms.html')

@app.route('/exposure', methods=['GET', 'POST'])
def display_exposure():
    if request.method == 'POST':
        exposure = []
        exposure = request.form.getlist('exposure')
        print(exposure)
    return render_template('exposure.html')

@app.route('/view_survey_results')
def display_survey_results():
    return render_template('view_survey_results.html')

@app.route('/drawMap')
def draw_map():
    map_data = pd.read_csv('./Data/us-zip-codes-cleaned.csv')
    lat = map_data['Lat'].mean()
    lon = map_data['Long'].mean()
    startingLocation = [lat, lon]  # [40.05, 74.40]
    hmap = folium.Map(location=startingLocation, zoom_start=8)
    max_amount = map_data['Risk'].max()
    hm_wide = HeatMap(
        list(zip(map_data.Lat.values, map_data.Long.values, map_data.Risk.values)),
        min_opacity=0.05,
        max_val=max_amount,
        radius=25, blur=15,
        max_zoom=4)

    # Adds the heatmap element to the map
    hmap.add_child(hm_wide)
    # Saves the map to heatmap.html
    hmap.save(os.path.join('./templates', 'heatmap.html'))
    # Render the heatmap
    return render_template('heatmap.html')

app.run(host='localhost', port=5000)


