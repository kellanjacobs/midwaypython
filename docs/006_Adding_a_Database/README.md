# Adding a Database

In this lesson we will setup the model files for out database connection. The cookiecutter did so much
of this already for us. We simply have to define our tables and our fields and we are ready to go. 

## Objectives
* Define our horse and race model
* Perform a database migration
* Initialize the database with new data

## Steps

First step is lets delete the dummy model that the cookiecutter created for us. 
Remove the `midway/models/mymodel.py` file. 

Inside the models directory lets create a new file `midway/models/horse.py`

```python
from sqlalchemy import (
    Column,
    Integer,
    String
)

from sqlalchemy.orm import relationship

from .meta import Base

class Horse(Base):
    """ The SQLAlchemy declarative model class for a Horse object. """
    __tablename__ = 'horses'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    str = Column(Integer, nullable=False, default=0)
    active = Column(Integer, nullable=False, default=1)
    races = relationship('Race', back_populates="horse")

    def __repr__(self):
        return self.name
````

We are creating a table named horses. Inside that table we have added four columns

* **id** is the primary key for this table
* **name** is the horses name
* **str** will store an interger that will be used in our application to weight the horses. Stronger horses will have an advantage.
* **active** Track if the horse is available to race. 

We have also set some defaults for a couple of the columns so that the user doesn't need to define them
if they don't want too. At this point we could create a constructor if we wanted too. But it is not 
required. Sqlalchemy creates one for us. 

Now lets create our second data model to define a race. Add the file `midway/models/race.py`

```python
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
)
from sqlalchemy.orm import relationship

from .meta import Base


class Race(Base):
    """ The SQLAlchemy declarative model class for a Page object. """
    __tablename__ = 'races'
    id = Column(Integer, primary_key=True)
    race_number = Column(Integer, nullable=False)
    score = Column(Integer, nullable=False)
    place = Column(Integer, default=99)
    horse_id = Column(ForeignKey('horses.id'), nullable=False)
    horse = relationship('Horse', back_populates="races")
```

Now tht we have our models defined it is time to tell pyramid about them. We do that inside the 
`midway/models/__init__.py` file. This file is alot of code but we are only changing two lines. We need
to take out the import of mymodel and replace it with the imports of horse and race.

```python
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import configure_mappers
import zope.sqlalchemy

# import or define all models here to ensure they are attached to the
# Base.metadata prior to any initialization routines
from .horse import Horse
from .race import Race
# run configure_mappers after defining all of the models to ensure
# all relationships can be setup
configure_mappers()


def get_engine(settings, prefix='sqlalchemy.'):
    return engine_from_config(settings, prefix)


def get_session_factory(engine):
    factory = sessionmaker()
    factory.configure(bind=engine)
    return factory


def get_tm_session(session_factory, transaction_manager):
    """
    Get a ``sqlalchemy.orm.Session`` instance backed by a transaction.

    This function will hook the session to the transaction manager which
    will take care of committing any changes.

    - When using pyramid_tm it will automatically be committed or aborted
      depending on whether an exception is raised.

    - When using scripts you should wrap the session in a manager yourself.
      For example::

          import transaction

          engine = get_engine(settings)
          session_factory = get_session_factory(engine)
          with transaction.manager:
              dbsession = get_tm_session(session_factory, transaction.manager)

    """
    dbsession = session_factory()
    zope.sqlalchemy.register(
        dbsession, transaction_manager=transaction_manager)
    return dbsession


def includeme(config):
    """
    Initialize the model for a Pyramid app.

    Activate this setup using ``config.include('midway.models')``.

    """
    settings = config.get_settings()
    settings['tm.manager_hook'] = 'pyramid_tm.explicit_manager'

    # use pyramid_tm to hook the transaction lifecycle to the request
    config.include('pyramid_tm')

    # use pyramid_retry to retry a request when transient exceptions occur
    config.include('pyramid_retry')

    session_factory = get_session_factory(get_engine(settings))
    config.registry['dbsession_factory'] = session_factory

    # make request.dbsession available for use in Pyramid
    config.add_request_method(
        # r.tm is the transaction manager used by pyramid_tm
        lambda r: get_tm_session(session_factory, r.tm),
        'dbsession',
        reify=True
    )
```

Now we can run the database migrations. 

```bash
$VENV/bin/alembic -c development.ini revision --autogenerate -m "use new models Horse and Race"
$VENV/bin/alembic -c development.ini upgrade head

```

The last step is to populate our database with some initial data. Lets open our `midway/initialize_db.py` file

```python
import argparse
import sys

from pyramid.paster import bootstrap, setup_logging
from sqlalchemy.exc import OperationalError
from random import randint

from .. import models


def setup_models(dbsession):
    """
    Add or update models / fixtures in the database.

    """
    peter = models.horse.Horse(name='Peter', str=randint(3,18))
    dbsession.add(peter)

    lois = models.horse.Horse(name='Lois', str=randint(3, 18))
    dbsession.add(lois)

    meg = models.horse.Horse(name='Meg', str=randint(3, 18))
    dbsession.add(meg)

    chris = models.horse.Horse(name='Chris', str=randint(3, 18))
    dbsession.add(chris)

    Stewie = models.horse.Horse(name='Stewie', str=randint(3, 18))
    dbsession.add(Stewie)

    Rupert = models.horse.Horse(name='Rupert', str=randint(3, 18))
    dbsession.add(Rupert)

    Brian = models.horse.Horse(name='Brian', str=randint(3, 18))
    dbsession.add(Brian)

    Cleveland = models.horse.Horse(name='Cleveland', str=randint(3, 18))
    dbsession.add(Cleveland)

    joe = models.horse.Horse(name='Joe', str=randint(3, 18))
    dbsession.add(joe)

    Quagmire = models.horse.Horse(name='Quagmire', str=randint(3, 18))
    dbsession.add(Quagmire)

    race = models.race.Race(race_number=0, score=100, horse_id=1)
    dbsession.add(race)


def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'config_uri',
        help='Configuration file, e.g., development.ini',
    )
    return parser.parse_args(argv[1:])


def main(argv=sys.argv):
    args = parse_args(argv)
    setup_logging(args.config_uri)
    env = bootstrap(args.config_uri)

    try:
        with env['request'].tm:
            dbsession = env['request'].dbsession
            setup_models(dbsession)
    except OperationalError:
        print('''
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to initialize your database tables with `alembic`.
    Check your README.txt for description and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.
            ''')

```

After we have saved this file we can go ahead and populate our database

```bash
$VENV/bin/initialize_midway_db development.ini
```