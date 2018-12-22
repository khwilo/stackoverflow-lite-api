# Stack Overflow Lite API

[![Build Status](https://travis-ci.org/khwilo/stackoverflow-lite-api.svg?branch=develop)](https://travis-ci.org/khwilo/stackoverflow-lite-api) [![Coverage Status](https://coveralls.io/repos/github/khwilo/stackoverflow-lite-api/badge.svg?branch=develop)](https://coveralls.io/github/khwilo/stackoverflow-lite-api?branch=develop)

API endpoints for the [Stack Overflow Lite](https://khwilo.github.io/stackoverflow-lite/UI/) web application.

## API endpoints descriptions

- `POST '/auth/signup'` - Register a new user
- `POST '/auth/login'` - Login a registered user
- `POST '/api/v1/questions'` - Post a question
- `GET '/api/v1/questions'` - Fetch all questions
- `GET '/api/v1/questions/<questionId>'` - Fetch a specific question
- `DELETE '/api/v1/questions/<questionId>'` - Delete a specific question
- `POST '/api/v1/questions/<questionId>/answers'` - Post an answer to a question
- `PUT '/api/v1/questions/<questionId>/answers/<answerId>'` - Update the description of the answer or mark the answer as accepted/rejected
