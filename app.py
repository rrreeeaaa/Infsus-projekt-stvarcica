
from flask import Flask, request, render_template, redirect
from pony.orm import db_session, select
from models import db, Proizvod
from datetime import datetime
from collections import Counter

app = Flask(__name__)
db.bind(provider='sqlite', filename='zalihe.sqlite', create_db=True)
db.generate_mapping(create_tables=True)

@app.route('/')
@db_session
def index():
    proizvodi = select(p for p in Proizvod)[:]
    kategorije = []
    for p in proizvodi:
        kategorije.append(p.kategorija)
    brojac = Counter(kategorije)
    return render_template('index.html', proizvodi=proizvodi,
                           kategorije=list(brojac.keys()), brojevi=list(brojac.values()))

@app.route('/dodaj', methods=['POST'])
@db_session
def dodaj():
    naziv = request.form['naziv']
    cijena = float(request.form['cijena'])
    kolicina = int(request.form['kolicina'])
    kategorija = request.form['kategorija']
    sada = datetime.now()

    Proizvod(naziv=naziv, cijena=cijena, kolicina=kolicina,
             kategorija=kategorija, datum_dodavanja=sada, datum_azuriranja=sada)
    return redirect('/')

@app.route('/obrisi/<int:proizvod_id>')
@db_session
def obrisi(proizvod_id):
    p = Proizvod.get(id=proizvod_id)
    if p:
        p.delete()
    return redirect('/')

@app.route('/uredi/<int:proizvod_id>', methods=['GET'])
@db_session
def prikazi_formu_za_uredi(proizvod_id):
    proizvod = Proizvod.get(id=proizvod_id)
    if not proizvod:
        return "Proizvod ne postoji", 404
    return render_template('uredi.html', proizvod=proizvod)

@app.route('/uredi/<int:proizvod_id>', methods=['POST'])
@db_session
def spremi_uredi(proizvod_id):
    proizvod = Proizvod.get(id=proizvod_id)
    if not proizvod:
        return "Proizvod ne postoji", 404

    proizvod.naziv = request.form['naziv']
    proizvod.cijena = float(request.form['cijena'])
    proizvod.kolicina = int(request.form['kolicina'])
    proizvod.kategorija = request.form['kategorija']
    proizvod.datum_azuriranja = datetime.now()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
