#############################################################################
### 	Author - Python Programmer                               ############
###		Description - 5G NR Calculation                          ############
### 	Date - 03-05-2023                                        ############
###																 ############
#############################################################################

import re #Regular expression 

def NR_LogAnalysis():
	BandNRSupportList = []
	CombonNRBandSupportList = []

	#Find all the NR band supported by UE capability
	with open("UECapabilityInfo.txt","r+") as uelogs:
		for eachline in uelogs:
			bandnrpattern = r"bandNR: \d+"
			BandNR = re.findall(bandnrpattern,eachline)
			#BandList NR should not be empty
			if BandNR != []:
				# print(BandNR)
				BandNRSupportList.append(BandNR[0])
				#If above string found exit
			if "supportedBandCombinationList" in eachline:
				break
		
	#Print Band NR list 
	print("\n NR UE Capability - SupportedBandListNR - \n", BandNRSupportList)


	NRBandCombo = []
	BandPair = [] 
	#Find all the NR band combination supported by UE capability
	with open("UECapabilityInfo.txt","r+") as uelogs:
		for eachline in uelogs:
			if "supportedBandCombinationList" in eachline:
				for eachline in uelogs: 
					bandnrpattern = r"bandNR: \d+"
					BandCombo = re.findall(bandnrpattern,eachline)
					#BandList NR should not be empty
					if BandCombo != [] :
						# print(BandCombo)
						BandPair.append(BandCombo[0])
					if "featureSetCombination" in eachline :
						if BandPair != []:
							NRBandCombo.append(BandPair)
							BandPair = []
					if "appliedFreqBandListFilter" in eachline:
						break
		
	#Print Combo NR list 
	print("\n NR UE Capability - Band Combination  - \n")
	for eachBand in NRBandCombo:
		print(eachBand)

#This is the main function 
def main():
    #This is the NR log analysis function 
    NR_LogAnalysis()

if __name__ == "__main__" :
	main()