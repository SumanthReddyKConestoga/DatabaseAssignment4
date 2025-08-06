USE subscriber_db;
CREATE TABLE subscriber (
  id INT AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255) NOT NULL,
  subscribed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
ALTER TABLE subscriber ADD INDEX idx_email (email);
