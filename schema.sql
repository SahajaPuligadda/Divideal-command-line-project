DROP TABLE IF EXISTS participants;

CREATE TABLE participants (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	pot_id INTEGER NOT NULL,
	participant_name VARCHAR NOT NULL,
	paid INTEGER NOT NULL,
	consumed INTEGER NOT NULL,
	net INTEGER NOT NULL,
	FOREIGN KEY (pot_id) REFERENCES pots (p_id)
);
