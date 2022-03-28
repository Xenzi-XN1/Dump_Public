#!/usr/bin/python3

import requests, json, time, sys, os

id = []


Banner = f"""
____
|  _ \ _   _ _ __ ___  _ __
| | | | | | | '_ ` _ \| '_ \  | @ Xenzi Ganz
| |_| | |_| | | | | | | |_) | | @ Guthub : /Xenzi-XN1
|____/ \__,_|_| |_| |_| .__/  | @ Team : Team Xenzi
                      |_| Public
"""
def login():
    os.system('clear')
    print(Banner)
    token = input('[!] Masukan Token: ')
    nama = requests.get("https://graph.facebook.com/me?&access_token="+token).json()["name"]
    open("token.txt", "w").write(token)
    time.sleep(3)
    dump()

def dump():
    try:
        token = open('token.txt', 'r').read()
    except IOError:
        print("\n[!] Token kadaluwarsa")
        time.sleep(3)
        login()
    try:
        data = requests.get('https://graph.facebook.com/me?access_token='+token)
        data1 = json.loads(data.text)
        nama = data1["name"]
        id = data1["id"]
        tll = data1["birthday"]
    except KeyError:
        print('\n[!] Token kadaluwarsa')
        time.sleep(3)
        login()
    except requests.exceptions.ConnectionError:
        exit('\n[!] Tidak ada koneksi internet')
    os.system('clear')
    print(Banner)
    print('[#] Username : %s' % (nama))
    print('[#] Id       : %s' % (id))
    print("\n[!] Masukan Id/Username Facebook")
    id = input('[+] Id/Username: ')
    try:
        cek=json.loads(requests.get("https://graph.facebook.com/%s?access_token=%s" % (id, token)).text)
        print("\n[+] Name : %s " % (cek['name']))
    except KeyError:
        exit("\n[!] Id/username Tidak di Temukan")
    dat=json.loads(requests.get("https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s" % (id, token)).text)["friends"]
    for x in dat['data']:
        try:
            print('* %s <-> %s ' % (x['id'], x['name']))
            open("id.txt", "a").write(x['id']+'<->'+x['name']+'\n')
            id.append(x['id']+'<->'+x['name'])
        except:continue
    print('\n[#] Seleai Tersimpan di | id.txt ')


if __name__ == '__main__':
   dump()
