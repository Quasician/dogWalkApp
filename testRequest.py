import requests

def getTimes():
    headers = { 'Content-type':'applicatoin/json',
                'x-api-key': 'FVTP4xt1vA5Gb66gkIxn99O8RsfTL8KH9BsSuExG'
              }
    base_url = 'https://jeyvj7tvwe.execute-api.us-east-2.amazonaws.com/beta2'
    resource_path = 'getAllTimes'
    url = '{}/{}'.format(base_url,resource_path)
    r = requests.get(url,headers=headers)
    print(r.text)

if __name__ == '__main__':
    getTimes()
