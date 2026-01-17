CREATE DATABASE JobScamDB;
GO
USE JobScamDB;

CREATE TABLE JobChecks (
    id INT IDENTITY PRIMARY KEY,
    job_text TEXT,
    trust_score INT,
    result VARCHAR(20),
    checked_at DATETIME DEFAULT GETDATE()
);
