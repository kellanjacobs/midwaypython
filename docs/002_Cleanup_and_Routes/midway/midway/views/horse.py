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
