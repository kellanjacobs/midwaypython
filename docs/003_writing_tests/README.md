# Writing tests

Like any good programmer we need a way to test our application. Lets use the built in pytest package
It is already integrated into pyramid for us. At this time we are only going to add unit tests. We
will add functional tests later.

## Objectives
* Write Unit tests to cover our views.
## Steps

Lets start by creating a module for our application. 

```bash
# Remove the built in test file. We will be writing our own. 
rm midway/midway/tests.py
# Create a new directory to keep our test files
mkdir midway/midway/tests
# Create an empty __init__.py file
touch midway/midway/tests/__init__.py
```

Create a file `midway/midway/test_views.py` and add the following unittests

```python
import unittest

from pyramid import testing


class MidwayViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_add_horse(self):
        from midway.views.horse import add_horse
        request = testing.DummyRequest()
        response = add_horse(request)
        self.assertEqual(response.status_code, 200)

    def test_del_horse(self):
        from midway.views.horse import delete_horse
        request = testing.DummyRequest()
        response = delete_horse(request)
        self.assertEqual(response.status_code, 200)

    def test_view_horse(self):
        from midway.views.horse import view_horse
        request = testing.DummyRequest()
        response = view_horse(request)
        self.assertEqual(response.status_code, 200)
```

Now that we have written our tests lets add our tests to pycharm. In the upper right hand corner of
the pycharm window click the environment we previously setup and hit *Edit Configuration* Click the 
+ symbol to add a new configuration. Select Python Tests->pytests

![Pycharm Pytest Setup 1](https://raw.githubusercontent.com/kellanjacobs/midwaypython/master/docs/003_writing_tests/images/pycharmtest1.png)

Configure the config to use a module and set midway as our module. Save your settings. 

![Pycharm Pytest Setup 2](https://raw.githubusercontent.com/kellanjacobs/midwaypython/master/docs/003_writing_tests/images/pycharmtest2.png)


