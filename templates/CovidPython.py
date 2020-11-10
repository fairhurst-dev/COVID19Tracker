from flask import FLASK, render_template, request, redirect, url_for, sessionfrom flask_mysqldb import MYSQLimport MySQLdb.cursorsimport reapp = Flask(__name__)app.config['MYSQL_HOST'] = 'MyConnection'app.config['MYSQL_USER'] = 'root'app.config['MYSQL_PASSWORD'] = 'root'app.config['MYSQL_DB'] = 'COVID_DATA'mysql = MYSQL(APP)@app.route('/BaselineData', methods=['GET', 'POST'])def baselineData():       if request.method == 'POST' and 'first' in request.form   and 'last' in request.form   and 'zip' in request.form   and 'DOB' in request.form   and 'household' in request.form           first_name = request.form['first']        last_name = request.form['last']        zip_code = request.form['zip']        date_of_birth = request.form['DOB']        household_size = request.form['household']if not re.match(r'[^@]+@[^@]+\.[^@]+', email):            msg = 'Invalid email address!'        elif not re.match(r'[A-Za-z]+', first_name):            msg = 'First name must contain only characters!'        elif not re.match(r'[A-Za-z]+', last_name):            msg = 'Last name must contain only characters!'        elif not re.match(r'[0-9]', zip_code):            msg = 'Zip code must contain only numbers!'        elif not re.match(r'[07001-08989]' ,zip_code):            msg = 'Zip code must be in New Jersey!'        elif not re.match(r'[0-9]', date_of_birth):            msg = 'Date of birth must contain only numbers in MMDDYYYY format!'            elif not first_name or not last_name or not zip_code or not date_of_birth:            msg = 'Please fill out the form!'        elif request.method == 'POST':            msg = 'Please fill out the form!'                return render_template('index.html', msg=msg)@app.route('/EmergencyData', methods=['GET', 'POST'])def emergencyData():if request.method == 'POST' and 'first' in request.form    and 'breathing' in request.form,    and 'blue' in request.form,    and 'chest' in request.form,    and 'dizziness' in request.form,    and 'confused' in request.form,    and 'speech' in request.form,    and 'seizures' in request.form,                difficulty_breathing = request.form.get('breathing')        blue_lips = request.form.get('blue')        chest_pain = request.form.get('chest')        dizziness = request.form.get('dizziness')        confusion = request.form.get('confused')        slurring = request.form.get('speech')        seizures = request.form.get('seizures')    return render_template('emergency_symptoms.html', msg=msg)@app.route('/ExposureData', methods=['GET', 'POST'])def exposureData():if request.method == 'POST' and 'first' in request.form    and 'diagnosed' in request.form,    and 'positive' in request.form,    and 'quarantine' in request.form,    and '6feet' in request.form,    and 'coughedon' in request.form,    and 'lived' in request.form,        COVID_diagnosis = request.form.get('diagnosed')        positive_test = request.form.get('positive')        quarantine = request.form.get('quarantine')        close_proximity = request.form.get('6feet')        coughed_on = request.form.get('coughedon')        same_house = request.form.get('lived')            return render_template('exposure.html', msg=msg)@app.route('/WellnessData', methods=['GET', 'POST'])def wellnessData():if request.method == 'POST' and 'first' in request.form    and 'fever' in request.form,    and 'cough' in request.form,    and 'short_breath' in request.form,    and 'fatigue' in request.form,    and 'aches' in request.form,    and 'headaches' in request.form,    and 'no_taste' in request.form,    and 'sore_throat' in request.form,    and 'congestion' in request.form,    and 'nausea' in request.form,    and 'lung_disease' in request.form,    and 'heart_conditions' in request.form,    and 'weak_immune_system' in request.form,    and 'obesity' in request.form,    and 'smokes' in request.form,    and 'diabetes' in request.form,    and 'blood_pressure' in request.form,    and 'blood_disorder' in request.form,    and 'neurological' in request.form,    and 'cancer' in request.form,                fever = request.form.get('fever')        cough = request.form.get('cough')        short_breath = request.form.get('short_breath')        fatigue = request.form.get('fatigue')        aches = request.form.get('aches')        headaches = request.form.get('headaches')        no_taste = request.form.get('no_taste')        sore_throat = request.form.get('sore_throat')        congestion = request.form.get('congestion')        nausea = request.form.get('nausea')        lung_disease = request.form.get('lung_disease')        heart_condition = request.form.get('heart_condition')        weak_immune_system = request.form.get('weak_immune_system')        obesity = request.form.get('obesity')        smokes = request.form.get('smokes')        diabetes = request.form.get('diabetes')        high_blood_pressure = request.form.get('blood_pressure')        blood_disorder = request.form.get('blood_disorder')        neurological_disease = request.form.get('neurological')        cancer = request.form.get('cancer')            return render_template('wellness.html', msg=msg)@app.route('/FeelingToday', methods=['GET', 'POST'])def feelingToday():if request.method == 'POST' and 'first' in request.form    and 'feeling_today' in request.form:               feeling_today = request.form['feeling_today']        symptoms = [difficult_breathing, blue_lips, chest_pain, dizziness, confusion, slurring,                     seizures, COVID_diagnosis, positive_test, quarantine, close_proximity, coughed_on,                     same_house, fever, cough, short_breath, fatigue, aches, headaches, no_taste,                     sore_throat, congestion, nausea, lung_disease, heart_condition, weak_immune_system,                     obesity, smokes, diabetes, high_blod_pressure, blood_disorder,                     neurological_disorder, cancer]                for x in symptoms:            if x = 1:                total_symptoms += 1        calculated_severity = total_symptoms / 33                cursor.execute('''INSERT INTO COVID_DATA (                        first_name,                        last_name,                        zip_code,                        date_of_birth,                        household_size,                        difficulty_breathing,                        blue_lips,                        chest_pain,                        dizziness,                        confusion,                        slurring,                        seizures,                        COVID_diagnosis,                        positive_test,                        quarantine,                        close_proximity,                        coughed_on,                        same_house,                        fever,                        cough,                        short_breath,                        fatigue,                        aches,                        headaches,                        no_taste,                        sore_throat,                        congestion,                        nausea,                        lung_disease,                        heart_condition,                        weak_immune_system,                        obesity,                        smokes,                        diabetes,                        high_blood_pressure,                        blood_disorder,                        neurological_disease,                        cancer,                        feeling_today,                        calculuated_severity                       ) VALUES                       (%d, %s, %s, %s, %s, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d,                       %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %f, %f)''',                       (                        USER_ID,                        FIRST_NAME,                        LAST_NAME,                        ZIP_CODE,                        DATE_OF_BIRTH,                        HOUSEHOLD_SIZE,                        DIFFICULTY_BREATHING,                        BLUE_LIPS,                        CHEST_PAIN,                        DIZZINESS,                        CONFUSION,                        SLURRED_SPEECH,                        SEIZURES,                        COVID_DIAGNOSIS,                        POSITIVE_TEST,                        TOLD_TO_QUARANTINE,                        PROXIMITY_TO_COVID,                        COUGHED_ON,                        LIVE_WITH_COVID,                        FEVER_CHILLS,                        COUGH,                        SHORTNESS_OF_BREATH,                        FATIGUE,                        BODY_ACHES,                        HEADACHES,                        LOSS_OF_TASTE_SMELL,                        SORE_THROAT,                        CONGESTION,                        NAUSEA_VOMITING,                        LUNG_DISEASE,                        HEART_CONDITIONS,                        WEAKENED_IMMUNE_SYSTEM,                        OBESITY,                        SMOKE_CIGARETTES,                        DIABETES,                        HIGH_BLOOD_PRESSURE,                        BLOOD_DISORDER,                        NEUROLOGICAL_DISEASE,                        CANCER,                        FEELING_TODAY,                        CALCULATED_SEVERITY))cursor.execute("""             CREATE TEMPORARY TABLE SYMPTOM_COUNT            SELECT COVID_DATA.ZIP_CODE, ZIP_CODES.LAT, ZIP_CODES.LONG, AVG(COVID_DATA.CALCULATED_SEVERITY)            FROM COVID_DATA            JOIN ZIP_CODES ON COVID_DATA.ZIP_CODE = ZIP_CODES.ZIPCODE            GROUP BY ZIP_CODE            );""")avg_zip = cursor.fetchall()avg_zip_list = [list(i) for i in avg_zip]cursor.execute("""            CREATE TEMPORARY TABLE AVG_FEELING            SELECT AVG(FEELING_TODAY)            FROM COVID_DATA            """)                            mysql.connection.commit()        msg = 'You have successfully completed entering the data!'    return render_template('Covid_Data.html', msg=msg)if __name__ == '__main__':    app.run()