# Elektroninen kokkikirja

Aiheeni on jälkiruokaohjeita sisältävä sovellus, josta käytäjä voi hakea ohjeita eri perusteilla 
(raaka-aine, vaikeus, tilaisuus). Kirjautunut käyttäjä pääsee lisäämään tietokantaan reseptejä sekä 
kirjoittamaan kommentteja ruokaohjeisiin. Käyttäjä pystyy muokaamaan ja poistamaan omia reseptejä ja kommentteja, minkä lisäksi ylläpitäjä pystyy muokkaamaan ja poistamaan reseptejä ja poistamaan kommentteja. Ylläpitäjä myös hallinnoi käyttäjiä. 

Toiminnot:
- kirjautuminen ja uuden käyttäjätunnuksen luominen
- ruokaohjeen lisääminen, muokkaaminen ja poistaminen
- ohjeiden hakeminen
- kommentin lisääminen ohjeeseen


[Tietokantakaavio](https://github.com/IidaHamalainen/elektroninen-kokkikirja/blob/master/dokumentaatio/kuvat/tietokantakaavio.png)

[Käyttötapaukset](https://github.com/IidaHamalainen/elektroninen-kokkikirja/blob/master/dokumentaatio/K%C3%A4ytt%C3%B6tapaukset.md)

**Sovellus Herokussa**

[elektroninen-kokkikirja](https://elektroninen-kokkikirja.herokuapp.com/)

#### Käyttäjätunnukset
Tällä hetkellä kaikki voivat hakea ohjeita ja katsoa yksittäisen ohjeen tietoja. Kirjautunut käyttäjä voi lisätä ohjeen, sekä muokata tai poistaa itse lisäämiään ohjeita. Käyttäjä voi myös lisätä kommentin omaan tai muiden lisäämään ohjeeseen. Toistaiseksi kaikilla käyttäjillä on nämä samat oikeudet, eli ei ole vielä ylläpitäjä-käyttäjää. Sovelluksessa pystyy luomaan uuden käyttäjän Luo uusi tunnus- napin kautta.

Herokun tietokantaan tallennettuja käyttäjiä:

- Tessa Testi, käyttäjätunnus tessa, salasana testi
- Anna, käyttäjätunnus ansku, salasana abcd
- Matti, käyttäjätunnus sieni, salasana salainen

##### Huomioita/ korjattavia:
- Herokussa ohjetta haettaessa alkukirjaimen koko merkitsee, Pulla ei siis löydyhakusanalla pulla, vaikka paikallisessa versiossa tämä toimii.

