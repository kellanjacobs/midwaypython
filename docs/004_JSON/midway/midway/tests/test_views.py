import unittest

from pyramid import testing


class MidwayViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_add_horse(self):
        from midway.views.horse import add_horse
        request = testing.DummyRequest()
        response = add_horse(request)
        self.assertEqual('addhorse', response['viewname'])

    def test_del_horse(self):
        from midway.views.horse import delete_horse
        request = testing.DummyRequest()
        response = delete_horse(request)
        self.assertEqual('delhorse', response['viewname'])

    def test_view_horse(self):
        from midway.views.horse import view_horse
        request = testing.DummyRequest()
        response = view_horse(request)
        self.assertEqual('viewhorse', response['viewname'])
