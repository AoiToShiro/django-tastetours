# from django.test import RequestFactory
# from django.test import TestCase
from test_plus.test import TestCase
from django.http import HttpRequest
from tours.views import (
    edooutpost, sumofireizakaya, tours
)

class HomePageTest(TestCase):

    def test_home_page_live(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_returns_correct_html(self):
        response = self.client.get(f'/')
        self.assertTemplateUsed(response, 'home.html')


class EdoTestCase(TestCase):

    def test_edo_page_live(self):
        response = self.client.get('/tours/edooutpost/')
        self.assertEqual(response.status_code, 200)

    def test_edo_tour_returns_correct_html(self):
        response = self.client.get(f'/tours/edooutpost/')
        self.assertTemplateUsed(response, 'edooutpost.html')

    def test_access_from_home_page(self):
        """Test that the link in the home page goes to the correct page"""
        # setup css id for the drop down menu: navbarDropdownMenuLink
        self.fail()

class SumoTestCase(TestCase):

    def test_edo_page_live(self):
        response = self.client.get('/tours/sumofireizakaya/')
        self.assertEqual(response.status_code, 200)

    def test_edo_tour_returns_correct_html(self):
        response = self.client.get(f'/tours/sumofireizakaya/')
        self.assertTemplateUsed(response, 'sumofireizakaya.html')
