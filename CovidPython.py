from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import pandas as pd
import folium
from folium.plugins import HeatMap
import os

# set FLASK_APP=CovidPython.py

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'db-mysql-nyc1-59147-do-user-8328444-0.b.db.ondigitalocean.com'
app.config['MYSQL_USER'] = 'doadmin'
app.config['MYSQL_PASSWORD'] = 'nre0x18lver0tcc6'
app.config['MYSQL_DB'] = 'COVID_DATA'
app.config['MYSQL_PORT'] = 25060

app.secret_key = 'Veritas'
mysql = MySQL(app)

input_dict = {'first_name': None, 'last_name': None, 'zip_code': None, 'date_of_birth': None, 'household_size': None,
              'difficulty_breathing': 0,
              'blue_lips': 0, 'chest_pain': 0, 'dizziness': 0, 'confusion': 0, 'slurring': 0, 'seizures': 0,
              'COVID_diagnosis': 0,
              'positive_test': 0, 'quarantine': 0, 'close_proximity': 0, 'coughed_on': 0, 'same_house': 0, 'fever': 0,
              'cough': 0,
              'short_breath': 0, 'fatigue': 0, 'aches': 0, 'headaches': 0, 'no_taste': 0, 'sore_throat': 0,
              'congestion': 0,
              'nausea': 0, 'lung_disease': 0, 'heart_condition': 0, 'weak_immune_system': 0, 'obesity': 0, 'smokes': 0,
              'diabetes': 0,
              'high_blood_pressure': 0, 'blood_disorder': 0, 'neurological_disorder': 0, 'cancer': 0,
              'feeling_today': 0, 'calculated_severity': 0}


@app.route('/', methods=['GET', 'POST'])
def baseline_data():
    msg = ''

    if request.method == 'POST':
        input_dict['first_name'] = request.form['first']
        input_dict['last_name'] = request.form['last']
        input_dict['zip_code'] = request.form['zip']
        input_dict['date_of_birth'] = request.form['DOB']
        input_dict['household_size'] = request.form['household']

        if not re.match(r'[A-Za-z]+', input_dict['first_name']):
            msg = 'First name must contain only characters!'
        elif not re.match(r'[A-Za-z]+', input_dict['last_name']):
            msg = 'Last name must contain only characters!'
        elif not re.match(r'[0-9]', input_dict['zip_code']):
            msg = 'Zip code must contain only numbers!'
        elif not re.match(r'[00000-99999]', input_dict['zip_code']):
            msg = 'Zip code must be in New Jersey!'
        elif not re.match(r'[0-9]', input_dict['date_of_birth']):
            msg = 'Date of birth must contain only numbers in MMDDYYYY format!'
        elif not re.match(r'[0-50]', input_dict['household_size']):
            msg = 'Household size contain only numbers less than 50!'
        elif not input_dict['first_name'] or not input_dict['last_name'] or not input_dict['zip_code'] or not \
        input_dict['date_of_birth'] or not input_dict['household_size']:
            msg = 'Please fill out the form!'
        elif request.method == 'POST':
            msg = 'Please fill out the form!'

    return render_template('index.html', msg=msg)

@app.route('/emergency_symptoms', methods=['GET', 'POST'])
def emergency_data():
    msg = ''
    url= ''
    emergency = [input_dict['difficulty_breathing'], input_dict['blue_lips'], input_dict['chest_pain'],
                 input_dict['dizziness'],
                 input_dict['confusion'], input_dict['slurring'], input_dict['seizures']
                 ]

    if request.method == 'POST':
        emergency_symptoms = request.form.getlist('emergency')

        if 'breathing' in emergency_symptoms:
            input_dict['difficulty_breathing'] = 1
        else:
            input_dict['difficulty_breathing'] = 0
        if 'blue' in emergency_symptoms:
            input_dict['blue_lips'] = 1
        else:
            input_dict['blue_lips'] = 0
        if 'chest' in emergency_symptoms:
            input_dict['chest_pain'] = 1
        else:
            input_dict['chest_pain'] = 0
        if 'dizziness' in emergency_symptoms:
            input_dict['dizziness'] = 1
        else:
            input_dict['dizziness'] = 0
        if 'confused' in emergency_symptoms:
            input_dict['confusion'] = 1
        else:
            input_dict['confusion'] = 0
        if 'speech' in emergency_symptoms:
            input_dict['slurring'] = 1
        else:
            input_dict['slurring'] = 0
        if 'seizures' in emergency_symptoms:
            input_dict['seizures'] = 1
        else:
            input_dict['seizures'] = 0

    return render_template('emergency_symptoms.html', url=url)


@app.route('/emergency_symptoms', methods=['GET', 'POST'])
def display_medical_emergency():

    return render_template('medical_emergency.html', methods=['GET','POST'])



@app.route('/exposure', methods=['GET', 'POST'])
def exposure_data():
    msg = ''
    exposure = []

    if request.method == 'POST':
        exposure = request.form.getlist('exposure')

        if 'diagnosed' in exposure:
            input_dict['COVID_diagnosis'] = 1
        else:
            input_dict['COVID_diagnosis'] = 0
        if 'positive' in exposure:
            input_dict['positive_test'] = 1
        else:
            input_dict['positive_test'] = 0
        if 'quarantine' in exposure:
            input_dict['quarantine'] = 1
        else:
            input_dict['quarantine'] = 0
        if '6feet' in exposure:
            input_dict['close_proximity'] = 1
        else:
            input_dict['close_proximity'] = 0
        if 'coughedon' in exposure:
            input_dict['coughed_on'] = 1
        else:
            input_dict['coughed_on'] = 0
        if 'lived' in exposure:
            input_dict['same_house'] = 1
        else:
            input_dict['same_house'] = 0

    return render_template('exposure.html', msg=msg)


@app.route('/wellness', methods=['GET', 'POST'])
def wellness_data():
    msg = ''
    wellness = []

    if request.method == 'POST':

        wellness = request.form.getlist('wellness')
        print(wellness)

        if 'fever' in wellness:
            input_dict['fever'] = 1
        else:
            input_dict['fever'] = 0
        if 'cough' in wellness:
            input_dict['cough'] = 1
        else:
            input_dict['cough'] = 0
        if 'short_breath' in wellness:
            input_dict['short_breath'] = 1
        else:
            input_dict['short_breath'] = 0
        if 'fatigue' in wellness:
            input_dict['fatigue'] = 1
        else:
            input_dict['fatigue'] = 0
        if 'aches' in wellness:
            input_dict['aches'] = 1
        else:
            input_dict['aches'] = 0
        if 'headaches' in wellness:
            input_dict['headaches'] = 1
        else:
            input_dict['headaches'] = 0

        if 'no_taste' in wellness:
            input_dict['no_taste'] = 1
        else:
            input_dict['no_taste'] = 0
        if 'sore_throat' in wellness:
            input_dict['sore_throat'] = 1
        else:
            input_dict['sore_throat'] = 0
        if 'congestion' in wellness:
            input_dict['congestion'] = 1
        else:
            input_dict['congestion'] = 0
        if 'nausea' in wellness:
            input_dict['nausea'] = 1
        else:
            input_dict['nausea'] = 0

        if 'lung_disease' in wellness:
            input_dict['lung_disease'] = 1
        else:
            input_dict['lung_disease'] = 0
        if 'heart_conditions' in wellness:
            input_dict['heart_condition'] = 1
        else:
            input_dict['heart_condition'] = 0
        if 'weak_immune_system' in wellness:
            input_dict['weak_immune_system'] = 1
        else:
            input_dict['weak_immune_system'] = 0
        if 'obesity' in wellness:
            input_dict['obesity'] = 1
        else:
            input_dict['obesity'] = 0
        if 'smokes' in wellness:
            input_dict['smokes'] = 1
        else:
            input_dict['smokes'] = 0
        if 'diabetes' in wellness:
            input_dict['diabetes'] = 1
        else:
            input_dict['diabetes'] = 0
        if 'blood_pressure' in wellness:
            input_dict['high_blood_pressure'] = 1
        else:
            input_dict['high_blood_pressure'] = 0
        if 'blood_disorder' in wellness:
            input_dict['blood_disorder'] = 1
        else:
            input_dict['blood_disorder'] = 0
        if 'neurological' in wellness:
            input_dict['neurological_disorder'] = 1
        else:
            input_dict['neurological_disorder'] = 0
        if 'cancer' in wellness:
            input_dict['cancer'] = 1
        else:
            input_dict['cancer'] = 0

    return render_template('wellness.html', msg=msg)


@app.route('/mental_health', methods=['GET', 'POST'])
def mental_health_data():
    msg = ''
    mental=[]

    mental = request.form.getlist('mental')

    if request.method == 'POST' and 'mental' in request.form:
        input_dict['feeling_today'] = mental[0]

    return render_template('mental_health.html', msg=msg)


@app.route('/view_survey_results')
def display_survey_results():
    msg = ''
    color = ""
    likelihood= ""
    step1 = ""
    step2 = ""
    step3 = ""

    symptoms = [input_dict['difficulty_breathing'], input_dict['chest_pain'],
                input_dict['fever'], input_dict['cough'],
                input_dict['short_breath'], input_dict['fatigue'], input_dict['aches'], input_dict['headaches'],
                input_dict['no_taste'], input_dict['sore_throat'], input_dict['congestion'], input_dict['nausea'],
                ]
    exposure = [input_dict['COVID_diagnosis'],
                input_dict['positive_test'], input_dict['quarantine'], input_dict['close_proximity'],
                input_dict['coughed_on'],
                input_dict['same_house']]

    total_symptoms = 0


    # calculate severity by averaging number of check boxes
    for x in symptoms:
        if x == 1:
            total_symptoms += 1
    input_dict['calculated_severity'] = round(total_symptoms / 12, 3)

    # immediate high severity for checking positive test or COVID diagnosis
    for y in exposure:
        if y == 1:
            input_dict['calculated_severity'] = 1.00

    print(input_dict)
    print(input_dict["calculated_severity"])

    if input_dict['calculated_severity'] > 0.0 and input_dict['calculated_severity'] < 0.33:
        color = "green"
        likelihood = "low"
        step1 = "1. Wear a mask and practice social distancing"
        step2 = "2. Practice good handwashing habits"
        step3 = "3. Stay healthy"

    elif input_dict['calculated_severity'] > 0.34 and input_dict['calculated_severity'] < 0.66:
        color = "yellow"
        likelihood = "medium"
        step1 = "1. Wear a mask and practice social distancing"
        step2 = "2. Contact a medical provider to discuss what to do next"
        step3 = "3. Schedule a COVID-19 test if possible"

    else:
        color = "red"
        likelihood = "high"
        step1 = "1. Immediately self-quarantine for 14 days"
        step2 = "2. Contact a medical provider and inform them of your symptoms"
        step3 = "3. Schedule a COVID-19 test as soon as possible"

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    cursor.execute('''INSERT INTO Collected_Data (
                         FIRST_NAME,
                         LAST_NAME,
                         ZIP_CODE,
                         DATE_OF_BIRTH,
                         HOUSEHOLD_SIZE,
                         DIFFICULTY_BREATHING,
                         BLUE_LIPS,
                         CHEST_PAIN,
                         DIZZINESS,
                         CONFUSION,
                         SLURRED_SPEECH,
                         SEIZURES,
                         COVID_DIAGNOSIS,
                         POSITIVE_TEST,
                         TOLD_TO_QUARANTINE,
                         PROXIMITY_TO_COVID,
                         COUGHED_ON,
                         LIVE_WITH_COVID,
                         FEVER_CHILLS,
                         COUGH,
                         SHORTNESS_OF_BREATH,
                         FATIGUE,
                         BODY_ACHES,
                         HEADACHES,
                         LOSS_OF_TASTE_SMELL,
                         SORE_THROAT,
                         CONGESTION,
                         NAUSEA_VOMITING,
                         LUNG_DISEASE,
                         HEART_CONDITIONS,
                         WEAKENED_IMMUNE_SYSTEM,
                         OBESITY,
                         SMOKE_CIGARETTES,
                         DIABETES,
                         HIGH_BLOOD_PRESSURE,
                         BLOOD_DISORDER,
                         NEUROLOGICAL_DISEASE,
                         CANCER,
                         FEELING_TODAY,
                         CALCULATED_SEVERITY
                         ) VALUES
                        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                         %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                         %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                         %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                   (
                       input_dict['first_name'],
                       input_dict['last_name'],
                       input_dict['zip_code'],
                       input_dict['date_of_birth'],
                       input_dict['household_size'],
                       input_dict['difficulty_breathing'],
                       input_dict['blue_lips'],
                       input_dict['chest_pain'],
                       input_dict['dizziness'],
                       input_dict['confusion'],

                       input_dict['slurring'],
                       input_dict['seizures'],
                       input_dict['COVID_diagnosis'],
                       input_dict['positive_test'],
                       input_dict['quarantine'],
                       input_dict['close_proximity'],
                       input_dict['coughed_on'],
                       input_dict['same_house'],
                       input_dict['fever'],
                       input_dict['cough'],

                       input_dict['short_breath'],
                       input_dict['fatigue'],
                       input_dict['aches'],
                       input_dict['headaches'],
                       input_dict['no_taste'],
                       input_dict['sore_throat'],
                       input_dict['congestion'],
                       input_dict['nausea'],
                       input_dict['lung_disease'],
                       input_dict['heart_condition'],

                       input_dict['weak_immune_system'],
                       input_dict['obesity'],
                       input_dict['smokes'],
                       input_dict['diabetes'],
                       input_dict['high_blood_pressure'],
                       input_dict['blood_disorder'],
                       input_dict['neurological_disorder'],
                       input_dict['cancer'],
                       input_dict['feeling_today'],
                       input_dict['calculated_severity']))

    mysql.connection.commit()
    msg = 'You have successfully completed entering the data!'
    return render_template('view_survey_results.html', calculated_severity = input_dict['calculated_severity'], color=color, likelihood=likelihood, step1=step1, step2=step2, step3=step3 )


@app.route('/drawMap')
def draw_map():
    update()

    map_data = pd.read_csv('./Data/us-zip-codes-cleaned.csv')

    lat = 40.05
    lon = -74.40

    starting_location = [lat, lon]  # starting location of the map depending on the inputted zipcode
    h_map = folium.Map(location=starting_location, zoom_start=8)
    max_amount = map_data['Risk'].max()
    hm_wide = HeatMap(
        list(zip(map_data.Lat.values, map_data.Long.values, map_data.Risk.values)),
        min_opacity=0.1, max_zoom=9,
        max_val=max_amount,
        radius=25, blur=20
    )
    # Adds the heatmap element to the map
    h_map.add_child(hm_wide)
    # Saves the map to heatmap.html
    h_map.save(os.path.join('./templates', 'heatmap.html'))
    # Render the heatmap
    return render_template('heatmap.html')


def update():
    new_risk = round(input_dict['calculated_severity'] * 100, 3)
    imported_zip = input_dict['zip_code']

    if imported_zip[0] == "0":
        imported_zip = imported_zip[1:]

    df = pd.read_csv('./Data/us-zip-codes-cleaned.csv', sep=',')

    df.loc[(df.Zipcode == imported_zip), 'Risk'] = new_risk

    print(df.loc[(df.Zipcode == input_dict['zip_code'])])

    df.to_csv(r'./Data/us-zip-codes-cleaned.csv', index=False)

    return


app.run(host='localhost', port=5000)
