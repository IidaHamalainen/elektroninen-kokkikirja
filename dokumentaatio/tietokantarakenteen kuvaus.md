## Tietokannan CREATE TABLE -lauseet:

```
CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	user_role VARCHAR(15) NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE ingredient (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE recipe (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	difficult VARCHAR(144) NOT NULL, 
	event VARCHAR(144) NOT NULL, 
	text VARCHAR(1000) NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
);

CREATE TABLE recipeingredient (
	ingredient_id INTEGER, 
	recipe_id INTEGER, 
	FOREIGN KEY(ingredient_id) REFERENCES ingredient (id), 
	FOREIGN KEY(recipe_id) REFERENCES recipe (id)
);

CREATE TABLE comment (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	comment_text VARCHAR(250) NOT NULL, 
	account_id INTEGER NOT NULL, 
	recipe_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(recipe_id) REFERENCES recipe (id)
);
```
