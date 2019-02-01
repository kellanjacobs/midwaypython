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
