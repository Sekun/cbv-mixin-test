from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import PermissionDenied
from .views import View1, View2, View3

class TestViews(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_view1(self):
        request = self.factory.get('/')
        request.user = AnonymousUser()
        with self.assertRaises(PermissionDenied):
            View1.as_view()(request)

    def test_view2(self):
        request = self.factory.get('/')
        request.user = AnonymousUser()
        with self.assertRaises(PermissionDenied):
            View2.as_view()(request)

    def test_view3(self):
        request = self.factory.get('/')
        request.user = AnonymousUser()
        response = View3.as_view()(request)
        self.assertEqual(response.status_code, 302)
        self.assertIn('login', response.url)
