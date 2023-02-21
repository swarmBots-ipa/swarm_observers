#!/usr/bin/env python3
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


class MileageObserverPlotter:
    
    def mileage_path_graph(path_travelled,actual_path_length):
        for i in range(len(path_travelled)):
            def trunc(values, decs =0):
                return np.trunc(values*10**decs)/(10**decs)
            path_travelled = np.array(path_travelled)
            path_travelled =trunc(path_travelled,decs=2)
            actual_path_length = np.array(actual_path_length)
            actual_path_length = trunc(actual_path_length,decs=2)
            iteration = []
            std =[]
           
            for j in range(len(actual_path_length[i])):
                iteration.append(str(j+1))
                std.append(0.1)
                
            path_travelled_data, mileage_std = path_travelled[i], std
            actual_path_length_data, path_dist_std = actual_path_length[i], std

            ind = np.arange(len(path_travelled_data))  # the x locations for the groups
            width = 0.30  # the width of the bars
            matplotlib.rc('xtick', labelsize =13)
            matplotlib.rc('ytick', labelsize =13)
            matplotlib.rc('axes', labelsize =13)
            matplotlib.rc('figure', titlesize =20)
            fig, ax = plt.subplots(figsize = (12,10))
            rects1 = ax.bar(ind - width/2, path_travelled_data, width, yerr=mileage_std,label='Path Travelled ')
            rects2 = ax.bar(ind + width/2, actual_path_length_data, width, yerr=path_dist_std,label='Actual Path Length')

            # Add some text for labels, title and custom x-axis tick labels, etc.
            ax.set_ylabel('Distance in meters')
            ax.set_xlabel('Iteration count')
            ax.set_title('Path Travelled vs Actual Path Length - Barista : ' + str(i))
            ax.set_xticks(ind)
            

            ax.set_xticklabels(iteration)
            #plt.xticks(rotation = 45,ha = 'right')
            ax.legend()
            

            def autolabel(rects, xpos='center'):
                ha = {'center': 'center', 'right': 'left', 'left': 'right'}
                offset = {'center': 0, 'right': 1, 'left': -1}

                for rect in rects:
                    height = rect.get_height()
                    ax.annotate('{}'.format(height),
                                xy=(rect.get_x() + rect.get_width() / 2, height),
                                xytext=(offset[xpos]*3, 3),  # use 3 points offset
                                textcoords="offset points",  # in both directions
                                ha=ha[xpos], va='bottom')


            autolabel(rects1, "left")
            autolabel(rects2, "right")

            fig.tight_layout()
            plt.savefig('../data/graphs/barista_'+str(i)+'.png')
        
        plt.show()   
    
    
