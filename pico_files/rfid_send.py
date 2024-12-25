import network
import time
import urequests  # For MicroPython use 'urequests' instead of 'requests'
from mfrc522 import simple_mfrc522

# Wi-Fi connection function
def connect_to_wifi(ssid, password):
    """Connect to the Wi-Fi network."""
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    print("Connecting to WiFi...", end="")
    # Wait for connection
    while not wlan.isconnected():
        print(".", end="")
        time.sleep(1)
    
    print("\nConnected to WiFi!")
    print("IP Address:", wlan.ifconfig()[0])

# RFID reading function
def read_card():
    """Read RFID card."""
    reader = simple_mfrc522(spi_id=0, sck=18, miso=16, mosi=19, cs=17, rst=9)
    print("Reading... Please place the card...")
    id, text = reader.read()
    print(f"ID: {id}\nText: {text}")
    return id, text.strip()  # Use `.strip()` to remove any trailing spaces

# Function to send POST request
def send_post_request(url):
    """Send a POST request to the specified URL."""
    try:
        print(f"Sending POST request to {url}...")
        # Adding a timeout to the request
        response = urequests.post(url, timeout=10)
        
        # Check response code and content
        print(f"Response code: {response.status_code}")
        print(f"Response content: {response.text}")  # `.text` for readable content
        response.close()
    except Exception as e:
        print(f"Error sending POST request: {e}")

# Main function
def main():
    # Wi-Fi credentials
    SSID = "ARRIS-B119-2.4"
    PASSWORD = "70DFF7A3B119"
    
    # Connect to Wi-Fi
    connect_to_wifi(SSID, PASSWORD)

    # Server URL to send the POST request
    url = "http://192.168.0.40:5000/run-script"
    
    # Define the expected text (password)
    expected_text = "your_text_here"  # The required text from the card

    while True:
        # Wait for a card to be placed on the RFID reader
        id, text = read_card()
        
        # Check if the text matches the expected password
        if text == expected_text:
            print("Valid card detected! Sending POST request...")
            send_post_request(url)
        else:
            print("Invalid card. Try again.")

# Run the main function
main()
