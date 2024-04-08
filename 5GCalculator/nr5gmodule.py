#############################################################################
### 	Author - Python Programmer                                ############
###		Description - NR 5G Parameter modules                     ############
### 	Date - 03-05-2023                                         ############
###																 ############
#############################################################################

#This is NR Parameter modules 
##https://nrarfcn.readthedocs.io/en/latest/

import nrarfcn as NR_5G 

"""####################################################################################################### 
NR Spec Reference : 33GPP TS 38.104 Table 5.4.2.1-1

Frequency range (MHz)    ΔFGlobal (kHz)      FREF-Offs (MHz)      NREF-Offs        Range of NREF(ARFCN)

    0 – 3000                 5                    0                  0                  0 – 599999
   3000 – 24250              15                  3000              600000            600000 – 2016666
  24250 – 100000             60                 24250.08           2016667           2016667 – 3279165


####################################################################################################### 
NR Spec Reference : 3GPP 38.104, table 5.1-1

Frequency range designation				Corresponding frequency range
    FR1					   				 410 MHz – 7125 MHz
    FR2(FR2-1,FR2-2)                 (24250 MHz – 52600 MHz52600 MHz – 71000 MHz )
	
####################################################################################################### 

5G NR ARFCN --> 5G NR FREQUENCY Conversion 

NREF  = 5G NR-ARFCN
FREF = 5G NR FREQUENCY
ΔFGlobal(PSS/SS stepsize) = Global frequency raster

Formula:
NREF(NR-ARFCN) = NREF-Offs +  (FREF – FREF-Offs) / ΔFGlobal 

5G NR FREQUENCY --> 5G NR ARFCN Conversion

Formula:
FREF(5G NR FREQUENCY) = FREF-Offs + ΔFGlobal (NREF – NREF-Offs)  
#Total NumberfResouce block = (Channel Bandwidth MHz/SubcarrierSpacing(Khz))12 ,1 RB = 12 scs 
#ActualNumPRBs =   Total NumberfResouce block -4(Guard band) 
######################################################################################################## """

#5G NR ARFCN --> 5G NR FREQUENCY  Conversion 
def get_nr_Freq_from_nr_Arfcn(nrarfcn):

	if(nrarfcn > 0 and nrarfcn < 3279165):
		nr_Freq = NR_5G.get_frequency(nrarfcn) 
	else :
		print("ENTER VALID NR-ARFCN (0 - 3279165)")
		nr_Freq = -1
	return nr_Freq 
	
#5G NR FREQUENCY --> 5G NR ARFCN Conversion 
def get_nr_Arfcn_from_nr_Freq(nrfreq):

	if(nrfreq > 410 and nrfreq < 71000):
		nrarfcn = NR_5G.get_nrarfcn(nrfreq) 
	else :
		nrarfcn =  -1
		print("ENTER VALID NR-FREQ (410 - 71000 MHZ)")
	return nrarfcn 
	
#5G NR FREQUENCY --> 5G NR Band list 
def get_nr_Bands_from_nr_Freq(nrfreq):

	if(nrfreq > 410 and nrfreq < 71000):
		nrBandList = NR_5G.get_bands_by_frequency(nrfreq) 
	else :
		nrBandList =  -1
		print("ENTER VALID NR-FREQ (410 - 71000 MHZ)")
	return nrBandList 
	
#5G NR ARFCN --> 5G NR Band list 
def get_nr_Bands_from_nr_Arfcn(nrarfcn):

	if(nrarfcn > 0 and nrarfcn < 3279165):
		nrBandList = NR_5G.get_bands_by_nrarfcn(nrarfcn) 
	else :
		nrBandList =  -1
		print("ENTER VALID NR-ARFCN (0 - 3279165)")
	return nrBandList 	

#5G NR Band Type FDD/TDD 
def get_duplex_mode_from_nr_Band(nrband):
	temp = nrband
	nrband = int((nrband[1:]))
	if((nrband >= 1 and nrband <= 104) or (nrband >= n257 and nrband <= n263)):
		bandType = NR_5G.get_duplex_mode(temp) 
	else :
		bandType =  -1
		print("ENTER VALID NR BAND Values (1 - 263)")
	return bandType 

#5G NR Band --> 5G NR ARFCN RANGE
def get_nr_ArfcnRange_from_nr_Band(nrband,direction):
	temp = nrband
	nrband = int((nrband[1:]))
	if((nrband >= 1 and nrband <= 104) or (nrband >= n257 and nrband <= n263)):
		nrarfcnrange = NR_5G.get_nrarfcn_range(temp) 
	else :
		nrarfcnrange =  -1
		print("ENTER VALID NR BAND Values (1 - 263)")
	return nrarfcnrange 	


#5G NR Band --> 5G NR FREQUENCY RANGE 
def get_nr_Freqrange_from_nr_Band(nrband,direction):
	temp = nrband
	nrband = int((nrband[1:]))
	if((nrband >= 1 and nrband <= 104) or (nrband >= n257 and nrband <= n263)):
		nrfreqrange = NR_5G.get_frequency_range(temp,direction) 
	else :
		nrfreqrange =  -1
		print("ENTER VALID NR BAND Values (1 - 263)")
	return nrfreqrange 

# Global Synchronisation Channel Number (GSCN) --> 5G NR FREQUENCY 
def get_nr_Freq_from_nr_GSCN(nrgscn):

	nrgscn = int(nrgscn)
	if(nrgscn >= 2 and nrgscn <= 26639):
		nrfreq = NR_5G.get_frequency_by_gscn(nrgscn) 
	else :
		nrfreq =  -1
		print("ENTER VALID NR GSCN (0 - 26639)")
	return nrfreq 

# 5G NR FREQUENCY  --> Global Synchronisation Channel Number (GSCN) 
def get_nr_GSCN_from_nr_Freq(nrfreq):

	nrfreq = int(nrfreq)
	if(nrfreq >= 410 and nrfreq <= 71000):
		nrgscn = NR_5G.get_gscn_by_frequency(nrfreq) 
	else :
		nrgscn =  -1
		print("ENTER VALID NR FREQ (410 - 71000 MHz)")
	return nrgscn 


# 5G NR Band --> Global Synchronisation Channel Number (GSCN) Range 
def get_nr_GSCNRange_from_nr_Band(nrband):

	temp = nrband
	nrband = int((nrband[1:]))
	if((nrband >= 1 and nrband <= 104) or (nrband >= n257 and nrband <= n263)):
		gscnrange = NR_5G.get_gscn_range(temp) 
	else :
		gscnrange =  -1
		print("ENTER VALID NR GSCN Range (2 - 26639)")
	return gscnrange  
	
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
