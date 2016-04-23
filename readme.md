
Install & setup
=====================
* With virtualenv
virtualenv flaskenv 
. flaskenv/bin/activate
python setup.py install

* install globally
python setup.py install

Run application
==================

python run.py

* enable DEBUG mode (inside run.py)
	line 4: app.run(debug=True)

* run globaly
	line 4 app.run(host='0.0.0.0', port=80, debug=False)
