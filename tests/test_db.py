import unittest
from peewee import *
import os
os.environ['TESTING'] = 'true'
from app import TimelinePost

MODELS = [TimelinePost]

# use an in-memory SQLite for tests
test_db = SqliteDatabase(':memory:')


class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        # Bind model classses to test db. Since we have a complete list of
        # all models, we do not need to recursively bind dependencies.
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        # Not strictly necessary since SQLite in-memory databases only live
        # for the duration of the connection, and in the next step we close
        # the connection ... but a good practice all the same.

        test_db.drop_tables(MODELS)

        # Close connection to db.
        test_db.close()

    def test_timeline_post(self):
        # Create 2 timeline posts
        first_post = TimelinePost.create(
            name='John Doe', email='john@example.com', content='Hello world! I\'m John!')
        self.assertEqual(first_post.id, 1)
        second_post = TimelinePost.create(
            name='Jane Doe', email='jane@example.com', content='Hello world! I\'m Jane!')
        self.assertEqual(second_post.id, 2)

        # Tested getting timeline posts and asserting that they are correct.

        self.assertEqual(TimelinePost.select(), [first_post, second_post])
