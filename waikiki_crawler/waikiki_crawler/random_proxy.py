import random
from pathlib import Path
import os

path = os.getcwd() + "\\proxy_list.txt"

def get_random_proxy():
   #p  = Path('.')
    #print(p)
    #proxy_list_path=list(p.glob('**/proxy_list.txt'))[0].resolve()

    with open(path) as f:
        proxies=f.readlines()
    proxy_ip = random.choice(proxies).strip().split(':')[0]
    print('****random proxy assigned*****')
    #print(proxy_ip)
    return proxy_ip   


