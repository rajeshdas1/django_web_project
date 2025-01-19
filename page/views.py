from django.http import HttpResponse
from django.template import loader
import socket
import platform
import os
from django.shortcuts import render


def home(request):
  template = 'index.html'
  return render(request, template, {"server_details": get_server_details()})

def get_server_details():
    # Get hostname
    hostname = socket.gethostname()
    
    # Get IP address
    ip_address = socket.gethostbyname(hostname)
    
    # Get OS details
    os_details = platform.platform()
    
    # Get CPU details
    cpu_info = platform.processor()
    
    # Get number of CPU cores
    cpu_cores = os.cpu_count()
    
    # Get system architecture
    architecture = platform.architecture()[0]
    
    return {
        "Hostname": hostname,
        "IP Address": ip_address,
        "OS": os_details,
        "CPU": cpu_info,
        "CPU Cores": cpu_cores,
        "Architecture": architecture
    }
