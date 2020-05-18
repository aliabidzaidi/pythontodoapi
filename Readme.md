## Running directly

```
python app.py
```

## Running with Factory method

create factory method using https://flask.palletsprojects.com/en/1.1.x/tutorial/factory/#the-application-factory

```
$env:FLASK_APP = "flaskr:create_app()"
$env:FLASK_ENV = "development"
flask run
```

## Deploying for production

configre setup.py with packages using https://flask.palletsprojects.com/en/1.1.x/tutorial/install/
```
python setup.py bdist_wheel
```

create new folder for installing .whl

```
pipenv install --python 2.7
pipenv shell
pip install .whl file
waitress-serve --listen *:5000  --call 'flaskr:create_app'
```
