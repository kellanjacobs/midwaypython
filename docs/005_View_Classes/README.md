# View Classes

In pyramid any route can return any view callable. Or any object that has a __call__ method. Up until this point we have
used standard python functions to define the code that is run when a url is requested. Often times though especially in API
development we find that code has logical groupings. Or sometimes we need to use the same setup for multiple functions.
In cases like this it is better to group these functions into a class. 

## Objectives
* Change our functions into a classes.
* Add default render to our view classes so we do not have to call it for each method.
* Add the other URLs that our application will need. 
* Update our unit tests to cover our new urls.

## Steps

First lets convert our functions into a single class. Open the `views/horse.py` file and change the code into a class.

```python
from pyramid.view import view_config

#from .. import models

class HorseViews:

    def __init__(self, request):
        self.request = request

    @view_config(route_name='addhorse', renderer='json')
    def add_horse(self):
        return {'viewname': 'addhorse'}

    @view_config(route_name='delhorse', renderer='json')
    def delete_horse(self):
        return {'viewname': 'delhorse'}

    @view_config(route_name='viewhorse', renderer='json')
    def view_horse(self):
        return {'viewname': 'viewhorse'}
```

Notice how each method @view_config decorator has `renderer='json'` We can move this up to the class level. Pyramid has 
the view_default decorator that we can add to the class to set defaults that will be used in each method. Lets try 
adding it.

```python
from pyramid.view import (
    view_config,
    view_defaults
    )

#from .. import models

@view_defaults(renderer='json')
class HorseViews:

    def __init__(self, request):
        self.request = request

    @view_config(route_name='addhorse')
    def add_horse(self):
        return {'viewname': 'addhorse'}

    @view_config(route_name='delhorse')
    def delete_horse(self):
        return {'viewname': 'delhorse'}

    @view_config(route_name='viewhorse')
    def view_horse(self):
        return {'viewname': 'viewhorse'}

```

Now that we have have updated the views into a class. Lets had three new urls. 

* /standings/races Will return a list of all races with the results
* /standings/horses Will return a list of all the horses in standing order. 
* /race/RACEID Will return the results of a single race.

Create a new file `midway/midway/views/standing.py` to the new StandingViews class.

```python
from pyramid.view import (
    view_config,
    view_defaults
    )

#from .. import models


@view_defaults(renderer='json')
class StandingViews:

    def __init__(self, request):
        self.request = request

    @view_config(route_name='horsestanding')
    def horse_standing(self):
        return {'viewname': 'horse standing'}

    @view_config(route_name='racestanding')
    def race_standing(self):
        return {'viewname': 'race standing'}
```

Create a new file `midway/midway/views/race.py` to the new RaceViews class.

```python
from pyramid.view import (
    view_config,
    view_defaults
    )

#from .. import models


@view_defaults(renderer='json')
class RaceViews:

    def __init__(self, request):
        self.request = request

    @view_config(route_name='singlerace')
    def race_results(self):
        return {'viewname': 'Single Race'}
```

Now lets add our new routes to our `routes.py` file.

```python
def includeme(config):
    config.add_route('addhorse', '/horse/add')
    config.add_route('delhorse', '/horse/delete')
    config.add_route('viewhorse', '/horse/{horseid}')
    config.add_route('racestanding', '/standings/race')
    config.add_route('horsestanding', '/standings/horses')
    config.add_route('singlerace', '/race/{raceid}')
```

Last lets modify our tests to not only take advantage of our changing to classes but also that add our three new urls.

```python
import unittest

from pyramid import testing


class HorseViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_add_horse(self):
        from midway.views.horse import HorseViews
        request = testing.DummyRequest()
        inst = HorseViews(request)
        response = inst.add_horse()
        self.assertEqual('addhorse', response['viewname'])

    def test_del_horse(self):
        from midway.views.horse import HorseViews
        request = testing.DummyRequest()
        inst = HorseViews(request)
        response = inst.delete_horse()
        self.assertEqual('delhorse', response['viewname'])

    def test_view_horse(self):
        from midway.views.horse import HorseViews
        request = testing.DummyRequest()
        inst = HorseViews(request)
        response = inst.view_horse()
        self.assertEqual('viewhorse', response['viewname'])

class StandingViewsTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_horse_standing(self):
        from midway.views.standing import StandingViews
        request = testing.DummyRequest()
        inst = StandingViews(request)
        response = inst.horse_standing()
        self.assertEqual('horse standing', response['viewname'])

    def test_race_standing(self):
        from midway.views.standing import StandingViews
        request = testing.DummyRequest()
        inst = StandingViews(request)
        response = inst.race_standing()
        self.assertEqual('race standing', response['viewname'])

class RaceViewsTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_single_race(self):
        from midway.views.race import RaceViews
        request = testing.DummyRequest()
        inst = RaceViews(request)
        response = inst.race_results()
        self.assertEqual('Single Race', response['viewname'])
```