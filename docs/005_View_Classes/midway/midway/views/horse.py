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
