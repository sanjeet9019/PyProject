#############################################################################
### 	Author - Python Programmer                               ############
###		Description - WirelessAP decoder and socket(appA)		 ############
### 	Date - 06-10-2023                                        ############
###								 								 ############
#############################################################################

import json
import os
import time
import datetime
import shutil
import socket

# File paths for the two JSON files to compare
file1_path = "WirelessAP_Org.json"
file2_path = "WirelessAP.json"

# Function to load and parse a JSON file
def load_json_file(file_path):
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except json.JSONDecodeError as e:
        print(f"Invalid JSON format in {file_path}: {e}")
        return None

#Function to print current wireless AP details 
def currentWirelessAPdetails():
    print("WirelessAP details - ")
    # Open and read the JSON file
    data = load_json_file(file1_path)
    # Access and manipulate the parsed JSON data
    access_points = data["access_points"]
    # Print information about each access_point
    for access_point in access_points:
        print(f"\nssid: {access_point['ssid']}",flush=True)
        print(f"snr: {access_point['snr']}",flush=True)
        print(f"channel : {access_point['channel']}\n",flush=True)


def sendWirelessAPInfo(message):
	#Sending the different values to appB 
	# Server configuration
	HOST = '127.0.0.1'  # Use your server's IP address or '127.0.0.1' for localhost
	PORT = 12345
	# Create a UDP socket
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	# Set up the server address and port
	server_address = (HOST, PORT)
	i = 0 
	while i < 1:
		print(f"Broadcasting: {message}",flush=True)
		server_socket.sendto(message.encode(), server_address)
		i = i + 1 
		time.sleep(2)  # Send a message every 5 seconds
	server_socket.close()


def copyJsonFile():
	# Backup JSON file path (specify a new name or directory)
	backup_file = "WirelessAP_Org.json"
	# Copy the original file to the backup file
	shutil.copy("WirelessAP.json", backup_file)


def main():

	#Copy the json file 
	copyJsonFile()
	
	#Read the json file and see any changes happened in between 
	# Initial timestamp of the JSON file
	last_modified = 0
	count = 0 
	while True:
		# Get the current modification timestamp of the JSON file
		current_modified = os.path.getmtime('WirelessAP.json')

		#Check if the file has been modified since the last check
		if current_modified != last_modified:
			last_modified = current_modified
			# Convert the Unix timestamp to a datetime object
			modification_time = datetime.datetime.fromtimestamp(last_modified)
			print("Modified file values ",modification_time,flush=True)

			# Load the JSON data from both files
			data1 = load_json_file(file1_path)
			data2 = load_json_file(file2_path)
			
			print("json file data1 \n",data1,flush=True)
			print("json file data2  \n",data2,flush=True)
			
			# Check if both files were successfully loaded
			if data1 is not None and data2 is not None:
				# Compare the two json data files 
				if data1 == data2:
					print("The JSON files have the same content.",flush=True)
				else:
					print("The JSON files have different content.",flush=True)
					# Find and print the differences
					# Access and manipulate the parsed JSON data,get the list 
					access_points1 = data1["access_points"]
					access_points2 = data2["access_points"]
					count = 1 
					# Iterate through keys in dict1 and compare values with dict2
					#get the dictionary 
					for dict1,dict2 in zip(access_points1,access_points2):
						# Iterate through keys in dict1 and compare values with dict2
						for key in dict1:
							if key in dict2 and dict1[key] == dict2[key]:
								print(f"Key '{key}' has the same value in both dictionaries: {dict1[key]}",flush=True)
							elif  dict1['ssid'] != dict2['ssid'] :
								message1 = f"{dict1['ssid']} is removed from the list\n"
								message2 = f"{dict2['ssid']} is added to the list with SNR {dict2['snr']} and channel {dict2['channel']}\n" 
								message = message1 + message2
								if count == 1 :
									sendWirelessAPInfo(message)
									count = 0 
							else :
								print(f"Key '{key}' has different values:",dict1['ssid'],flush=True)
								print(f"  dict1: {dict1[key]}",flush=True)
								print(f"  dict2: {dict2.get(key, 'Key not found in dict2')}",flush=True)
								if key == "snr":
									key1 = key.upper()
									message = f"{dict1['ssid']}'s {key1} has changed from {dict1[key]} to {dict2.get(key, 'Key not found in dict2')}"
								else :
									message = f"{dict1['ssid']}'s {key} has changed from {dict1[key]} to {dict2.get(key, 'Key not found in dict2')}"
								sendWirelessAPInfo(message)
		else : #Print the current present values of WirelessAP 
				currentWirelessAPdetails()
		try :
			# Sleep for a certain interval (e.g., 5 seconds) before checking again updated json wirelessAP file
			time.sleep(5)
		except KeyboardInterrupt:
			print("\nCtrl+C detected. Do you want to continue? (y/n): ", end="")
			response = input().strip().lower()
			if response == 'n':
				print("While True  terminated.")
				# Delete the file
				os.remove(file1_path)
				break
			elif response != 'y':
				print("Invalid input. Please enter 'y' to continue or 'n' to terminate.")

if __name__ == "__main__" :
	main()
