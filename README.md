# flask-API using SQLAlchemy

### 📚 Learning Objectives
- Create Models and migrate them to a Postgres database
- Perform CRUD Operations with SQLAlchemy
- Query it all via an API

## Project Initialization

Let's set up our app! We are going to need to
- Set up a virtual environment
- add our `.gitignore` _(curious what to put in it? Checkout [GitHub's suggested Python gitignore](https://github.com/github/gitignore/blob/master/Python.gitignore))_
- initialize and empty git repository
- Activate the virtual environment
- Upgrade our Pip in the venv
- Install Flask, Flask-Sqlalchemy, and Psycopg2
- Copy our installs into a `requirements.txt` file.
- Create a `models.py` file for our models and an `api.py` for our flask server.

_Not sure of the commands? Follow these:_

```zshell
python3 -m venv flaSQL
echo "lib\nbin\n__pycache__/\ninstance/\n.webassets-cache\n.vscode\n.DS_Store" >> .gitignore
git init
. flaSQL/bin/activate
pip install --upgrade pip
pip3 install flask
pip3 install Flask-SQLAlchemy
pip3 install psycopg2
pip3 freeze > requirements.txt
touch models.py api.py
```

## Model Setup

When using SQLAlchemy in a Flask server, they need to be able to communicate with each other. This setup is going to happen in our `models.py` file. We are doing it in this file because models are often set up initially and then left alone, so the Flask app setup makes sense to be here. 

>If you have app setup that's more sizable, you can put it in a separate file and import what you need from it.

After importing Flask from flask and SQLAlchemy from flask_sqlalchemy, the flask app needs to be created, the database URI set to it, and SQLAlchemy given the newly created and configured app.

```python=
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/flasql'
db = SQLAlchemy(app)
```

We have three config settings in here. 
1. `SQLALCHEMY_TRACK_MODIFICATIONS` is a feature that is going to be removed on the next major release. This line isn't necessary, but if we don't have it, it'll throw us a warning which is annoying. Also, the python community is big on being explicit which means delaring this to be false even though is defaulted to that behavior is a shibboleth you can use to show how cool you are with the python community.
2. `SQLALCHEMY_ECHO` will print out all the SQL queries it is issuing. This defaults to False, but since I'm a nosey dev, I want to see everything my middleware does, so I set this to true. If you want to keep your console clean and your debugging harder, you can take that line out or embody the python lifestyle and **explicity** set it to False.
3. `SQLALCHEMY_DATABASE_URI` is pretty self explanitory. This URI tells our program everything it needs to know about our databse. This database URI will change when going into production, but for now, localhost is where our postgres database lives. 
> A Database URI is crafted like this:
`[DB_TYPE]+[DB_CONNECTOR]://[USERNAME]:[PASSWORD]@[HOST]:[PORT]/[DB_NAME]`
For macs, the database connector, username, password, and port are all assumed. Note that not all operating systems function that way.

## To run the program in the terminal
export FLASK_ENV=development
export FLASK_APP=api.py
export FLASK_DEBUG=1    
flask run
