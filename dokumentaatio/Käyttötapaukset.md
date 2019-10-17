# Tärkeimmät käyttötapaukset

- Käyttäjänä pystyn hakemaan reseptejä raaka-aineen, vaikeuden tai tilaisuuden perusteella

SQL esimerkki, jossa haetaan kaikki maitoa sisältävät reseptit:

```
SELECT ingredient.name, recipe.name FROM Recipe 
  JOIN Recipeingredient ON recipe.id = recipeingredient.recipe_id 
  JOIN Ingredient on recipeingredient.ingredient_id = ingredient.id 
  WHERE ingredient.name='Maito';
```

SQL esimerkki, jossa haetaan helpot reseptit:
```
SELECT * FROM Recipe WHERE difficult = 'Helppo'; 
```

- Käyttäjänä pystyn lisäämään reseptin sovellukseen
```
INSERT INTO Recipe(id, name, difficult, event, text, account_id) 
  VALUES(3,'Torttu','Keskitaso','Arki','torttuohje yms', 1);
```
Aineen lisäys reseptiin:
```
INSERT INTO Recipeingredient(recipe_id, ingredient_id) Values (3, 1);
```
- Käyttäjänä pystyn muokkaamaan lisäämiäni reseptejä. Ylläpitäjänä voin muokata kaikkia reseptejä.
Esimerkkinä tilaisuuden päivitys:
```
UPDATE Recipe SET event='Juhla' WHERE id=1;
```
- Käyttäjänä pystyn poistamaan lisäämäni reseptin / Ylläpitäjänä pystyn poistamaan kaikkien lisäämiä reseptejä
```
DELETE FROM Recipe WHERE id=1;
```
- Käytäjänä pystyn kommentoimaan muiden lisäämiä reseptejä
```
INSERT INTO Comment(id, comment_text, account_id, recipe_id) 
  VALUES(3,'Hyvä ohje!', 2, 1);
```

- Käyttäjänä pystyn poistamaan oman kommentin / Ylläpitäjänä voin poistaa minkä vain kommentin
```
DELETE FROM Comment WHERE id=3;
```
- Käyttäjänä pystyn muokkaamaan kommenttiani
```
UPDATE Comment SET comment_text='muokattu teksti' WHERE id=1;
```
- Ylläpitäjänä voin lisätä raaka-aineen tietokantaan
```
INSERT INTO Ingredient(id, name) 
  VALUES(1, 'Suklaa');
```


- Ylläpitäjänä pystyn hallitsemaan jäsenten tietoja.
Tätä ei ehditty toteuttaa
