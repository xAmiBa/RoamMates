

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
  email text,
  UNIQUE (email)
);

INSERT INTO users (username, password, email) VALUES ('amina', 'amina1', 'amina@gmail.com');
INSERT INTO users (username, password, email) VALUES ('daniel', 'daniel1', 'daniel@gmail.com');
INSERT INTO users (username, password, email) VALUES ('piotr', 'piotr1', 'piotr@gmail.com');
INSERT INTO users (username, password, email) VALUES ('david', 'david1', 'david1@gmail.com');
INSERT INTO users (username, password, email) VALUES
('traveler01', 'pass123', 'traveler01@example.com'),
('wanderlust22', 'explore321', 'wanderlust22@example.com'),
('globe_trotter', 'worldtraveler', 'globe_trotter@example.com'),
('adventurous_soul', 'discoveries456', 'adventurous_soul@example.com'),
('exploration_master', 'journey789', 'exploration_master@example.com'),
('journey_seeker', 'adventure456', 'journey_seeker@example.com'),
('world_explorer', 'explore789', 'world_explorer@example.com'),
('nomadic_spirit', 'nomad123', 'nomadic_spirit@example.com'),
('discoverer123', 'discoverpass', 'discoverer123@example.com'),
('globetrotting_guru', 'gurutravel', 'globetrotting_guru@example.com'),
('travel_enthusiast', 'enthusiastic123', 'travel_enthusiast@example.com'),
('explorer_adventures', 'adventures456', 'explorer_adventures@example.com'),
('wanderer55', 'wander55', 'wanderer55@example.com'),
('jetsetter22', 'jetset22', 'jetsetter22@example.com'),
('adventure_seekers', 'seekers789', 'adventure_seekers@example.com'),
('nomad_life', 'nomadlife123', 'nomad_life@example.com'),
('explore_the_world', 'exploreworld', 'explore_the_world@example.com'),
('roaming_free', 'free123', 'roaming_free@example.com'),
('discover_everywhere', 'everywhere456', 'discover_everywhere@example.com'),
('passport_ready', 'passport123', 'passport_ready@example.com'),
('globetrotting_dreamer', 'dreamer789', 'globetrotting_dreamer@example.com'),
('wanderlust_passion', 'passion123', 'wanderlust_passion@example.com'),
('journey_inspirer', 'inspirer456', 'journey_inspirer@example.com'),
('exploration_addict', 'addict789', 'exploration_addict@example.com'),
('travel_buff', 'buff123', 'travel_buff@example.com'),
('adventure_seeker', 'seeker789', 'adventure_seeker@example.com'),
('wandering_heart', 'heart123', 'wandering_heart@example.com'),
('discovery_quest', 'quest456', 'discovery_quest@example.com'),
('explore_and_dream', 'dream123', 'explore_and_dream@example.com'),
('world_wanderer', 'wanderer789', 'world_wanderer@example.com'),
('nomad_soul', 'soul123', 'nomad_soul@example.com'),
('adventure_awaits', 'awaits456', 'adventure_awaits@example.com'),
('travel_dreamer', 'dreamer789', 'travel_dreamer@example.com'),
('wanderlust_journey', 'journey123', 'wanderlust_journey@example.com'),
('exploration_lover', 'lover456', 'exploration_lover@example.com'),
('journey_explorer', 'explorer789', 'journey_explorer@example.com'),
('discover_new_horizons', 'horizons123', 'discover_new_horizons@example.com'),
('adventurous_spirit', 'spirit456', 'adventurous_spirit@example.com'),
('explore_the_unknown', 'unknown789', 'explore_the_unknown@example.com'),
('wander_and_wonder', 'wonder123', 'wander_and_wonder@example.com'),
('travel_passionate', 'passionate789', 'travel_passionate@example.com'),
('global_nomad', 'globalnomad123', 'global_nomad@example.com'),
('adventure_joy', 'joy456', 'adventure_joy@example.com'),
('explorer_of_worlds', 'worlds789', 'explorer_of_worlds@example.com'),
('discoverer_spirit', 'spirit123', 'discoverer_spirit@example.com'),
('wanderlust_dreaming', 'dreaming789', 'wanderlust_dreaming@example.com');

-- Then, we recreate them
-- CREATE SEQUENCE IF NOT EXISTS profiles_id_seq;
CREATE TABLE profiles (
  user_id INT PRIMARY KEY,
  picture text,
  name text,
  age text,
  gender text,
  bio text,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

INSERT INTO profiles (user_id, picture, name, age, gender, bio) VALUES
(1, 'https://www.echoclinics.nhs.uk/wp-content/uploads/female-placeholder.jpg', 'Amina', '25', 'female', 'Passionate about exploring new cultures and trying local cuisines. Always seeking the next adventure to add to my travel diary. On a mission to visit every continent and experience the diversity our world has to offer.'),
(2, 'https://www.treasury.gov.ph/wp-content/uploads/2022/01/male-placeholder-image.jpeg', 'Daniel', '30', 'male', 'Adventure enthusiast with a love for nature and outdoor activities. Constantly looking for hidden gems off the beaten path. I believe that every journey is an opportunity to learn and grow.'),
(3, 'https://www.echoclinics.nhs.uk/wp-content/uploads/female-placeholder.jpg', 'Kai', '22', 'other', 'Test user with a passion for testing the limits of exploration. Seeking unique experiences and meeting fellow travelers along the way. Lets embark on a journey of discovery together.'),
(4, 'https://www.treasury.gov.ph/wp-content/uploads/2022/01/male-placeholder-image.jpeg', 'Jenny', '28', 'other', 'Travel enthusiast exploring new horizons and creating memories. Join me on this exciting journey as we uncover the wonders of the world.'),
(5, 'https://www.echoclinics.nhs.uk/wp-content/uploads/female-placeholder.jpg', 'Pablo', '24', 'other', 'Just a soul with an insatiable wanderlust, always seeking new places and faces. Lets share stories and make memories in every corner of the globe.'),
(6, 'https://www.treasury.gov.ph/wp-content/uploads/2022/01/male-placeholder-image.jpeg', 'Julius', '29', 'other', 'Adventurous spirit with an open mind and a curious heart. Embracing the unknown and finding joy in every journey. Join me on the quest for the extraordinary.'),
(7, 'https://www.echoclinics.nhs.uk/wp-content/uploads/female-placeholder.jpg', 'Testuser', '27', 'other', 'Testing the waters of exploration! Seeking travel buddies to share laughter, experiences, and the joy of discovering new places. Let the adventures begin.'),
(8, 'https://www.treasury.gov.ph/wp-content/uploads/2022/01/male-placeholder-image.jpeg', 'Anna', '32', 'female', 'Passionate traveler exploring the world one destination at a time. From bustling cities to serene landscapes, each journey is a chapter in my global adventure.'),
(9, 'https://www.echoclinics.nhs.uk/wp-content/uploads/female-placeholder.jpg', 'Kiki', '26', 'other', 'Wanderer at heart, seeking the thrill of the unknown. Join me in exploring diverse cultures, savoring delicious cuisine, and creating lasting memories.'),
(10, 'https://www.treasury.gov.ph/wp-content/uploads/2022/01/male-placeholder-image.jpeg', 'Jack', '30', 'male', 'World traveler on a mission to experience the beauty of every continent. From iconic landmarks to hidden gems, lets embark on a global journey together.'),
(11, 'https://www.echoclinics.nhs.uk/wp-content/uploads/female-placeholder.jpg', 'Paulina', '34', 'female', 'Adventurous soul with a love for cultural immersion and off-the-beaten-path experiences. Join me in discovering the beauty of our planet and creating memories that last a lifetime.'),
(12, 'https://www.treasury.gov.ph/wp-content/uploads/2022/01/male-placeholder-image.jpeg', 'Lucas', '40', 'male', 'Exploration master on a quest to unravel the mysteries of different landscapes. Lets venture into the unknown and make each journey a unique story to tell.'),
(13, 'https://www.echoclinics.nhs.uk/wp-content/uploads/female-placeholder.jpg', 'Arial', '23', 'other', 'Journey seeker with an insatiable curiosity for new experiences. Whether its the bustling city or serene nature, Im ready to explore and embrace the diversity our world has to offer.'),
(14, 'https://www.treasury.gov.ph/wp-content/uploads/2022/01/male-placeholder-image.jpeg', 'Fatima', '38', 'female', 'Passionate about exploring every corner of the globe. From ancient wonders to modern marvels, I believe in the magic of travel to broaden perspectives and create connections.'),
(15, 'https://www.echoclinics.nhs.uk/wp-content/uploads/female-placeholder.jpg', 'Heydi', '32', 'other', 'Nomadic spirit with a love for spontaneity and adventure. Join me on the journey of a lifetime, filled with laughter, exploration, and the joy of discovering hidden gems.'),
(16, 'https://www.treasury.gov.ph/wp-content/uploads/2022/01/male-placeholder-image.jpeg', 'Francesco', '27', 'male', 'Passionate discoverer with an eye for detail and a heart for exploration. Lets embark on a journey of discovery together, uncovering the beauty of diverse cultures and landscapes.'),
(17, 'https://www.echoclinics.nhs.uk/wp-content/uploads/female-placeholder.jpg', 'Katie', '35', 'female', 'Globetrotting guru with a thirst for knowledge and a love for immersive travel experiences. Join me on a journey of self-discovery and cultural enrichment.'),
(18, 'https://www.treasury.gov.ph/wp-content/uploads/2022/01/male-placeholder-image.jpeg', 'Dave', '29', 'male', 'Enthusiastic traveler seeking the thrill of new adventures. From mountains to beaches, Im ready to explore it all. Lets create unforgettable memories together!'),
(19, 'https://www.echoclinics.nhs.uk/wp-content/uploads/female-placeholder.jpg', 'Lola', '31', 'other', 'Adventures await! Join me in exploring new horizons, meeting diverse people, and savoring the beauty of our planet. Lets make each journey a chapter in our shared story.'),
(20, 'https://www.treasury.gov.ph/wp-content/uploads/2022/01/male-placeholder-image.jpeg', 'Andrew', '25', 'male', 'Wanderer at heart, always seeking the next destination to fuel my curiosity. From city lights to natural wonders, Im on a perpetual quest for exploration and discovery.'),
(21, 'https://www.echoclinics.nhs.uk/wp-content/uploads/female-placeholder.jpg', 'Mike', '30', 'other', 'Jetsetter with a passion for fast-paced exploration. Join me in discovering the worlds most vibrant cities and tranquil retreats. Lets make each journey an unforgettable adventure!'),
(22, 'https://www.treasury.gov.ph/wp-content/uploads/2022/01/male-placeholder-image.jpeg', 'John', '28', 'male', 'Part of the adventure seekers community, Im on a mission to experience the extraordinary. Join me in exploring diverse landscapes and creating memories that last a lifetime.'),
(23, 'https://www.echoclinics.nhs.uk/wp-content/uploads/female-placeholder.jpg', 'Stacy', '33', 'other', 'Living the nomad life and loving every moment. Join me on a journey of freedom, exploration, and cultural immersion. Lets make our own path and discover the beauty of the world together.'),
(24, 'https://www.treasury.gov.ph/wp-content/uploads/2022/01/male-placeholder-image.jpeg', 'Alan', '36', 'male', 'Passionate about exploring the world and embracing diverse cultures. From historic landmarks to hidden gems, lets embark on a journey of discovery together.'),
(25, 'https://www.echoclinics.nhs.uk/wp-content/uploads/female-placeholder.jpg', 'Samantha', '29', 'female', 'Roaming free and embracing the beauty of spontaneous travel. Join me in creating memories in every destination'),
(26, 'https://www.treasury.gov.ph/wp-content/uploads/2022/01/male-placeholder-image.jpeg', 'Discover_Everywhere', '34', 'male', 'Passionate about discovering new places and cultures. Whether its the bustling streets of a city or the tranquility of nature, lets explore everywhere together.'),
(27, 'https://www.echoclinics.nhs.uk/wp-content/uploads/female-placeholder.jpg', 'Ellie', '31', 'female', 'Always with my passport ready for the next adventure. Join me in exploring the worlds wonders, meeting fascinating people, and creating a lifetime of travel memories.'),
(28, 'https://www.treasury.gov.ph/wp-content/uploads/2022/01/male-placeholder-image.jpeg', 'Globetrotting_Dreamer', '37', 'male', 'Dreamer with a passion for globetrotting. Lets turn dreams into reality as we embark on a journey to explore the most beautiful destinations around the globe.'),
(29, 'https://www.echoclinics.nhs.uk/wp-content/uploads/female-placeholder.jpg', 'Onoura', '29', 'female', 'Wanderlust-filled soul with a passion for travel. Join me on an adventure of discovery, where every new destination becomes a canvas for shared memories and experiences.'),
(30, 'https://www.treasury.gov.ph/wp-content/uploads/2022/01/male-placeholder-image.jpeg', 'Joe', '33', 'male', 'Inspiring journeys one adventure at a time. Join me on a quest to explore the world, find hidden gems, and inspire others to embark on their own extraordinary journeys.'),
(31, 'https://www.echoclinics.nhs.uk/wp-content/uploads/female-placeholder.jpg', 'Maymuna', '35', 'female', 'Addicted to exploration and seeking the next thrill. From bustling cities to serene landscapes, Im on a constant quest for new experiences and unforgettable moments.'),
(32, 'https://www.treasury.gov.ph/wp-content/uploads/2022/01/male-placeholder-image.jpeg', 'Dan', '28', 'male', 'A travel buff with a love for diverse cultures and cuisines. Join me in the pursuit of unique travel experiences, where every journey unfolds a new chapter of adventure.'),
(33, 'https://www.echoclinics.nhs.uk/wp-content/uploads/female-placeholder.jpg', 'Ewa', '30', 'female', 'Seeking the thrill of adventure in every destination. Join me on an expedition to discover the beauty of the world, meet incredible people, and create lasting memories.'),
(34, 'https://www.treasury.gov.ph/wp-content/uploads/2022/01/male-placeholder-image.jpeg', 'Solomon', '32', 'male', 'With a wandering heart and an open mind, Im ready to explore the wonders of the world. Join me in embracing diverse cultures, captivating landscapes, and the joy of discovery.'),
(35, 'https://www.echoclinics.nhs.uk/wp-content/uploads/female-placeholder.jpg', 'Elle', '29', 'other', 'Embarking on a quest for discovery and adventure. Join me as we explore new horizons, from ancient wonders to modern marvels, creating unforgettable moments along the way.'),
(36, 'https://www.treasury.gov.ph/wp-content/uploads/2022/01/male-placeholder-image.jpeg', 'Sudhansh', '36', 'male', 'On a mission to explore and dream big. Join me in uncovering the beauty of the world, embracing diverse cultures, and making each journey a canvas for dreams to come true.'),
(37, 'https://www.echoclinics.nhs.uk/wp-content/uploads/female-placeholder.jpg', 'Khadija', '33', 'female', 'Wandering the world with curiosity and wonder. Join me in discovering hidden gems, connecting with locals, and making memories in every corner of our beautiful planet.'),
(38, 'https://www.treasury.gov.ph/wp-content/uploads/2022/01/male-placeholder-image.jpeg', 'Amir', '31', 'male', 'A nomad soul with a passion for freedom and exploration. Join me in embracing the nomadic lifestyle, discovering new cultures, and creating a life filled with incredible adventures.'),
(39, 'https://www.echoclinics.nhs.uk/wp-content/uploads/female-placeholder.jpg', 'Andrea', '28', 'female', 'An adventurer at heart, always ready for what awaits. Join me in exploring the unknown, seeking thrills, and creating stories that will be cherished for a lifetime.'),
(40, 'https://www.echoclinics.nhs.uk/wp-content/uploads/female-placeholder.jpg', 'Carolina', '31', 'female', 'Bringing joy to every adventure and seeking happiness in exploration. Join me in discovering the beauty of our world, finding joy in the journey, and making each moment a celebration of life.'),
(41, 'https://www.echoclinics.nhs.uk/wp-content/uploads/female-placeholder.jpg', 'Daria', '26', 'female', 'Dreaming of far-off places and exciting adventures. Join me in turning travel dreams into reality, exploring the world, and making memories that last a lifetime.'),
(42, 'https://www.treasury.gov.ph/wp-content/uploads/2022/01/male-placeholder-image.jpeg', 'Ali', '29', 'male', 'Embarking on a wanderlust-filled journey of discovery. From mountains to beaches, join me in exploring the beauty of diverse landscapes and creating a tapestry of travel experiences.'),
(43, 'https://www.echoclinics.nhs.uk/wp-content/uploads/female-placeholder.jpg', 'Ellen', '32', 'female', 'Lover of exploration and seeker of new horizons. Join me in the adventure of a lifetime, where every journey becomes an opportunity for personal growth, cultural immersion, and shared experiences.'),
(44, 'https://www.treasury.gov.ph/wp-content/uploads/2022/01/male-placeholder-image.jpeg', 'Hilary', '27', 'male', 'Exploring the world one journey at a time. Join me in discovering new perspectives, meeting fascinating people, and making every expedition a story worth telling.'),
(45, 'https://www.echoclinics.nhs.uk/wp-content/uploads/female-placeholder.jpg', 'Selma', '30', 'other', 'On a mission to discover new horizons and embrace the unknown. Join me in navigating through diverse cultures, uncovering hidden gems, and creating a mosaic of travel memories.'),
(46, 'https://www.treasury.gov.ph/wp-content/uploads/2022/01/male-placeholder-image.jpeg', 'Henry', '28', 'other', 'Fueled by an adventurous spirit and a love for the extraordinary. Join me in seeking out adrenaline-pumping experiences, exploring the unexplored, and making each journey unforgettable.'),
(47, 'https://www.echoclinics.nhs.uk/wp-content/uploads/female-placeholder.jpg', 'Hafsah', '35', 'female', 'Fearlessly exploring the unknown and embracing the thrill of discovery. Join me in venturing beyond familiar boundaries, experiencing new cultures, and making the uncharted territory our playground.'),
(48, 'https://www.treasury.gov.ph/wp-content/uploads/2022/01/male-placeholder-image.jpeg', 'Matt', '32', 'male', 'Wandering through diverse landscapes and wondering at the beauty of the world. Join me in savoring the magic of travel, connecting with different cultures, and creating memories that stand the test of time.'),
(49, 'https://www.echoclinics.nhs.uk/wp-content/uploads/female-placeholder.jpg', 'Gina', '29', 'female', 'Passionate about travel and the endless possibilities it brings. Join me in exploring the wonders of the world, meeting fellow wanderers, and creating a tapestry of travel stories.'),
(50, 'https://www.treasury.gov.ph/wp-content/uploads/2022/01/male-placeholder-image.jpeg', 'Henry', '33', 'other', 'A global nomad with a heart full of wanderlust. Join me in navigating through diverse cultures, embracing the beauty of our planet, and creating a legacy of global adventures.');

CREATE SEQUENCE IF NOT EXISTS requests_id_seq;
CREATE TABLE requests (
  id SERIAL PRIMARY KEY,
  status boolean,
  request_from int,
  request_to int,
  FOREIGN KEY (request_to) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (request_from) REFERENCES users(id) ON DELETE CASCADE

);

INSERT INTO requests (status, request_from, request_to) VALUES (null, 1, 2); -- unresolved request
INSERT INTO requests (status, request_from, request_to) VALUES (true, 2, 1); -- resolved request (accepted)
INSERT INTO requests (status, request_from, request_to) VALUES (null, 7, 18);
INSERT INTO requests (status, request_from, request_to) VALUES (false, 19, 13);
INSERT INTO requests (status, request_from, request_to) VALUES (true, 2, 4);
INSERT INTO requests (status, request_from, request_to) VALUES (null, 10, 3);
INSERT INTO requests (status, request_from, request_to) VALUES (true, 16, 1);
INSERT INTO requests (status, request_from, request_to) VALUES (false, 6, 15);
INSERT INTO requests (status, request_from, request_to) VALUES (null, 20, 12);
INSERT INTO requests (status, request_from, request_to) VALUES (true, 9, 5);
INSERT INTO requests (status, request_from, request_to) VALUES (false, 11, 8);
INSERT INTO requests (status, request_from, request_to) VALUES (true, 14, 17);
INSERT INTO requests (status, request_from, request_to) VALUES (null, 3, 7);
INSERT INTO requests (status, request_from, request_to) VALUES (false, 16, 14);
INSERT INTO requests (status, request_from, request_to) VALUES (true, 20, 2);
INSERT INTO requests (status, request_from, request_to) VALUES (null, 12, 10);
INSERT INTO requests (status, request_from, request_to) VALUES (false, 5, 9);
INSERT INTO requests (status, request_from, request_to) VALUES (true, 4, 6);
INSERT INTO requests (status, request_from, request_to) VALUES (null, 18, 11);
INSERT INTO requests (status, request_from, request_to) VALUES (false, 13, 15);
INSERT INTO requests (status, request_from, request_to) VALUES (true, 8, 19);
INSERT INTO requests (status, request_from, request_to) VALUES (null, 1, 16);
INSERT INTO requests (status, request_from, request_to) VALUES (true, 17, 20);
INSERT INTO requests (status, request_from, request_to) VALUES (false, 15, 12);
INSERT INTO requests (status, request_from, request_to) VALUES (null, 2, 14);
INSERT INTO requests (status, request_from, request_to) VALUES (false, 7, 3);
INSERT INTO requests (status, request_from, request_to) VALUES (true, 1, 4);
INSERT INTO requests (status, request_from, request_to) VALUES (null, 10, 6);
INSERT INTO requests (status, request_from, request_to) VALUES (true, 8, 19);
INSERT INTO requests (status, request_from, request_to) VALUES (false, 13, 11);
INSERT INTO requests (status, request_from, request_to) VALUES (null, 17, 9);
INSERT INTO requests (status, request_from, request_to) VALUES (false, 16, 18);
INSERT INTO requests (status, request_from, request_to) VALUES (true, 5, 2);
INSERT INTO requests (status, request_from, request_to) VALUES (null, 20, 1);
INSERT INTO requests (status, request_from, request_to) VALUES (false, 4, 15);
INSERT INTO requests (status, request_from, request_to) VALUES (true, 3, 7);
INSERT INTO requests (status, request_from, request_to) VALUES (null, 14, 10);
INSERT INTO requests (status, request_from, request_to) VALUES (true, 12, 8);
INSERT INTO requests (status, request_from, request_to) VALUES (false, 19, 13);
INSERT INTO requests (status, request_from, request_to) VALUES (null, 9, 11);
INSERT INTO requests (status, request_from, request_to) VALUES (false, 2, 5);
INSERT INTO requests (status, request_from, request_to) VALUES (true, 1, 18);
INSERT INTO requests (status, request_from, request_to) VALUES (null, 6, 14);
INSERT INTO requests (status, request_from, request_to) VALUES (false, 16, 12);
INSERT INTO requests (status, request_from, request_to) VALUES (true, 8, 3);
INSERT INTO requests (status, request_from, request_to) VALUES (null, 17, 9);
INSERT INTO requests (status, request_from, request_to) VALUES (true, 13, 4);
INSERT INTO requests (status, request_from, request_to) VALUES (false, 10, 15);
INSERT INTO requests (status, request_from, request_to) VALUES (null, 7, 19);
INSERT INTO requests (status, request_from, request_to) VALUES (false, 14, 2);
INSERT INTO requests (status, request_from, request_to) VALUES (true, 11, 5);
INSERT INTO requests (status, request_from, request_to) VALUES (null, 18, 1);
INSERT INTO requests (status, request_from, request_to) VALUES (true, 9, 6);



CREATE SEQUENCE IF NOT EXISTS preferences_id_seq;
CREATE TABLE preferences (
  id SERIAL PRIMARY KEY,
  user_id INT,
  age_slot VARCHAR(10) CHECK (age_slot IN ('[18, 24]', '[25, 30]', '[30, 100]')) NOT NULL,
  gender VARCHAR(10) CHECK (gender IN ('male', 'female', 'other')) NOT NULL,
  continent VARCHAR(20) CHECK (continent IN ('Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania', 'Antarctica')) NOT NULL,
  season VARCHAR(10) CHECK (season IN ('spring', 'summer', 'autumn', 'winter')) NOT NULL,
  category VARCHAR(20) CHECK (category IN ('mountains', 'beach', 'resort', 'city', 'nature', 'sport')) NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

INSERT INTO preferences (user_id, age_slot, gender, continent, season, category) VALUES (1, '[18, 24]', 'other', 'North America', 'winter', 'resort'); 
INSERT INTO preferences (user_id, age_slot, gender, continent, season, category) VALUES (2, '[25, 30]', 'female', 'Europe', 'spring', 'beach'); 
INSERT INTO preferences (user_id, age_slot, gender, continent, season, category) VALUES
(3, '[18, 24]', 'other', 'North America', 'autumn', 'beach'),
(4, '[25, 30]', 'male', 'South America', 'summer', 'nature'),
(5, '[30, 100]', 'female', 'Europe', 'winter', 'resort'),
(6, '[18, 24]', 'male', 'Oceania', 'spring', 'city'),
(7, '[25, 30]', 'female', 'Africa', 'autumn', 'mountains'),
(8, '[30, 100]', 'other', 'Antarctica', 'winter', 'sport'),
(9, '[18, 24]', 'female', 'Asia', 'summer', 'beach'),
(10, '[25, 30]', 'male', 'North America', 'spring', 'nature'),
(11, '[30, 100]', 'female', 'Europe', 'autumn', 'resort'),
(12, '[18, 24]', 'male', 'South America', 'winter', 'city'),
(13, '[25, 30]', 'other', 'Oceania', 'summer', 'mountains'),
(14, '[30, 100]', 'female', 'Africa', 'spring', 'sport'),
(15, '[18, 24]', 'male', 'Antarctica', 'autumn', 'beach'),
(16, '[25, 30]', 'male', 'Asia', 'winter', 'nature'),
(17, '[30, 100]', 'female', 'North America', 'summer', 'resort'),
(18, '[18, 24]', 'other', 'Europe', 'spring', 'city'),
(19, '[25, 30]', 'female', 'South America', 'autumn', 'mountains'),
(20, '[30, 100]', 'male', 'Oceania', 'winter', 'sport'),
(21, '[18, 24]', 'female', 'Africa', 'summer', 'beach'),
(22, '[25, 30]', 'male', 'Antarctica', 'spring', 'nature'),
(23, '[30, 100]', 'other', 'Asia', 'autumn', 'resort'),
(24, '[18, 24]', 'male', 'Europe', 'winter', 'city'),
(25, '[25, 30]', 'female', 'North America', 'summer', 'mountains'),
(26, '[30, 100]', 'male', 'South America', 'spring', 'sport'),
(27, '[18, 24]', 'other', 'Oceania', 'autumn', 'beach'),
(28, '[25, 30]', 'female', 'Africa', 'winter', 'nature'),
(29, '[30, 100]', 'male', 'Asia', 'summer', 'resort'),
(30, '[18, 24]', 'female', 'Antarctica', 'spring', 'city'),
(31, '[25, 30]', 'other', 'Europe', 'autumn', 'mountains'),
(32, '[30, 100]', 'male', 'North America', 'winter', 'sport'),
(33, '[18, 24]', 'male', 'South America', 'summer', 'beach'),
(34, '[25, 30]', 'female', 'Oceania', 'spring', 'nature'),
(35, '[30, 100]', 'other', 'Africa', 'autumn', 'resort'),
(36, '[18, 24]', 'female', 'Asia', 'winter', 'city'),
(37, '[25, 30]', 'male', 'Antarctica', 'summer', 'mountains'),
(38, '[30, 100]', 'male', 'Europe', 'spring', 'sport'),
(39, '[18, 24]', 'female', 'North America', 'autumn', 'beach'),
(40, '[25, 30]', 'other', 'South America', 'winter', 'nature'),
(41, '[30, 100]', 'male', 'Oceania', 'summer', 'resort'),
(42, '[18, 24]', 'male', 'Africa', 'spring', 'city'),
(43, '[25, 30]', 'female', 'Asia', 'autumn', 'mountains'),
(44, '[30, 100]', 'other', 'Antarctica', 'winter', 'sport'),
(45, '[18, 24]', 'female', 'Europe', 'summer', 'beach'),
(46, '[30, 100]', 'male', 'Oceania', 'summer', 'resort'),
(47, '[30, 100]', 'female', 'South America', 'spring', 'nature'),
(48, '[18, 24]', 'male', 'Oceania', 'autumn', 'resort'),
(49, '[25, 30]', 'other', 'Africa', 'winter', 'city'),
(50, '[30, 100]', 'female', 'Asia', 'summer', 'mountains');

-- # Write file into database in terminal
-- run from api dir
-- psql -h 127.0.0.1 roammates < seeds/roammates_seed.sql
-- or run from main dir
-- psql -h 127.0.0.1 roammates < api/seeds/roammates_seed.sql
