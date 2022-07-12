import unittest
import os
os.environ['TESTING'] = 'true'
from app import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Lucy Wang</title>" in html
        # Check that the response's content is html and not empty.
        assert response.content_type == "text/html; charset=utf-8"
        assert response.content_length > 0
        # Check that needed links are present in the home page
        assert "<a href=\"/timeline\">" in html
        assert "<a href=\"/map\">" in html


    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0
        # Created a new test post and checked status code, type of response, and part of the information.
        response2 = self.client.post(
            "/api/timeline_post", data={"name": "Bob Wheeler", "email": "bob@example.com", "content": "Hello world! I\'m Bob!"})
        assert response2.status_code == 200
        assert response2.is_json
        json2 = response2.get_json()
        assert json2.get("name") == "Bob Wheeler"
        # Requested for all current posts to ensure that a new post has been added.
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 1
        # Created a new test post and checked status code, type of response, and part of the information.
        response3 = self.client.post(
            "/api/timeline_post", data={"name": "Pedro Alvarez", "email": "pedro@example.com", "content": "Hello world! I\'m Pedro!"})
        assert response3.status_code == 200
        assert response3.is_json
        json3 = response3.get_json()
        assert json3.get("name") == "Pedro Alvarez"
        # Requested for all current posts to ensure that a new post has been added.
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 2

        # Check that the response's content is html and not empty.
        timelineResponse = self.client.get("/timeline")
        assert timelineResponse.status_code == 200
        assert timelineResponse.content_type == "text/html; charset=utf-8"
        assert timelineResponse.content_length > 0
        html = timelineResponse.get_data(as_text=True)
        # Check that needed input fields are present in the timeline page
        assert "<input type=\"text\" name=\"name\"" in html
        assert "<input type=\"text\" name=\"email\"" in html
        assert "<textarea type=\"text\" name=\"content\"" in html
        # Check that previously created posts are rendered to timeline page.
        assert "Bob Wheeler" in html
        assert "bob@example.com" in html
        assert "Pedro Alvarez" in html
        assert "pedro@example.com" in html


    def test_malformed_timeline_post(self):
        # POST request missing name
        response = self.client.post(
            "/api/timeline_post", data={"email": "john@example.com", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        response_text = response.get_data(as_text=True)
        assert "Invalid name" in response_text

        # POST request with empty content
        response = self.client.post(
            "/api/timeline_post", data={"name": "John Doe", "email": "john@example.com", "content": ""})
        assert response.status_code == 400
        response_text = response.get_data(as_text=True)
        assert "Invalid content" in response_text

        # POST request with malformed email
        response = self.client.post("/api/timeline_post", data={
                                    "name": "John Doe", "email": "not-an-email", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        response_text = response.get_data(as_text=True)
        assert "Invalid email" in response_text
