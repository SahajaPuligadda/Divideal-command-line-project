DROP TABLE IF EXISTS consumer;

CREATE TABLE consumer (
	c_id INTEGER PRIMARY KEY AUTOINCREMENT,
	item_id INTEGER NOT NULL,
	consumer_name VARCHAR NOT NULL,
	amount INTEGER NOT NULL,
	FOREIGN KEY (item_id) REFERENCES items (id)
);
