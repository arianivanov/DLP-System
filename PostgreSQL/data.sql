CREATE TABLE data (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    confidentiality_label VARCHAR(50) NOT NULL
);