Requests table - names of columns updated (request_from, request_to)

- run: createdb roammates
- the access through tableplus or run in browser: postgresql://dev:roammates@localhost/roammates
- seed the database from main dir run: psql -h 127.0.0.1 roammates < api/seeds/roammates_seed.sql

Granting access to DB:
- run: createdb test_roammates
- in sql run: CREATE USER dev WITH PASSWORD roammates;
- GRANT ALL PRIVILEGES ON DATABASE test_roammates TO dev;

