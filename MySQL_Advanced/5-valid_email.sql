-- Script defines trigger reset_pwd
-- reset_pwd resets valid_email if
-- email has beem updated
DELIMITER $$

CREATE TRIGGER reset_pwd
BEFORE UPDATE ON users

FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END $$

DELIMITER ;
