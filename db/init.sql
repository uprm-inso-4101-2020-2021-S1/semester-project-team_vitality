GRANT ALL PRIVILEGES ON DATABASE arrangealldb TO arrangeall;

CREATE TABLE services (
serviceId BIGSERIAL NOT NULL PRIMARY KEY,
service_name VARCHAR(50) NOT NULL);

CREATE TABLE users (
userid BIGSERIAL NOT NULL PRIMARY KEY, 
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL,
email VARCHAR(150) UNIQUE NOT NULL,
password VARCHAR(150) NOT NULL,
username VARCHAR(50) UNIQUE NOT NULL,
role VARCHAR(10) NOT NULL);

CREATE TABLE businesses (
businessId BIGSERIAL NOT NULL PRIMARY KEY, 
business_name VARCHAR(100) NOT NULL,
address VARCHAR(150) NOT NULL,
city VARCHAR(50) NOT NULL,
zip_code VARCHAR(5) NOT NULL,
business_email VARCHAR(150) NOT NULL,
business_phone VARCHAR(12) NOT NULL,
max_capacity INT NOT NULL,
business_ownerId INT NOT NULL REFERENCES users(userid),
serviceId INT REFERENCES services(serviceId));

CREATE TABLE appointment (
apptId BIGSERIAL NOT NULL PRIMARY KEY, 
start_time TIMESTAMP NOT NULL,
end_time TIMESTAMP NOT NULL,
confirmation_number INT,
businessId INT NOT NULL REFERENCES businesses(businessId),
userid INT REFERENCES users(userid));

INSERT INTO services(service_name) VALUES ('food');
INSERT INTO services(service_name) VALUES ('transportation');
INSERT INTO services(service_name) VALUES ('health');
INSERT INTO services(service_name) VALUES ('hair');
INSERT INTO services(service_name) VALUES ('construction');
INSERT INTO services(service_name) VALUES ('clothes');
INSERT INTO services(service_name) VALUES ('sports');
INSERT INTO services(service_name) VALUES ('technology');
INSERT INTO services(service_name) VALUES ('education');
INSERT INTO services(service_name) VALUES ('pets');

INSERT INTO users(first_name, last_name, email, password, username, role) VALUES ('carlos', 'torres', 'carlos@gmail.com', 'carlos', 'carlos', 'customer');
INSERT INTO users(first_name, last_name, email, password, username, role) VALUES ('carlos2', 'torres2', 'carlos2@gmail.com', 'carlos2', 'carlos2', 'customer');
INSERT INTO users(first_name, last_name, email, password, username, role) VALUES ('seba', 'ster', 'sebaster@gmail.com', 'seba123', 'sebaster', 'owner');

INSERT INTO businesses(business_name, address, city, zip_code, business_email, business_phone, max_capacity, business_ownerid, serviceid) VALUES ('Jaranas', 'Calle Post', 'maya', '00680', 'jaranas@gmail.com', '787-111-2222', 25, 3, 1);