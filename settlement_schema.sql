DROP TABLE IF EXISTS settlement;

CREATE TABLE settlement (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	pot_id INTEGER NOT NULL,
	payee_name VARCHAR NOT NULL,
	amount INTEGER NOT NULL,
	receiver_name VARCHAR NOT NULL,
	FOREIGN KEY (pot_id) REFERENCES pots (p_id)
	
);