# Query the Database

In this section we will use SQL Alchemy to query the database. First we will start by using the built 
in [pshell](https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/commandline.html#interactive-shell) 
command. This is a command line utility that allows us to interact with our application. 

## Objectives
* Use pshell to test queries to the database. 
* Change our Views that will display data only to pull that data from the database.

## Steps

### 1. Using pshell

[pshell](https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/commandline.html#interactive-shell)
is an interactive shell that allows us to load our app and execute commands against it. We can run
python that we could in the python command line. The difference is the shell is executed 
in the context of our application.

Lets give it a try.

```bash
$VENV/bin/pshell development.ini
Python 3.7.2 (default, Dec 27 2018, 07:35:06)
[Clang 10.0.0 (clang-1000.11.45.5)] on darwin
Type "help" for more information.

Environment:
  app          The WSGI application.
  dbsession    <sqlalchemy.orm.session.Session object at 0x10552c7b8>
  models       <module 'midway.models' from '/Users/dnowak/develop/midwaypython/midway/midway/models/__init__.py'>
  registry     Active Pyramid registry.
  request      Active request object.
  root         Root of the default resource tree.
  root_factory Default root factory used to create `root`.
  tm           <transaction._manager.TransactionManager object at 0x105526208>

>>>horses = dbsession.query(models.Horse).all()
>>> horses
[Peter, Lois, Meg, Chris, Stewie, Rupert, Brian, Cleveland, Joe, Quagmire]
>>> horses[1].name
'Lois'
>>> horses[1].active
1
>>> horses[1].active = 0
>>> horses[1].active
0
>>> tm.commit()
>>> tm.begin()
<transaction._transaction.Transaction object at 0x1054b2208>
>>> active_horses = dbsession.query(models.Horse).filter_by(active=1).all()
>>> active_horses
[Peter, Meg, Chris, Stewie, Rupert, Brian, Cleveland, Joe, Quagmire]
>>> exit()
>>> race = dbsession.query(models.Race).filter_by(race_number=1).all()
>>> for r in race:
...     print(f'Race Number: {r.race_number} Place: {r.place} Horse: {r.horse.name}')
...
Race Number: 1 Place: 1 Horse: Joe
Race Number: 1 Place: 2 Horse: Quagmire
Race Number: 1 Place: 3 Horse: Stewie
Race Number: 1 Place: 4 Horse: Brian
Race Number: 1 Place: 5 Horse: Meg

```

### 2. Getting one horses data

Go ahead and open your `midway/midway/models/horse.py` file. Lets add a method to return our data about our horse as 
a python dictionary. 

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
    active = Column(Integer, nullable=False, default=1)
    races = relationship('Race', back_populates="horse")

    def __repr__(self):
        return self.name

    def json(self):
        return {"name": self.name, "active": self.active}
```
Add a json method to your Race model as well. 

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
    place = Column(Integer, default=99)
    horse_id = Column(ForeignKey('horses.id'), nullable=False)
    horse = relationship('Horse', back_populates="races")

    def json(self):
        return {"Race_Number": self.race_number, "Place": self.place}
```
Lets change the view to use our json method. 

```python

@view_defaults(renderer='json')
class HorseViews:

    def __init__(self, request):
        self.request = request

    @view_config(route_name='addhorse')
    def add_horse(self):
        return self.request.json_body

    @view_config(route_name='delhorse')
    def delete_horse(self):
        return self.request.json_body

    @view_config(route_name='viewhorse')
    def view_horse(self):
        '''Returns a single horse object as json'''
        horseid = self.request.matchdict['horseid']
        h = self.request.dbsession.query(models.Horse).filter_by(id=horseid).first()
        races = list(map(lambda x: x.json(), self.request.dbsession.query(models.Race).filter_by(horse_id=horseid).all()))
        horse_record = h.json()
        horse_record['races'] = races
        if h is None:
            return {"error": "Horse Not found"}
        else:
            return horse_record
```

### 3. Getting one Race data

Ok now its your turn. Lets see how you are remembering all this. Look at the code that we used in the console above.
Wasn't it great that when we pulled a race info you could access the horse name without doing any kind of crazy join. 
Using that example and the code above. Modify your `midway/midway/views/race.py` to return a single race view. 

I am not going to include the code here, but if you get really stuck you will find the code in the repo online. The
json you should return should look like this

```json
{"Race_number": 1,
 "Racers": [{"Horse_Name": "Peter", "Place": 1},
            {"Horse_Name": "Stewie", "Place": 2},
            {"Horse_Name": "Brian", "Place": 3},
            {"Horse_Name": "Meg", "Place": 4},
            {"Horse_Name": "Chris", "Place": 5}]
}
```

### List all the races

You did great on that one. Lets modify the standings race view. This code is almost identical as the last one except 
we need to return all races. 

```json
{"Races": [
  {"Race_number": 1,
   "Racers": [{"Horse_Name": "Peter", "Place": 1},
              {"Horse_Name": "Stewie", "Place": 2},
              {"Horse_Name": "Brian", "Place": 3},
              {"Horse_Name": "Meg", "Place": 4},
              {"Horse_Name": "Chris", "Place": 5}]
  },
  {"Race_number": 2,
   "Racers": [{"Horse_Name": "Peter", "Place": 1},
              {"Horse_Name": "Stewie", "Place": 2},
              {"Horse_Name": "Brian", "Place": 3},
              {"Horse_Name": "Meg", "Place": 4},
              {"Horse_Name": "Chris", "Place": 5}]
  }]
}
```



