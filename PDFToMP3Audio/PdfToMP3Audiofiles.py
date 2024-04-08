#############################################################################
### 	Author - Python Programmer                                ###########
###	Description - PDF to mp3 audio file                           ###########
### 	Date - 03-05-2023                                         ###########
###								                                  ###########
#############################################################################
# https://nanonets.com/blog/pypdf2-library-working-with-pdf-files-in-python/


import pyttsx3 #https://pyttsx3.readthedocs.io/en/latest/
import PyPDF2  #https://pypdf2.readthedocs.io/en/3.0.0/


def pdftomp3audioplayer():

	#Open the Technotes 5G as PDF read mode 
	with open("TechNotes_5G.pdf","rb") as Tech_5GNotes:
    #PDF Reader
		pdfreader = PyPDF2.PdfReader(Tech_5GNotes)
		#Calculate the number of Pages in the PDF 
		number_of_pages = len(pdfreader.pages)
		#Init the Text-to-speech platform/google text to speech 
		texttospeechplt = pyttsx3.init()

		#Go each page and convert each page from text to speech/audio form 
		for page_num in range(number_of_pages):
			#extracting text from the given PDF 
			textfrompdf = pdfreader.pages[page_num].extract_text() 
			# remaintextafterspace = textfrompdf.strip().replace('\n',' ')  
			print(textfrompdf.encode("utf-8"))            ## Print the content of text from PDF
			texttospeechplt.say(textfrompdf)        ## Let The Speaker Speak The Text
			texttospeechplt.save_to_file(textfrompdf,'TechNotes_5G.mp3')  ## Saving Text In a audio file 'TechNotes_5G.mp3'
			texttospeechplt.runAndWait()
			texttospeechplt.stop()

#This is the main functions 
def main():
    #This is pdf to mp3 player functions 
    pdftomp3audioplayer()

if __name__ == "__main__" :
	main()
