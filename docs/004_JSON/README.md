# Returning JSON

In this step we will create a ini file where we will store the settings for our application. 

## Objectives
* Switch our application to return JSON
* Modify the unit tests test the returned json

## Steps

Modify our view config decorators to add `renderer='json` and modify the return insted of a pyramid response object we 
need to return a dictionary. 

```python
from pyramid.view import view_config

#from .. import models

@view_config(route_name='addhorse', renderer='json')
def add_horse(request):
    return {'viewname': 'addhorse'}

@view_config(route_name='delhorse', renderer='json')
def delete_horse(request):
    return {'viewname': 'delhorse'}

@view_config(route_name='viewhorse', renderer='json')
def view_horse(request):
    return {'viewname': 'viewhorse'}
```

Next modify your `test_views.py` to change the test to test for the json response instead of just a 200 status code. 

```python
import unittest

from pyramid import testing


class MidwayViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_add_horse(self):
        from midway.views.default import add_horse
        request = testing.DummyRequest()
        response = add_horse(request)
        self.assertEqual('addhorse', response['viewname'])

    def test_del_horse(self):
        from midway.views.default import delete_horse
        request = testing.DummyRequest()
        response = delete_horse(request)
        self.assertEqual('delhorse', response['viewname'])

    def test_view_horse(self):
        from midway.views.default import view_horse
        request = testing.DummyRequest()
        response = view_horse(request)
        self.assertEqual('viewhorse', response['viewname'])
```