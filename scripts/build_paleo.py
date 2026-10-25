"""PALEOMAP PaleoDEMs (Scotese & Wright 2018, CC BY 4.0) -> data/paleo.js
Download Scotese_Wright_2018_Maps_1-88_1degX1deg_PaleoDEMS_nc.zip from https://zenodo.org/records/5460860
and unzip it next to this script. pip install netCDF4 numpy
Each frame is classified into 6 elevation bands and run-length encoded (count, value byte pairs, base64)."""
import netCDF4, glob, re, numpy as np, base64, json
TH = [-200, 0, 600, 1800, 3200]
frames = {}
for f in glob.glob('Scotese_Wright_2018_Maps_1-88_1degX1deg_PaleoDEMS_nc_v2/*.nc'):
    age = float(re.search(r'_([\d.]+)Ma\.nc$', f).group(1))
    if age <= 540: frames[age] = f
out = {'w': 360, 'h': 181, 'th': TH, 'frames': []}
for a in sorted(frames):
    d = netCDF4.Dataset(frames[a]); z = np.array(d.variables['z'][:])
    if d.variables['lat'][0] < d.variables['lat'][-1]: z = z[::-1]
    c = np.digitize(z[:, :360], TH).astype(np.uint8).ravel()
    rle = bytearray(); i = 0
    while i < len(c):
        j = i
        while j < len(c) and c[j] == c[i] and j - i < 255: j += 1
        rle += bytes([j - i, c[i]]); i = j
    out['frames'].append([a, base64.b64encode(bytes(rle)).decode()])
open('data/paleo.js', 'w').write('window.PALEO=' + json.dumps(out, separators=(',', ':')) + ';\n')
