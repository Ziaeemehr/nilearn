import nilearn
import numpy as np
import pylab as plt
import scipy.io as sio
from nilearn import plotting

# load connectome hagmann 2008 data ---------------------------------
mat_cont = sio.loadmat("matfile/hagmann_998.mat")
C = mat_cont['CIJ_fbden_average']
L = mat_cont['CIJ_edgelength_average']
xyz = mat_cont['talairach']

# get atlas data ----------------------------------------------------
destrieux = nilearn.datasets.fetch_atlas_destrieux_2009()
coordinates, int_labels = plotting.find_parcellation_cut_coords(
    destrieux['maps'],
    return_label_names=True)

print(coordinates.shape) # (148, 3)
print(len(int_labels))   # 143
np.savetxt("data/destrieux_2009_coordinates.txt", coordinates, fmt="%18.9f")

# extracting labels of each resion ----------------------------------
labels_int_string = [[destrieux.labels[i][0],
                      destrieux.labels[i][1].decode('UTF-8')]
                     for i in range(1, len(destrieux.labels))]

ofile = open("data/destrieux_2009_labels.txt", "w")
int_labels_dest = [destrieux.labels[j][0]
                   for j in range(len(destrieux.labels))]
my_list = []
for i in int_labels:
    if i in int_labels_dest:
        ofile.write("{:3d} {:s} \n".format(
            i, destrieux.labels[i][1].decode('UTF-8')))
ofile.close()

