-- Create Index
-- For name and Score
CREATE INDEX idx_name_first_score ON names (name(1), score);
