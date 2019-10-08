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
- Käyttäjänä pystyn muokkaamaan lisäämiäni reseptejä.
Esimerkkinä tilaisuuden päivitys:
```
UPDATE Recipe SET event='Juhla' WHERE id=1;
```
- Käyttäjänä pystyn poistamaan lisäämäni reseptin
```
DELETE FROM Recipe WHERE id=1;
```
- Käytäjänä pystyn kommentoimaan muiden lisäämiä reseptejä ja muokkaamaan kommenttejani
- Käyttäjänä pystyn poistamaan oman kommentin

- Ylläpitäjänä pystyn muokkaamaan ja poistamaan kaikkien käyttäjien reseptejä 
- Ylläpitäjänä pystyn poistamaan käyttäjien kommentteja, jos ne esimerkiksi ovat loukkaavia
- Ylläpitäjänä pystyn hallitsemaan jäsenten tietoja
