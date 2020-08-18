

Casting Agency Final Project

Content

    Motivation
    Installing Dependencies
    Authentication
    Run the project locally
    Application Endpoints
    Testing
    Running server on Heroku

MOTIVATION

This is the final project of the Full Stack Web Developer Nanodegree Program. It covers the following technical topics:

- Database modeling with postgres & sqlalchemy,
- API to perform CRUD Operations on the database with Flask,
- Automated testing with Unittest,
- Authorization & Role Based Access Control(RABC) Authorization with Auth0
- Deployment on Heroku

The project resembles a casting agency which is responsible for creating movies, managing actors. Within the agency there are three roles:

    Executive producer
    Casting director
    Casting assistant

INSTALLING DEPENDENCIES

POSTMAN

    Postman is a collaboration platform for API development. Postman's features simplify each step of building an API and streamline collaboration so you can create better APIs—faster.

Make sure you cd (Change Dirctory) into the correct folder (with all app files) before following the setup steps. Also, you need the latest version of Python 3 and postgres installed on your machine.

I recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized.

To install a python3 virtual environment, Make sure that in your terminal you are inside the project directory, Then copy and paste the following command:

- 	vitualenv -p python3 env

This will setup a virtualenv in the project directory, Next is to activate that virtualenv:

-	source env/bin/activate

This will activate the environment in which all project dependencies will be stored.

(NB) Once this is complete you can finally instill the project dependencies and to do this navigate inside the project to where the requirements.txt file is stored and paste this command in the terminal:

 -	pip install -r requirements.txt

 This will install all the necessary files needed to run the project locally

(NB) In order to run the project locally you need to have Authentication Setup on Auth0 https://auth0.com/

AUTHENCATION

-	Create a new Auth0 Account
-	Select a unique tenant domain
-	Create a new, regular web application
-	Create a new API
    -	In API Settings:
        -	Enable RBAC
        -	Enable Add Permissions in the Access Token
-	Create new API permissions:
    -	get:actors
    -	get:movies
    -	post:actors
    -	post:movies
    -	patch:actors
    -	patch:movies
    -	delete:actors
    -	delete:movies
-	Create new roles for:
    -	Casting Assistant
        -	Can get actors and movies
    -	Casting Director
        -	Can perform all actions the Casting Assistant has and add or delete a actor from the database as well as modify actors or movies.
    -	Executive Producer
    	-	Can perform all actions.
-	Assign these roles to Three different people.

- 	Now you need to login as those users to get the token that will be used for each role,
-	Navigate to the following link:
	-	https://auth0.com/docs/flows/call-your-api-using-the-authorization-code-flow
-	Under Example authorization URL, click on login and log into your AuthO account.
	-	Click on the dropdown and choose the application that you have just created now.
	-	Copy and paste the url into an incognito tab,
	-	In the url link remove STATE and change the audience to your API AUDIENCE,
	-	Remove the SCOPE and change the response_type to token.
	-	Enter and log into the respective users accounts to get the token.
	<b>(NOTE: this process needs to happen at least 3 times as you will have 3 different users.)</b>
- Store the tokens in a text editor as you will need it later.

RUN THE PROJECT LOCALLY

-	Open the project in a html text editor of your choice,
-	Go to config and replace the necessary bearer tokens with your saved tokens,
-	Using the postgres cli as root user create 2 databases using these commands
	-	createdb casting_agency
	-	createdb casting_agency_test
-	Once that is complete import the json file into both databases:
	-	psql casting_agency < casting_agency.json
	-	psql casting_agency_test < casting_agency.json

-	When that is finish you can finally run the project locally through your terminal:
	-	export FLASK_APP=app.py
	-	export FLASK_ENV=development
	-	flask run

API Documentation

Here you can find all existing endpoints, which methods can be used, how to work with them & example responses you´ll get.

Additionally, common pitfalls & error messages are explained, if applicable.
Base URL

https://vast-inlet-80598.herokuapp.com/


How to work with each endpoint using Postman

	- Enter base url,
	- Under headers enter Authorization as key, Bearer {token} as value,
	- On the dropdown choose your appropriate request method,
	- When doing a POST you insert your data in the body tab and with the correct details,
	- Next to cookies on your right hand side click on the "code" button
	- Copy the curl command in your terminal
	

1. GET /actors

Query paginated actors.

$ curl --location --request GET 'https://vast-inlet-80598.herokuapp.com/actors' --header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxaMUoyVnplalRiUjhYb0liV1BEMSJ9.eyJpc3MiOiJodHRwczovL24xZWxsYXMuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMWFlYmExM2U2NGNjMDAzZDY4Yzc5YyIsImF1ZCI6ImFnZW5jeSIsImlhdCI6MTU5Nzc1NTEzMSwiZXhwIjoxNTk3ODQxNTMxLCJhenAiOiJxNG1xNkpEWUEybFZSY2YwSHk5YXY4ZGQyM3doZ1RLOCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.VwtKsUkgTH94M7NNf97TLlsMiXU7skxcMxrb8mcJLYE_ZhjEuvZ-qlA56mKoS9ffQ1gD3C-O7D21Jojk0Fp1pgYG8UXuOo0TMeHiKzn22C9D70TlayZtXAOag__ON0jOhZMuXeZ8fzLZlzdrNUImGz2pxQc68JRThtb8pOY7F9--PTCXXrP0or6FLs3MRVlXLZDkxmZccQquV5cLXZM-cB8nX4L0YWU78HzM86J5pUq2qcsmwIPhRj753czsBqBuvreB-pqz-eHJIj_o3atgHtj6qe6XdIOzLbFfrHsf_nL1HxRA6cKzxHocpGBuCtqhhB4IQiuevNWqWtJRinbvZg' --data-raw ''

	Fetches a list of actors given that the Bearer has the appropriate permissions.
	
        List of actors with following fields:
            integer id
            string name
            string gender
            integer age
        boolean success

Example response

{
  "current_actors": [
    {
      "age": "21", 
      "gender": "Female", 
      "id": 1, 
      "name": "Junice"
    }, 
    {
      "age": "24", 
      "gender": "Male", 
      "id": 2, 
      "name": "Neil"
    }, 
    {
      "age": "22", 
      "gender": "Male", 
      "id": 3, 
      "name": "Sage"
    }, 
    {
      "age": "24", 
      "gender": "Male", 
      "id": 4, 
      "name": "Huncho"
    }, 
    {
      "age": "24", 
      "gender": "Male", 
      "id": 5, 
      "name": "Huncho"
    }
  ], 
  "success": true
}

Errors

If you try to fetch a page which does not have any actors, you will encounter an error which looks like this:

$ curl --location --request GET 'https://vast-inlet-80598.herokuapp.com/actors?page=12373281' --header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxaMUoyVnplalRiUjhYb0liV1BEMSJ9.eyJpc3MiOiJodHRwczovL24xZWxsYXMuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMWFlYmExM2U2NGNjMDAzZDY4Yzc5YyIsImF1ZCI6ImFnZW5jeSIsImlhdCI6MTU5Nzc1NTEzMSwiZXhwIjoxNTk3ODQxNTMxLCJhenAiOiJxNG1xNkpEWUEybFZSY2YwSHk5YXY4ZGQyM3doZ1RLOCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.VwtKsUkgTH94M7NNf97TLlsMiXU7skxcMxrb8mcJLYE_ZhjEuvZ-qlA56mKoS9ffQ1gD3C-O7D21Jojk0Fp1pgYG8UXuOo0TMeHiKzn22C9D70TlayZtXAOag__ON0jOhZMuXeZ8fzLZlzdrNUImGz2pxQc68JRThtb8pOY7F9--PTCXXrP0or6FLs3MRVlXLZDkxmZccQquV5cLXZM-cB8nX4L0YWU78HzM86J5pUq2qcsmwIPhRj753czsBqBuvreB-pqz-eHJIj_o3atgHtj6qe6XdIOzLbFfrHsf_nL1HxRA6cKzxHocpGBuCtqhhB4IQiuevNWqWtJRinbvZg' --data-raw ''

{
  "error": 404,
  "message": "No Actors Found In Database.",
}


2. POST /actors

Insert a new actor into the database.

$ curl --location --request POST 'https://vast-inlet-80598.herokuapp.com/actors' --header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxaMUoyVnplalRiUjhYb0liV1BEMSJ9.eyJpc3MiOiJodHRwczovL24xZWxsYXMuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMWFlYmExM2U2NGNjMDAzZDY4Yzc5YyIsImF1ZCI6ImFnZW5jeSIsImlhdCI6MTU5Nzc1NTEzMSwiZXhwIjoxNTk3ODQxNTMxLCJhenAiOiJxNG1xNkpEWUEybFZSY2YwSHk5YXY4ZGQyM3doZ1RLOCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.VwtKsUkgTH94M7NNf97TLlsMiXU7skxcMxrb8mcJLYE_ZhjEuvZ-qlA56mKoS9ffQ1gD3C-O7D21Jojk0Fp1pgYG8UXuOo0TMeHiKzn22C9D70TlayZtXAOag__ON0jOhZMuXeZ8fzLZlzdrNUImGz2pxQc68JRThtb8pOY7F9--PTCXXrP0or6FLs3MRVlXLZDkxmZccQquV5cLXZM-cB8nX4L0YWU78HzM86J5pUq2qcsmwIPhRj753czsBqBuvreB-pqz-eHJIj_o3atgHtj6qe6XdIOzLbFfrHsf_nL1HxRA6cKzxHocpGBuCtqhhB4IQiuevNWqWtJRinbvZg' --header 'Content-Type: application/json' --data-raw '{
    "name": "Batman",
    "gender": "Male",
    "age": "45"
}'

Example

{
    "created": 5,
    "success": true
}

Errors

If you try to create a new actor without a requiered field like name, it will throw a 422 error:

$ curl --location --request POST 'https://vast-inlet-80598.herokuapp.com/actors' --header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxaMUoyVnplalRiUjhYb0liV1BEMSJ9.eyJpc3MiOiJodHRwczovL24xZWxsYXMuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMWFlYmExM2U2NGNjMDAzZDY4Yzc5YyIsImF1ZCI6ImFnZW5jeSIsImlhdCI6MTU5Nzc1NTEzMSwiZXhwIjoxNTk3ODQxNTMxLCJhenAiOiJxNG1xNkpEWUEybFZSY2YwSHk5YXY4ZGQyM3doZ1RLOCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.VwtKsUkgTH94M7NNf97TLlsMiXU7skxcMxrb8mcJLYE_ZhjEuvZ-qlA56mKoS9ffQ1gD3C-O7D21Jojk0Fp1pgYG8UXuOo0TMeHiKzn22C9D70TlayZtXAOag__ON0jOhZMuXeZ8fzLZlzdrNUImGz2pxQc68JRThtb8pOY7F9--PTCXXrP0or6FLs3MRVlXLZDkxmZccQquV5cLXZM-cB8nX4L0YWU78HzM86J5pUq2qcsmwIPhRj753czsBqBuvreB-pqz-eHJIj_o3atgHtj6qe6XdIOzLbFfrHsf_nL1HxRA6cKzxHocpGBuCtqhhB4IQiuevNWqWtJRinbvZg' --header 'Content-Type: application/json' --data-raw '{
    "gender": "Male",
    "age": "45"
}'

Will return:

{
  "error": 422,
  "message": "No Name Provided.",
}

3. PATCH /actors

Edit an existing Actor

$ curl --location --request PATCH 'https://vast-inlet-80598.herokuapp.com/actors/1' --header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxaMUoyVnplalRiUjhYb0liV1BEMSJ9.eyJpc3MiOiJodHRwczovL24xZWxsYXMuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMWFlYmExM2U2NGNjMDAzZDY4Yzc5YyIsImF1ZCI6ImFnZW5jeSIsImlhdCI6MTU5Nzc1NTEzMSwiZXhwIjoxNTk3ODQxNTMxLCJhenAiOiJxNG1xNkpEWUEybFZSY2YwSHk5YXY4ZGQyM3doZ1RLOCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.VwtKsUkgTH94M7NNf97TLlsMiXU7skxcMxrb8mcJLYE_ZhjEuvZ-qlA56mKoS9ffQ1gD3C-O7D21Jojk0Fp1pgYG8UXuOo0TMeHiKzn22C9D70TlayZtXAOag__ON0jOhZMuXeZ8fzLZlzdrNUImGz2pxQc68JRThtb8pOY7F9--PTCXXrP0or6FLs3MRVlXLZDkxmZccQquV5cLXZM-cB8nX4L0YWU78HzM86J5pUq2qcsmwIPhRj753czsBqBuvreB-pqz-eHJIj_o3atgHtj6qe6XdIOzLbFfrHsf_nL1HxRA6cKzxHocpGBuCtqhhB4IQiuevNWqWtJRinbvZg' --header 'Content-Type: application/json' --data-raw '{
    "name": "SuperLady",
    "gender": "Female",
    "age": "32"
}'


Example response

{
  "actor": [
    {
      "age": "32", 
      "gender": "Female", 
      "id": 1, 
      "name": "SuperLady"
    }
  ], 
  "success": true, 
  "updated": 1
}

Errors

If you try to update a actor with an invalid id it will throw an 404 Error:

$ curl --location --request PATCH 'https://vast-inlet-80598.herokuapp.com/actors/237' --header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxaMUoyVnplalRiUjhYb0liV1BEMSJ9.eyJpc3MiOiJodHRwczovL24xZWxsYXMuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMWFlYmExM2U2NGNjMDAzZDY4Yzc5YyIsImF1ZCI6ImFnZW5jeSIsImlhdCI6MTU5Nzc1NTEzMSwiZXhwIjoxNTk3ODQxNTMxLCJhenAiOiJxNG1xNkpEWUEybFZSY2YwSHk5YXY4ZGQyM3doZ1RLOCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.VwtKsUkgTH94M7NNf97TLlsMiXU7skxcMxrb8mcJLYE_ZhjEuvZ-qlA56mKoS9ffQ1gD3C-O7D21Jojk0Fp1pgYG8UXuOo0TMeHiKzn22C9D70TlayZtXAOag__ON0jOhZMuXeZ8fzLZlzdrNUImGz2pxQc68JRThtb8pOY7F9--PTCXXrP0or6FLs3MRVlXLZDkxmZccQquV5cLXZM-cB8nX4L0YWU78HzM86J5pUq2qcsmwIPhRj753czsBqBuvreB-pqz-eHJIj_o3atgHtj6qe6XdIOzLbFfrHsf_nL1HxRA6cKzxHocpGBuCtqhhB4IQiuevNWqWtJRinbvZg' --header 'Content-Type: application/json' --data-raw '{
    "name": "SuperLady",
    "gender": "Female",
    "age": "32"
}

will return

{
  "error": 404,
  "message": "Actor with id 237 not found in database.",
}

4. DELETE /actors

Deleting a Actor

$ curl --location --request DELETE 'https://vast-inlet-80598.herokuapp.com/actors/1' --header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxaMUoyVnplalRiUjhYb0liV1BEMSJ9.eyJpc3MiOiJodHRwczovL24xZWxsYXMuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMWFlYmExM2U2NGNjMDAzZDY4Yzc5YyIsImF1ZCI6ImFnZW5jeSIsImlhdCI6MTU5Nzc1NTEzMSwiZXhwIjoxNTk3ODQxNTMxLCJhenAiOiJxNG1xNkpEWUEybFZSY2YwSHk5YXY4ZGQyM3doZ1RLOCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.VwtKsUkgTH94M7NNf97TLlsMiXU7skxcMxrb8mcJLYE_ZhjEuvZ-qlA56mKoS9ffQ1gD3C-O7D21Jojk0Fp1pgYG8UXuOo0TMeHiKzn22C9D70TlayZtXAOag__ON0jOhZMuXeZ8fzLZlzdrNUImGz2pxQc68JRThtb8pOY7F9--PTCXXrP0or6FLs3MRVlXLZDkxmZccQquV5cLXZM-cB8nX4L0YWU78HzM86J5pUq2qcsmwIPhRj753czsBqBuvreB-pqz-eHJIj_o3atgHtj6qe6XdIOzLbFfrHsf_nL1HxRA6cKzxHocpGBuCtqhhB4IQiuevNWqWtJRinbvZg' --data-raw ''

Example response

{
    "deleted": 1,
    "success": true
}

Errors

If you try to delete a actor with an invalid id, it will throw a 404 Error:

$ curl --location --request DELETE 'https://vast-inlet-80598.herokuapp.com/actors/291' --header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxaMUoyVnplalRiUjhYb0liV1BEMSJ9.eyJpc3MiOiJodHRwczovL24xZWxsYXMuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMWFlYmExM2U2NGNjMDAzZDY4Yzc5YyIsImF1ZCI6ImFnZW5jeSIsImlhdCI6MTU5Nzc1NTEzMSwiZXhwIjoxNTk3ODQxNTMxLCJhenAiOiJxNG1xNkpEWUEybFZSY2YwSHk5YXY4ZGQyM3doZ1RLOCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.VwtKsUkgTH94M7NNf97TLlsMiXU7skxcMxrb8mcJLYE_ZhjEuvZ-qlA56mKoS9ffQ1gD3C-O7D21Jojk0Fp1pgYG8UXuOo0TMeHiKzn22C9D70TlayZtXAOag__ON0jOhZMuXeZ8fzLZlzdrNUImGz2pxQc68JRThtb8pOY7F9--PTCXXrP0or6FLs3MRVlXLZDkxmZccQquV5cLXZM-cB8nX4L0YWU78HzM86J5pUq2qcsmwIPhRj753czsBqBuvreB-pqz-eHJIj_o3atgHtj6qe6XdIOzLbFfrHsf_nL1HxRA6cKzxHocpGBuCtqhhB4IQiuevNWqWtJRinbvZg' --data-raw ''

will return

{
  "error": 404 Not Found,
  "message": "Actor with id 291 not found in database.",
  "success": false
}

5. GET /movies

Query paginated movies.

$ curl --location --request GET 'https://vast-inlet-80598.herokuapp.com/movies' --header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxaMUoyVnplalRiUjhYb0liV1BEMSJ9.eyJpc3MiOiJodHRwczovL24xZWxsYXMuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMWFlYmExM2U2NGNjMDAzZDY4Yzc5YyIsImF1ZCI6ImFnZW5jeSIsImlhdCI6MTU5Nzc1NTEzMSwiZXhwIjoxNTk3ODQxNTMxLCJhenAiOiJxNG1xNkpEWUEybFZSY2YwSHk5YXY4ZGQyM3doZ1RLOCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.VwtKsUkgTH94M7NNf97TLlsMiXU7skxcMxrb8mcJLYE_ZhjEuvZ-qlA56mKoS9ffQ1gD3C-O7D21Jojk0Fp1pgYG8UXuOo0TMeHiKzn22C9D70TlayZtXAOag__ON0jOhZMuXeZ8fzLZlzdrNUImGz2pxQc68JRThtb8pOY7F9--PTCXXrP0or6FLs3MRVlXLZDkxmZccQquV5cLXZM-cB8nX4L0YWU78HzM86J5pUq2qcsmwIPhRj753czsBqBuvreB-pqz-eHJIj_o3atgHtj6qe6XdIOzLbFfrHsf_nL1HxRA6cKzxHocpGBuCtqhhB4IQiuevNWqWtJRinbvZg' --data-raw ''

    Fetches a list of movies
        List of movies with following fields:
            integer id
            string name
            date release_date
        boolean success

Example response

{
  "movies": [
    {
      "id": 1, 
      "release_date": "Tue, 04 Aug 2020 00:00:00 GMT", 
      "title": "The return of the Big Lung"
    }, 
    {
      "id": 2, 
      "release_date": "Wed, 05 Aug 2020 00:00:00 GMT", 
      "title": "The happiness of a Wednesday"
    }
  ], 
  "success": true
}


Errors

If you try to fetch a page that does not have any movies, you will encounter a error which looks like this:

$ curl --location --request GET 'https://vast-inlet-80598.herokuapp.com/movies?page=12373281' --header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxaMUoyVnplalRiUjhYb0liV1BEMSJ9.eyJpc3MiOiJodHRwczovL24xZWxsYXMuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMWFlYmExM2U2NGNjMDAzZDY4Yzc5YyIsImF1ZCI6ImFnZW5jeSIsImlhdCI6MTU5Nzc1NTEzMSwiZXhwIjoxNTk3ODQxNTMxLCJhenAiOiJxNG1xNkpEWUEybFZSY2YwSHk5YXY4ZGQyM3doZ1RLOCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.VwtKsUkgTH94M7NNf97TLlsMiXU7skxcMxrb8mcJLYE_ZhjEuvZ-qlA56mKoS9ffQ1gD3C-O7D21Jojk0Fp1pgYG8UXuOo0TMeHiKzn22C9D70TlayZtXAOag__ON0jOhZMuXeZ8fzLZlzdrNUImGz2pxQc68JRThtb8pOY7F9--PTCXXrP0or6FLs3MRVlXLZDkxmZccQquV5cLXZM-cB8nX4L0YWU78HzM86J5pUq2qcsmwIPhRj753czsBqBuvreB-pqz-eHJIj_o3atgHtj6qe6XdIOzLbFfrHsf_nL1HxRA6cKzxHocpGBuCtqhhB4IQiuevNWqWtJRinbvZg' --data-raw ''

will return

{
  "error": 404 Not Found,
  "message": "no movies found in database.",
}

6. POST /movies

Inserting a new Movie into the database.

$ curl --location --request POST 'https://vast-inlet-80598.herokuapp.com/movies' --header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxaMUoyVnplalRiUjhYb0liV1BEMSJ9.eyJpc3MiOiJodHRwczovL24xZWxsYXMuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMWFlYmExM2U2NGNjMDAzZDY4Yzc5YyIsImF1ZCI6ImFnZW5jeSIsImlhdCI6MTU5Nzc1NTEzMSwiZXhwIjoxNTk3ODQxNTMxLCJhenAiOiJxNG1xNkpEWUEybFZSY2YwSHk5YXY4ZGQyM3doZ1RLOCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.VwtKsUkgTH94M7NNf97TLlsMiXU7skxcMxrb8mcJLYE_ZhjEuvZ-qlA56mKoS9ffQ1gD3C-O7D21Jojk0Fp1pgYG8UXuOo0TMeHiKzn22C9D70TlayZtXAOag__ON0jOhZMuXeZ8fzLZlzdrNUImGz2pxQc68JRThtb8pOY7F9--PTCXXrP0or6FLs3MRVlXLZDkxmZccQquV5cLXZM-cB8nX4L0YWU78HzM86J5pUq2qcsmwIPhRj753czsBqBuvreB-pqz-eHJIj_o3atgHtj6qe6XdIOzLbFfrHsf_nL1HxRA6cKzxHocpGBuCtqhhB4IQiuevNWqWtJRinbvZg' --header 'Content-Type: application/json' --data-raw '{
    "title": "The Boringness of the Abyss",
    "release_date": "Thur, 1 Oct 2020"
}'

Example response

{
    "created": 3,
    "success": true
}

Errors

If you try to create a new movie without a requiered field like release_date, it will throw a 422 error:

$ curl --location --request POST 'https://vast-inlet-80598.herokuapp.com/movies' --header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxaMUoyVnplalRiUjhYb0liV1BEMSJ9.eyJpc3MiOiJodHRwczovL24xZWxsYXMuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMWFlYmExM2U2NGNjMDAzZDY4Yzc5YyIsImF1ZCI6ImFnZW5jeSIsImlhdCI6MTU5Nzc1NTEzMSwiZXhwIjoxNTk3ODQxNTMxLCJhenAiOiJxNG1xNkpEWUEybFZSY2YwSHk5YXY4ZGQyM3doZ1RLOCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.VwtKsUkgTH94M7NNf97TLlsMiXU7skxcMxrb8mcJLYE_ZhjEuvZ-qlA56mKoS9ffQ1gD3C-O7D21Jojk0Fp1pgYG8UXuOo0TMeHiKzn22C9D70TlayZtXAOag__ON0jOhZMuXeZ8fzLZlzdrNUImGz2pxQc68JRThtb8pOY7F9--PTCXXrP0or6FLs3MRVlXLZDkxmZccQquV5cLXZM-cB8nX4L0YWU78HzM86J5pUq2qcsmwIPhRj753czsBqBuvreB-pqz-eHJIj_o3atgHtj6qe6XdIOzLbFfrHsf_nL1HxRA6cKzxHocpGBuCtqhhB4IQiuevNWqWtJRinbvZg' --header 'Content-Type: application/json' --data-raw '{
    "title": "The Boringness of the Abyss"
}'

will return

{
  "error": 422 Unprocessable Entity,
  "message": "No release date provided.",
}

7. PATCH /movies

Editing an existing Movie

$ curl --location --request PATCH 'https://vast-inlet-80598.herokuapp.com/movies/1' --header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxaMUoyVnplalRiUjhYb0liV1BEMSJ9.eyJpc3MiOiJodHRwczovL24xZWxsYXMuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMWFlYmExM2U2NGNjMDAzZDY4Yzc5YyIsImF1ZCI6ImFnZW5jeSIsImlhdCI6MTU5Nzc1NTEzMSwiZXhwIjoxNTk3ODQxNTMxLCJhenAiOiJxNG1xNkpEWUEybFZSY2YwSHk5YXY4ZGQyM3doZ1RLOCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.VwtKsUkgTH94M7NNf97TLlsMiXU7skxcMxrb8mcJLYE_ZhjEuvZ-qlA56mKoS9ffQ1gD3C-O7D21Jojk0Fp1pgYG8UXuOo0TMeHiKzn22C9D70TlayZtXAOag__ON0jOhZMuXeZ8fzLZlzdrNUImGz2pxQc68JRThtb8pOY7F9--PTCXXrP0or6FLs3MRVlXLZDkxmZccQquV5cLXZM-cB8nX4L0YWU78HzM86J5pUq2qcsmwIPhRj753czsBqBuvreB-pqz-eHJIj_o3atgHtj6qe6XdIOzLbFfrHsf_nL1HxRA6cKzxHocpGBuCtqhhB4IQiuevNWqWtJRinbvZg' --header 'Content-Type: application/json' --data-raw '{
    "title": "Something to Ponder",
    "release_date": "Fri, 28 Dec 2020"
}'


Example response

{
  "edited": 1, 
  "movie": [
    {
      "id": 1, 
      "release_date": "Mon, 28 Dec 2020 00:00:00 GMT", 
      "title": "Something to Ponder"
    }
  ], 
  "success": true
}


Errors

If you try to update a movie with an invalid id it will throw an 404 error:

$ curl --location --request PATCH 'https://vast-inlet-80598.herokuapp.com/movies/928' --header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxaMUoyVnplalRiUjhYb0liV1BEMSJ9.eyJpc3MiOiJodHRwczovL24xZWxsYXMuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMWFlYmExM2U2NGNjMDAzZDY4Yzc5YyIsImF1ZCI6ImFnZW5jeSIsImlhdCI6MTU5Nzc1NTEzMSwiZXhwIjoxNTk3ODQxNTMxLCJhenAiOiJxNG1xNkpEWUEybFZSY2YwSHk5YXY4ZGQyM3doZ1RLOCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.VwtKsUkgTH94M7NNf97TLlsMiXU7skxcMxrb8mcJLYE_ZhjEuvZ-qlA56mKoS9ffQ1gD3C-O7D21Jojk0Fp1pgYG8UXuOo0TMeHiKzn22C9D70TlayZtXAOag__ON0jOhZMuXeZ8fzLZlzdrNUImGz2pxQc68JRThtb8pOY7F9--PTCXXrP0or6FLs3MRVlXLZDkxmZccQquV5cLXZM-cB8nX4L0YWU78HzM86J5pUq2qcsmwIPhRj753czsBqBuvreB-pqz-eHJIj_o3atgHtj6qe6XdIOzLbFfrHsf_nL1HxRA6cKzxHocpGBuCtqhhB4IQiuevNWqWtJRinbvZg' --header 'Content-Type: application/json' --data-raw '{
    "title": "Something to Ponder",
    "release_date": "Fri, 28 Dec 2020"
}'

will return

{
  "error": 404 Not Found,
  "message": "Movie with id 928 not found in database.",
}

8. DELETE /movies

Deleting a movie

$ curl --location --request DELETE 'https://vast-inlet-80598.herokuapp.com/movies/1' --header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxaMUoyVnplalRiUjhYb0liV1BEMSJ9.eyJpc3MiOiJodHRwczovL24xZWxsYXMuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMWFlYmExM2U2NGNjMDAzZDY4Yzc5YyIsImF1ZCI6ImFnZW5jeSIsImlhdCI6MTU5Nzc1NTEzMSwiZXhwIjoxNTk3ODQxNTMxLCJhenAiOiJxNG1xNkpEWUEybFZSY2YwSHk5YXY4ZGQyM3doZ1RLOCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.VwtKsUkgTH94M7NNf97TLlsMiXU7skxcMxrb8mcJLYE_ZhjEuvZ-qlA56mKoS9ffQ1gD3C-O7D21Jojk0Fp1pgYG8UXuOo0TMeHiKzn22C9D70TlayZtXAOag__ON0jOhZMuXeZ8fzLZlzdrNUImGz2pxQc68JRThtb8pOY7F9--PTCXXrP0or6FLs3MRVlXLZDkxmZccQquV5cLXZM-cB8nX4L0YWU78HzM86J5pUq2qcsmwIPhRj753czsBqBuvreB-pqz-eHJIj_o3atgHtj6qe6XdIOzLbFfrHsf_nL1HxRA6cKzxHocpGBuCtqhhB4IQiuevNWqWtJRinbvZg' --header 'Content-Type: application/json' --data-raw ''

Example response

{
  "deleted": 1, 
  "success": true
}

Errors

If you try to delete a movie with an invalid id, it will throw a 404 Error:

$ curl --location --request DELETE 'https://vast-inlet-80598.herokuapp.com/movies/639' --header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxaMUoyVnplalRiUjhYb0liV1BEMSJ9.eyJpc3MiOiJodHRwczovL24xZWxsYXMuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMWFlYmExM2U2NGNjMDAzZDY4Yzc5YyIsImF1ZCI6ImFnZW5jeSIsImlhdCI6MTU5Nzc1NTEzMSwiZXhwIjoxNTk3ODQxNTMxLCJhenAiOiJxNG1xNkpEWUEybFZSY2YwSHk5YXY4ZGQyM3doZ1RLOCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.VwtKsUkgTH94M7NNf97TLlsMiXU7skxcMxrb8mcJLYE_ZhjEuvZ-qlA56mKoS9ffQ1gD3C-O7D21Jojk0Fp1pgYG8UXuOo0TMeHiKzn22C9D70TlayZtXAOag__ON0jOhZMuXeZ8fzLZlzdrNUImGz2pxQc68JRThtb8pOY7F9--PTCXXrP0or6FLs3MRVlXLZDkxmZccQquV5cLXZM-cB8nX4L0YWU78HzM86J5pUq2qcsmwIPhRj753czsBqBuvreB-pqz-eHJIj_o3atgHtj6qe6XdIOzLbFfrHsf_nL1HxRA6cKzxHocpGBuCtqhhB4IQiuevNWqWtJRinbvZg' --header 'Content-Type: application/json' --data-raw ''

will return

{
  "error": 404 Not Found,
  "message": "Movie with id 639 not found in database.",
  "success": false
}

