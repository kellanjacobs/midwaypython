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
