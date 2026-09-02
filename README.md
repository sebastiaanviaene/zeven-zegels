# Zeven Zegels

Een interactieve geheime kaart voor Lisa's 31e verjaardag. Verrassingsweekend in de Duitse
Vulkaneifel, 11 tot 13 september 2026.

De kaart toont zeven plekken. Elke plek zit op slot en gaat open met een code die jij op het
juiste moment doorgeeft. Wat open is, blijft open, ook als ze de tab sluit.

> Deze repo is privé. Hij bevat de codes en de volledige planning, dus hou dat zo.

## De codes

| # | Plek | Wanneer je hem geeft | Code |
|---|------|----------------------|------|
| 1 | de auto | vrijdag, zodra jullie vertrekken | `MAAR` |
| 2 | de tent | vrijdagavond, bij aankomst op de tentplek | `OBSTBAUM` |
| 3 | de start | zaterdag 08:30, aan het Kurhaus | `LIESER` |
| 4 | halfweg | zaterdag, rond kilometer 10 | `URPFERD` |
| 5 | het huis | zaterdag 16:00, bij het inchecken | `WEITBLICK` |
| 6 | eten | zaterdag 19:00, aan tafel | `VULCANO` |
| 7 | de meren | zondagochtend | `DRONKE` |

Hoofdletters maken niet uit, spaties eromheen ook niet.

## De aftelklok

De hele kaart zit achter een aftelklok tot **vrijdag 11 september 2026, 00:00** lokale tijd.
Daarvoor ziet ze alleen de klok en de boodschap dat de kaart pas vrijdag opengaat.

**Adminkoode: `KOMPAS`** — opent de poort meteen, ook nu. Bedoeld om te testen.

Die keuze wordt in de browser onthouden. Druk na het testen op **alles opnieuw sluiten**
onderaan de pagina: dat wist zowel de poort als alle geopende zegels, en zet alles terug
naar de begintoestand.

Wil je een andere datum? Pas `OPENS_AT` aan in `index.html`. Let op dat de maand
nul-geïndexeerd is: `new Date(2026, 8, 11)` is 11 september 2026.

## Het weekend

| | |
|---|---|
| **Vrijdag 11/9** | Aarschot naar Bengel, ~2u30. Trekkingplatz "Unter den Obstbäumen" bij de oude Öl- und Kornmühle Springiersbach, €15, inchecken vanaf 14:00. Wandelen: Rundweg Nr. 1 (Rot), 6,1 km, vanaf de kloosterparking op ~1,5 km van de tent. |
| **Zaterdag 12/9** | 07:30 opbreken. 08:30 start aan het Kurhaus, Grafenstraße 23, Manderscheid. Grafschaft-Pfad plus Manderscheider Burgenstieg, samen ~20 km en ~580 hm. 16:00 inchecken op Kyllblick 12. 19:00 Trattoria Vulcano, Grafenstraße 18. |
| **Zondag 13/9** | Uitchecken tussen 10:00 en 10:30. Dan de Dauner Maare (8,6 km) of de Vulkaneifel-Therme in Bad Bertrich. Daarna ~2u45 naar huis. |

### Vrijdag, de opties

- **Prinzenkopfturm** bij Pünderich: uitkijktoren over de Zeller Hamm, de langste meander van de
  Moezel. Gratis en dag en nacht toegankelijk, 700 m en ~10 min omhoog vanaf de parking onder de
  Marienburg. 4,9/5 uit 1.551 beoordelingen op komoot. Rijden vanaf Bengel: geschat 20-25 min.
- **Bullayer Herbstfest**, do 10 t/m ma 14 september, aan de voet van de Prinzenkopf. Op
  zaterdagavond regelt de brandweer het verkeer vanwege het vuurwerk, dus reken vrijdag en
  zaterdag op drukte en parkeerdruk daar. Ook: Fröhlicher Weinmarkt in Traben-Trarbach, 11-13 sep.
- **Vulkaneifel-Therme Bad Bertrich**, Clara-Viebig-Straße 3-7, +49 2674 913070. **Dagelijks
  09:00-22:00.** Dagticket €16,50, twee uur €12. Kaartverkoop stopt een uur voor sluiting.
  Eventueel met het rondje **Elfengrotte** ervoor: 2,4 km, 45 min, start bij de Tourist Info,
  Kurfürstenstraße 32.
- **Te voet vanaf de tent:** Rundweg Nr. 1 (Rot), 6,1 km, 151 hm, 1u45, rode pijlen, vanaf de
  parking bij Klosterkirche Springiersbach. Let op: die lus heeft nul beoordelingen online, dus
  neem de GPX mee.

### Eten en winkels

| Waar | Wanneer |
|---|---|
| Kaiser Döner 89, Trierer Str. 5, Bengel · 06532 954 60 39 | vrijdag 12:00-21:30 |
| Alte Dorfschänke, Dorfstraße 14, Kinderbeuern · 06532 95480 | vrijdag 12:00-14:00 en 16:00-22:00, **keuken tot 20:00**, reserveren |
| La Terrazza, Lindenplatz 1, Zell · +49 6542 963319 | dagelijks 11:00-23:00 |
| Fachmarkt Becker, Trierer Str. 34, Bengel | ma-vr 06:00-18:30, za-zo 07:00-14:00, met Imbiss |
| Netto, Im Hageflur 8, Bausendorf | vrijdag 07:00-20:00 |
| Alftalbäckerei Gaulke, Hauptstraße 25, Kinderbeuern | **zaterdag 06:00-11:00** — het ontbijt |
| Klosterladen Springiersbach | ma-vr 09:00-11:30 en 14:00-17:00, geen café |

### Aandachtspunten

- **Onderweg op zaterdag is er niets.** Geen kraan, geen café, geen winkel. Twee liter water
  per persoon en de lunch mee.
- **Koken mag op de trekkingplaats.** De pagina van de Ortsgemeinde Bengel noemt zitplaatsen en
  een vuurplaats waarop je "nach Herzenslust" kan koken of grillen, en een wandelverslag bevestigt
  dat een campingbrander er toegestaan was. De algemene FAQ van het netwerk zegt wél "kein offenes
  Feuer", dus de tegenstrijdigheid staat er nog. Navragen: (0160) 2422391.
- **Check de omleiding.** De officiële GPX van de Grafschaft-Pfad heet momenteel
  `umleitung-grafschaft-pfad.gpx`. Actuele status op
  [gesundland-vulkaneifel.de/info/wege-info](https://www.gesundland-vulkaneifel.de/info/wege-info/).
- **VulkanBike Eifel-Marathon** valt op zaterdag 12 september 2026, met zo'n 2000 mountainbikers
  rond Daun. Manderscheid ligt buiten het parcours, maar wandel die dag niet richting Daun.
- **Inchecken in het appartement kan maar tot 21:00** en je moet je aankomstuur doorgeven.
  Uitchecken is een venster van een half uur.

## Technisch

Eén bestand, `index.html`. Geen build, geen dependencies, geen framework. De enige externe
bron is Google Fonts. De voortgang zit in `localStorage`, dus die is per browser en per
apparaat: als ze halverwege van telefoon wisselt, begint ze opnieuw.

De codes staan niet leesbaar in de broncode, ze zijn opgeslagen als hash. Iemand die de
JavaScript openklikt kan ze niet zomaar aflezen, maar het is een spelletje en geen kluis.
