-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and
-- store the average weighted score for all students.
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE user_id_var INT;
    DECLARE total_weighted_score DECIMAL(10, 2);
    DECLARE total_weight DECIMAL(10, 2);
    DECLARE average_weighted_score DECIMAL(10, 2);

    DECLARE done INT DEFAULT FALSE;
    DECLARE cur CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN cur;

    user_loop: LOOP
        FETCH cur INTO user_id_var;
        IF done THEN
            LEAVE user_loop;
        END IF;

        -- Calculate total weighted score and total weight for the user
        SELECT SUM(score * weight), SUM(weight)
        INTO total_weighted_score, total_weight
        FROM scores
        WHERE user_id = user_id_var;

        -- Calculate average weighted score
        IF total_weight > 0 THEN
            SET average_weighted_score = total_weighted_score / total_weight;
        ELSE
            SET average_weighted_score = 0;
        END IF;

        -- Store the result in a table or do whatever you want with it
        -- For example, inserting into another table
        INSERT INTO average_weighted_scores (user_id, average_score)
        VALUES (user_id_var, average_weighted_score);
    END LOOP;

    CLOSE cur;
END //

DELIMITER ;
