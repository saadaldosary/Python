import requests as rq , colorama, sys
colorama.init()
#defining colors
gr = colorama.Fore.GREEN
rd = colorama.Fore.RED
rst = colorama.Fore.RESET

def dirForce(url):
    #directories file 
    Dir = open('list.txt','r').read().splitlines()
    #Extentions file
    Ext = open('ext.txt','r').read().splitlines()
    
    #first forloop to brute the directories first 
    for _ in Dir:
        newUrl = f'http://{url}/{_}'
        sender = rq.get(newUrl)
        if sender.status_code == 200 or sender.status_code == 302:
            print(f'{gr} [Found] =>  {sender.url} {rst}')
            
            #in case the we didnt find matched directrories with the same name we will try to add extentions i.e php,js,sql...
        elif sender.status_code == 404:
            for x in Ext:
                UrlWithExt = newUrl+x
                sender2 = rq.get(UrlWithExt)
                if sender2.status_code == 200 or sender2.status_code == 302:
                    print(f'{gr} [Found] =>  {sender2.url} {rst}')
                else:
                    print(f'{rd} [Not Found] => {UrlWithExt} {rst}')
        else:
            print(f'{rd} [Not Found] => {newUrl} {rst}')

userUrl = sys.argv[1]
dirForce(userUrl)
