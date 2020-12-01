- CIJ_edgelength_average      998x998       % Average length of each link                          
- CIJ_fbden_average           998x998       % this corresponds to the link' strengths used as W in the paper                         
- CIJ_resampled_average       998x998       % is a resampling of the CIJ_fbden_average one by Olaf 
- COR_fMRI_average            998x998       % the average FUNCTIONAL correlation found between BOLD signals
- roi_lbls                      1x998       % the "names" of each node                          
- roi_xyz_avg                   3x998       % xyz position of each node
- talairach                     998x3       % the Talairich coordinates of each node, e.g.,, to plot the i node you may do:
                                            % xyz=talairach(i,:);
                                            % plot3(xyz(1),xyz(2),xyz(3),'x') 
