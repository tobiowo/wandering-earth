"""UN DESA International Migrant Stock 2024: Destination and origin (CC BY 3.0 IGO) -> data/mig.js
Download undesa_pd_2024_ims_stock_by_sex_destination_and_origin.xlsx from
https://www.un.org/development/desa/pd/content/international-migrant-stock . pip install openpyxl
Values are thousands of people for 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2024."""
import openpyxl, json, re
wb = openpyxl.load_workbook('undesa_pd_2024_ims_stock_by_sex_destination_and_origin.xlsx', read_only=True)
rows = [r for r in wb['Table 1'].iter_rows(min_row=12, values_only=True) if r[0] is not None]
REG = {2,14,17,18,11,15,19,21,5,13,29,142,143,30,34,35,145,150,151,154,155,39,9,53,54,57,61,419,202,830}
names = {}
for r in rows:
    for code, name in ((r[4], r[1]), (r[6], r[5])):
        if code < 900 and code not in REG and name.upper() != name: names[code] = re.sub(r'\*$', '', name)
emi, imm, pairs = {}, {}, []
for r in rows:
    d, o = r[4], r[6]; v = [x if isinstance(x, (int, float)) else 0 for x in r[7:15]]
    k = [round(x / 1000) for x in v]
    if d == 900 and o in names: emi[o] = k
    elif o == 900 and d in names: imm[d] = k
    elif d in names and o in names and max(v) >= 30000: pairs.append([o, d] + k)
open('data/mig.js', 'w').write('window.MIG=' + json.dumps({'names': names, 'emi': emi, 'imm': imm, 'pairs': pairs}, separators=(',', ':'), ensure_ascii=False) + ';\n')
