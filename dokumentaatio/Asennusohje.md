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

Luo Heroku cli komennolla `heroku create sovelluksennimi`

Asenna Gunicorn-palvelin `pip install gunicorn` ja luo Procfile-tiedosto `echo "web: gunicorn --preload --workers 1 application:app" > Procfile`

Asenna ajuri psycopg2: `pip install psycopg2`

Luo sovellukseen ympäristömuuttuja HEROKU: `heroku config:set HEROKU=1`

Lisää Herokuun PostgreSQL tietokanta: `heroku addons:add heroku-postgresql:hobby-dev`

Lataa sovellus herokuun komennolla `git push heroku master`

