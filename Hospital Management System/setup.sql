-- Create database
CREATE DATABASE IF NOT EXISTS user_db;
USE user_db;

-- Table for storing user information (for login)
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role ENUM('Admin', 'Doctor', 'Pharmacist') NOT NULL
);

-- Table for storing doctor information
CREATE TABLE IF NOT EXISTS doctors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    specialization VARCHAR(100),
    phone VARCHAR(15),
    email VARCHAR(100) UNIQUE
);

-- Table for storing patient information
CREATE TABLE IF NOT EXISTS patients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    date_of_birth DATE,
    gender ENUM('Male', 'Female', 'Other'),
    phone VARCHAR(15),
    email VARCHAR(100) UNIQUE
);

-- Table for storing appointments (including patient_name and doctor_name)
CREATE TABLE IF NOT EXISTS appointments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_name VARCHAR(100) NOT NULL,
    doctor_name VARCHAR(100) NOT NULL,
    date DATE NOT NULL,
    time TIME NOT NULL,
    FOREIGN KEY (patient_name) REFERENCES patients(name) ON DELETE CASCADE,
    FOREIGN KEY (doctor_name) REFERENCES doctors(name) ON DELETE CASCADE
);

-- Table for storing billing information
CREATE TABLE IF NOT EXISTS bills (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_name VARCHAR(100) NOT NULL,
    appointment_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_status ENUM('Paid', 'Unpaid') DEFAULT 'Unpaid',
    date DATE NOT NULL,
    FOREIGN KEY (patient_name) REFERENCES patients(name) ON DELETE CASCADE,
    FOREIGN KEY (appointment_id) REFERENCES appointments(id) ON DELETE CASCADE
);

-- Sample Data Insertion

-- Insert initial users
INSERT INTO users (username, password, role) VALUES
('admin', 'admin_password', 'Admin'),
('doctor1', 'doctor_password', 'Doctor'),
('pharmacist1', 'pharmacist_password', 'Pharmacist');

-- Insert sample doctors
INSERT INTO doctors (name, specialization, phone, email) VALUES
('Dr. John Smith', 'Cardiologist', '1234567890', 'john.smith@hospital.com'),
('Dr. Jane Doe', 'Dermatologist', '0987654321', 'jane.doe@hospital.com');

-- Insert sample patients
INSERT INTO patients (name, date_of_birth, gender, phone, email) VALUES
('Alice Brown', '1990-01-01', 'Female', '5551112222', 'alice.brown@gmail.com'),
('Bob White', '1985-05-12', 'Male', '5553334444', 'bob.white@gmail.com');

-- Insert sample appointments (using names for easier search and update)
INSERT INTO appointments (patient_name, doctor_name, date, time) VALUES
('Alice Brown', 'Dr. John Smith', '2024-11-15', '10:30:00'),  -- Alice with Dr. John Smith
('Bob White', 'Dr. Jane Doe', '2024-11-15', '11:00:00');  -- Bob with Dr. Jane Doe

-- Insert sample bills (using names for easier search and update)
INSERT INTO bills (patient_name, appointment_id, amount, payment_status, date) VALUES
('Alice Brown', 1, 150.00, 'Paid', '2024-11-15'),  -- Alice's bill for appointment 1
('Bob White', 2, 200.00, 'Unpaid', '2024-11-15'); -- Bob's bill for appointment 2