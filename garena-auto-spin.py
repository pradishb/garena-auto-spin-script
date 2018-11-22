import requests
import time
import threading


url = 'http://luckydraw2.gamehub.sg.garenanow.com/service/luckydraw/'
data = {'sk': 'e7bd0ab670db68f6210adcf22c6c3663fd14213854252104453c41e55962bd34',
        'region': 'SG',
        'tid': '1542870106',
        'game': 'lol',
        'version': 1542111453
        }


def send():
    response = requests.post(url, data=data)
    print(response.content)
    threading.Timer(28800, send).start()
    file = open(str(time.ctime())+".json", "w")
    file.write(response.content.decode("utf-8"))
    file.close()


send()
