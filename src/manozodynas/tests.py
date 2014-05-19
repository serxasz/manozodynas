# encoding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse
from manozodynas.testutils import StatefulTesting
import requests


class IndexTestCase(StatefulTesting):
    def test_index_page(self):
        self.open(reverse('age_form'))
        self.assertStatusCode(200)
        self.selectForm('#forma')
	self.submitForm({
	    'Age': '20',
	    })
	self.assertStatusCode(302)
	self.selectTable('#rezultatai')
	self.assertTableHasRows(u'20')

#class IndexTestCase(TestCase):
#    def test_simple_page(self):
#        response = requests.get('localhost:8000')
#        response.status_code == 200



class LoginTestCase(StatefulTesting):

    fixtures = ['test_fixture.json']

    def test_login_page(self):
        self.open(reverse('login'))
        self.assertStatusCode(200)

    def test_good_login(self):
        self.open(reverse('login'))
        self.selectForm('#login')
        self.submitForm({
            'username': 'test',
            'password': 'test',
        })
        self.assertStatusCode(302)

    def test_bad_login(self):
        self.open(reverse('login'))
        self.selectForm('#login')
        self.submitForm({
            'username': 'bad',
            'password': 'bad',
        })
        self.assertStatusCode(200)
        self.selectOne('.errorlist')

    def test_no_input(self):
        self.open(reverse('login'))
        self.selectForm('#login')
        self.submitForm({
            'username': '',
            'password': '',
        })
        self.assertStatusCode(200)
        self.selectMany('.errorlist')

    def test_no_username(self):
        self.open(reverse('login'))
        self.selectForm('#login')
        self.submitForm({
            'username': '',
            'password': 'test',
        })
        self.assertStatusCode(200)
        self.selectOne('.errorlist')

    def test_no_password(self):
        self.open(reverse('login'))
        self.selectForm('#login')
        self.submitForm({
            'username': 'test',
            'password': '',
        })
        self.assertStatusCode(200)
        self.selectOne('.errorlist')

