# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjä voi kerrata koulumatematiikkaa. Rekisteröityneen käyttäjän tunnuksessa pidetään kirjaa tehdyistä tehtävistä.

## Käyttäjät

Käyttäjärooleja on kolme, jotka ovat ylläpitäjä, rekisteröitynyt käyttäjä ja käyttäjä.

*Ylläpitäjä*n tunnuksella voi
   - kirjautua sovellukseen antamalla käyttäjätunnuksen ja salasanan
   - kirjauduttuaan sovellukseen nollata valitsemansa rekisteröityneen käyttäjän salasanan.


*Rekisteröitynyt käyttäjä* voi
   - kirjautua sovellukseen antamalla käyttäjätunnuksen ja salasanan
   - kirjauduttuaan sovellukseen valita näytettäväksi haluamansa tehtävänannot, ja vastata näytettäviin tehtävänantoihin


*Rekisteröimätön käyttäjä* voi
   - ohittaa aloitusnäkymän saadakseen sovellukselta näytettäväksi yhden satunnaisesti valitun tehtävänannon, johon ei voi kuitenkaan vastata
   - palata aloitusnäkymään

## Käyttöliittymäluonnos
Aloitusruudussa voidaan kirjautua sovellukseen kirjoittamalla käyttäjätunnus ja salasana. Aloitusruudusta voidaan myös siirtyä uuden käyttäjän luomisen ruutuun, jossa voidaan rekisteröidä uusi käyttäjä kirjoittamalla nimi, käyttäjätunnus ja salasana. Aloitusruutu voidaan ohittaa jonka jälkeen sovellus siirtyy vapaamatkustaja-ruutuun.

Vapaamatkustaja-ruudussa näytetään yksi satunnaisesti valittu tehtävänanto johon käyttäjä ei kuitenkaan voi palauttaa omaa vastausehdotustaan. Vapaamatkustaja-ruudusta voidaan palata takaisin aloitusruutuun. Saman ohjelmasuorituskerran aikana toistamiseen vapaamatkustaja-ruutuun siirryttäessä näytetään vain yhtä ja samaa tehtävänantoa.

Uuden käyttäjän luomisesta siirrytään etusivu-ruutuun, josta voidaan kirjautua ulos, tarkastella tilastoja, ja jatkaa tehtävien ratkaisemista jolloin avautuu ratkaistavan tehtävän ruutu.

Ratkaistavan tehtävän ruudusta voidaan palata takaisin etusivu-ruutuun tehtävää ratkaisematta. Ruudussa voidaan syöttää vastaus tehtävänantoon sovelluksen tarkistettavaksi. Palaute avautuu olemassa olevaan ruutuun. Palautteen saatuaan käyttäjä voi valita esitettäväksi uuden tehtävänannon samasta kategoriasta tai vaihtaa kategoriaa alasvetovalikosta, ja edelleen palata takaisin aloitusruutuun ilman uutta tehtävänantoa.

Ylläpitäjä-tunnuksilla kirjautuneen käyttäjän etusivu-ruutu sisältää vain ylläpitoon tarvittavan toiminnallisuuden. Ylläpitäjä on siis täysin eri rooli kuin käyttäjä.

## Perusversion tarjoama toiminnallisuus


### Ennen kirjautumista
Esimerkkitehtävänannon katsominen. Rekisteröityminen. Ohjelman sulkeminen.

### Kirjautumisen jälkeen
Ylläpitäjän roolissa käyttäjätunnuksen salasanan nollaus joko a) omavalintaiseen tai b) sovelluksen tarjoamaan arvoon.
Käyttäjän roolissa halutun tehtävänannon valitseminen. Oman vastausehdotuksen syöttäminen annettuun tehtävänantoon. Omien tilastojen havainnointi.

### Jatkokehitysideoita
Ylläpitäjälle mahdollisuus lisätä tehtäviä olemassaolevaa runkoa hyväksikäyttäen.
 
Salasanat tietokannassa entistä vahvemmin salattuina esim. hyödyntäen scrypt-kirjastoa.

Viimestellympää ja enemmän teemaan nojaavaa grafiikkaa sis. mm. animaatiot.

Lisää käyttäjien välistä vuorovaikuttamista kuten tulostaulut ja reaktiot.

Käyttäjän roolia/vuorovaikuttamisen osuutta salasanan nollauksessa tulisi kasvattaa.

Ylläpitäjän tunnukseen tulisi sisältyä mahdollisuus toimia käyttäjän roolissa. Ylläpitäjän tunnuksilla kirjauduttua aloitusruudusta tulisi voida siirtyä esimerkiksi salasana syöttämällä ylläpitäjän tarvitsemat toiminnallisuudet sisältämään ruutuun.






