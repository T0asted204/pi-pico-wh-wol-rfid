from mfrc522 import simple_mfrc522

reader = simple_mfrc522(spi_id=0,sck=18,miso=16,mosi=19,cs=17,rst=9)

def read():
    print("Reading...Please place the card...")
    id, text = reader.read()
    print("ID: %s\nText: %s" % (id,text))

read()