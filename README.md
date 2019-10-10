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

[Tietokannan rakenteen kuvaus](https://github.com/IidaHamalainen/elektroninen-kokkikirja/blob/master/dokumentaatio/tietokantarakenteen%20kuvaus.md)

[Käyttötapaukset](https://github.com/IidaHamalainen/elektroninen-kokkikirja/blob/master/dokumentaatio/K%C3%A4ytt%C3%B6tapaukset.md)

**Sovellus Herokussa**

[elektroninen-kokkikirja](https://elektroninen-kokkikirja.herokuapp.com/)

#### Käyttäjätunnukset
Tällä hetkellä kaikki voivat hakea ohjeita ja katsoa yksittäisen ohjeen tietoja. Kirjautunut käyttäjä voi lisätä ohjeen, sekä muokata tai poistaa itse lisäämiään ohjeita. Käyttäjä voi myös lisätä kommentin omaan tai muiden lisäämään ohjeeseen ja poistaa oman kommenttinsa. Sovelluksessa pystyy luomaan uuden käyttäjän Luo uusi tunnus- napin kautta.

Herokun tietokantaan tallennettuja käyttäjiä:

- Tessa Testi, käyttäjätunnus tessa, salasana testi
- Anna, käyttäjätunnus ansku, salasana abcd
- Matti, käyttäjätunnus sieni, salasana salainen

- Admin, käyttäjätunnus admin, salasana admin. 
Admin voi perustoimintojen lisäksi poistaa ja muokata kaikkien käyttäjien ohjeita ja poistaa kommentteja.

##### Huomioita/ korjattavia:
- Herokussa ohjetta haettaessa alkukirjaimen koko merkitsee, Pulla ei siis löydyhakusanalla pulla, vaikka paikallisessa versiossa tämä toimii.

