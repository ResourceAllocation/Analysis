file = 'default_scenario_EventLogReport.txt'

class delivered_msg(object):

	def Split_File(self):
		fil = open(file,"r")
		data = fil.read()
		data = data.split("\n")
		fil.close()
		#print(data)
		return data

	def Split_status(self,data):
		c = open("C.txt", "w")
		de = open("DE.txt", "w")

		for row in data:
			if (len(row) < 1):
				continue;
			x = row.split(" ")
			if (x[1] == 'C'):
				c.write(row + "\n")
			if (x[1] == 'DE'):
				de.write(row + "\n")
		c.close()
		de.close()


	def C_count(self):
		c = open("C.txt","r")
		data = c.read()
		data = data.split("\n")
		n = len(data)
		#print(n)
		x = data[n-2]
		first = x.split(" ")
		first = float(first[0])
		first = round(first)
		#print(first)
		req_time = first-7200
		#print(req_time)
		for i in data:
			if(len(i)<1):
				continue

			i = i.split(" ")
			i[0] = float(i[0])
			#print(i)
			if(i[0] >= req_time):
				#print(i[0])
				message = i[3]
				break

		c.close()
		return message

	def D_count(self,count1):
		de = open("DE.txt","r")
		data = de.read()
		data = data.split("\n")
		count2 = float(0)
		for i in data:
			if(len(i)<1):
				continue

			i = i.split(" ")
			m = i[4][0]
			m_no = float(i[4][1:])
			#print(m_no)
			
			if(i[1] == "DE" and i[3] == "ADB8" and m=="M" and m_no <= count1):
				count2 = count2+1

		de.close()
		return count2


		

deliver = delivered_msg()
data = deliver.Split_File()
deliver.Split_status(data)

count1 = deliver.C_count()
count1 = float(count1[1:])
print("Message created = "+ str(count1))
count2 = deliver.D_count(count1)
print("Message Delivered = "+ str(count2))

prob = int(count1/count2 * 100)

print("Delivery Probability = "+ str(prob) + " %")
