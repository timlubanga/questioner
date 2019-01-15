[![Build Status](https://travis-ci.org/timlubanga/questioner.svg?branch=develop)](https://travis-ci.org/timlubanga/questioner)
[![Coverage Status](https://coveralls.io/repos/github/timlubanga/questioner/badge.svg?branch=develop)](https://coveralls.io/github/timlubanga/questioner?branch=develop&service=github)
[![Maintainability](https://api.codeclimate.com/v1/badges/681fac35359e2da858bc/maintainability)](https://codeclimate.com/github/timlubanga/questioner/maintainability)

Questioner helps the meetup organizer prioritize
questions to be answered.Questions with the highest number of upvotes are prioritized. Other users can vote on asked questions and they bubble to the top
or bottom of the log. The app allow users to share knowledge and skills in the field of programming. 


## Required Features
  - Create a user account
  - Sign in a user
  - Create a meetup record
  - Create a question record
  - Confirm attendance to a meetup (RSVP)
  - Upvote on a question record
  - Downvote on a question record
  - Fetch all meetup records
  - Fetch a specific meetup record 
## List of endpoints
| Method | Endpoint | functionality |
|--------|----------|----------|
|  POST  | `/api/v1/users/<username> `    |   Create a user account       |
|  POST  | `/api/v1/meetup/<topic_name>`     |   Create a meetup record       |
|  GET  | `/api/v1/meetup/<topic_name> `   | Fetch a specific meetup record. |
|  POST  | `/api/v1/questions/<title_name> `    |   Create a question for a specific meetup.       |
|  Update | `/api/v1/questions/<title_name>    |  Update question record      |
|  delete | `/api/v1/questions/<title_name`   |  delete a user record


## Installation
Install python on your computer
- Clone the repository from github and change directory to Questioner
 ``` 
    $ https://github.com/timlubanga/questioner.git
    $ cd Questioner 
```
- Install a virtual environment and activate it 
 ```
  $ virtualenv env
  $ source env/bin/activate
  ````
- Install all the requirements using requirements.txt
``` 
    $ pip install -r requirements.txt 
```
- Start the flask application
 ```
    $ export FLASK_DEBUG=1
    $ export FLASK_ENV=development
    $ export FLASK_APP=run.py
    $ flask run
 ```
 ## Testing Endpoints
 - Install Post Man http client to test the endpoints
 - Open the Post Man test client and enter an endpoint url
  ```http://localhost:5000/api/v1/<endpoint>```
## Tests
 To run the tests you have to use the terminal in a virtual environment
- To view running of all tests
```
$ cd app/tests/v1     
$ pytest
```
- To view the coverage of all tests
```
$ pytest --cov app
```
## Author 
Timothy lubanga

