GRANT ALL PRIVILEGES ON DATABASE arrangealldb TO arrangeall;

CREATE TABLE services (
service_id BIGSERIAL NOT NULL PRIMARY KEY,
service_name VARCHAR(50) NOT NULL);

CREATE TABLE users (
user_id BIGSERIAL NOT NULL PRIMARY KEY, 
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL,
email VARCHAR(150) UNIQUE NOT NULL,
password VARCHAR(150) NOT NULL,
username VARCHAR(50) UNIQUE NOT NULL,
role VARCHAR(10) NOT NULL);

CREATE TABLE businesses (
business_id BIGSERIAL NOT NULL PRIMARY KEY, 
business_name VARCHAR(100) NOT NULL,
address VARCHAR(150) NOT NULL,
city VARCHAR(50) NOT NULL,
zip_code VARCHAR(5) NOT NULL,
business_email VARCHAR(150) NOT NULL,
business_phone VARCHAR(12) NOT NULL,
max_capacity INT NOT NULL,
owner_id INT NOT NULL REFERENCES users(user_id),
service_id INT REFERENCES services(service_id));

CREATE TABLE appointment (
appt_id BIGSERIAL NOT NULL PRIMARY KEY,
start_time VARCHAR(50) NOT NULL,
end_time VARCHAR(50) NOT NULL,
confirmation_number INT,
business_id INT NOT NULL REFERENCES businesses(business_id),
business_name VARCHAR(100) NOT NULL,
user_id INT REFERENCES users(user_id),
number_of_customers INT);

INSERT INTO services(service_name) VALUES ('food');
INSERT INTO services(service_name) VALUES ('transportation');
INSERT INTO services(service_name) VALUES ('health');
INSERT INTO services(service_name) VALUES ('utilities');
INSERT INTO services(service_name) VALUES ('clothes');
INSERT INTO services(service_name) VALUES ('sports');
INSERT INTO services(service_name) VALUES ('technology');
INSERT INTO services(service_name) VALUES ('education');
INSERT INTO services(service_name) VALUES ('pets');

INSERT INTO users(first_name, last_name, email, password, username, role) VALUES ('carlos', 'torres', 'carlos@gmail.com', 'carlos', 'carlos', 'customer');
INSERT INTO users(first_name, last_name, email, password, username, role) VALUES ('carlos2', 'torres2', 'carlos2@gmail.com', 'carlos2', 'carlos2', 'owner');
INSERT INTO users(first_name, last_name, email, password, username, role) VALUES ('seba', 'ster', 'sebaster@gmail.com', 'seba123', 'sebaster', 'owner');

INSERT INTO businesses(business_name, address, city, zip_code, business_email, business_phone, max_capacity, owner_id, service_id) VALUES ('Jaranas', 'Calle Post', 'Mayaguez', '00680', 'jaranas@gmail.com', '787-111-2222', 25, 3, 1);
INSERT INTO businesses(business_name, address, city, zip_code, business_email, business_phone, max_capacity, owner_id, service_id) VALUES ('Casianos', 'Avenida Eugenio Maria de Hostos', 'Mayaguez', '00682', 'casianos@gmail.com', '787-333-4444', 15, 2, 1);
INSERT INTO businesses(business_name, address, city, zip_code, business_email, business_phone, max_capacity, owner_id, service_id) VALUES ('Don Cafe', 'Calle Post', 'Mayaguez', '00680', 'doncafe@gmail.com', '787-555-7777', 40, 3, 1);

INSERT INTO appointment(start_time, end_time, confirmation_number, business_id, business_name, user_id, number_of_customers) VALUES ('November 11 at 2:00 PM', 'November 11 at 3:00 PM', 5678, 1, 'Jaranas', 1, 2);
INSERT INTO appointment(start_time, end_time, confirmation_number, business_id, business_name, user_id, number_of_customers) VALUES ('November 13 at 11:00 AM', 'November 13 at 12:00 AM', 1234, 2, 'Casianos', 1, 4);
INSERT INTO appointment(start_time, end_time, confirmation_number, business_id, business_name, user_id, number_of_customers) VALUES ('November 15 at 8:00 AM', 'November 15 at 9:00 AM', 4321, 3, 'Don Cafe', 1, 1);
