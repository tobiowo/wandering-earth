#!/usr/bin/env bash
# Historical borders (A. Ourednik, historical-basemaps, GPL-3.0) -> data/borders.js
# git clone --depth 1 https://github.com/aourednik/historical-basemaps.git ; npm i -g mapshaper
set -e
mkdir -p tmp_borders
for f in bc3000 bc2000 bc1500 bc1000 bc700 bc500 bc323 bc200 bc1 200 400 600 800 1000 1200 1279 1400 1492 1530 1600 1700 1783 1815 1880 1914 1920 1938 1945 1960 1994 2010; do
  mapshaper -i historical-basemaps/geojson/world_$f.geojson -filter-fields NAME,SUBJECTO,BORDERPRECISION \
    -simplify 6% keep-shapes -filter-slivers min-area=2000km2 -o tmp_borders/$f.json format=topojson quantization=8000
done
node -e "const fs=require('fs');const o={};for(const f of fs.readdirSync('tmp_borders')){const k=f.replace('.json','');o[k.startsWith('bc')?-parseInt(k.slice(2)):parseInt(k)]=JSON.parse(fs.readFileSync('tmp_borders/'+f));}fs.writeFileSync('data/borders.js','window.BORDERS='+JSON.stringify(o)+';\n');"
