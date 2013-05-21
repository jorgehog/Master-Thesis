import os, re

cwd = os.getcwd()

map = range(12)
map[0] = "V6"
map[1] = "E2"
map[2] = "V2"
map[3] = "E6"
map[4] = "V30"
map[5] = "E42"
map[6] = "V20"
map[7] = "E30"
map[8] = "V42"
map[9] = "E20"
map[10] = "E12"
map[11] = "V12"
 
for f in os.listdir(cwd):
    if "E_vs_w" not in f:
        continue

    id = re.findall("E_vs_w_(\d+)\.png", f)[0]

    newF = f.replace(id, map[int(id)])

    os.rename(os.path.join(cwd, f), os.path.join(cwd, newF))
