import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

def get_free():
	url='https://steamstats.cn/xi'
	headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 Edg/90.0.818.41'}
	r=requests.get(url,headers=headers)
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	soup = BeautifulSoup(r.text, "html.parser")
	tbody=soup.find('tbody')
	tr=tbody.find_all('tr')
	i=1
	text="今日喜加一"+'\n'
	for tr in tr:
		td=tr.find_all('td')
		name=td[1].string.strip().replace('\n', '').replace('\r', '')
		gametype=td[2].string.replace(" ","").replace('\n', '').replace('\r', '')
		start=td[3].string.replace(" ","").replace('\n', '').replace('\r', '')
		end=td[4].string.replace(" ","").replace('\n', '').replace('\r', '')
		time=td[5].string.replace(" ","").replace('\n', '').replace('\r', '')
		oringin=td[6].find('span').string.replace(" ","").replace('\n', '').replace('\r', '')
		aurl=td[6].find('a')['href']
		text=text+"序号："+str(i)+'\n'+"游戏名称："+name+'\n'+"DLC/game："+gametype+'\n'+"开始时间："+start+'\n'+"结束时间："+end+'\n'+"是否永久："+time+'\n'+"平台："+oringin+'\n'+"地址："+aurl+'\n'
		i=i+1
	return text


if __name__=="__main__":
    text = get_free()
    # 替换通知
    print(text)