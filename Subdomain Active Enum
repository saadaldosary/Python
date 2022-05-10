import requests as rq
import socket

def subdomain_passive(domain):
    hed={'Host':'sonar.omnisint.io',
    'Cookie':'_ga=GA1.1.1444638025.1641710457; __stripe_mid=7e8a206c-4bd8-4ea8-995c-27847901bd54effaec; _ga_817HH8V4KD=GS1.1.1641710457.1.1.1641710911.0',
    'Sec-Ch-Ua':'Not A;Brand";v="99", "Chromium";v="96"',
    'Sec-Ch-Ua-Mobile':'?0',
    'Sec-Ch-Ua-Platform':'Windows',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site':'none',
    'Sec-Fetch-Mode':'navigate',
    'Sec-Fetch-User':'?1',
    'Sec-Fetch-Dest':'document',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'en-US,en;q=0.9'}
    saveSub = open('subdomains.txt','w')
    u = f"https://sonar.omnisint.io/subdomains/{domain}"
    sender = rq.get(url=u , headers=hed)
    for subdomain in sender.json():
        # subdomainIP = socket.gethostbyname(subdomain)
        saveSub.write(f'{subdomain}\n')

domain = input("enter domain : ")
subdomain_passive(domain)
