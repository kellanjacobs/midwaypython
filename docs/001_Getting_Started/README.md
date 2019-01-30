# Getting Started

In this first step we are going to setup pyramid and, setup pycharm and run the demo site. We will
look at the components that the basic cookiecutter pyramid site gives us. 

## Objectives
* Setup a virtual environment
* Install pyramid into the virtual environment
* Use the cookiecutter package to setup the base of our application
* Tie our application into pycharm for easy development

## Fork the Github Repo

First we will want to fork a copy of the github repo for this class. This will become important later when
we are going to do the deployment steps. 

Navigate to [https://github.com/kellanjacobs/midwaypython](https://github.com/kellanjacobs/midwaypython)

Click the fork button in the top righthand corner. And add a copy of this code to your github account. 

Now clone down a copy for yourself. 

```bash
git clone git@github.com:YOURGITHUBUSERNAME/midwaypython.git
cd midwaypython
```
## Setting up your virtual environment

When you do python development you will save yourself many headaches by always using a virtual 
environment to run your code in. In python3 this feature is built in. 

```bash
# Set a bash variable for your virtual environment.
export VENV=`pwd`/ve
# Create the virtual environment
python3 -m venv $VENV
# Update pip and setup tools
$VENV/bin/pip install --upgrade pip setuptools
```

## Getting pyramid installed and running.

Lets install a few packages into our virtual environment. We will install Pyramid and Cookiecutter. 
Cookiecutter is used to create a blueprint for a pyramid project with sane defaults. For a django
developer you might think this is the same as the django start project command. Where pyramid is
different than django is it lets you make decisions about what packages you will use. This is just
a suggested layout based on the options you choose. Any one of these components can be changed at 
anytime. 

```bash
# Install pyramid and cookiecutter
$VENV/bin/pip install "pyramid==1.10.1" cookiecutter
# Use cookiecutter to create our app with defaults
$VENV/bin/cookiecutter gh:Pylons/pyramid-cookiecutter-starter --checkout 1.10-branch
```

Your output from the last command should look something like this. 

```bash
You've downloaded /Users/dnowak/.cookiecutters/pyramid-cookiecutter-starter before. Is it okay to delete and re-download it? [yes]:
project_name [Pyramid Scaffold]: midway
repo_name [midway]:
Select template_language:
1 - jinja2
2 - chameleon
3 - mako
Choose from 1, 2, 3 (1, 2, 3) [1]:
Select backend:
1 - none
2 - sqlalchemy
3 - zodb
Choose from 1, 2, 3 (1, 2, 3) [1]: 2

===============================================================================
Documentation: https://docs.pylonsproject.org/projects/pyramid/en/latest/
Tutorials:     https://docs.pylonsproject.org/projects/pyramid_tutorials/en/latest/
Twitter:       https://twitter.com/PylonsProject
Mailing List:  https://groups.google.com/forum/#!forum/pylons-discuss
Welcome to Pyramid.  Sorry for the convenience.
===============================================================================

Change directory into your newly created project.
    cd midway

Create a Python virtual environment.
    python3 -m venv env

Upgrade packaging tools.
    env/bin/pip install --upgrade pip setuptools

Install the project in editable mode with its testing requirements.
    env/bin/pip install -e ".[testing]"

Migrate the database using Alembic.
    # Generate your first revision.
    env/bin/alembic -c development.ini revision --autogenerate -m "init"
    # Upgrade to that revision.
    env/bin/alembic -c development.ini upgrade head
    # Load default data.
    env/bin/initialize_midway_db development.ini

Run your project's tests.
    env/bin/pytest

Run your project.
    env/bin/pserve development.ini
```

What has cookiecutter done for us. It has created a basic project structure. We chose our templating
language in this case **jinja2** and we decided to use **sqlalchemy** for our database layer. 
Other pieces we got are a package called alembic for performing database migrations. 

Lets complete the setup 

```bash
# Change into the midway directory we created. 
cd midway
# Lets install our application in our virtual environment.
$VENV/bin/pip install -e ".[testing]"
# Generate our first database revision
$VENV/bin/alembic -c development.ini revision --autogenerate -m "init"
# Upgrade to that revision
$VENV/bin/alembic -c development.ini upgrade head
# Load the default data
$VENV/bin/initialize_midway_db development.ini
```

## Configure Pycharm

From the menu bar select PyCharm->Preferences or use the shortcut key `cmd+,`

Find our project ProjectL midway and select Project Interpreter. Click the sprocket in the upper 
right hand corner and select add.

![Pycharm Setup 1](https://github.com/kellanjacobs/midwaypython/blob/master/docs/001_Getting_Started/images/pycharmsetup1.png)

Pycharm should have found your virtual environment. If it hasn't then find your virtual environment if not link to the python binary inside your ve folder of your project

![Pycharm Setup 2](https://github.com/kellanjacobs/midwaypython/blob/master/docs/001_Getting_Started/images/pycharmsetup2.png)

Save your settings.

Back at the main pycharm window click the add configuration button in the upper right hand corner. 

Select the + symbol and add a new pyramid server template. Select your python interpreter that we created above and add 
the full path to your development.ini file.

![Pycharm Setup 3](https://github.com/kellanjacobs/midwaypython/blob/master/docs/001_Getting_Started/images/pycharmsetup3.png)

Now you can simply push the play button inside pycharm to run your server. 