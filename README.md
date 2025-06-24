# **STVARČICA**

Izradila sam web aplikaciju za upravljanje zalihama proizvoda, koja omogućuje korisnicima unos, pregled, ažuriranje i brisanje proizvoda. Aplikacija je jednostavna za korištenje i idealna za poslovna okruženja poput malih trgovina, ugostiteljskih objekata, skladišta ili ureda koji žele imati kontrolu nad količinom i vrstom proizvoda koje posjeduju.

Korisnik u aplikaciji može:

 * unijeti novi proizvod s osnovnim podacima (naziv, količina, cijena, kategorija)

* ažurirati postojeće proizvode ako se npr. promijeni cijena ili broj komada

* obrisati proizvod koji više nije u uporabi

* jasno i pregledno vidjeti popis svih proizvoda

Jedna od korisnih dodatnih funkcionalnosti je grafikon koji prikazuje broj proizvoda po kategorijama, što omogućava brzu vizualnu analizu zaliha i donošenje boljih poslovnih odluka.

## Pokretanje aplikacije
Aplikacija se pokreće kroz Docker, što znači da nije potrebno ručno instalirati ovisnosti, a sve se pokreće jednim naredbama:
- docker build -t zalihe_app .
- docker run -p 5000:5000 zalihe_app


## Usecase dijagram:
![image](https://github.com/user-attachments/assets/3c2f5f2d-45ef-4ee0-992c-58962062cfbe)
