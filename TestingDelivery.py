import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple
from TestingInterface import TestInterface
from TestingData import TestingData

class TestingDelivery(TestingData):
   
    def __init__(self):
        TestingData.__init__(self)

    def Split_status(self):
        tCreated=0
        tDelivered=0
        tVolumeCreated=0
        tVolumeDelivered=0
        iCreated=0
        iDelivered=0
        iVolumeCreated=0
        iVolumeDelivered=0
        vCreated=0
        vVolumeCreated=0
        vDelivered=0
        vVolumeDelivered=0
        for lines in TestingData.getPriorityC(self):
            if (len(lines) < 1):
                continue;
            x=lines
            if(x[3][1]=='T'):
                tCreated+=1
                tVolumeCreated+=int(x[len(x)-1])
            if(x[3][1]=='I'):
                iCreated+=1
                iVolumeCreated+=int(x[len(x)-1])
            if(x[3][1]=='V'):
                vCreated+=1
                vVolumeCreated+=int(x[len(x)-1])
        for lines in TestingData.getPriorityDE(self):
            if(len(lines)<1):
                continue
            x=lines
            if (x[3] != 'ADB5'):
                continue
            if (x[1] == 'DE'):
                if(x[4][1]=='T'):
                    tDelivered+=1
                    tVolumeDelivered+=int(x[len(x)-1])
                if(x[4][1]=='I'):
                    iDelivered+=1
                    iVolumeDelivered+=int(x[len(x)-1])
                if(x[4][1]=='V'):
                    vDelivered+=1
                    vVolumeDelivered+=int(x[len(x)-1])
        ratiosVolume=[]            
        ratios=[]
        ratios.append(tDelivered/tCreated)
        ratios.append(iDelivered/iCreated)
        ratios.append(vDelivered/vCreated)
        ratiosVolume.append(tVolumeDelivered/tVolumeCreated)
        ratiosVolume.append(iVolumeDelivered/iVolumeCreated)
        ratiosVolume.append(vVolumeDelivered/vVolumeCreated)
        print("\nPriority\n")
        print("\nTotal packet details\n")
        print(" Type    Created       Delivered      Precenttages            Volume\n")
        print(" Text       "+str(tCreated)+"       "+str(tDelivered)+"         "+str(ratios[0])+"\n")
        print(" Image      "+str(iCreated)+"       "+str(iDelivered)+"         "+str(ratios[1])+"\n")
        print(" Video      "+str(vCreated)+"       "+str(vDelivered)+"         "+str(ratios[2])+"\n")  
        print("\nVolume of Packets \n")
        print(" Type    Created       Delivered      Precenttages\n")
        print(" Text       "+str(tVolumeCreated)+"       "+str(tVolumeDelivered)+"         "+str(ratiosVolume[0])+"\n")
        print(" Image      "+str(iVolumeCreated)+"       "+str(iVolumeDelivered)+"         "+str(ratiosVolume[1])+"\n")
        print(" Video      "+str(vVolumeCreated)+"       "+str(vVolumeDelivered)+"         "+str(ratiosVolume[2])+"\n")  
        

        tCreated=0
        tDelivered=0
        tVolumeCreated=0
        tVolumeDelivered=0
        iCreated=0
        iDelivered=0
        iVolumeCreated=0
        iVolumeDelivered=0
        vCreated=0
        vVolumeCreated=0
        vDelivered=0
        vVolumeDelivered=0
        for lines in TestingData.getNonPriorityC(self):
            if (len(lines) < 1):
                continue;
            x = lines           
            
            
            if(x[3][1]=='T'):
                tCreated+=1
                tVolumeCreated += int(x[len(x)-1])
            if(x[3][1]=='I'):
                iCreated+=1
                iVolumeCreated+= int(x[len(x)-1])
            if(x[3][1]=='V'):
                vCreated+=1
                vVolumeCreated += int(x[len(x)-1])
        for lines in TestingData.getNonPriorityDE(self):
            if(len(lines)<=0):
                continue
            x=lines    
            if (x[3] != 'ADB5'):
                continue
            if (x[1] == 'DE'):
                if(x[4][1]=='T'):
                    tDelivered+=1
                    tVolumeDelivered += int(x[len(x)-1])
                if(x[4][1]=='I'):
                    iDelivered+=1
                    iVolumeDelivered += int(x[len(x)-1])
                if(x[4][1]=='V'):
                    vDelivered+=1
                    vVolumeDelivered += int(x[len(x)-1])
        ratios.append(tDelivered/tCreated)
        ratios.append(iDelivered/iCreated)
        ratios.append(vDelivered/vCreated)
        ratiosVolume.append(tVolumeDelivered/tVolumeCreated)
        ratiosVolume.append(iVolumeDelivered/iVolumeCreated)
        ratiosVolume.append(vVolumeDelivered/vVolumeCreated)
        print("\nNon Priority \n")
        print(" Type    Created       Delivered       Percentages           Volume \n")
        print(" Text       "+str(tCreated)+"       "+str(tDelivered)+"         "+str(ratios[3])+"\n")
        print(" Image      "+str(iCreated)+"       "+str(iDelivered)+"         "+str(ratios[4])+"\n")
        print(" Video      "+str(vCreated)+"       "+str(vDelivered)+"         "+str(ratios[5])+"\n")   
        print("\nVolume of Packets \n")
        print(" Type    Created       Delivered      Precentages\n")
        print(" Text       "+str(tVolumeCreated)+"       "+str(tVolumeDelivered)+"         "+str(ratiosVolume[3])+"\n")
        print(" Image      "+str(iVolumeCreated)+"       "+str(iVolumeDelivered)+"         "+str(ratiosVolume[4])+"\n")
        print(" Video      "+str(vVolumeCreated)+"       "+str(vVolumeDelivered)+"         "+str(ratiosVolume[5])+"\n")  
        self.plotRatios(ratios,"Ratio of Total Packets delivered and created")
        self.plotRatios(ratiosVolume,"Ratio of Total bytes Created and Delivered")
    def plotRatios(self,ratios,msg):
        n_groups = 3

        priorities = (ratios[0], ratios[1], ratios[2])

        non_priorities = (ratios[3], ratios[4], ratios[5])

        fig, ax = plt.subplots()

        index = np.arange(n_groups)
        bar_width = 0.35

        opacity = 0.4

        rects1 = ax.bar(index, priorities, bar_width,
                        alpha=opacity, color='b',
                        label='Priority')

        rects2 = ax.bar(index + bar_width, non_priorities, bar_width,
                        alpha=opacity, color='r',
                        label='Non Priorities')

        ax.set_xlabel('Type of messages')
        ax.set_ylabel('Ratio of Packet created and packets delivered')
        ax.set_title(msg)
        ax.set_xticks(index + bar_width / 2)
        ax.set_xticklabels(('Text','Image', 'Video'))
        ax.legend()
        fig.tight_layout()
        plt.show()
