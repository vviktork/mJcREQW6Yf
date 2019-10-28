# -*- coding: utf-8 -*-

from django.test import TestCase
import unittest
from .image_graph import image_graph
from .dot_graph import dot_graf


class TestRegvestIcinga (unittest.TestCase):

    def test_dot_graph(self):
        """Schedule calculation sin(t), t + 2/t"""

        data1 = {'dt': 12, 'interval': 1, 'formula': 'sin(t)'}
        request1 = [0.0, -0.08106995962062931]
        data2 = {'dt': 12, 'interval': 1, 'formula': 't + 2/t'}
        request2 =  [0.0, 86400.00002314815]
        dg1 = dot_graf(data1)
        dg2 = dot_graf(data2)
        self.assertListEqual(dg1[1], request1)
        self.assertListEqual(dg2[1], request2)

    def test_image_graph(self):
        """Test image"""

        data = [['27/10 14:00', '26/10 14:00'], [0.0, 86400.00002314815]]
        dg = image_graph(data)
        self. assertIs(type(dg), str)
