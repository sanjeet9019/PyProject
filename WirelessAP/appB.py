#############################################################################
### 	Author - Python Programmer                               ############
###		Description - WirelessAP client(appB)				     ############
### 	Date - 03-05-2023                                        ############
###								 								 ############
#############################################################################

import socket

def createWirelessAPsocket():
	# Client configuration
	HOST = '127.0.0.1'  # Use your server's IP address or '127.0.0.1' for localhost
	PORT = 12345

	# Create a UDP socket for receiving messages
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	# Set up the client address and port
	client_address = (HOST, PORT)

	# Bind the socket to the client address
	client_socket.bind(client_address)

	print("AppB Socket Client created and waiting the output from appA if any \n\n",flush=True)
	return client_socket


#appB client waiting from appA  
def main():
	#Create client socket 
	client_socket = createWirelessAPsocket()
	#This while loop will wait from msg from appA about changed in wirelessAP details 
	while True:
		try :
			data, addr = client_socket.recvfrom(1024)
			message = data.decode()
			print(f"{message}",flush=True)
		except KeyboardInterrupt:
			print("\nCtrl+C detected. Do you want to continue? (y/n): ", end="")
			response = input().strip().lower()
			if response == 'n':
				print("Loop terminated.")
				break
			elif response != 'y':
				print("Invalid input. Please enter 'y' to continue or 'n' to terminate.")

if __name__ == "__main__" :
	main()
