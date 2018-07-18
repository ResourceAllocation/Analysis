import matplotlib.pyplot as plt
#import plotly.plotly as py
import numpy as np
file='default_scenario_EventLogReport.txt'
class split_data(object):

	def Remove_ADB5(self):
		fil= open(file,"r")
		data=fil.read()
		data=data.replace("ADB5","")
		data=data.replace(" \n","\n")
		fil.close()
		fil=open(file,"w")
		fil.write(data)
		fil.close()
	def Split_File(self):
		fil=open(file,"r")
		data=fil.read()
		data=data.split("\n")
		n=len(data)
		return data
	def Split_status(self,data):
		#older=''
		conn=open("CONN.txt","w")
		c=open("C.txt","w")
		s=open("S.txt","w")
		r=open("R.txt","w")
		de=open("DE.txt","w")
		for row in data:
			if(len(row)<1):
				continue;
			x=row.split(" ")	
			if(x[1]=='CONN'):
				conn.write(row+"\n")
			if(x[1]=='C'):
				c.write(row+"\n")
			if(x[1]=='S'):
				s.write(row+"\n")
			if(x[1]=='R'):
				r.write(row+"\n")
			if(x[1]=='DE'):
				de.write(row+"\n")
		conn.close()
		c.close()
		s.close()
		r.close()
		de.close()


DRate_DTN_TO_ADB=0
DRATE_ADB_TO_GC=0
DRATE_GC_TO_WIFI=0
DRATE_WIFI_TO_WIFI=0
DRATE_WIFI_TO_DB=0
to_wifi={}
to_MCS={}
to_DB={}
delivered_DB={}
delivered_MCS={}
delivered_wifi={}
class Analysis(object):
	
	def __init__(self,L_WIFI_TO_DB=0,L_WIFI_TO_WIFI=0,L_GC_TO_WIFI=0,ADB_Total=0,total_messages=0,l_DB_TO_GC=None,l_DTN_TO_DB=None,Data_Mule_Delivered=None,Data_Mule=None,Delivered_DB=None,ADB5=None,ADB6=None,ADB7=None,ADB8=None,ADB9=None,Node_Message=None,latency=None):
		self.ADB5=()
		self.L_WIFI_TO_DB=0
		self.latency={}
		self.L_WIFI_TO_WIFI=0
		self.ADB6=(17,18,19)
		self.ADB7=(20,21,22)
		self.ADB8=(23,24,25)
		self.ADB9=(26,27,28)
		self.Node_Message={}
		self.Delivered_DB={}
		self.Data_Mule_Recieved={}
		self.Data_Mule_Delivered={}
		self.l_DTN_TO_DB=0
		self.l_DB_TO_GC=0
		self.ADB_Total=0
		self.total_messages=0
		self.L_GC_TO_WIFI=0
	def Print_ADB(self):
		print(self.ADB5)
		print(self.ADB6)
		print(self.ADB7)
		print(self.ADB8)
		print(self.ADB9)
	def search(self,ADB,node):
		for i in ADB:
			if(str(i)==node):
				return True
		return False
	def NodeMessageMapping(self,data):		
		for row in data:
			if(len(row)<1):
				continue
			message=row[3]
			if(message[0]!='M'):
				continue
			self.total_messages+=1
			node=row[2].split('_')[1]
			if(self.search(self.ADB5,node)==True):
				node="ADB5"
			elif(self.search(self.ADB6,node)==True):
				node="ADB6"
			elif(self.search(self.ADB7,node)==True):
				node="ADB7"
			elif(self.search(self.ADB8,node)==True):
				node="ADB8"
			elif(self.search(self.ADB9,node)==True):
				node="ADB9"
			else:
				node="ADB5"
			if (message not in self.Node_Message):
				self.Node_Message[message]=(node,row[0])
	def Convert_Into_List(self,data):	
		data=data.split('\n')
		n=len(data)
		for i in range(0,n-1):
			data[i]=data[i].split(' ')
			for x in data[i]:
				if(x==' ' or  x==''):
					data[i].remove(x)
		return data
	def DTN_to_ADB(self):
		fil=open('C.txt','r')
		data=fil.read()
		data=self.Convert_Into_List(data)

		self.NodeMessageMapping(data)
		fil.close()
	def Fill_Data_Mule_Delivered(self,row,message):
		end_time=row[0]
		if(message not in self.Data_Mule_Delivered ):
			self.Data_Mule_Delivered[message]=end_time
	def Fill_to_wifi(self,data,message):
		if(message[0]!='M'):
			return
		if(message not in to_wifi):
			to_wifi[message]=data[0]
	def FILL_to_MCS(self,data,message):
		if(message[0]!='M'):
			return
		if(message not in to_MCS):
			to_MCS[message]=data[0]
	def FILL_to_DB(self,data,message):
		if(message[0]!='M'):
			return
		if(message not in to_DB):
			to_DB[message]=data[0]		
	def Fill_delivered_wifi(self,data,message):
		if(message not in delivered_wifi):
			delivered_wifi[message]=data[0]
	def Fill_delivered_MCS(self,data,message):
		if(message not in delivered_MCS):
			delivered_MCS[message]=data[0]
	def Fill_delivered_DB(self,data,message):
		if(message not in delivered_DB):
			delivered_DB[message]=data[0]		
	def Finish_Time(self):
		co=0
		fil=open('DE.txt','r')
		data=fil.read()
		ADB={'ADB5':0,'ADB6':0,'ADB7':0,'ADB8':0,'ADB9':0}
		count={'ADB5':0,'ADB6':0,'ADB7':0,'ADB8':0,'ADB9':0}
		data=self.Convert_Into_List(data)
		done=[]
		for row in data:
			if(len(row)<1):
				continue
			message=row[-2:-1][0]
			if(message[0]!='M'):
				continue
			source=row[2] #getting the source of message
			if(source[0]=='C'):
				self.Fill_Data_Mule_Delivered(row,message)
			if(row[3]=="WIFI_11"):
				self.Fill_delivered_wifi(row,message)
			if(row[3]=="WIFI_10"):
				self.Fill_delivered_MCS(row,message)
			if(row[2]=='WIFI_10'):
				self.Fill_delivered_DB(row,message)
			node=row[-3:-2][0]
			if(node[0]!='A' and self.Node_Message[message][0]!='ADB5'):
				continue
			end_time=row[0]
			if(message in done):
				continue
			if(message not in self.Delivered_DB):
				self.Delivered_DB[message]=(node,end_time)
			done.append(message)
			if(self.Node_Message[message][0]==self.Delivered_DB[message][0] or self.Node_Message[message][0]=='ADB5'):
				co+=1
				x=float(self.Delivered_DB[message][1])-float(self.Node_Message[message][1])
				if(self.Node_Message[message][0]=='ADB5'):
					ADB['ADB5']=ADB['ADB5']+(x)
					count['ADB5']+=1
				else:	
					count[node]+=1
					ADB[node]=ADB[node]+(x)
		total_time=0
		total_count=len(self.Delivered_DB)
		for i in ADB:
			total_time=total_time+ADB[i]
		self.l_DTN_TO_DB=total_time/total_count
		global DRate_DTN_TO_ADB
		DRate_DTN_TO_ADB=total_count/self.total_messages
		print('\n')
		print('...........................')
		print("Total latency from DTN to ADB is :- "+str(self.l_DTN_TO_DB))
		print("Total Message delivered to ADB is "+str(total_count))
		print("Total Messages Created is :- "+str(self.total_messages))
		print("Delivery ratio from DTN to ADB is:- "+str(DRate_DTN_TO_ADB))
		
		self.ADB_Total=count['ADB6']+count['ADB9']+count['ADB8']
		fil.close()
		
	def DB_TO_GC(self):
		fil=open('S.txt','r')
		data=fil.read()
		data=self.Convert_Into_List(data)
		for row in data:
			if(len(row)<1):
				continue

			if(row[3]=="WIFI_11"):
				self.Fill_to_wifi(row,row[4])
			if(row[3]=="WIFI_10"):
				self.FILL_to_MCS(row,row[4])
			if(row[2]=='WIFI_10'):
				self.FILL_to_DB(row,row[3])
			cd=row[3]
			if(cd[0]!='C'):
				continue
			message=row[4]
			if(message not in self.Data_Mule_Recieved):
				self.Data_Mule_Recieved[message]=row[0]
		total_time=0
		total_count=0
		n=len(self.Data_Mule_Delivered)
		for i in self.Data_Mule_Delivered:
			start_time=float(self.Data_Mule_Recieved[i])
			end_time=float(self.Data_Mule_Delivered[i])
			self.l_DB_TO_GC+=(end_time-start_time)
		self.l_DB_TO_GC=self.l_DB_TO_GC/n
		global DRATE_ADB_TO_GC
		DRATE_ADB_TO_GC=n/self.ADB_Total
		print('\n')
		print('...........................')
		print ("Total Latency from ADB to Group Center is ",self.l_DB_TO_GC)	
		print ("Total Messages recieved by Data mules is:- ",self.ADB_Total)
		print("Total Messages Delivered by Data mules to GC:- ",n)
		print("Total Delivery rate from ADB to GC is:- ",n/self.ADB_Total)
		fil.close()
	def GC_TO_WIFI(self):
		print('\n')
		print('...........................')
		for i in to_wifi:
			start_time=float(to_wifi[i])
			end_time=float(delivered_wifi[i])
			self.L_GC_TO_WIFI+=( end_time-start_time)
		self.L_GC_TO_WIFI=self.L_GC_TO_WIFI/len(delivered_wifi)
		global DRATE_GC_TO_WIFI
		DRATE_GC_TO_WIFI=len(delivered_wifi)/len(to_wifi)
		print("Latency from GC to WIFI:- ",self.L_GC_TO_WIFI)
		print("Total Messages Recieved by GC ",len(to_wifi))
		print("Total Messages Recieved by WIFI ",len(delivered_wifi))
		print("Total Delivery rate from GC to WIFI is:- ",DRATE_GC_TO_WIFI)
	def WIFI_TO_WIFI(self):
		print('\n')
		print('...........................')
		for i in to_MCS:
			end_time=float(delivered_MCS[i])
			start_time=float(to_MCS[i])
			self.L_WIFI_TO_WIFI+= (end_time-start_time)
		global DRATE_WIFI_TO_WIFI
		DRATE_WIFI_TO_WIFI=len(to_MCS)/len(delivered_MCS)
		self.L_WIFI_TO_WIFI=self.L_WIFI_TO_WIFI/len(delivered_MCS)
		print("Latency from WIFI to WIFI:- ",self.L_WIFI_TO_WIFI)
		print("Total Messages Recieved by GC ",len(to_MCS))
		print("Total Messages Recieved by WIFI ",len(delivered_MCS))
		print("Total Delivery rate from WIFI to WIFI is:- ",DRATE_WIFI_TO_WIFI)
	def WIFI_TO_DB(self):
		print('\n')
		print('...........................')
		for i in to_DB:
			end_time=float(delivered_DB[i])
			start_time=float(to_DB[i])
			self.L_WIFI_TO_DB+= (end_time-start_time)
		global DRATE_WIFI_TO_DB
		DRATE_WIFI_TO_DB=len(to_DB)/len(delivered_DB)
		self.L_WIFI_TO_DB=self.L_WIFI_TO_DB/len(delivered_DB)
		print("Latency from WIFI to MCS:- ",self.L_WIFI_TO_DB)
		print("Total Messages Recieved by MCS WIFI ",len(to_DB))
		print("Total Messages Recieved by MCS ",len(delivered_DB))
		print("Total Delivery rate from MCS WIFI to MCS DB is:- ",DRATE_WIFI_TO_DB)
	def plotGraph(self):
		objects = ('DTN_to_ADB', 'ADB_TO_GC', 'GC_TO_WIFI', 'WIFI_TO_WIFI', 'WIFI_TO_DB')
		#objects2 = ('DTN_to_ADB', 'ADB_TO_GC', 'GC_TO_WIFI', 'WIFI_TO_WIFI', 'WIFI_TO_DB')
		y_pos = np.arange(len(objects))
		performance = [self.l_DTN_TO_DB,self.l_DB_TO_GC,self.L_GC_TO_WIFI,self.L_WIFI_TO_WIFI,self.L_WIFI_TO_DB]
		performance1 = [DRate_DTN_TO_ADB,DRATE_ADB_TO_GC,DRATE_GC_TO_WIFI,DRATE_WIFI_TO_WIFI,DRATE_WIFI_TO_DB]
 
		plt.bar(y_pos, performance, align='center', alpha=1,color='blue')
		plt.xticks(y_pos, objects)
		plt.ylabel('Latency(In Seconds)')
		plt.title('Latency Graph')
 
		plt.show()
	def PlotDataRate(self):
		objects = ('DTN_to_ADB', 'ADB_TO_GC', 'GC_TO_WIFI', 'WIFI_TO_WIFI', 'WIFI_TO_DB')
		y_pos = np.arange(len(objects))
		print(DRate_DTN_TO_ADB,DRATE_ADB_TO_GC,DRATE_GC_TO_WIFI,DRATE_WIFI_TO_WIFI,DRATE_WIFI_TO_DB)
		performance1 = [DRate_DTN_TO_ADB,DRATE_ADB_TO_GC,DRATE_GC_TO_WIFI,DRATE_WIFI_TO_WIFI,DRATE_WIFI_TO_DB]
		plt.bar(y_pos, performance1, align='center', alpha=1,color='blue')
		plt.xticks(y_pos, objects)
		plt.ylabel(' Data delivery Rate ')
		plt.title(' Data delivery rate Graph ')
		plt.show()
split_obj=split_data()		
split_obj.Remove_ADB5()
data=split_obj.Split_File()
split_obj.Split_status(data)
obj=Analysis()
#obj.Print_ADB()
obj.DTN_to_ADB()
obj.Finish_Time()
obj.DB_TO_GC()
obj.GC_TO_WIFI()
obj.WIFI_TO_WIFI()
obj.WIFI_TO_DB()
obj.plotGraph()
obj.PlotDataRate()