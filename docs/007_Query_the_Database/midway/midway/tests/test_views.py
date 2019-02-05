import unittest

from pyramid import testing


class HorseViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_add_horse(self):
        from midway.views.default import HorseViews
        request = testing.DummyRequest()
        inst = HorseViews(request)
        response = inst.add_horse()
        self.assertEqual('addhorse', response['viewname'])

    def test_del_horse(self):
        from midway.views.default import HorseViews
        request = testing.DummyRequest()
        inst = HorseViews(request)
        response = inst.delete_horse()
        self.assertEqual('delhorse', response['viewname'])

    def test_view_horse(self):
        from midway.views.default import HorseViews
        request = testing.DummyRequest()
        inst = HorseViews(request)
        response = inst.view_horse()
        self.assertEqual('viewhorse', response['viewname'])

class StandingViewsTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_horse_standing(self):
        from midway.views.default import StandingViews
        request = testing.DummyRequest()
        inst = StandingViews(request)
        response = inst.horse_standing()
        self.assertEqual('horse standing', response['viewname'])

    def test_race_standing(self):
        from midway.views.default import StandingViews
        request = testing.DummyRequest()
        inst = StandingViews(request)
        response = inst.race_standing()
        self.assertEqual('race standing', response['viewname'])

class RaceViewsTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_single_race(self):
        from midway.views.default import RaceViews
        request = testing.DummyRequest()
        inst = RaceViews(request)
        response = inst.race_results()
        self.assertEqual('Single Race', response['viewname'])