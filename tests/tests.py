import unittest
import pytest
from unittest.mock import patch
from app import app
from faker import Faker
import json


@pytest.fixture 
def client():
    app.config['Testing'] = True 
    with app.test_client() as client:
        yield client


class TestEmployees(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_post(client, mocker):
        fake = Faker()
        name = fake.random_letters()
        position = fake.random_letters()
        payload = {'id': 1, 'name': name, 'position': position}

        mocker.patch.object(client, 'post', return_value=app.response_class(
        response= json.dumps({'id': 1, 'name': name, 'position': position}),
        status=200,
        mimetype='application/json'
        ))

        response = client.post('/employees', json=payload)
        data=response.get_json()
        assert data['result'] == payload



    def test_get(self):

        payload = {'id': 1, 'name': 'Sam', 'position': 'admin'}
        response = self.app.get('/employees', json=payload)
        data = response.get_json()
        self.assertEqual(data['result'], 200)


class TestProduct(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_post(client, mocker):

        fake = Faker()
        name = fake.random_letters()
        price = fake.random_digit(digits=3)
        payload = {'id': 1, 'name': name, 'price': price}

        mocker.patch.object(client, 'post', return_value=app.response_class(
        response= json.dumps({'id': 1, 'name': name, 'price': price}),
        status=200,
        mimetype='application/json'
        ))

        response = client.post('/products', json=payload)
        data=response.get_json()
        assert data['result'] == payload


    def test_get(self):

        payload = {'id': 1, 'name': 'laptop', 'price': 30.99}
        response = self.app.get('/products', json=payload)
        data = response.get_json()
        self.assertEqual(data['result'], 200)


class TestOrders(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_post(client, mocker):
        fake = Faker()
        
        customer_id = fake.random_digit(digits=1)
        product_id = fake.random_digit(digits=1)
        quantity = fake.random_digit(digits=2)
        total_price = fake.random_digit(digits=3)
        payload = {'id': 1, 'customer_id': customer_id, 'product_id': product_id, 'quantity': quantity, 'total_price': total_price}

        mocker.patch.object(client, 'post', return_value=app.response_class(
        response= json.dumps({'id': 1, 'customer_id': customer_id, 'product_id': product_id, 'quantity': quantity, 'total_price': total_price}),
        status=200,
        mimetype='application/json'
        ))

        response = client.post('/orders', json=payload)
        data=response.get_json()
        assert data['result'] == payload



    def test_get(self):

        payload = {'id': 1, 'customer_id': 1, 'product_id': 1, 'quantity': 20, 'total_price': 100}
        response = self.app.get('/orders', json=payload)
        data = response.get_json()
        self.assertEqual(data['result'], 200)


class TestCustomers(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_post(client, mocker):
        fake = Faker()
        name = fake.random_letters()
        email = fake.email()
        phone = fake.phone_number()
        payload = {'id': 1, 'name': name, 'email': email, 'phone': phone}

        mocker.patch.object(client, 'post', return_value=app.response_class(
        response= json.dumps({'id': 1, 'name': name, 'email': email, 'phone': phone}),
        status=200,
        mimetype='application/json'
        ))

        response = client.post('/customers', json=payload)
        data=response.get_json()
        assert data['result'] == payload



    def test_get(self):

        payload = {'id': 1, 'name': 'Sam', 'email': 'samuelckraft@gmail.com', 'phone': '6154565555'}
        response = self.app.get('/customers', json=payload)
        data = response.get_json()
        self.assertEqual(data['result'], 200)


class TestProduction(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_post(client, mocker):
        fake = Faker()
        product_id = fake.random_digit(digits=1)
        quantity_produced = fake.random_digit(digits=2)
        date_produced = fake.date()

        payload = {'id': 1, 'product_id': product_id, 'quantity_produced': quantity_produced, 'date_produced': date_produced}

        mocker.patch.object(client, 'post', return_value=app.response_class(
        response= json.dumps({'id': 1, 'product_id': product_id, 'quantity_produced': quantity_produced, 'date_produced': date_produced}),
        status=200,
        mimetype='application/json'
        ))

        response = client.post('/production', json=payload)
        data=response.get_json()
        assert data['result'] == payload



    def test_get(self):

        payload = {'id': 1, 'product_id': 1, 'quantity_produced': 20, 'date_produced': '2024-01-01'}
        response = self.app.get('/production', json=payload)
        data = response.get_json()
        self.assertEqual(data['result'], 200)


if __name__ == '__main__':
    pytest.main([__file__]) 