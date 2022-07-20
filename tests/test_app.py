import unittest
import os
os.environ['TESTING'] = 'true'
from app import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        html = response.get_data(as_text=True)
        self.assertIn("<title>Lucy Wang</title>", html)
        # Check that the response's content is html and not empty.
        self.assertEqual(response.content_type, "text/html; charset=utf-8")
        self.assertGreater(response.content_length, 0)
        # Check that needed links are present in the home page
        self.assertIn('<div id="navbar_container">', html)


    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.is_json)
        json = response.get_json()
        self.assertIn("timeline_posts", json)
        self.assertEqual(len(json["timeline_posts"]), 0)

        # Created a new test post and checked status code, type of response, and part of the information.
        response2 = self.client.post(
            "/api/timeline_post", data={"name": "Bob Wheeler", "email": "bob@example.com", "content": "Hello world! I\'m Bob!"})
        self.assertEqual(response2.status_code, 200)
        self.assertTrue(response2.is_json)
        json2 = response2.get_json()
        self.assertEqual(json2.get("name"), "Bob Wheeler")

        # Requested for all current posts to ensure that a new post has been added.
        response = self.client.get("/api/timeline_post")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.is_json)
        json = response.get_json()
        self.assertIn("timeline_posts", json)
        self.assertEqual(len(json["timeline_posts"]), 1)

        # Created a new test post and checked status code, type of response, and part of the information.
        response3 = self.client.post(
            "/api/timeline_post", data={"name": "Pedro Alvarez", "email": "pedro@example.com", "content": "Hello world! I\'m Pedro!"})
        self.assertEqual(response3.status_code, 200)
        self.assertTrue(response3.is_json)
        json3 = response3.get_json()
        self.assertEqual(json3.get("name"), "Pedro Alvarez")

        # Requested for all current posts to ensure that a new post has been added.
        response = self.client.get("/api/timeline_post")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.is_json)
        json = response.get_json()
        self.assertIn("timeline_posts", json)
        self.assertEqual(len(json["timeline_posts"]), 2)

        # Check that the response's content is html and not empty.
        timelineResponse = self.client.get("/timeline")
        self.assertEqual(timelineResponse.status_code, 200)
        self.assertEqual(timelineResponse.content_type, "text/html; charset=utf-8")
        self.assertGreater(timelineResponse.content_length, 0)
        html = timelineResponse.get_data(as_text=True)

        # Check that needed input fields are present in the timeline page
        self.assertIn("<input type=\"text\" name=\"name\"", html)
        self.assertIn("<input type=\"text\" name=\"email\"", html)
        self.assertIn("<textarea type=\"text\" name=\"content\"", html)

        # Check that previously created posts are rendered to timeline page.
        self.assertIn("Bob Wheeler", html)
        self.assertIn("bob@example.com", html)
        self.assertIn("Pedro Alvarez", html)
        self.assertIn("pedro@example.com", html)


    def test_malformed_timeline_post(self):
        # POST request missing name
        response = self.client.post(
            "/api/timeline_post", data={"email": "john@example.com", "content": "Hello world, I'm John!"})
        self.assertEqual(response.status_code, 400)
        response_text = response.get_data(as_text=True)
        self.assertIn("Invalid name", response_text)

        # POST request with empty content
        response = self.client.post(
            "/api/timeline_post", data={"name": "John Doe", "email": "john@example.com", "content": ""})
        self.assertEqual(response.status_code, 400)
        response_text = response.get_data(as_text=True)
        self.assertIn("Invalid content", response_text)

        # POST request with malformed email
        response = self.client.post("/api/timeline_post", data={
                                    "name": "John Doe", "email": "not-an-email", "content": "Hello world, I'm John!"})
        self.assertEqual(response.status_code, 400)
        response_text = response.get_data(as_text=True)
        self.assertIn("Invalid email", response_text)
