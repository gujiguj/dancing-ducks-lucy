from app import app
import unittest
import os
os.environ['TESTING'] = 'true'


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>MLH Fellow</title>" in html
        # Added more tests relating to the home page
        assert response.content_type == "text/html; charset=utf-8"
        assert response.content_length > 0
        assert "<a href=\"/timeline\">" in html
        assert "<a href=\"/map\">" in html


    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0
        # Added more tests relating to the /api/timeline_post GET and POST apis
        response2 = self.client.post(
            "/api/timeline_post", data={"name": "Bob Wheeler", "email": "bob@example.com", "content": "Hello world! I\'m Bob!"})
        assert response2.status_code == 200
        assert response2.is_json
        json2 = response2.get_json()
        assert json2.get("name") == "Bob Wheeler"
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 1
        response3 = self.client.post(
            "/api/timeline_post", data={"name": "Pedro Alvarez", "email": "pedro@example.com", "content": "Hello world! I\'m Pedro!"})
        assert response3.status_code == 200
        assert response3.is_json
        json3 = response3.get_json()
        assert json3.get("name") == "Pedro Alvarez"
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 2

        # Added more tests relating to the timeline page
        timelineResponse = self.client.get("/timeline")
        assert timelineResponse.status_code == 200
        assert timelineResponse.content_type == "text/html; charset=utf-8"
        assert timelineResponse.content_length > 0
        html = timelineResponse.get_data(as_text=True)
        assert "<input type=\"text\" name=\"name\"" in html
        assert "<input type=\"text\" name=\"email\"" in html
        assert "<textarea type=\"text\" name=\"content\"" in html


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
