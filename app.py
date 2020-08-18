"""App file for final project."""
from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from auth import requires_auth
from models import setup_db, Actor, Movie

ROWS_PER_PAGE = 10


def pagination(request, selection):
    """Paginaton of Actors."""
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * ROWS_PER_PAGE
    end = start + ROWS_PER_PAGE

    objects_formatted = [object_name.format() for object_name in selection]
    current_objects = objects_formatted[start:end]
    return current_objects


def create_app(test_config=None):
    """Create and configure the app."""
    app = Flask(__name__)
    setup_db(app)
    CORS(app, resources={r"*": {"origins": "*"}})

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type:application/json, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response

    def get_error_message(error, default_text):
        """Get error messages."""
        try:
            return error.description['message']
        except:
            return default_text

    @app.route('/')
    def landing_page():
        return "Welcome to the Casting Agency!"

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(token):
        """Return a list of actors."""
        actors = Actor.query.order_by(Actor.id).all()
        current_actors = pagination(request, actors)

        if len(current_actors) == 0:
            abort(404, {'message': 'No Actors Found In Database'})

        result = {
            'success': True,
            'current_actors': current_actors
        }
        return jsonify(result)

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def create_actors(token):
        """Create a new Actor."""
        body = request.get_json()

        if not body:
            abort(404, {'message', 'Request does not contain a valid JSON body'})

        name = body.get('name', None)
        age = body.get('age', None)
        gender = body.get('gender', 'Other')

        if not name:
            abort(422, {'message': 'No Name Provided'})

        if not age:
            abort(422, {'message': 'No Age Provided'})

        new_actor = (Actor(
            name=name,
            age=age,
            gender=gender
        ))
        new_actor.insert()

        return jsonify({
            'success': True,
            'created': new_actor.id
        })

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def edit_actors(token, actor_id):
        """Edit actors."""
        body = request.get_json()

        if not actor_id:
            abort(400, {'message': 'Please add an actor id to the requested url'})

        if not body:
            abort(400, {'message': 'Request does not contain a vaild JSON body.'})

        actor_to_update = Actor.query.filter(Actor.id == actor_id).one_or_none()

        if not actor_to_update:
            abort(404, {'message': 'Actor with id {} not found in database.'.format(actor_id)})

        name = body.get('name', actor_to_update.name)
        age = body.get('age', actor_to_update.age)
        gender = body.get('gender', actor_to_update.gender)

        actor_to_update.name = name
        actor_to_update.age = age
        actor_to_update.gender = gender

        actor_to_update.update()

        return jsonify({
            'success': True,
            'updated': actor_to_update.id,
            'actor': [actor_to_update.format()]
        })

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(token, actor_id):
        """Delete a Actor."""
        if not actor_id:
            abort(400, {'message': 'Please add an actor id to the requested url'})

        actor_to_delete = Actor.query.filter(Actor.id == actor_id).one_or_none()

        if not actor_to_delete:
            abort(404, {'message': 'Actor with id {} not found in datebase.'.format(actor_id)})

        actor_to_delete.delete()

        return jsonify({
            'success': True,
            'deleted': actor_id
        })

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(token):
        """Get movies route."""
        selection = Movie.query.order_by(Movie.id).all()
        paginated_movies = pagination(request, selection)

        if len(paginated_movies) == 0:
            abort(404, {'message': 'No movies found in database.'})

        return jsonify({
            'success': True,
            'movies': paginated_movies
        })

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def create_movies(token):
        """Create movies route."""
        if request.data:
            body = request.get_json()

            if not body:
                abort(400, {'message': 'Request does not contain a vaild JSON body'})

            title = body.get('title', None)
            release_date = body.get('release_date', None)

            if not title:
                abort(422, {'message': 'No title provided'})

            if not release_date:
                abort(422, {'message': 'No "release_date" provided'})

            new_movie = (Movie(
                title=title,
                release_date=release_date
            ))
            new_movie.insert()

            return jsonify({
                'success': True,
                'created': new_movie.id
            })
        else:
            abort(422)

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def edit_movies(token, movie_id):
        """Edit movies method."""
        body = request.get_json()

        if not movie_id:
            abort(400, {'message': 'Please add a valid movie ID to the requested url'})

        if not body:
            abort(400, {'message': 'Request does not contain a vaild JSON body'})

        movie_to_update = Movie.query.filter(Movie.id == movie_id).one_or_none()

        if not movie_to_update:
            abort(404, {'message': 'Movie with id {} not found in database.'.format(movie_id)})

        title = body.get('title', movie_to_update.title)
        release_date = body.get('release_date', movie_to_update.release_date)

        movie_to_update.title = title
        movie_to_update.release_date = release_date

        movie_to_update.update()

        return jsonify({
            'success': True,
            'edited': movie_to_update.id,
            'movie': [movie_to_update.format()]
        })

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movies(token, movie_id):
        """Delete method for movies."""
        if not movie_id:
            abort(400, {'message': 'Please add a movie id to the requested url'})

        movie_to_delete = Movie.query.filter(Movie.id == movie_id).one_or_none()

        if not movie_to_delete:
            abort(404, {'message': 'Movie with id {} not found in database.'.format(movie_id)})

        movie_to_delete.delete()

        return jsonify({
            'success': True,
            'deleted': movie_id
        })

        @app.errorhandler(404)
        def not_found(error):
            return jsonify({
                'success': False,
                'error': 404,
                'message': 'Resource Not Found'
            }), 404

        @app.errorhandler(422)
        def unprocessable(error):
            return jsonify({
                'success': False,
                'error': 422,
                'message': 'unprocessable'
            }), 422

        @app.errorhandler(400)
        def bad_request(error):
            return jsonify({
                "success": False,
                "error": 400,
                "message": "bad request"
            }), 400

    return app
app = create_app()

if __name__ == '__main__':
    app.run()
