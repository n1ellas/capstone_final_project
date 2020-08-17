"""Test."""
import unittest
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from config import bearer_tokens
# import datetime
import json
from models import setup_db
from datetime import date


auth_header_executive_producer = {
    'Authorization': bearer_tokens['Executive_Producer']
}

auth_header_casting_director = {
    'Authorization': bearer_tokens['Casting_Director']
}

auth_header_casting_assistant = {
    'Authorization': bearer_tokens['Casting_Assistant']
}


class AgencyTestCase(unittest.TestCase):
    """This class represents the agency test case."""

    def setUp(self):
        """Setting up."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "casting_agency_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format('neil', 'bad112boy', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)

    def tearDown(self):
        """Executed after reach test."""
        pass

    def test_get_actors(self):
        """Test GET all actors."""
        res = self.client().get('/actors?page=1', headers=auth_header_casting_assistant)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_create_new_actor(self):
        """Test POST for new actor."""
        create_actor_test = {
            'name': 'Soobat',
            'gender': 'Female',
            'age': '32'
        }
        res = self.client().post('/actors', json=create_actor_test, headers=auth_header_casting_director)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'], True)

    def test_edit_actor(self):
        """Test PATCH existing actors."""
        edit_actor = {
            'age': 25,
            'name': 'john'
        }
        res = self.client().patch('/actors/2', json=edit_actor, headers=auth_header_casting_director)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['actor']) > 0)
        self.assertEqual(data['updated'], 2)

    def test_delete_actor(self):
        """Test DELETE for existing Actor."""
        res = self.client().delete('/actors/3', headers=auth_header_casting_director)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_get_movies(self):
        """Test GET all the movies."""
        res = self.client().get('/movies?page=1', headers=auth_header_casting_assistant)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_create_new_movie(self):
        """Test POST a new movie."""
        create_movie_test = {
            'title': 'The Release of the Slob',
            'release_date': date.today()
        }
        res = self.client().post('/movies', json=create_movie_test, headers=auth_header_executive_producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_edit_movie(self):
        """Test PATCH a existing movie."""
        edit_movie = {
            'title': 'This is a new title',
            'release_date': date.today()
        }
        res = self.client().patch('/movies/2', json=edit_movie, headers=auth_header_executive_producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['movie']) > 0)

    def test_delete_movie(self):
        """Test DELETE for a existing movie."""
        res = self.client().delete('/movies/1', headers=auth_header_executive_producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

# ---------------------------------------------------------------------
# Error Testing methods.
# ---------------------------------------------------------------------

    def test_error_401_get_actors(self):
        """Test GET actors without Authorization."""
        res = self.client().get('/actors?page=1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Authorization header is expected.')

    def test_error_404_get_actors(self):
        """Test Error GET all actors."""
        res = self.client().get('/actors?page=12429350', headers=auth_header_casting_assistant)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'No actors found on requested page.')

    # def test_error_401_create_new_actor(self):
    #     """Test POST for a new actor without Authorization."""
    #     error_create_new_actor = {
    #         'name': 'Byson',
    #         'gender': 'Male',
    #         'age': 500
    #     }
    #     res = self.client().post('/actors', json=error_create_new_actor)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 401)
    #     self.assertFalse(data['success'])

    def test_error_422_create_new_actor(self):
        """Test Error POST for a new actor without name."""
        actor_without_name = {
            'age': 25
        }

        res = self.client().post('/actors', json=actor_without_name, headers=auth_header_casting_director)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'No name provided.')

    def test_error_400_edit_actor(self):
            """Test PATCH with no json body."""
            res = self.client().patch('/actors/125612', headers=auth_header_casting_director)
            data = json.loads(res.data)

            self.assertEqual(res.status_code, 400)
            self.assertFalse(data['success'])
            self.assertEqual(data['message'], 'Request does not contain a valid JSON body.')

    def test_error_404_edit_actor(self):
        """Test PATCH with non valid ID."""
        edit_actor_with_new_age = {
            'age': 45
        }
        res = self.client().patch('/actors/123412', json=edit_actor_with_new_age, headers=auth_header_casting_director)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Actor with id 123412 not found in database.')

    # def test_error_401_delete_actor(self):
    #     """Test DELETE existing actor without Authorization."""
    #     res = self.client().delete('/actors/1')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 401)
    #     self.assertFalse(data['success'])
    #     self.assertEqual(data['message'], 'Authorization header is expected.')

    def test_error_403_delete_actor(self):
        """Test DELETE existing actor with missing Permissions."""
        res = self.client().delete('/actors/1', headers=auth_header_casting_assistant)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Permission not found.')

    def test_error_404_delete_actor(self):
        """Test DELETE for non existing actor."""
        res = self.client().delete('/actors/15125', headers=auth_header_executive_producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Actor with ID 15125 not found in database.')

    def test_error_422_create_new_movie(self):
        """Test Error for POST new movie without title."""
        new_movie = {
            'release_date': date.today()
        }

        res = self.client().post('/movies', json=new_movie, headers=auth_header_executive_producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'No Title Provided.')

    def test_error_401_get_movies(self):
        """Test GET all movies without Authorization."""
        res = self.client().get('/movies?page=1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Authorization header is expected.')

    def test_error_404_get_movies(self):
        """Test Error for GET all movies."""
        res = self.client().get('/movies?page=1125125125', headers=auth_header_casting_director)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'No movies found on requested page.')

    def test_error_400_edit_movie(self):
        """Test PATCH with a non valid JSON body."""
        res = self.client().patch('/movies/1', headers=auth_header_casting_director)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Request does not contain a valid JSON body.')

    def test_error_404_edit_movie(self):
        """Test PATCH with non valid ID."""
        edit_movie = {
            'release_date': date.today()
        }

        res = self.client().patch('/movies/123412', json=edit_movie, headers=auth_header_executive_producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Movie with id 123412 not found in database.')

    # def test_error_401_delete_movie(self):
    #     """Test DELETE for a existing movie without Authorization."""
    #     res = self.client().delete('/movies/1')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 401)
    #     self.assertFalse(data['success'])
    #     self.assertEqual(data['message'], 'Authorization header is expected.')

    def test_error_403_delete_movie(self):
        """Test DELETE existing movie with wrong permissions."""
        res = self.client().delete('/movies/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Permission not found.')

    def test_error_404_delete_movie(self):
        """Test DELETE for a non existing movie."""
        res = self.client().delete('/movies/151251')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Movie with id 151251 not found in database.')

# Make the tests conveniently executable.
# From app directory, run 'python test_app.py' to start tests
if __name__ == "__main__":
    unittest.main()
