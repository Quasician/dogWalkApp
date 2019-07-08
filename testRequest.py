import requests
import json

def getTimes(base_url, key):
    headers = { 'Content-type':'applicatoin/json',
                'x-api-key': key
              }

    resource_path = 'getAllTimes'
    url = '{}/{}'.format(base_url,resource_path)
    r = requests.get(url,headers=headers)
    print(r.text)

def addTime(base_url, key, timestamp,pressed):
    headers = {
                'x-api-key': key
              }
    
    if pressed ==False:
        update = 'Walk is over'
    else:
        update = 'Walk is starting'

    resource_path = 'addTime'
    url = '{}/{}'.format(base_url,resource_path)
    r = requests.post(url,data=json.dumps({'Time':timestamp, 'ButtonUpdate':update}),headers=headers)
    print(r.text)

#if __name__ == '__main__':
#    getTimes()
