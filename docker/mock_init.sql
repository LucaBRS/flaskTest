-- Create the gas_prices table
CREATE TABLE IF NOT EXISTS gas_prices (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    lat FLOAT NOT NULL,
    lng FLOAT NOT NULL,
    gas FLOAT NOT NULL,
    diesel FLOAT NOT NULL
);

-- Create the gas_prices table
CREATE TABLE IF NOT EXISTS gas_p (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    lat FLOAT NOT NULL,
    lng FLOAT NOT NULL,
    gas FLOAT NOT NULL,
    diesel FLOAT NOT NULL
);






INSERT INTO gas_prices (name, lat, lng, gas, diesel) VALUES
    ('Gas Station 1', 37.1234, -122.4567, 3.5, 3.0);

INSERT INTO gas_prices (name, lat, lng, gas, diesel) VALUES
    ('Gas Station 2', 37.2345, -122.5678, 3.6, 3.1);

INSERT INTO gas_prices (name, lat, lng, gas, diesel) VALUES
    ('Gas Station 3', 37.3456, -122.6789, 3.7, 3.2);

INSERT INTO gas_prices (name, lat, lng, gas, diesel) VALUES
    ('Gas Station 4', 37.4567, -122.7890, 3.8, 3.3);

INSERT INTO gas_prices (name, lat, lng, gas, diesel) VALUES
    ('Gas Station 5', 37.5678, -122.8901, 3.9, 3.4);

INSERT INTO gas_prices (name, lat, lng, gas, diesel) VALUES
    ('Gas Station 6', 37.6789, -122.9012, 4.0, 3.5);



-- INSERT INTO gas_prices (name, lat, lng, gas, diesel) VALUES
--     ('Gas Station 1', 37.1234, -122.4567, 3.5, 3.0),
--     ('Gas Station 2', 37.2345, -122.5678, 3.6, 3.1),
--     ('Gas Station 3', 37.3456, -122.6789, 3.7, 3.2),
--     ('Gas Station 4', 37.4567, -122.7890, 3.8, 3.3),
--     ('Gas Station 5', 37.5678, -122.8901, 3.9, 3.4),
--     ('Gas Station 6', 37.6789, -122.9012, 4.0, 3.5),
--     ('Gas Station 7', 37.7890, -122.0123, 4.1, 3.6),
--     ('Gas Station 8', 37.8901, -122.1234, 4.2, 3.7),
--     ('Gas Station 9', 37.9012, -122.2345, 4.3, 3.8),
--     ('Gas Station 10', 38.0123, -122.3456, 4.4, 3.9),
--     ('Gas Station 11', 38.1234, -122.4567, 4.5, 4.0),
--     ('Gas Station 12', 38.2345, -122.5678, 4.6, 4.1),
--     ('Gas Station 13', 38.3456, -122.6789, 4.7, 4.2),
--     ('Gas Station 14', 38.4567, -122.7890, 4.8, 4.3),
--     ('Gas Station 15', 38.5678, -122.8901, 4.9, 4.4),
--     ('Gas Station 16', 38.6789, -122.9012, 5.0, 4.5),
--     ('Gas Station 17', 38.7890, -122.0123, 5.1, 4.6),
--     ('Gas Station 18', 38.8901, -122.1234, 5.2, 4.7),
--     ('Gas Station 19', 38.9012, -122.2345, 5.3, 4.8),
--     ('Gas Station 20', 39.0123, -122.3456, 5.4, 4.9),
--     ('Gas Station 21', 39.1234, -122.4567, 5.5, 5.0),
--     ('Gas Station 22', 39.2345, -122.5678, 5.6, 5.1),
--     ('Gas Station 23', 39.3456, -122.6789, 5.7, 5.2),
--     ('Gas Station 24', 39.4567, -122.7890, 5.8, 5.3),
--     ('Gas Station 25', 39.5678, -122.8901, 5.9, 5.4),
--     ('Gas Station 26', 39.6789, -122.9012, 6.0, 5.5),
--     ('Gas Station 27', 39.7890, -122.0123, 6.1, 5.6),
--     ('Gas Station 28', 39.8901, -122.1234, 6.2, 5.7),
--     ('Gas Station 29', 39.9012, -122.2345, 6.3, 5.8),
--     ('Gas Station 30', 40.0123, -122.3456, 6.4, 5.9),
--     ('Gas Station 31', 40.1234, -122.4567, 6.5, 6.0),
--     ('Gas Station 32', 40.2345, -122.5678, 6.6, 6.1),
--     ('Gas Station 33', 40.3456, -122.6789, 6.7, 6.2),
--     ('Gas Station 34', 40.4567, -122.7890, 6.8, 6.3),
--     ('Gas Station 35', 40.5678, -122.8901, 6.9, 6.4),
--     ('Gas Station 36', 40.6789, -122.9012, 7.0, 6.5),
--     ('Gas Station 37', 40.7890, -122.0123, 7.1, 6.6),
--     ('Gas Station 38', 40.8901, -122.1234, 7.2, 6.7),
--     ('Gas Station 39', 40.9012, -122.2345, 7.3, 6.8),
--     ('Gas Station 40', 41.0123, -122.3456, 7.4, 6.9),
--     ('Gas Station 41', 41.1234, -122.4567, 7.5, 7.0),
--     ('Gas Station 42', 41.2345, -122.5678, 7.6, 7.1),
--     ('Gas Station 43', 41.3456, -122.6789, 7.7, 7.2),
--     ('Gas Station 44', 41.4567, -122.7890, 7.8, 7.3),
--     ('Gas Station 45', 41.5678, -122.8901, 7.9, 7.4),
--     ('Gas Station 46', 41.6789, -122.9012, 8.0, 7.5),
--     ('Gas Station 47', 41.7890, -122.0123, 8.1, 7.6),
--     ('Gas Station 48', 41.8901, -122.1234, 8.2, 7.7),
--     ('Gas Station 49', 41.9012, -122.2345, 8.3, 7.8),
--     ('Gas Station 50', 42.0123, -122.3456, 8.4, 7.9);
