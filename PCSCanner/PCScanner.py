#############################################################################
### 	Author - Python Programmer                               ############
###		Description - Laptop Monitoring tools 				     ############
### 	Date - 21-10-2023                                        ############
###								 								 ############
#############################################################################

import socket
import psutil
import os
import time
from ping3 import ping, verbose_ping
import speedtest
import pyshark
import platform


def MonitoringHDDSpace():
    print("\n\nMonitoring HDD Space \n")
    disk_usage = psutil.disk_usage('/')
    bytestoGB = 1024 ** 3
    print(f"Total disk space: {(disk_usage.total)/bytestoGB:.2f} GigaBytes")
    print(f"Used disk space: {(disk_usage.used)/bytestoGB:.2f} GigaBytes")
    print(f"Free disk space: {(disk_usage.free)/bytestoGB:.2f} GigaBytes")
    print(f"Disk space usage percentage: {disk_usage.percent}%")

def MonitoringFiles():
    print("\n\nMonitoring Files \n")
    folder_path = r"C:\Users\sanprasa\Desktop\python\PyProject"
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            print(f"File: {file_path}, Size: {os.path.getsize(file_path)} bytes")
            
def MonitoringNetworkActivity():
    print("\n\nMonitoring Network Activity \n")
    network_stats = psutil.net_io_counters()
    print(f"Network(NIC) card Bytes sent: {network_stats.bytes_sent}")
    print(f"Network(NIC) card Bytes received: {network_stats.bytes_recv}")
    print(f"Packets Sent: {network_stats.packets_sent} packets")
    print(f"Packets Received: {network_stats.packets_recv} packets")

# Function to Active monitor network interfaces and connections
def MonitorActivateNetworkIF():
    # Get information about network interfaces
    network_interfaces = psutil.net_if_stats()

    # Filter and print only active network interfaces
    print("\n\nMonitoring Active Network Interfaces:\n")
    for interface, stats in network_interfaces.items():
        if stats.isup:
            print(f"Interface: {interface}")
            print(f"Status: {'Up' if stats.isup else 'Down'}")
            print(f"Speed: {stats.speed} Mbps")
            print(f"MTU: {stats.mtu}")
            print("")
    # If you want to print only the names of active network interfaces:
    active_interfaces = [interface for interface, stats in network_interfaces.items() if stats.isup]
    print("Active Network Interface Names:", active_interfaces)


def MonitoringNetworkLatency():
    print("\n\nMonitoring Network Latency \n")
    host = "google.com"
    latency = ping(host)
    print(f"Network Latency to {host}: {latency} ms")

def MonitoringCPUUsage():
    print("\n\nMonitoring CPU Usage \n")
    
    # Get the CPU architecture and model
    cpu_model = platform.processor()
    print(f"CPU Model: {cpu_model}")
    
    # Get CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")
    
    
def MonitoringProcesses():
    print("\n\nMonitoring Processes \n")
    # List all running processes
    # Iterate through the running processes
    for process in psutil.process_iter(attrs=['pid', 'name']):
        try:
            process_info = process.info
            process_name = process_info['name']
            # Exclude common system service processes by name
            if (
                "svchost.exe" not in process_name
                and "services.exe" not in process_name
                and "lsass.exe" not in process_name
                and "csrss.exe" not in process_name
                and "smss.exe" not in process_name
                and "wininit.exe" not in process_name
                and "fontdrvhost.exe" not in process_name
                and "conhost.exe" not in process_name
                and "WUDFHost.exe" not in process_name
                and "msedge.exe" not in process_name
                and "IntelCpHDCPSvc.exe" not in process_name
                ):
                # Print information about non-service processes
                print(f"Process Name: {process_info['name']}")
                # print(f"Process ID (PID): {process_info['pid']}")
                # Add more process information as needed
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass  # Handle exceptions as needed

#pip install speedtest-cli
def MonitoringSpeedTest():
    print("\n\nMonitoring Network Download and Upload Speed")
    print("Calculating Download and Upload Speed ....Pls wait for 60 seconds \n")
    start_time = time.time()
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000  # Convert to Mbps - same as 1000000
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    
    # Record the end time
    end_time = time.time()
    # Calculate the elapsed time
    elapsed_time = end_time - start_time
    # # Print the elapsed time in seconds
    # print(f"Time taken: {elapsed_time:.6f} seconds")
    
    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    
    

def main():
    print(f"Laptop PC Monitoring tools \n\n")
    while True:
        MonitoringHDDSpace()
        MonitoringFiles()
        MonitoringNetworkActivity()
        MonitoringNetworkLatency()
        MonitoringSpeedTest()
        MonitoringCPUUsage()
        MonitoringProcesses()
        MonitorActivateNetworkIF()
        try :
            # Sleep for a certain interval (e.g., 5 seconds)
            time.sleep(10)
        except KeyboardInterrupt:
            print("\nCtrl+C detected. Do you want to continue? (y/n): ", end="")
            response = input().strip().lower()
            if response == 'n':
                print("While True  terminated.")
                break
            elif response != 'y':
                    print("Invalid input. Please enter 'y' to continue or 'n' to terminate.")
        
if __name__ == "__main__" :
	main()
