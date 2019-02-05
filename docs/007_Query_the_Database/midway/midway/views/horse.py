from pyramid.view import (
    view_config,
    view_defaults
    )

from .. import models


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


