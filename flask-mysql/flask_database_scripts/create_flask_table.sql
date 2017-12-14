CREATE TABLE flask_model (
  db_index INT NOT NULL PRIMARY KEY,
  stock_ticker VARCHAR(32),
  stock_description VARCHAR(128),
  current_holding DECIMAL(10, 3),
  current_stock_price DECIMAL(10, 2),
  entry_stock_price DECIMAL(10, 2)
);