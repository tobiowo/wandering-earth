// Merge Natural Earth countries (world-atlas 110m) into land groups -> data/plates.js
// npm i world-atlas topojson-client d3-geo
const topo=require('world-atlas/countries-110m.json'),tc=require('topojson-client'),fs=require('fs');
const all=topo.objects.countries.geometries;
const m=tc.merge(topo,all);
const round=a=>Array.isArray(a[0])?a.map(round):[Math.round(a[0]*10)/10,Math.round(a[1]*10)/10];
fs.writeFileSync('data/plates.js','window.PLATES='+JSON.stringify({LAND:round(m.coordinates)})+';\n');
