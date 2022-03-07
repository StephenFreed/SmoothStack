import os
import sys
sys.path.append("/Users/stephenfreed/Projects/SmoothStack/Flask_1-3/Flask_Blog/")

from app_package import application
from flask_login import current_user
import unittest


class FlaskTest_NoLogIn(unittest.TestCase):

# ~~~~~ Check Pages Load Correctly Not Logged In ~~~~~

    def test_index_statuscode(self):
        tester = application.test_client(self)
        response = tester.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)


    def test_home_statuscode(self):
        tester = application.test_client(self)
        response = tester.get("/home")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)


    def test_about_statuscode(self):
        tester = application.test_client(self)
        response = tester.get("/about")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)


    def test_about_content_type(self):
        tester = application.test_client(self)
        response = tester.get("/about")
        self.assertEqual(response.content_type, "text/html; charset=utf-8")


    def test_register_data(self):
        tester = application.test_client(self)
        response = tester.get("/register", content_type="html/text")
        self.assertTrue(b"Join Today" in response.data)


    def test_login_data(self):
        tester = application.test_client(self)
        response = tester.get("/login", content_type="html/text")
        self.assertTrue(b"Log In" in response.data)


    def test_logout_statuscode(self):
        tester = application.test_client(self)
        response = tester.get("/logout")
        statuscode = response.status_code
        self.assertEqual(statuscode, 302)


    def test_account_statuscode(self):
        tester = application.test_client(self)
        response = tester.get("/account")
        statuscode = response.status_code
        self.assertEqual(statuscode, 302)

    def test_database(self):
        tester = os.path.exists("app_package/database/site.db")
        self.assertTrue(tester)


class FlaskTest_LoggedIn(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_login(self):
        tester = application.test_client(self)
        response = tester.post("/login", data={"email": "admin@gmail.com",
                                        "password": "password"}, follow_redirects=True)
                                        
        self.assertTrue(b"Smoothstack" in response.data)

    


if __name__ == "__main__":
    unittest.main()
