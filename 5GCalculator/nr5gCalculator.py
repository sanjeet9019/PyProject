#############################################################################
### 	Author - Python Programmer                               ############
###		Description - 5G NR Calculation                          ############
### 	Date - 03-05-2023                                        ############
###																 ############
#############################################################################

import nr5gmodule as nrmod

def case_one():
	#5G NR ARFCN --> 5G NR FREQUENCY  Conversion 
	print("5G NR ARFCN --> 5G NR FREQUENCY ,INFO I/P - NR ARFCN O/P - NR FREQUENCY(MHz)")
	nr_Arfcn = input("ENTER NR ARFCN : ")
	nr_Freq = nrmod.get_nr_Freq_from_nr_Arfcn(int(nr_Arfcn))
	print("NR ARFCN = {} --> NR FREQUENCY = {} MHz ".format(nr_Arfcn,nr_Freq))
	print("\n")


def case_two():
	#5G NR FREQUENCY --> 5G NR ARFCN Conversion 
	print("5G NR FREQUENCY --> 5G NR ARFCN ,INFO I/P - NR FREQUENCY(MHz) O/P - NR ARFCN")
	nr_Freq = input("ENTER NR FREQUENCY(MHz) : ")
	nr_Arfcn = nrmod.get_nr_Arfcn_from_nr_Freq(int(nr_Freq))
	print("NR FREQUENCY = {} MHz --> NR ARFCN  = {}".format(nr_Freq,nr_Arfcn))
	print("\n")

def case_three():
	#5G NR FREQUENCY --> 5G NR Band list 
	print("5G NR FREQUENCY --> 5G NR BANDLIST ,INFO: I/P - NR FREQUENCY(MHz) O/P - NR BANDLIST ")
	nr_Freq = input("ENTER NR FREQUENCY(MHz) : ")
	nr_BandList = nrmod.get_nr_Bands_from_nr_Freq(int(nr_Freq))
	print("NR FREQUENCY = {} MHz --> NR BAND LIST  = {} ".format(nr_Freq,nr_BandList))
	print("\n")

def case_four():
	#5G NR ARFCN --> 5G NR Band list 
	print("5G NR ARFCN --> 5G NR BANDLIST,INFO: I/P - NR ARFCN O/P - NR BANDLIST ")
	nr_Arfcn = input("ENTER NR ARFCN : ")
	nr_BandList = nrmod.get_nr_Bands_from_nr_Arfcn(int(nr_Arfcn))  #return List 
	print("NR ARFCN = {} --> NR BAND LIST = {}".format(nr_Arfcn,nr_BandList))
	print("\n")


def case_five():
	#5G NR Band Type FDD/TDD 
	print("5G NR BAND --> BAND TYPE(FDD/TDD),INFO: I/P - NR BAND O/P - NR BANDTYPE(FDD/TDD)")
	nr_Band = input("ENTER NR BAND : ")
	nr_BandType = nrmod.get_duplex_mode_from_nr_Band(nr_Band)
	print("NR BAND = {} NR BAND TYPE = {}".format(nr_Band,nr_BandType))
	print("\n")


def case_six():
	#5G NR Band --> 5G NR ARFCN RANGE
	print("5G NR BAND --> 5G NR ARFCN RANGE,INFO: I/P - NR BAND AND DIRECTION(DL/UL) O/P - 5G NR ARFCN RANGE")
	nr_Band = input("ENTER 5G NR BAND : ")
	direction = input("ENTER 5G NR DIRECTION(ul/dl) : ")
	nr_ArfcnRange = nrmod.get_nr_ArfcnRange_from_nr_Band(nr_Band,direction) #return tuple readonly
	print("5G NR BAND = {} --> 5G NR ARFCN RANGE = {} ".format(nr_Band,nr_ArfcnRange))
	print("\n")


def case_seven():
	#5G NR Band --> 5G NR FREQUENCY RANGE
	print("5G NR BAND --> 5G NR FREQUENCY RANGE,INFO: I/P - NR BAND AND DIRECTION(DL/UL) O/P - 5G NR FREQUENCY RANGE(MHz)")
	nr_Band = input("ENTER 5G NR BAND : ")
	direction = input("ENTER 5G NR DIRECTION(ul/dl) : ")
	nr_FreqRange = nrmod.get_nr_Freqrange_from_nr_Band(nr_Band,direction) #return Tuple readonly
	print("5G NR Band = {} --> 5G NR FREQUENCY RANGE = {} MHz".format(nr_Band,nr_FreqRange))
	print("\n")


def case_eight():
	# Global Synchronisation Channel Number (GSCN) --> 5G NR FREQUENCY 
	print("5G NR GSCN --> 5G NR FREQUENCY ,INFO: I/P - NR GSCN O/P - 5G NR FREQUENCY(MHz)")
	nr_GSCN = input("ENTER 5G NR GSCN(0 - 26639): ")
	nr_Freq = nrmod.get_nr_Freq_from_nr_GSCN(nr_GSCN) #return Tuple readonly
	print("5G NR(GSCN) = {} --> 5G NR FREQUENCY = {} MHz".format(nr_GSCN,nr_Freq))
	print("\n")

def case_nine():
	# 5G NR FREQUENCY  --> Global Synchronisation Channel Number (GSCN)
	print("5G NR FREQUENCY --> 5G NR GSCN,INFO: I/P - 5G NR FREQUENCY(MHz) O/P - NR GSCN")
	nr_Freq = input("ENTER 5G NR FREQUENCY : ")
	nr_GSCN = nrmod.get_nr_GSCN_from_nr_Freq(nr_Freq) 
	print("5G NR FREQUENCY = {} MHz --> 5G NR (GSCN) = {} ".format(nr_Freq,nr_GSCN))
	print("\n")


def case_ten():
	# 5G NR Band  --> Global Synchronisation Channel Number (GSCN) Range
	print("5G NR BAND --> 5G NR GSCN,INFO: I/P - BAND O/P - NR GSCN")
	nr_Band = input("ENTER 5G NR BAND : ")
	nr_GSCN = nrmod.get_nr_GSCNRange_from_nr_Band(nr_Band) 
	print("5G NR BAND = {} --> (GSCN) RANGE = {}".format(nr_Band,nr_GSCN))
	print("\n")

def case_eleven():
	# 5G NR Numerology --> Subcarrier Spacing  values 
	print("5G NR NUMEROLOGY --> SUBCARRIER SPACE (KHz) ,INFO: I/P - NUMEROLOGY(0-3) O/P - NR SUBCARRIER SPACE(KHz)")
	numerology = int(input("ENTER 5G NUMEROLOGY(0-3) : ")) 
	subcarrier_spacing = nrmod.get_NRsubcarrier_spacing_from_numerology(numerology)
	print("NR NUMEROLOGY = {} --> SUBCARRIER SPACING = {} KHz".format(numerology,subcarrier_spacing))
	print("\n")


def case_twelve():
	#5G NR Number of PRBs  
	print("CACULATE NUMBER OF PRBs(PHYSICAL RESOURCE BLOCKS),INFO: I/P - NUMEROLOGY(0-3) AND CHANNEL BANDWIDTH O/P - NUMBER OF PRBs ")
	numerology = int(input("ENTER 5G NR NUMEROLOGY(0-4) : ")) 
	SubcarrierSpacing = nrmod.get_NRsubcarrier_spacing_from_numerology(numerology)
	channelBW = int(input("ENTER CHANNEL BANDWIDTH(MHz) : ")) #MHz
	nr_PRBs = nrmod.get_nr_NumberOfPRBs(channelBW,SubcarrierSpacing) 
	print("NUMBER OF PRBs = {}".format(nr_PRBs))
	print("\n")

def case_default():
    print("Invalid choice")

# Define the switch function
def switch(case):
    switcher = {
        1: case_one,
        2: case_two,
	3: case_three,
	4: case_four,
	5: case_five,
	6: case_six,
	7: case_seven,
	8: case_eight,
	9: case_nine,
	10: case_ten,
	11: case_eleven,
	12: case_twelve
    }
    # Get the function from the dictionary
    # If the key is not found, use the default case
	# dictionary.get(key, default_value)
    func = switcher.get(case, case_default)
    print("\n")
    # Execute the function
    func()

#5G calculator  function 
def nr5GCalculator():

    choices = '''
	\n\n************************************************** 5G NR CALCULATION ********************************************************\n
1. 5G NR ARFCN --> 5G NR FREQUENCY ,INFO I/P - NR ARFCN O/P - NR FREQUENCY(MHz)
2. 5G NR FREQUENCY --> 5G NR ARFCN ,INFO I/P - NR FREQUENCY(MHz) O/P - NR ARFCN
3. 5G NR FREQUENCY --> 5G NR BANDLIST ,INFO: I/P - NR FREQUENCY(MHz) O/P - NR BANDLIST
4. 5G NR ARFCN --> 5G NR BANDLIST,INFO: I/P - NR ARFCN O/P - NR BANDLIST
5. 5G NR BAND --> BAND TYPE(FDD/TDD),INFO: I/P - NR BAND O/P - NR BANDTYPE(FDD/TDD)
6. 5G NR BAND --> 5G NR ARFCN RANGE,INFO: I/P - NR BAND AND DIRECTION(DL/UL) O/P - 5G NR ARFCN RANGE
7. 5G NR BAND --> 5G NR FREQUENCY RANGE,INFO: I/P - NR BAND AND DIRECTION(DL/UL) O/P - 5G NR FREQUENCY RANGE(MHz)
8. 5G NR GSCN --> 5G NR FREQUENCY ,INFO: I/P - NR GSCN O/P - 5G NR FREQUENCY(MHz)
9. 5G NR FREQUENCY --> 5G NR GSCN,INFO: I/P - 5G NR FREQUENCY(MHz) O/P - NR GSCN
10. 5G NR BAND --> 5G NR GSCN,INFO: I/P - BAND O/P - NR GSCN
11. 5G NR NUMEROLOGY --> SUBCARRIER SPACE (KHz) ,INFO: I/P - NUMEROLOGY(0-3) O/P - NR SUBCARRIER SPACE(KHz)
12. CACULATE NUMBER OF PRBs(PHYSICAL RESOURCE BLOCKS),INFO: I/P - NUMEROLOGY(0-3) AND CHANNEL BANDWIDTH O/P - NUMBER OF PRBs \n\n'''

    # Infinite loop
    while True:
        print(choices)
        choice = int(input("ENTER YOUR CHOICES (1-12): "))
        #Call the switch case functions
        switch(choice)
        user_input = input("CONTINUE ? PRESS (y/n): ")
        if user_input.lower() != "y":
            break

#This is the main function of the program 
def main():
    #5G calculator 
    nr5GCalculator()

if __name__ == "__main__" :
    main()