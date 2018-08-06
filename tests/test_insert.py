"""

"""
import os
import shutil
from unittest import TestCase


from tree.Tree import TreeStorage


class InsertTest(TestCase):

    def setUp(self):
        self.tree = TreeStorage(os.path.dirname(os.path.abspath(__file__)) + "/storage/")

    def tearDown(self):
        shutil.rmtree(self.tree.path_to_tree)

    def test_insert_base64(self):
        """

        """
        base = b"""TWFuIGlzIGRpc3Rpbmd1aXNoZWQsIG5vdCBvbmx5IGJ5IGhpcyByZWFzb24sIGJ1dCBieSB0
        aGlzIHNpbmd1bGFyIHBhc3Npb24gZnJvbSBvdGhlciBhbmltYWxzLCB3aGljaCBpcyBhIGx1
        c3Qgb2YgdGhlIG1pbmQsIHRoYXQgYnkgYSBwZXJzZXZlcmFuY2Ugb2YgZGVsaWdodCBpbiB0
        aGUgY29udGludWVkIGFuZCBpbmRlZmF0aWdhYmxlIGdlbmVyYXRpb24gb2Yga25vd2xlZGdl
        LCBleGNlZWRzIHRoZSBzaG9ydCB2ZWhlbWVuY2Ugb2YgYW55IGNhcm5hbCBwbGVhc3VyZS4="""
        status_insert = self.tree.insert(base)
        self.assertEqual(status_insert, 396)
