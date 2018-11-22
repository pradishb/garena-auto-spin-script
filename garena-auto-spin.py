import sys
import os
import requests
import time
import threading
import dropbox


url = 'http://luckydraw2.gamehub.sg.garenanow.com/service/luckydraw/'
data = {'sk': 'e7bd0ab670db68f6210adcf22c6c3663fd14213854252104453c41e55962bd34',
        'region': 'SG',
        'tid': '1542870106',
        'game': 'lol',
        'version': 1542111453
        }

dbx = dropbox.Dropbox(
    'ngaX7suUUyAAAAAAAAAAKT2rkFTWb7-R-pDsJ9bcin5Myi-1pbTfDcdM4pSg2qYA')


def upload_to_dropbox(filename, data):
    print ("Attempting to upload...")
    try:
        dbx.files_upload(data, '/' + filename, mute=True)
    except Exception as err:
        print("Failed to upload")
        print(err)
    print("Finished up load.")


def send():
    response = requests.post(url, data=data)
    print(response.content)
    upload_to_dropbox(str(time.ctime()) + ".json", response.content)
    threading.Timer(5, send).start()


send()
