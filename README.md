# Politico2
[![Coverage Status](https://coveralls.io/repos/github/BRIGHTON-ASUMANI/politico2/badge.svg?branch=develop-163671198)](https://coveralls.io/github/BRIGHTON-ASUMANI/politico2?branch=develop-163671198)     [![Build Status](https://travis-ci.com/BRIGHTON-ASUMANI/politico2.svg?branch=develop-163671198)](https://travis-ci.com/BRIGHTON-ASUMANI/politico2)      [![Maintainability](https://api.codeclimate.com/v1/badges/1cf13a9a12a4a3fb21be/maintainability)](https://codeclimate.com/github/BRIGHTON-ASUMANI/politico2/maintainability)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d2ff595d97ba4a9b93bce2771ec8561d)](https://www.codacy.com/app/BRIGHTON-ASUMANI/politico2?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=BRIGHTON-ASUMANI/politico2&amp;utm_campaign=Badge_Grade)  [![MIT license](http://img.shields.io/badge/license-MIT-brightgreen.svg)](http://opensource.org/licenses/MIT)    [![Heroku](http:/politico2.herokuapp.com/api/v1/)]     [![Run in Postman](https://run.pstmn.io/button.svg)](https://www.getpostman.com/run-collection/:collection_id)   

An application containing endpoints related to a voting system 

### __Endpoints__
| Route   |      Methods      |  Endpont |
|----------|:-------------:|------:|
| api/v1/parties | POST and GET | Fetch and add parties |
| api/v1/offices | POST and GET | Fetch and add offices |
| api/v1/parties/int:party_id |  GET and DELETE  |   Get a single party and delete a single party |
| api/v1/offices/int:office_id |  GET   |   Get a single office |
| api/v2/parties/int:party_id/name | PATCH  | Edit a party |

### __Technologies used__
1. Flask python framework
2. Travis CI for testing
3. coverage
4. python3.6
5. Code climate
6. JSON

### __Application functionality__
> * As a user i should be able to do the following 
    1. Parties can be created and fetched 
    2. Offices can be created and fetched by the user
    3. Get specific party
    4. Get specific office
    5  Delete a specific party
    6. Edit a specific party

