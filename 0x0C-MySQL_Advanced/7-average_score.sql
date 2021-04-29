-- Get Average score
-- For users
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
SET @num2 = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id);
UPDATE users SET average_score = (@num2) WHERE id = user_id;
END $$
DELIMITER ;
