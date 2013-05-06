import os, re
from os.path import join

cwd = os.getcwd()

for f in os.listdir(cwd):
    if not f.endswith(".png"):
        continue
    if not "vmc" in f and not "dmc" in f:
        continue

    F = join(cwd, f)
    
    g = f.strip("_0.png")
    g = re.sub("\wmc_edge\d+\.?\d+", "", g)
    g = g.replace(".", "") + ".png"
    g = g.replace("radial_out_", "")
    g = re.sub("(\d+)c(\d+)\.png", "_\g<1>", g) + ".png"
    newF = join(cwd, g)
    
    print g
    os.rename(F, newF)
