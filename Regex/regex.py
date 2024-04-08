import re 
salarydata = []

def regex():
	
	with open(r"test.txt","r") as file :
		content = file.read()
		string = "age"
		pattern = r"\d+"
		# phonenumber = r"\+\d{2}\s\d{6}\s\d{4}"
		phonenumber = r"\+\d+\s\d+\s\d+"
		emaild = r"\w+\.?\w+\@\w+\.\w+"
		age = rf"{string} is \d+"
		location = rf"lives in \(\w+\)"
		salary = r"\-?\$\d+\.\d+"
		startend = r"Spain"
		dot = r"\d."
		list = re.findall(startend,content)
		print("Regex list ",list)
		for data in list :
			print(data)
			# salarydata.append(data)

		# print(salarydata)
		
if __name__ == "__main__" :
	regex()