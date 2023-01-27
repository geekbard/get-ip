from requests import get
import socket
# ------------------------- #

# Get local ip address:
local_ip = socket.gethostbyname(socket.gethostname())
print(f"Private address: {local_ip}")

# Get public ip address: 
public_ip = get("https://api.ipify.org").text
print(f"Public address: {public_ip}")
