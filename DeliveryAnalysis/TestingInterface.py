from TestingData import TestingData
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple
class TestInterface(TestingData):
	messagesPath={}
	def __init__(self):   # Parsing tha data into file 

		self.__NPRDtnCreated=[]
		self.__NPRDtnCreated.append(TestingData.getPRTotalCreatedT(self))
		self.__NPRDtnCreated.append(TestingData.getPRTotalCreatedI(self))
		self.__NPRDtnCreated.append(TestingData.getPRTotalCreatedV(self))

		self.__NPRAdbDelivered=[0,0,0]
		self.__NPRCDDelivered=[0,0,0]
		self.__NPRGCDelivered=[0,0,0]
		self.__NPRWIFIRecieved=[0,0,0]
		self.__NPRMCSWIFIDelivered=[0,0,0]
		self.__NPRMCSADBDelivered=[0,0,0]

		self.__PRDtnCreated=[]
		self.__PRDtnCreated.append(TestingData.getPRTotalCreatedT(self))
		self.__PRDtnCreated.append(TestingData.getPRTotalCreatedI(self))
		self.__PRDtnCreated.append(TestingData.getPRTotalCreatedV(self))
		self.__PRAdbDelivered=[0,0,0]
		self.__PRCDDelivered=[0,0,0]
		self.__PRGCDelivered=[0,0,0]
		self.__PRWIFIRecieved=[0,0,0]
		self.__PRMCSWIFIDelivered=[0,0,0]
		self.__PRMCSADBDelivered=[0,0,0]

	def get_DtnCreated(self):
		return self.__NPRDtnCreated;
	def get_AdbDelivered(self):
		return self.__NPRAdbDelivered;
	def get_CDDelivered(self):
		return self.__NPRCDDelivered;
	def get_GCDelivered(self):
		return self.__NPRGCDelivered;
	def get_WIFIRecieved(self):
		return self.__NPRWIFIRecieved;
	def get_MCSWIFIDelevered(self):
		return self.__NPRMCSWIFIDelivered;
	def get_MCSADBDelivered(self):
		return self.__NPRMCSADBDelivered;

	def AddMessage(self,line,Array):
		#print(type(Array))
		if(line[4][1]=='T'):
			Array[0]+=1
		elif(line[4][1]=='I'):
			Array[1]+=1
		elif(line[4][1]=='V'):
			Array[2]+=1
		return Array
	def CountDeliveredSent(self):
		for line in TestingData.getNonPriorityDE(self):
			if(line[2][0]=='d'):
				if(line[3][0]=='A'):
					#print("Done 1")
					self.__NPRAdbDelivered=self.AddMessage(line,self.__NPRAdbDelivered)
					
			if(line[2][0]=='C'):
				#print("Done 2")
				self.__NPRGCDelivered=self.AddMessage(line,self.__NPRGCDelivered)
			if(line[2][0]=='A'):
				if(line[3][0]=='C'):
					#print("Done 3")
					self.__NPRCDDelivered=self.AddMessage(line,self.__NPRCDDelivered)
				if(line[3][0]=='W'):
					#print("Done 4")
					self.__NPRWIFIRecieved=self.AddMessage(line,self.__NPRWIFIRecieved)
			if(line[2][0]=='W'):
				if(line[3][0]=='W'):
					#print("Done 5")
					self.__NPRMCSWIFIDelivered=self.AddMessage(line,self.__NPRMCSWIFIDelivered)
				if(line[3][0] == 'A'):
					#print("Done 6")
					self.__NPRMCSADBDelivered=self.AddMessage(line,self.__NPRMCSADBDelivered)
		#self.__NPRDtnCreated=len(TestingData.getNonPriorityC(self))

		for line in TestingData.getPriorityDE(self):
			if(line[2][0]=='d'):
				if(line[3][0]=='A'):
					self.__PRAdbDelivered=self.AddMessage(line,self.__PRAdbDelivered)
			if(line[2][0]=='C'):
				self.__PRGCDelivered=self.AddMessage(line,self.__PRGCDelivered)
			if(line[2][0]=='A'):
				if(line[3][0]=='C'):
					self.__PRCDDelivered=self.AddMessage(line,self.__PRCDDelivered)
				if(line[3][0]=='W'):
					self.__PRWIFIRecieved=self.AddMessage(line,self.__PRWIFIRecieved)
			if(line[2][0]=='W'):
				if(line[3][0]=='W'):
					self.__PRMCSWIFIDelivered=self.AddMessage(line,self.__PRMCSWIFIDelivered)
				if(line[3][0] == 'A'):
					self.__PRMCSADBDelivered=self.AddMessage(line,self.__PRMCSADBDelivered)
		#self.__PRDtnCreated=len(TestingData.getPriorityC(self))

	def PrintDelivery(self,i):
		print("Non Priority InterfaceWise\n")
		print("Interface        Created        Delivered\n")
		print("DTN           "+str(self.__NPRDtnCreated[i]),end="            ")
		print(self.__NPRAdbDelivered[i],end="\n")
		print("ADB            "+str(self.__NPRAdbDelivered[i]),end="            ")
		print(self.__NPRCDDelivered[i])
		print("CD             "+str(self.__NPRCDDelivered[i]),end="            ")
		print(self.__NPRGCDelivered[i])
		print("GC             "+str(self.__NPRGCDelivered[i]),end="            ")
		print(self.__NPRWIFIRecieved[i])
		print("GC_WIFI        "+str(self.__NPRWIFIRecieved[i]),end="            ")
		print(self.__NPRMCSWIFIDelivered[0])
		print("MCS            "+str(self.__NPRMCSWIFIDelivered[i]),end="            ")
		print(self.__NPRMCSADBDelivered[i])

		print("\nPriority InterfaceWise\n")
		
		print("Interface        Created        Delivered\n")
		print("DTN           "+str(self.__PRDtnCreated[i]),end="            ")
		print(self.__PRAdbDelivered[i],end="\n")
		print("ADB            "+str(self.__PRAdbDelivered[i]),end="            ")
		print(self.__PRCDDelivered[i])
		print("CD             "+str(self.__PRCDDelivered[i]),end="              ")
		print(self.__PRGCDelivered[i])
		print("GC             "+str(self.__PRGCDelivered[i]),end="              ")
		print(self.__PRWIFIRecieved[i])
		print("GC_WIFI        "+str(self.__PRWIFIRecieved[i]),end="            ")
		print(self.__PRMCSWIFIDelivered[i])
		print("MCS            "+str(self.__PRMCSWIFIDelivered[i]),end="            ")
		print(self.__PRMCSADBDelivered[i])
	def plotDelivery(self,i):
		n_groups = 7
		non_priorities = (self.__NPRDtnCreated[i],self.__NPRAdbDelivered[i],self.__NPRCDDelivered[i],self.__NPRGCDelivered[i],self.__NPRWIFIRecieved[i],self.__NPRMCSWIFIDelivered[i],self.__NPRMCSADBDelivered[i])
		priorities = (self.__PRDtnCreated[i],self.__PRAdbDelivered[i],self.__PRCDDelivered[i],self.__PRGCDelivered[i],self.__PRWIFIRecieved[i],self.__PRMCSWIFIDelivered[i],self.__PRMCSADBDelivered[i])
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
		ax.set_title('hihiii')
		ax.set_xticks(index + bar_width / 2)
		ax.set_xticklabels(('DTN','ADB', 'DataMules','GC','GC_WIFI','MCS_WIFI','MCS_ADB'))
		ax.legend()
		fig.tight_layout()
		plt.show()