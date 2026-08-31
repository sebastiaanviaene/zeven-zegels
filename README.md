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
| **Vrijdag 11/9** | Aarschot naar Bengel, ~2u30. Trekkingplatz "Unter den Obstbäumen" in het Kondelwald, €15. Coördinaten krijg je bij de bevestiging. |
| **Zaterdag 12/9** | 07:30 opbreken. 08:30 start aan het Kurhaus, Grafenstraße 23, Manderscheid. Grafschaft-Pfad plus Manderscheider Burgenstieg, samen ~20 km en ~580 hm. 16:00 inchecken op Kyllblick 12. 19:00 Trattoria Vulcano, Grafenstraße 18. |
| **Zondag 13/9** | Uitchecken tussen 10:00 en 10:30. Dan de Dauner Maare (8,6 km) of de Vulkaneifel-Therme in Bad Bertrich (€16,50). Daarna ~2u45 naar huis. |

### Aandachtspunten

- **Onderweg op zaterdag is er niets.** Geen kraan, geen café, geen winkel. Twee liter water
  per persoon en de lunch mee.
- **Vuur is verboden** op de trekkingplaats, ook gasbranders. Boetes lopen op tot €25.000.
  Er is een tegenstrijdigheid tussen de plaatsbeschrijving en de netwerkregels: navragen via
  info@moselregion.com.
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
