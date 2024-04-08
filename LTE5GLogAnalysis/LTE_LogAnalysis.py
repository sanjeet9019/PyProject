#############################################################################
### 	Author - Python Programmer                               ############
###		Description - LTE Log Analysis			                 ############
### 	Date - 03-05-2023                                        ############
###								 								 ############
#############################################################################

import re #Regular expression 

def LTE_LogAnalysis() :
	RSRPLIST = []
	CQILIST = []
	#Seach for RSRP and CQI values 
	with open("LTENetworkLogs.txt","r+") as ltelogfile:
		for eachline in ltelogfile:
			rsrppattern = r"RSRP = \-?\d+"
			cqipattern = r"CQI = \-?\d+"
			rsrp = re.findall(rsrppattern,eachline)
			cqi = re.findall(cqipattern,eachline)
			if rsrp != [] and cqi != []:
				# print(rsrp)
				RSRPLIST.append(rsrp[0])
				# print(cqi)
				CQILIST.append(cqi[0])


	print("\n\nRSRP Values - {}\n".format(RSRPLIST))
	print("CQI Values - {}\n".format(CQILIST))


	#This will print a LTE message from search  string 
	with open("LTENetworkLogs.txt","r+") as ltelogfile:
		found = 0
		for eachline in ltelogfile :
			searchword = r"MSG2"
			stopword = "MSG3"
			pattern = rf"\b{searchword}"
			msg1 = re.search(searchword,eachline)
			if msg1 != None:
				found = 1
				print("Seach Found !!!!!\n\n")
				print(eachline)
				for eachline in ltelogfile :
					if stopword in eachline:
						break 
					print(eachline.strip())

		if found == 0 :
			print(f"Search string = {searchword} is not found !!")

#This is the main function
def main():
    #This is the LTE log analysis functios 
    LTE_LogAnalysis()

if __name__ == "__main__" :
	main()