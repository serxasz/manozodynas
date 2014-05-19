# encoding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse
# from manozodynas.testutils import StatefulTesting
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

