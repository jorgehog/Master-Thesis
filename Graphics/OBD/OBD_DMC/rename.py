import os, re
from os.path import join

cwd = os.getcwd()

for f in os.listdir(cwd):
    if not f.endswith(".png"):
        continue
    if not "vmc" in f and not "dmc" in f:
        continue

    F = join(cwd, f)
    
    g = f.strip(".png")
    g = re.sub("\wmc_edge\d+\.?\d+", "", g)
    g = g.replace(".", "") + ".png"
    g = g.replace("_0", "_2D")
    g = g.replace("_1", "_3D")
    
    newF = join(cwd, g)
    
    
    os.rename(F, newF)
