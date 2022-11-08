from flask import Flask

from app.handlers.routes import configure_routes

#Fedu, Medu, Walc, absences, age, failures, freetime, goout, health
def test_base_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)

    assert response.status_code == 200
    assert response.get_data() == b'try the predict route it is great!'

def test_predict_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict'

    response = client.get(url, query_string = {'Fedu': 4, 'Medu': 4, 'Walc': 1, 'absences': 0, 'age': 18, 'failures': 0, 'freetime': 1, 'goout': 1, 'health': 5})

    assert response.status_code == 200

def test_predict_route2():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict'

    response = client.get(url, query_string = {'Fedu': 4, 'Medu': 3, 'Walc': 2, 'absences': 6, 'age': 19, 'failures': 1, 'freetime': 3, 'goout': 3, 'health': 3})

    assert response.status_code == 200

def test_predict_route3():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict'

    response = client.get(url, query_string = {'Fedu': 0, 'Medu': 0, 'Walc': 5, 'absences': 93, 'age': 22, 'failures': 4, 'freetime': 5, 'goout': 5, 'health': 1})

    assert response.status_code == 200

# Out of Bound Input - Fedu is higher than given ranges
def test_predict_route4():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict'

    response = client.get(url, query_string = {'Fedu': 8, 'Medu': 4, 'Walc': 1, 'absences': 0, 'age': 18, 'failures': 0, 'freetime': 1, 'goout': 1, 'health': 5})
    assert response.status_code == 404

# Out of Bound Input - Negative absences
def test_predict_route5():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict'

    response = client.get(url, query_string = {'Fedu': 4, 'Medu': 4, 'Walc': 1, 'absences': -16, 'age': 18, 'failures': 0, 'freetime': 1, 'goout': 1, 'health': 5})

    assert response.status_code == 404


# Wrong Types - Fedu is a string
def test_predict_route5():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict'

    response = client.get(url, query_string = {'Fedu': 'good', 'Medu': 4, 'Walc': 1, 'absences': 0, 'age': 18, 'failures': 0, 'freetime': 1, 'goout': 1, 'health': 5})

    assert response.status_code == 404


# Missing One Input
def test_predict_route6():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict'

    response = client.get(url, query_string = {'Medu': 4, 'Walc': 1, 'absences': 0, 'age': 18, 'failures': 0, 'freetime': 1, 'goout': 1, 'health': 5})

    assert response.status_code == 404

# Missing Multiple Inputs
def test_predict_route6():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict'

    response = client.get(url, query_string = {'Walc': 1, 'absences': 0})

    assert response.status_code == 404

# Additional Input - famsize
def test_predict_route5():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict'

    response = client.get(url, query_string = {'Fedu': 4, 'Medu': 4, 'Walc': 1, 'absences': 0, 'age': 18, 'failures': 0, 'freetime': 1, 'goout': 1, 'health': 5, 'famsize':3 })

    assert response.status_code == 404
