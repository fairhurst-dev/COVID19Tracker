# reference https://github.com/suarez605/SpainRentalHeatMaps

import os
from flask import Flask, render_template, request
import pandas as pd
import folium
from folium.plugins import HeatMap


app = Flask(__name__)

app.secret_key = 'Veritas'

@app.route('/')
def display_intro():
    return render_template('index.html')

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
draw_map():
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


