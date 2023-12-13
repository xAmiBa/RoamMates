

DROP TABLE IF EXISTS preferences;
DROP SEQUENCE IF EXISTS preferences_id_seq;
DROP TABLE IF EXISTS requests;
DROP SEQUENCE IF EXISTS requests_id_seq;
DROP TABLE IF EXISTS profiles;
DROP SEQUENCE IF EXISTS profiles_id_seq;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username text,
  password text,
  email text
);

INSERT INTO users (username, password, email) VALUES ('amina', 'amina1', 'amina@gmail.com');
INSERT INTO users (username, password, email) VALUES ('daniel', 'daniel1', 'daniel@gmail.com');



-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS profiles_id_seq;
CREATE TABLE profiles (
  id SERIAL PRIMARY KEY,
  user_id int,
  picture text,
  name text,
  age text,
  gender text,
  bio text,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

INSERT INTO profiles (user_id, picture, name, age, gender, bio) VALUES (1, null, 'Amina', '28', 'Female', 'Test bio Amina');
INSERT INTO profiles (user_id, picture, name, age, gender, bio) VALUES (2, null, 'Daniel', '24', 'Male', 'Test bio Daniel');


CREATE SEQUENCE IF NOT EXISTS requests_id_seq;
CREATE TABLE requests (
  id SERIAL PRIMARY KEY,
  status boolean,
  request_from int,
  request_to int,
  FOREIGN KEY (request_to) REFERENCES users(id) ON DELETE CASCADE
);

INSERT INTO requests (status, request_from, request_to) VALUES (null, 1, 2); -- unresolved request
INSERT INTO requests (status, request_from, request_to) VALUES (true, 2, 1); -- resolved request (accepted)


CREATE SEQUENCE IF NOT EXISTS preferences_id_seq;
CREATE TABLE preferences (
  id SERIAL PRIMARY KEY,
  user_id int,
  age_slot text,
  gender text,
  continent text,
  season text,
  category text,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

INSERT INTO preferences (user_id, age_slot, gender, continent, season, category) VALUES (1, '[18, 24]', 'Other', 'North America', 'Winter', 'Resort'); 
INSERT INTO preferences (user_id, age_slot, gender, continent, season, category) VALUES (2, '[25, 30]', 'Female', 'Europe', 'Spring', 'Beach'); 

-- # Write file into database in terminal
-- run from api dir
-- psql -h 127.0.0.1 roammates < seeds/roammates_seed.sql
-- or run from main dir
-- psql -h 127.0.0.1 roammates < api/seeds/roammates_seed.sql
