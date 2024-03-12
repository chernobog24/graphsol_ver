import numpy as np

dataset_name = '1amc'
datapath = 'data/'
coordfile = datapath + dataset_name +'_extractedmin'
numStructures = 11451
numBeads=54
numAminos=28
coords = np.zeros((numStructures, numBeads, 3))

with open(coordfile, 'r') as c:
    coordslines = c.readlines()
    
    for i in range(numStructures):
        for j in range(numBeads):
            coords[i][j] = [float(x) for x in coordslines[i*numBeads+j].split()]

print(coords[0][0][0])