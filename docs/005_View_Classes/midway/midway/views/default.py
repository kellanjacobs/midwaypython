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

@view_defaults(renderer='json')
class RaceViews:

    def __init__(self, request):
        self.request = request

    @view_config(route_name='singlerace')
    def race_results(self):
        return {'viewname': 'Single Race'}
