# Asennusohje

Sovelluksen paikalliseen käyttöön tarvitaan python3 ja sqlite3.

Lataa sovelluksen ZIP-tiedosto [etusivulta](https://github.com/IidaHamalainen/elektroninen-kokkikirja)
ja pura se haluamaasi hakemistoon. Terminaalin kautta mene juurihakemistoon ja luo virtuaaliympäristö komennolla `python -m venv venv`

Käynnistä viruaaliympäristö komennolla `source venv/bin/activate`

Tarvittaessa asenna Flask ja asenna sovelluksen riippuvuudet:
```
pip install Flask
pip install -r requirements.txt
```
Käynnistä sovellus komennolla `python run.py`
Sovellus käynnistyy nyt osoitteeseen http://localhost:5000/

### Heroku
Luo sovellukseen ympäristömuuttuja HEROKU: `heroku config:set HEROKU=1`
