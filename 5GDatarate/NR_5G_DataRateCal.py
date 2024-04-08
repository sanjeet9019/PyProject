#############################################################################
### 	Author - Python Programmer                               ############
###	Description - 5G NR Data Throughput                      ############
### 	Date - 03-05-2023                                        ############
###								 ############
#############################################################################

#https://nrarfcn.readthedocs.io/en/latest/

import nrarfcn as NR_5G 
from PIL import Image 


nrthrougput = ''' #####################5G Throughput Calculation ###############################
INPUT PARAMETERS =
J - NUMBER OF CC 
V - MIMO LAYERS
Qm - MODULATION ORDER
f - SCALING FACTOR 
FDD = 1 
TDD = 0.76
Rmax - CODING RATE (0.93) 
Nprb - NOS OF PRB 
Ts - OFDM SYMBOL DURATION
Ts - 10^-3/(14*SUBCARRIER)
OH - OVERHEAD
[0.14], FR1 for DL
[0.08], FR1 for UL
[0.18], FR2 for DL
[0.10], FR2 for UL
Ts = 0.001/(14*SUBCARRIER)

Total NumberfResouce block = (Channel Bandwidth MHz/SubcarrierSpacing(Khz))12 ,1 RB = 12 scs 
ActualNumPRBs =   Total NumberfResouce block -4(Guard band) 

5G NR DATATHROUGHPUT = NUMBEROFCC *(Number of MIMO * Modulation Factor * Scaling Factor * Code Factor * Code rate * [(RB *12)/ Symbol duration](1 – OH))/1000000
5G NR DATATHROUGHPUT =  NUMBEROFCC *((V * Q *f * R* ((N * 12 )/T)*(1 - OH))/(1000000))

###################################################################################################################################################### '''

# 5G NR Numerology --> SubcarrierSpacing 	
def get_NRsubcarrier_spacing_from_numerology(numerology):
    subcarrier_spacing = 15 * (2 ** numerology) # in KHz
    return subcarrier_spacing


#5G NR Numerology --> SubcarrierSpacing 	
def get_nr_NumberOfPRBs(channelBW,SubcarrierSpacing):
	channelBW = channelBW * 1000 # MHz to Khz 
	TotalPRBs =   (channelBW/SubcarrierSpacing)/12 
	ActualPRBs =  int(TotalPRBs) - 4 #Guard band 
	return ActualPRBs

#This is the main function for 5G Throughput calculation
def main() :

    print("5G THROUGHPUT CALCULATION \n\n")
    
    # Load the image from file
    image = Image.open("NR_Throughput.jpg")
    # Display the image
    image.show()

    print(nrthrougput)
    print("5G DATA THROUGHPUT  = NUMBEROFCC*[(NUMBEROFMIMO * MODULATIONORDER * SCALINGFACTOR * CODINGRATE * [(NUMBEROFPRB *12)/ SYMBOLDURATION](1 - OVERHEAD))]/(1000000)]\n\n")

    J = NUMBEROFCC = int(input("ENTER NUMBER OF CC : ")) 
    V = NUMBEROFMIMO = int(input("ENTER NUMBER OF MIMO LAYERS : "))
    Q = MODULATIONORDER = int(input("ENTER MODULATION ORDER : "))
    B = BANDTYPE  = (input("ENTER BAND TYPE FDD/TDD : "))

 
    if (B == "FDD"):
        f = SCALINGFACTOR = 1
    else:
        f = SCALINGFACTOR = 0.76

    R = CODINGRATE = 0.93

    #5G NR Number of PRBs 
    print("CACULATE NUMBER OF PRBs(PHYSICAL RESOURCE BLOCKS),INFO: I/P - NUMEROLOGY(0-3) AND CHANNEL BANDWIDTH O/P - NUMBER OF PRBs ")
    NUMEROLOGY = int(input("ENTER 5G NR NUMEROLOGY(0-3) : ")) 
    SubcarrierSpacing = get_NRsubcarrier_spacing_from_numerology(NUMEROLOGY)
    channelBW = int(input("ENTER CHANNEL BANDWIDTH(MHz) : ")) #MHz
    nr_PRBs = get_nr_NumberOfPRBs(channelBW,SubcarrierSpacing) 
    N = NUMBEROFPRB = nr_PRBs

    T = SYMBOLDURATION = (0.001/14*SubcarrierSpacing)
    OH = OVERHEAD = 0.14

    print("\n\n")

    print("**********5G THROUGHPUT CALCULATION PARAMETER*************\n\n")

    print("1.NUMBEROFCC = {} \n2.NUMBEROFMIMO = {} \n3.MODULATIONORDER = {} \n4.SCALINGFACTOR = {} \n5.CODINGRATE = {} \n"
      "6.NUMBEROFPRB = {} \n7.SYMBOLDURATION = {} \n8.OVERHEAD = {} \n\n".format(NUMBEROFCC,NUMBEROFMIMO,MODULATIONORDER,SCALINGFACTOR,CODINGRATE,NUMBEROFPRB,SYMBOLDURATION,OVERHEAD))


    NR_DATATHROUGHPUT =  NUMBEROFCC *((V * Q *f * R* ((N * 12 )/T)*(1 - OH))/(1000000))

    print("5G NR DATA THROUGHPUT {:.4f} Mbps".format(NR_DATATHROUGHPUT))


if __name__ == "__main__" :
    main()