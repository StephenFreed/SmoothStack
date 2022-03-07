import sys
sys.path.append("/Users/stephenfreed/Projects/SmoothStack/Flask_1-3/Flask_Blog/")

from app_package import application
import unittest


class FlaskTest(unittest.TestCase):


    def setUpClass():
        pass


    def tearDownClass():
        pass


    def setUp(self):
        pass


    def tearDown(self):
        pass

    # check status code
    def test_index_statuscode(self):
        tester = application.test_client(self)
        response = tester.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)


    # check status code
    def test_about_statuscode(self):
        tester = application.test_client(self)
        response = tester.get("/about")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)


    # check status code
    def test_regester_statuscode(self):
        tester = application.test_client(self)
        response = tester.get("/register")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)


    # check for content_type returned
    def test_register_content_type(self):
        tester = application.test_client(self)
        response = tester.get("/register")
        self.assertEqual(response.content_type, "text/html; charset=utf-8")


    # check for data on page
    def test_register_data(self):
        tester = application.test_client(self)
        response = tester.get("/register", content_type="html/text")
        self.assertTrue(b"Join Today" in response.data)


    # check status code
    def test_login_statuscode(self):
        tester = application.test_client(self)
        response = tester.get("/login")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)


    # check status code
    def test_logout_statuscode(self):
        tester = application.test_client(self)
        response = tester.get("/logout")
        statuscode = response.status_code
        self.assertEqual(statuscode, 302)


    # check status code
    def test_account_statuscode(self):
        tester = application.test_client(self)
        response = tester.get("/account")
        statuscode = response.status_code
        self.assertEqual(statuscode, 302)




if __name__ == "__main__":
    unittest.main()
