# Elektroninen kokkikirja

Aiheeni on jälkiruokaohjeita sisältävä sovellus, josta käytäjä voi hakea ohjeita eri perusteilla 
(raaka-aine, vaikeus, tilaisuus). Kirjautunut käyttäjä pääsee lisäämään tietokantaan reseptejä sekä 
kirjoittamaan kommentteja ruokaohjeisiin. Käyttäjä pystyy muokaamaan ja poistamaan omia reseptejä ja kommentteja, minkä lisäksi ylläpitäjä pystyy muokkaamaan ja poistamaan reseptejä ja poistamaan kommentteja. Ylläpitäjä myös hallinnoi käyttäjiä. 

Toiminnot:
- kirjautuminen
- ruokaohjeen lisääminen
- ohjeiden näyttäminen eri hakuperusteilla
- kommentin lisääminen ohjeeseen
- ohjeiden poistaminen

[Tietokantakaavio](https://github.com/IidaHamalainen/elektroninen-kokkikirja/blob/master/dokumentaatio/kuvat/tietokantakaavio.png)

[Käyttötapaukset](https://github.com/IidaHamalainen/elektroninen-kokkikirja/blob/master/dokumentaatio/K%C3%A4ytt%C3%B6tapaukset.md)

**Sovellus Herokussa**

[elektroninen-kokkikirja](https://elektroninen-kokkikirja.herokuapp.com/)

#### Käyttäjätunnukset
19.9. Tällä hetkellä kaikki voivat hakea ohjeita ja katsoa yksittäisen ohjeen tietoja. Kirjautunut käyttäjä voi lisätä ohjeen, sekä muokata tai poistaa ohjeita. Toistaiseksi kaikilla käyttäjillä on nämä samat oikeudet, eli ei ole vielä ylläpitäjä-käyttäjää. Sovelluksessa pystyy luomaan uuden käyttäjän.

Tietokantaan tallennettuja käyttäjiä:
- xavier, käyttäjätunnus xyz, salasana abcd
- Tessa Testi, käyttäjätunnus tessa, salasana tessa

Herokussa täytyy ensimmäiseksi luoda käyttäjä, sillä sinne ei vielä ole lisätty tietokantaa vaan sessio alkaa tyhjästä. Tämä tarkoittaa myös että reseptejä ei ole valmiina, vaan niiden lisäystäkin pääsee kokeilemaan ennen kuin hakee ohjeita.


