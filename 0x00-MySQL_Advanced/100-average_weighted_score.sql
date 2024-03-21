-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student.
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE total_weighted_score DECIMAL(10, 2);
    DECLARE total_weight DECIMAL(10, 2);
    DECLARE average_weighted_score DECIMAL(10, 2);

    -- Calculate total weighted score and total weight for the user
    SELECT SUM(score * weight), SUM(weight)
    INTO total_weighted_score, total_weight
    FROM scores
    WHERE user_id = user_id;

    -- Calculate average weighted score
    IF total_weight > 0 THEN
        SET average_weighted_score = total_weighted_score / total_weight;
    ELSE
        SET average_weighted_score = 0;
    END IF;

    -- Store the result in a table or do whatever you want with it
    -- For example, inserting into another table
    INSERT INTO average_weighted_scores (user_id, average_score)
    VALUES (user_id, average_weighted_score);
END //

DELIMITER ;
