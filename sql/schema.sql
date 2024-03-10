PRAGMA foreign_keys = ON;

-- students table 
CREATE TABLE students(
  first_name VARCHAR(20) NOT NULL,
  last_name VARCHAR(40) NOT NULL,
  PRIMARY KEY(first_name)
);
