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
- **Figures cited on the page:** IOM, *World Migration Report 2026*; UNHCR, *Global Trends* (June 2026); World Bank remittance estimates (2024); SlaveVoyages trans-Atlantic estimates; A. McKeown, "Global Migration, 1846–1940", *Journal of World History* (2004).

## Caveats

- Reconstructions older than about 200 million years are less certain, because the seafloor that recorded plate motions has been destroyed.
- After 2 million years ago the map uses today's coastlines; ice-age sea levels and land bridges are not drawn.
- Prehistoric routes are generalized paths, and several dates (first arrivals in Australia and the Americas) are debated.

## Rebuilding the data

The scripts in `scripts/` regenerate each file in `data/` from the original downloads; each script lists what to download at the top.

## Licence

The code in this repository is released under the GNU General Public License v3.0 (see `LICENSE`), matching the historical-basemaps data it includes. The PaleoDEM and UN data keep their own Creative Commons licences listed above, and their credits must be kept with any reuse.
