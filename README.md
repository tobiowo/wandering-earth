# Wandering Earth

An interactive map that runs from the Cambrian, 540 million years ago, to the 304 million international migrants of today. Drag the timeline to watch the continents gather into Pangaea and break apart, follow people out of Africa and across the oceans, see empires and borders change over 5,000 years, and explore where every country's diaspora lives.

**Live site:** https://tobiowo.github.io/wandering-earth/

## What's on the map

| Time | Layer | Source |
|---|---|---|
| 540 – 2 million years ago | Ancient land, shallow seas and mountains, every 5 million years | Scotese & Wright (2018), PALEOMAP PaleoDEMs |
| 2 million years ago – today | Human dispersal and historic migration routes | Dated archaeological and genetic sites; SlaveVoyages; McKeown (2004) |
| 3000 BCE – 2010 | Historical borders (31 snapshots) | Ourednik, historical-basemaps |
| 1990 – 2024 | Diasporas, destinations and every country pair with 30,000+ migrants | UN DESA, International Migrant Stock 2024 |
| Today | Headline figures | IOM World Migration Report 2026, UNHCR, World Bank |

The page is a single static `index.html` with no build step. It loads d3 and topojson-client from public CDNs and its data from `data/`.

## Data sources and licences

- **Ancient geography:** C. R. Scotese and N. M. Wright (2018), *PALEOMAP Paleodigital Elevation Models (PaleoDEMS) for the Phanerozoic*, [Zenodo 5460860](https://zenodo.org/records/5460860). CC BY 4.0. Classified into six elevation bands and run-length encoded in `data/paleo.js`.
- **Migrant stock:** United Nations, Department of Economic and Social Affairs, Population Division (2024), *International Migrant Stock 2024*. [un.org](https://www.un.org/development/desa/pd/content/international-migrant-stock). CC BY 3.0 IGO. Reduced to totals by country and country pairs of 30,000+ in `data/mig.js`.
- **Historical borders:** A. Ourednik and contributors, [historical-basemaps](https://github.com/aourednik/historical-basemaps). GPL-3.0. Simplified with mapshaper in `data/borders.js`. The upstream project is a work in progress and ancient borders are approximate; report border errors upstream.
- **Coastlines:** Natural Earth (public domain) via [world-atlas](https://github.com/topojson/world-atlas).
- **Historic migration streams:** each line after 1500 is drawn as a stream (one migration system) branching to its main destinations. Widths are proportional to the number of people where a source gives a count; dashed branches have no count of their own. Sources:
  - [SlaveVoyages](https://www.slavevoyages.org/assessment/estimates), Trans-Atlantic Slave Trade estimates (embarked and disembarked by region, 1501–1866)
  - A. McKeown, ["Global Migration, 1846–1940"](https://historycooperative.org/journal/global-migration-1846-1940/), *Journal of World History* (2004): European, South Asian, southern Chinese and North Asian streams
  - T. Hatton & J. Williamson, *The Age of Mass Migration: Causes and Economic Impact*, Oxford University Press (1998), chapter 2: return migration, Canada context
  - R. Abramitzky & L. Boustan, ["Immigration in American Economic History"](https://doi.org/10.1257/jel.20151189), *Journal of Economic Literature* (2017): United States, return migration
  - M. Boyd & M. Vickers, ["100 years of immigration in Canada"](https://www150.statcan.gc.ca/n1/pub/11-008-x/2000002/article/5164-fra.pdf), *Canadian Social Trends*, Statistics Canada (2000): Canada (all origins, so the branch stays dashed)
  - B. Sánchez-Alonso, [The age of mass migration in Latin America](https://ehes.org/wp/EHES_134.pdf), EHES working paper 134: Argentina and Brazil
  - UK National Archives, [The age of mass migration](https://www.nationalarchives.gov.uk/explore-the-collection/explore-by-time-period/victorians/age-of-mass-migration/): Australia and New Zealand
  - US National Archives, [The Great Migration](https://www.archives.gov/research/african-americans/migrations/great-migration)
  - Statistisches Bundesamt (1958), via [Demographic estimates of the flight and expulsion of Germans](https://en.wikipedia.org/wiki/Demographic_estimates_of_the_flight_and_expulsion_of_Germans)
  - J. Chatterji, ["Partitioned Lands, Partitioned Histories"](https://www.cambridge.org/core/books/from-the-ashes-of-1947/partitioned-lands-partitioned-histories/5E2B0F0753C59835EB27762D5B407F8E), in *From the Ashes of 1947*: Partition
  - Gaps: no European-only count for Canada, no count for South Africa, and no Punjab/Bengal split for Partition.
- **Modern figures cited on the page:** IOM, *World Migration Report 2026*; UNHCR, *Global Trends* (June 2026); World Bank remittance estimates (2024).

## Caveats

- Reconstructions older than about 200 million years are less certain, because the seafloor that recorded plate motions has been destroyed.
- After 2 million years ago the map uses today's coastlines; ice-age sea levels and land bridges are not drawn.
- Prehistoric routes are generalized paths, and several dates (first arrivals in Australia and the Americas) are debated.

## Rebuilding the data

The scripts in `scripts/` regenerate each file in `data/` from the original downloads; each script lists what to download at the top.

## Licence

The code in this repository is released under the GNU General Public License v3.0 (see `LICENSE`), matching the historical-basemaps data it includes. The PaleoDEM and UN data keep their own Creative Commons licences listed above, and their credits must be kept with any reuse.
