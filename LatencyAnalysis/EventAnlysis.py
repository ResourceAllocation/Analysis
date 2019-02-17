import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

FileName = "abc.txt"
Messages = { "DE":[], "S":[] }

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
	Delivered = {}
	Time = 0.00
	NoOfMEssages = 0
	for Event in Messages["DE"]:
		if ( 0 <= Event[2].find(Source) and 0 <= Event[3].find(Destination) ):
			Delivered[ Event[4] ] = float(Event[0])

	for Event in Messages["S"]:
		if ( 0 <= Event[2].find(Source) and 0 <= Event[3].find(Destination) ):
			if ( Event[4] in Delivered ):
				NoOfMEssages += 1
				Time += Delivered[Event[4]] - float(Event[0])
	return Time/float(NoOfMEssages)

def DTN_TO_ADB():

	print "\nDTN To ADB (In Seconds) :-", Get_Latency("dtn","ADB"),"\n"


def ADB_To_CD():
	
	print "\nADB To CD (In Seconds) :-", Get_Latency("ADB","CD"),"\n"


def CD_to_GC():

	print "\nCD To GC (In Seconds) :-", Get_Latency("CD","ADB"),"\n"


def GC_to_GC_WiFi():

	print "\nGC To GC WIFI (In Seconds) :-", Get_Latency("ADB","WIFI"),"\n"


def GC_WIFI_to_MCS_WiFi():
	
	print "\nGC WIFI To MCS WIFI (In Seconds) :-", Get_Latency("WIFI","WIFI"),"\n"


def MCS_WIFI_to_MCS_ADB():

	print "\nMCS WiFi To MCS ADB (In Seconds) :-", Get_Latency("WIFI","ADB"),"\n"


# Parsing the messages accoring to status in an dictionary
def Parse_Status(Messages, Status):
	
	FileDescriptor = open(Status+".txt","w")
	FileData = open(FileName,"r").read().split("\n")
	
	for StatusRow in FileData:

		StatusRow = StatusRow.split(" ")
		if ( 2 < len(StatusRow) and Status == StatusRow[1] ):
			Messages[Status].append(StatusRow)
def Plot():
 
	objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
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
	plt.ylabel('Usage')
	plt.title('Programming language usage')
	 
	plt.show()

def main():

	Parse_Status(Messages,"DE")
	Parse_Status(Messages,"S")
	# DTN_TO_ADB()
	# ADB_To_CD()
	# CD_to_GC()
	# GC_to_GC_WiFi()
	# GC_WIFI_to_MCS_WiFi()
	# MCS_WIFI_to_MCS_ADB()

main()