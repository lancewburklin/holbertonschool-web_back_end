-- Update a column
-- When a column is updated
delimiter $$
CREATE TRIGGER upd
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END$$
delimiter ;
