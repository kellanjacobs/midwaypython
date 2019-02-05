from pyramid.view import (
    view_config,
    view_defaults
    )

from .. import models


@view_defaults(renderer='json')
class RaceViews:

    def __init__(self, request):
        self.request = request

    @view_config(route_name='singlerace')
    def race_results(self):
        racenumber = self.request.matchdict['raceid']
        racers = self.request.dbsession.query(models.Race).filter_by(race_number=racenumber).all()
        race_list = list()
        for r in racers:
            race_list.append({"Horse_Name": r.horse.name, "Place": r.place})

        return {"Race_number": racenumber, "Racers": race_list}
