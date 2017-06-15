import requests
#coding:uft8
def goip(ip):
    url = 'http://ip.taobao.com/service/getIpInfo.php'
    try:         
        r = requests.get(url,params=ip,timeout=3)
    except requests.RequestException as e:
        print(e)
    else:
        data = r.json()
        if data[u'code'] == 0:
            return data['data']['country'],data['data']['country_id'],data['data']['ip']
        else:
            print("查询失败")
if __name__ == '__main__':
    ip={'ip':'45.77.61.249'}
    print(goip(ip))

