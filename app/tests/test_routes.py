from flask import Flask

from app.handlers.routes import configure_routes

#think about how the api should behave when the request body fields are as expected, and when its not
def test_base_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)

    assert response.status_code == 200
    assert response.get_data() == b'try the predict route it is great!'

def test_predict_route(): #what is being returned?
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict'

    response = client.get(url, query_string = {'school':"GP", 'higher':"yes", 'Mjob': "teacher", 'Fjob': "health", 'studytime':8, 'paid':"yes", 'failures':0})

    assert response.status_code == 200

def test_predict_route2():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict'

    response = client.get(url, query_string = {'school':"GP", 'higher':"yes", 'Mjob': "services", 'Fjob': "other", 'studytime':4, 'paid':"yes", 'failures':1})

    assert response.status_code == 200

def test_predict_route3():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict'

    response = client.get(url, query_string = {'school':"MS", 'higher':"no", 'Mjob': "at_home", 'Fjob': "at_home", 'studytime':0, 'paid':"no", 'failures':3})

    assert response.status_code == 200

# Incorrect Input - School Name
def test_predict_route4():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict'

    response = client.get(url, query_string = {'school':"hi", 'higher':"yes", 'Mjob': "civil", 'Fjob': "health", 'studytime':8, 'paid':"yes", 'failures':0})

    assert response.status_code == 404

# Out of Bound Input - Negative Study Time
def test_predict_route5():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict'

    response = client.get(url, query_string = {'school':"MS", 'higher':"yes", 'Mjob': "teacher", 'Fjob': "health", 'studytime':-1, 'paid':"yes", 'failures':0})

    assert response.status_code == 404


# Wrong Types - School is an Int
def test_predict_route5():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict'

    response = client.get(url, query_string = {'school':9, 'higher':"yes", 'Mjob': "teacher", 'Fjob': "health", 'studytime':8, 'paid':"yes", 'failures':0})

    assert response.status_code == 404


# Missing One Input
def test_predict_route6():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict'

    response = client.get(url, query_string = {'school':"GP", 'higher':"yes", 'Mjob': 'teacher', 'Fjob': "health", 'studytime':8, 'paid':"yes"})

    assert response.status_code == 404

# Missing Multiple Inputs
def test_predict_route6():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict'

    response = client.get(url, query_string = {'school':"GP", 'higher':"yes"})

    assert response.status_code == 404

# Additional Input - famsize
def test_predict_route5():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict'

    response = client.get(url, query_string = {'school':"MS", 'higher':"yes", 'Mjob': "teacher", 'Fjob': "health", 'studytime':-1, 'paid':"yes", 'failures':0, 'famsize':3 })

    assert response.status_code == 404
