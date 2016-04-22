-------------------------
MOBILE & INTERNET 4
Habimana Martial
-------------------------

Requirements
=============
* Python 2.7
* Sqlite3
* pip (python packae installer)
* virtualenv (optioneel lees:http://flask.pocoo.org/docs/0.10/installation/)

Install & setup
=====================
* met virtualenv
virtualenv flaskenv 
. flaskenv/bin/activate
python setup.py install

* zonder
python setup.py install

Run application
==================

python run.py

* enable DEBUG mode (inside run.py)
	line 4: app.run(debug=True)

* run globaly
	line 4 app.run(host='0.0.0.0', port=80, debug=False)
	!-> Je moet root gebruiker zijn om poort 80 te gebruiken


