import unittest
import json
from app import app

class ApiTests(unittest.TestCase):
    def setUp(self):
        self.app= app.test_client(self)
    #------------CONTACT ROUTE ---------------
    def testContactRouteGetRequestAlpha(self):    #WITHOUT API KEY
        response=self.app.get('/contact') #EXPECTED 403
        status=response.status_code
        content_type=response.content_type
        self.assertEqual(content_type,'application/json')
        self.assertEqual(status,403)
    def testContactRouteGetRequestBeta(self):       #WITH INVALID APIKEY
        response=self.app.get('/contact?api_key=abcd7612492347t12487') 
        status=response.status_code      #EXPECTED 403
        content_type=response.content_type
        self.assertEqual(content_type,'application/json')
        self.assertEqual(status,403)
    def testContactRouteGetRequestGamma(self):     #WITH CORRECT API KEY  
        response=self.app.get('/contact?api_key=9847c593c7c5a0fb93d08acc913b72eddef37fd594625f6c090bb5af08e33ea8')
        status=response.status_code       #EXPECTED 200
        content_type=response.content_type
        self.assertEqual(content_type,'application/json')
        self.assertEqual(status,200)


    def testContactRoutePostRequestAlpha(self):    #WITHOUT API KEY
        param=json.dumps({
            "firstname":"sample",
            "lastname":"sam2",
            "email":"sample@gmail.com",
            "message":"Hi from Test"
        })
        response=self.app.post('/contact',json=param) #EXPECTED 403
        status=response.status_code
        content_type=response.content_type
        self.assertEqual(content_type,'application/json')
        self.assertEqual(status,403)
    def testContactRoutePostRequestBeta(self):      #WITH INVALID APIKEY
        param=json.dumps({
            "firstname":"sample",
            "lastname":"sam2",
            "email":"sample@gmail.com",
            "message":"Hi from Test"
        })
        response=self.app.post('/contact?api_key=abcd7612492347t12487',json=param) 
        status=response.status_code      #EXPECTED 403
        content_type=response.content_type
        self.assertEqual(content_type,'application/json')
        self.assertEqual(status,403)
    #------------CONTACT ROUTE END ---------------

    #------------LANDING ROUTE ---------------
    def testLandingRouteGetRequestAlpha(self):    #WITHOUT API KEY
        response=self.app.get('/landing') #EXPECTED 403
        status=response.status_code
        content_type=response.content_type
        self.assertEqual(content_type,'application/json')
        self.assertEqual(status,403)
    def testLandingRouteGetRequestBeta(self):       #WITH INVALID APIKEY
        response=self.app.get('/landing?api_key=abcd7612492347t12487') 
        status=response.status_code      #EXPECTED 403
        content_type=response.content_type
        self.assertEqual(content_type,'application/json')
        self.assertEqual(status,403)
    def testLandingRouteGetRequestGamma(self):     #WITH CORRECT API KEY  
        response=self.app.get('/landing?api_key=9847c593c7c5a0fb93d08acc913b72eddef37fd594625f6c090bb5af08e33ea8')
        status=response.status_code       #EXPECTED 200
        content_type=response.content_type
        self.assertEqual(content_type,'application/json')
        self.assertEqual(status,200)


    def testLandingRoutePostRequestAlpha(self):    #WITHOUT API KEY
        param=json.dumps({
            "firstname":"sample", 
            "email":"sample@gmail.com",
        })
        response=self.app.post('/landing',json=param) #EXPECTED 403
        status=response.status_code
        content_type=response.content_type
        self.assertEqual(content_type,'application/json')
        self.assertEqual(status,403)
    def testLandingRoutePostRequestBeta(self):      #WITH INVALID APIKEY
        param=json.dumps({
            "firstname":"sample",
            "email":"sample@gmail.com",
        })
        response=self.app.post('/landing?api_key=abcd7612492347t12487',json=param) 
        status=response.status_code      #EXPECTED 403
        content_type=response.content_type
        self.assertEqual(content_type,'application/json')
        self.assertEqual(status,403)
    #------------LANDING ROUTE END---------------

    #------------SUBSCRIBE ROUTE ---------------
    def testSubscribeRouteGetRequestAlpha(self):    #WITHOUT API KEY
        response=self.app.get('/subscribe') #EXPECTED 403
        status=response.status_code
        content_type=response.content_type
        self.assertEqual(content_type,'application/json')
        self.assertEqual(status,403)
    def testSubscribeRouteGetRequestBeta(self):       #WITH INVALID APIKEY
        response=self.app.get('/subscribe?api_key=abcd7612492347t12487') 
        status=response.status_code      #EXPECTED 403
        content_type=response.content_type
        self.assertEqual(content_type,'application/json')
        self.assertEqual(status,403)
    def testSubscribeRouteGetRequestGamma(self):     #WITH CORRECT API KEY  
        response=self.app.get('/subscribe?api_key=9847c593c7c5a0fb93d08acc913b72eddef37fd594625f6c090bb5af08e33ea8')
        status=response.status_code       #EXPECTED 200
        content_type=response.content_type
        self.assertEqual(content_type,'application/json')
        self.assertEqual(status,200)

    
    def testSubscribeRoutePostRequestAlpha(self):    #WITHOUT API KEY
        param=json.dumps({
            "email":"sample@gmail.com"
        })
        response=self.app.post('/subscribe',json=param) #EXPECTED 403
        status=response.status_code
        content_type=response.content_type
        self.assertEqual(content_type,'application/json')
        self.assertEqual(status,403)
    def testSubscribeRoutePostRequestBeta(self):      #WITH INVALID APIKEY
        param=json.dumps({
            "email":"sample@gmail.com"
        })
        response=self.app.post('/subscribe?api_key=abcd7612492347t12487',json=param) 
        status=response.status_code      #EXPECTED 403
        content_type=response.content_type
        self.assertEqual(content_type,'application/json')
        self.assertEqual(status,403)
    #------------SUBSCRIBE ROUTE END---------------

    

if __name__=="__main__":
    unittest.main()