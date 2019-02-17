class TestingData(object):
	non_priority_file = "Report4/NPRdefault_scenario_EventLogReport.txt"
	priority_file = 'Report4/PRdefault_scenario_EventLogReport.txt'
	TotalSimulation=14400
	TTL=3600
	def __init__(self,non_priority_data=None,priority_data=None):   # Parsing tha data into file 
		self.__non_priority_data=open(self.non_priority_file,'r').readlines()
		self.__priority_data=open(self.priority_file,'r').readlines()
		self.__PRMessageCreaedBeforeTTL={''}
		self.__NPRMessageCreaedBeforeTTL={''}
		self.__PriorityC=[]
		self.__PriorityS=[]
		self.__PriorityDE=[]
		self.__PRTotalCreatedT=0
		self.__PRTotalCreatedI=0
		self.__PRTotalCreatedV=0

		self.__NPRTotalCreatedT=0
		self.__NPRTotalCreatedI=0
		self.__NPRTotalCreatedV=0

		self.__Non_PriorityC=[]
		self.__Non_PriorityS=[]
		self.__Non_PriorityDE=[]

		self.RemoveN()

		self.ParseFiles('C')
		
		self.ParseFiles('S')
		
		self.ParseFiles('DE')
		#print(len(self.__non_priority_data))
		#print(len(self.__priority_data))

	def getPRTotalCreatedT(self):
		return self.__PRTotalCreatedT
	def getPRTotalCreatedI(self):
		return self.__PRTotalCreatedI
	def getPRTotalCreatedV(self):
		return self.__PRTotalCreatedV
	def getNPRTotalCreatedT(self):
		return self.__NPRTotalCreatedT
	def getNPRTotalCreatedI(self):	
		return self.__NPRTotalCreatedI
	def getNPRTotalCreatedV(self):
		return self.__NPRTotalCreatedV	
	def getPriorityData(self):
		return self.__priority_data
	def getNonPriorityData(self):
		return self.__non_priority_data
	def getPriorityC(self):
		return(self.__PriorityC)
	def getPriorityS(self):
		return(self.__PriorityS)
	def getPriorityDE(self):
		return(self.__PriorityDE)
	def getNonPriorityC(self):
		return(self.__Non_PriorityC)
	def getNonPriorityS(self):
		return(self.__Non_PriorityS)
	def getNonPriorityDE(self):
		return(self.__Non_PriorityDE)

	def RemoveN(self):
		
		temp=[]
		for line in self.__non_priority_data:
			line=line.split()
			if(line[-4][0]=='N' or line[-3][0]=='N'):
				continue
			temp.append(line)
		self.__non_priority_data=temp
		
		temp=[]
		for line in self.__priority_data:
			line=line.split()
			if(line[-4][0]=='N' or line[-3][0]=='N'):
				continue
			temp.append(line)
		self.__priority_data=temp

	# Parse the diffrent action log according to its acions in diffrent files
	def ParseFiles(self,action):
		File=open("Priority"+action+".txt","w")
		
		for line in self.__priority_data:
			if(line[1]==action):
				if(action =='C' and float(line[0])<= self.TotalSimulation-self.TTL):
					self.__PriorityC.append(line)
					self.__PRMessageCreaedBeforeTTL.add(line[3])
					if(line[3][1] == 'T'):
						self.__PRTotalCreatedT+=1
					elif(line[3][1] == 'I'):
						self.__PRTotalCreatedI+=1
					elif(line[3][1] == 'V'):
						self.__PRTotalCreatedV+=1
				if(action == 'S' and line[4] in self.__PRMessageCreaedBeforeTTL):
					#print(line[4])
					self.__PriorityS.append(line)
				if(action == 'DE' and line[4] in self.__PRMessageCreaedBeforeTTL):
					self.__PriorityDE.append(line)
				l=len(line)
				for i in line:
					File.write(str(i)+" ")
				File.write("\n")
		File.close()

		File=open("Non_Priority"+action+".txt","w")
		for line in self.__non_priority_data:
			if(line[1]==action):
				if(float(line[0])<= self.TotalSimulation-self.TTL and action =='C'):
					self.__Non_PriorityC.append(line)
					self.__NPRMessageCreaedBeforeTTL.add(line[3])
					if(line[3][1] == 'T'):
						self.__NPRTotalCreatedT+=1
					elif(line[3][1] == 'I'):
						self.__NPRTotalCreatedI+=1
					elif(line[3][1] == 'V'):
						self.__NPRTotalCreatedV+=1
				elif(action =='S' and line[4] in self.__NPRMessageCreaedBeforeTTL):
					self.__Non_PriorityS.append(line)
				elif(action == 'DE' and line[4] in self.__NPRMessageCreaedBeforeTTL):
					self.__Non_PriorityDE.append(line)
				l=len(line)
				for i in line:
					File.write(str(i)+" ")
				File.write("\n")
		File.close()
