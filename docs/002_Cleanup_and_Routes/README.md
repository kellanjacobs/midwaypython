# Cleanup and Routes

In this section we will look at what cookiecutter actually created and configured for us. We will
also clean up some of the extra stuff we don't need. Lastly we add change a couple of routes in our
application. 

## Objectives
* Understand what exactly cookiecutter created for us. 
* Remove the extra example code that we do not need. 
* Add three new routes and functions for them to our application

## Steps

### 1. Remove Unnecessary files

Pyramid cookiecutter created all the boiler plate code we need to get
and application up and running. Because pyramid is so flexiable it 
created a website for us that had traditional web assets such as
image file. Since we are writing an API we don't need these website
specific files. Lets go ahead and delete them. 

```bash
# Start in the root directory you cloned of the project
# Remove the static and template directories we can also 
# delete the 404 view
rm -Rf midway/midway/static/
rm -Rf midway/midway/templates/
rm midway/midway/views/notfound.py
```

### 2. Disable the pyramid_debugtoolbar
The pyramid_debug toolbar is great. But since we are making API calls in our application we don't want to inject 
JavaScript into our json. Modify our `midway/setup.py` file. Around line 15 remove `'pyramid_debugtoolbar',`. 

```python
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'plaster_pastedeploy',
    'pyramid',
    'pyramid_jinja2',
    'waitress',
    'alembic',
    'pyramid_retry',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
]

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest >= 3.7.4',
    'pytest-cov',
]

setup(
    name='midway',
    version='0.01',
    description='midway',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='Daniel Nowak',
    author_email='',
    url='',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': tests_require,
    },
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = midway:main',
        ],
        'console_scripts': [
            'initialize_midway_db=midway.scripts.initialize_db:main',
        ],
    },
)
```

The `midway/setup.py` downloaded the module, but it is the `development.ini` that actually enables it. 
Edit the `midway/development.ini` file and remove `pyramid.includes = pyramid_debugtoolbar` from lines 14 and 15.

```python
###
# app configuration
# https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/environment.html
###

[app:main]
use = egg:midway

pyramid.reload_templates = true
pyramid.debug_authorization = false
pyramid.debug_notfound = false
pyramid.debug_routematch = false
pyramid.default_locale_name = en

sqlalchemy.url = sqlite:///%(here)s/midway.sqlite

retry.attempts = 3

[pshell]
setup = midway.pshell.setup

###
# wsgi server configuration
###

[alembic]
# path to migration scripts
script_location = midway/alembic
file_template = %%(year)d%%(month).2d%%(day).2d_%%(rev)s
# file_template = %%(rev)s_%%(slug)s

[server:main]
use = egg:waitress#main
listen = localhost:6543

###
# logging configuration
# https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/logging.html
###

[loggers]
keys = root, midway, sqlalchemy

[handlers]
keys = console

[formatters]
keys = generic

[logger_root]
level = INFO
handlers = console

[logger_midway]
level = DEBUG
handlers =
qualname = midway

[logger_sqlalchemy]
level = WARN
handlers =
qualname = sqlalchemy.engine
# "level = INFO" logs SQL queries.
# "level = DEBUG" logs SQL queries and results.
# "level = WARN" logs neither.  (Recommended for production systems.)

[handler_console]
class = StreamHandler
args = (sys.stderr,)
level = NOTSET
formatter = generic

[formatter_generic]
format = %(asctime)s %(levelname)-5.5s [%(name)s:%(lineno)s][%(threadName)s] %(message)s

```

Lets add routes for our application end points. Edit the `midway/midway/routes.py` to remove the home
route and add three new routes to manage our horses. 

```python
def includeme(config):
    config.add_route('addhorse', '/horse/add')
    config.add_route('delhorse', '/horse/delete')
    config.add_route('viewhorse', '/horse/{horseid}')
```

Now lets rename `midway/midway/views/default.py` to `midway/midway/views/horse.py` and add the following code.

```python
from pyramid.view import view_config
from pyramid.response import Response

#from .. import models

@view_config(route_name='addhorse')
def add_horse(request):
    return Response('<body><h1>Added a horse</h1></body>')

@view_config(route_name='delhorse')
def delete_horse(request):
    return Response('<body><h1>Deleted a horse</h1></body>')

@view_config(route_name='viewhorse')
def view_horse(request):
    return Response('<body><h1>Details for our horse</h1></body>')
```