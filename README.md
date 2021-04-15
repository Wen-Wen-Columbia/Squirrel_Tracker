![image](https://github.com/Wen-Wen-Columbia/Squirrel_Tracker/blob/master/sightings/image/Welcome.jpg)

# Squirrel Tracker
This is Squirrel Tracker app for Joffrey Hosencratz and IEOR4501 Tools for Analytics (2021 Spring).

# Summary
This app tracks squirrels in NYC Central Park with attributions including Latitud, Longitude, Unique Squirrel ID, Shift, Date, Age, Primary Fur Color and more. Also, it shows the first 100 sightings marked on a map.The data was from the [2018 Central Park Squirrel Census Data](https://data.cityofnewyork.us/api/views/vfnx-vebw/rows.csv).

# Requirements
Use the package manager pip to install required packages(django==3.2).
```python
$ pip install -r requirements.txt
```

# Functions
This app supports:
- [x] A list containing all squirrel sightings
- [x] A map with the first 100 squirrel sightings
- [x] A new squirrel sighting adding
- [x] A existing squirrel sighting updating
- [x] General statistics about the exsiting squirrel sightings
- [x] commands that can import and export squirrel sightings as follows:
```python
# import:
python manage.py import_squirrel_data /path/to/file.csv

# export
python manage.py export_squirrel_data /path/to/file.csv
```

# Application Link
[Click](https://adept-crossing-309006.et.r.appspot.com/) to view this app. Or the link is https://adept-crossing-309006.et.r.appspot.com/.

# Contributors
Project Gourp 52

UNIs: [ww2573, qz2410]
