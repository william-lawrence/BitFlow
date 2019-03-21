import pyspeedtest
import csv
import time
st = pyspeedtest.SpeedTest()

output_file = open('output.csv', 'w', newline='')
output_writer = csv.writer(output_file)

for i in range(0, 5):
    ping = get_ping()
    download = get_download_speed()
    upload = get_upload_speed()
    write_current_speed_information_to_console(ping, download, upload)
    output_writer.writerow([str(i), ping, download, upload])
    time.sleep(5)

output_file.close()

def get_ping():
    "Gets the ping in ms"
    return str(st.ping())

def get_download_speed():
    return str(st.download())

def get_upload_speed():
    return str(st.upload())

def write_current_speed_information_to_console(ping, download, upload):
    return print(str(i) + ", " + ping + ", " + download + ", " + upload)
