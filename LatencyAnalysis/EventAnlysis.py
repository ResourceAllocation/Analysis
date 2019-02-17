import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

FileName = "abc.txt"
Messages = { "DE":[], "S":[], "C":[] }

# Input : 
#
#	Source (String) : Consist the source of device of which message is started transferring
#	Destination (String) : Consist the Destination of device of which message is transferred
#
# Processing :
# 	This function is calculating the latency of messages transferring from source and destination
#
# Output : 
#
#	Return the latency in Seconds.
#

def Get_Latency(Source,Destination):
	print(Messages)
	DeliveredI = {}
	DeliveredT = {}
	DeliveredV = {}

	TimeI = 0.00
	TimeT = 0.00
	TimeV = 0.00

	NoOfMEssagesI = 0
	NoOfMEssagesT = 0
	NoOfMEssagesV = 0

	for Event in Messages["DE"]:
		if ( 0 <= Event[2].find(Source) and 0 <= Event[3].find(Destination) ):
			if ( "I" == Event[4][1] ):
				DeliveredI[ Event[4] ] = float(Event[0])
			else:
				if ( "T" == Event[4][1] ):
					DeliveredT[ Event[4] ] = float(Event[0])
				else:
					if ( "V" == Event[4][1] ):
						DeliveredV[ Event[4] ] = float(Event[0])


	for Event in Messages["S"]:
		if ( 0 <= Event[2].find(Source) and 0 <= Event[3].find(Destination) ):
			if ( Event[4][1] == "I" and  Event[4] in DeliveredI ):
				NoOfMEssagesI += 1
				TimeI += DeliveredI[Event[4]] - float(Event[0])
			else:
				if ( Event[4][1] == "T" and  Event[4] in DeliveredT ):
					NoOfMEssagesT += 1
					TimeT += DeliveredT[Event[4]] - float(Event[0])
				else:
					if ( Event[4][1] == "V" and  Event[4] in DeliveredV ):
						NoOfMEssagesV += 1
						TimeV += DeliveredV[Event[4]] - float(Event[0])
	return {
		"Text"    : TimeT/NoOfMEssagesT,
		"Images"  : TimeI/NoOfMEssagesI,
		"Video"   : TimeV/NoOfMEssagesV
	}

def DTN_TO_ADB():

	Value = Get_Latency("dtn","ADB")
	print ("\nDTN To ADB (In Seconds) :-",Value ,"\n")
	return Value

def ADB_To_CD():
	
	Value = Get_Latency("ADB","CD")
	print ("\nADB To CD (In Seconds) :-", Value,"\n")
	return Value


def CD_to_GC():

	Value = Get_Latency("CD","ADB")
	print ("\nCD To GC (In Seconds) :-", Value,"\n")
	return Value 

def GC_to_GC_WiFi():

	Value = Get_Latency("ADB","WIFI")
	print ("\nGC To GC WIFI (In Seconds) :-", Value,"\n")
	return Value

def GC_WIFI_to_MCS_WiFi():
	
	Value = Get_Latency("WIFI","WIFI")
	print ("\nGC WIFI To MCS WIFI (In Seconds) :-", Value,"\n")
	return Value

def MCS_WIFI_to_MCS_ADB():

	Value = Get_Latency("WIFI","ADB")
	print ("\nMCS WiFi To MCS ADB (In Seconds) :-", Value,"\n")
	return Value

# Parsing the messages accoring to status in an dictionary
def Parse_Status(Messages, Status):
	
	FileDescriptor = open(Status+".txt","w")
	FileData = open(FileName,"r").read().split("\n")
	
	for StatusRow in FileData:

		StatusRow = StatusRow.split(" ")
		if ( 2 < len(StatusRow) and Status == StatusRow[1] ):
			Messages[Status].append(StatusRow)
def Plot():
 
	objects = (
		'DTN_TO_ADB', 
		'ADB_To_CD', 
		'CD_to_GC', 
		'GC_to_GC_WiFi', 
		'GC_WIFI_to_MCS_WiFi', 
		'MCS_WIFI_to_MCS_ADB'
		)
	y_pos = np.arange(len(objects))
	performance = [DTN_TO_ADB(),
		ADB_To_CD(), 
		CD_to_GC(), 
		GC_to_GC_WiFi(), 
		GC_WIFI_to_MCS_WiFi(), 
		MCS_WIFI_to_MCS_ADB()
	]
	 
	plt.bar(y_pos, performance, align='center', alpha=0.5)
	plt.xticks(y_pos, objects)
	plt.ylabel('Time In Seconds')
	plt.title('latency')
	 
	plt.show()

def GetConfig():
	FileDescriptor = open("Config.txt","w")
	if ( FileDescriptor ):

		print (" Config File not found Error")
		quit()

	else:

		Data = FileDescriptor.read()
		if( 0<= Data.find("FileName") ):
			Data = Data.split("\n")
			for Row in Data:
				if ( 2 < len(Row) ):
					Data = Row.split("=")
					break
			FileName = Data[1]
		else:
			print("FileName Property Not Found in Config File")
			quit()

def main():

	Parse_Status(Messages,"DE")
	Parse_Status(Messages,"S")
	Parse_Status(Messages,"C")
	# Plot()
	DTN_TO_ADB()
	ADB_To_CD()
	CD_to_GC()
	GC_to_GC_WiFi()
	GC_WIFI_to_MCS_WiFi()
	MCS_WIFI_to_MCS_ADB()


main()