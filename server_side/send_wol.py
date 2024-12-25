import pygame
from wakeonlan import send_magic_packet

# Function to send Wake-on-LAN packet
def send_wol(mac_address):
    try:
        send_magic_packet(mac_address)
        print(f"WOL packet sent to {mac_address}")
    except Exception as e:
        print(f"Error sending WOL packet: {e}")

# Initialize the mixer module in pygame
pygame.mixer.init()

# Load and play the MP3 file
pygame.mixer.music.load("/home/usd/Music/example.mp3")  # Replace with the actual path to your MP3 file
pygame.mixer.music.play()

# Send Wake-on-LAN packet to a specific MAC address
mac_address = "11:22:33:44:55:66"  # Replace with the target MAC address
send_wol(mac_address)

# Wait until the song finishes
while pygame.mixer.music.get_busy():  # Keep playing until done
    pygame.time.Clock().tick(10)
