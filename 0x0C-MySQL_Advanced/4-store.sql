-- Storing in SQL
-- Creating a trigger warning
CREATE TRIGGER quant AFTER INSERT ON orders FOR EACH ROW UPDATE items SET quantity = quantity - NEW.number WHERE name LIKE NEW.item_name;
