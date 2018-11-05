#coding:utf-8
import requests
import unittest

class V2exAPITestCase(unittest.TestCase):
    def test_node_api(self):
        url = "https://www.v2ex.com/api/nodes/show.json"
        querystring = {"name":"python"}

        # headers = {
        #   'Cache-Control': "no-cache",
        #  'Postman-Token': "be6ebdab-40d5-4c0b-a279-3f67077796d1"
        #  }

       # response = requests.request("GET", url, headers=headers, params=querystring).json()
        response = requests.request("GET", url, params=querystring).json()
        self.assertEqual(response['name'],'python')
        self.assertEqual(response['id'],90)

if __name__ == '__main__':
    unittest.main()