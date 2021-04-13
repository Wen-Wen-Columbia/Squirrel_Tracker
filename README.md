![image](https://github.com/Wen-Wen-Columbia/Squirrel_Tracker/blob/master/sightings/image/Welcome.jpg)

# Squirrel Tracker
This is Squirrel Tracker project for Joffrey Hosencratz and for the IEOR4501 Tools for Analytics course (2021 Spring).

# Summary
This app can track squirrels in NYC Central Park with the attributions like Latitud, Longitude, Unique Squirrel ID, Shift, Date, Age, Primary Fur Color. Moreover, it shows a map with sightings.The data was imported from the [2018 Central Park Squirrel Census Data](https://data.cityofnewyork.us/api/views/vfnx-vebw/rows.csv).

# Requirements
Use the package manager pip to install required packages.
```python
$ pip install -r requirements.txt
```

# Functions
This app supports:
- [x] A list that contains all squirrel sightings
- [x] A map that plots the first 100 squirrel sightings
- [x] Add a new squirrel sighting
- [x] Update current sightings
- [x] Show some common statistics about the squirrel sightings
- [x] Import and export the data of squirrel sightings as follows:
```python
# import:
python manage.py import_squirrel_data /path/to/file.csv

# export
python manage.py export_squirrel_data /path/to/file.csv
```

# Application Link
[Click](https://adept-crossing-309006.et.r.appspot.com/) to view this app. Or the link for this app is https://adept-crossing-309006.et.r.appspot.com/.

# Contributors
Project Gourp 52

UNIs: [ww2573, qz2410]
