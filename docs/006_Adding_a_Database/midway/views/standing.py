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
