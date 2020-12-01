### Quick references

- [nilearn.datasets: Automatic Dataset Fetching](https://nilearn.github.io/modules/reference.html#module-nilearn.datasets)

- [Connectome extraction: inverse covariance for direct connections](https://nilearn.github.io/connectivity/connectome_extraction.html)

- [Comparing connectomes on different reference atlases](https://nilearn.github.io/auto_examples/03_connectivity/plot_atlas_comparison.html#sphx-glr-auto-examples-03-connectivity-plot-atlas-comparison-py)




multiplying the coordinates of a node by the inverse of the image affine will give you the voxel index and you can read the atlas image at that location to find the label. you can then sum over the voxels in each region to get the number of connections between regions. Note you could also directly use the atlas to define the connectome, thus you would directly have a connectome with one node per atlas region. general comments: we prefer to use github issues for bug reports, and the neurostars forum for usage questions