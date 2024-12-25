okay so basically right before getting started to make this whole thing work you need to first do a few things
firstly the pico-wh cannot send wol packets because it does not run linux so what we do is basically code the pico 
to act as a medium which sends a signal to your computer/server that would be running the server.py file in a cmd or termial window constantly

SERVER_SIDE
server.py 
this file uses flask to run a simple webserver which takes in post requests trasnmitted by the pico to do your bidding(sending wol packets)
if you dont know how to install flask heres their webpage link 
https://flask.palletsprojects.com/en/stable/installation/#install-flask

send_wol.py
this file does as the name suggests and is responsible for sending the wol packet to the target machine
this file also uses pygame to play a sound whenever the post request is detected (maby in the future i might make it so it only plays the sound after card is detected or packet is sent)
if you dont want it to play a sound just simply remove anything pertaining to pygame in the file

PICO_FILES/CLIENT_SIDE

/lib
this contains the coded needed for the mfrc522 to work 

read.py
this just allowes you to check what message is stored on your rfid card 

write.py
this file allows you write a message to your card which is needed for the send.py file to work as it only works if your card contains a select message (like a password)

send.py 
this file is what sends the post request to the server.py file, this file if you scroll down also allows you to 
make it so it only sends the request when an rfid card with the permitted message is read
please remember to change this message



WARNING!!!!!!!!!!!!
please remeber to go through each file and make sure they all have the custum credentials you need
your wifi ssid/server_ip/ports/music_file_location and everything else will all be different to mines,
ive included indents in the code which make it easy to read to please do that before runnign it 

also check the way i connected my mfrc522 to my pi pico because this could be different to yours 

but if you still need help check out my yt channel 
https://www.youtube.com/@T0asted204
