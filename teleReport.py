#!/bin/python
#from asyncio import run
#from cgi import print_arguments
#from locale import strcoll
from os import system
from platform import system as stm
try:
    from telethon.sync import TelegramClient
except ModuleNotFoundError or ImportError:
    system('pip3 install telethon')
    from telethon.sync import TelegramClient
try:
    from pyfiglet import figlet_format
except ModuleNotFoundError or ImportError:
    system('pip3 install pyfiglet')
    from pyfiglet import figlet_format
from telethon import functions, types
import tracemalloc
from time import sleep
# platform system
typeSys : str = stm()
# start tracemalloc
tracemalloc.start()
class Report:
    def __init__(self, name: str, api_id : str, api_hash : str, target : str, message : str, _id_ : list) -> bool:
        self.name = name
        self.api_id = api_id
        self.api_hash = api_hash
        self.target = target
        self.message = message
        self._id_ = _id_
    #@staticmethod
        with TelegramClient(self.name, self.api_id, self.api_hash) as client:
                result = client(functions.messages.ReportRequest(
                    peer=self.target,
                    id=self._id_,
                    reason=types.InputReportReasonSpam(),
                    message=self.message
                ))
                assert (result)
# ............... start ..............
if 'linux' in typeSys.lower() or 'mac' in typeSys.lower():
    system('clear')
else:
    system('cls')
logo : list = ['telegram', 'telegram.me', 'telegram . org', 't.me reporter', 'reporter', 'www.telegram.org']
from random import choice
banners : str = choice(logo)
bnr : str = figlet_format(banners)
for banner in bnr:
    print('\033[92m'+banner, flush=True, end='')
    sleep(0.005)
methods : str = input('\n\033[31m[~] \033[36mmethods\033[93m\t:\n\n\033[31m[*] \033[92maccount-group  \033[31m[\033[93m0\033[31m]\n\033[31m[*] \033[92mchannel-public \033[31m[\033[93m1\033[31m]\n\n\033[31m[?] \033[36mplease enter a number method \033[31m_> \033[0m')
name : str = input('\n\033[31m[?] \033[20;37mplease enter your name account \033[31m_> \033[0m')
api_hash : str = input('\n\033[31m[?] \033[20;37mmplease enter your api_hash account \033[31m_> \033[0')
api_id : str = input('\n\033[31m[?] \033[20;37mmplease enter api_id account \033[31m_> \033[0m')
sleep(1)
target : str = input('\n\033[35m[#] \033[92menter username target \033[35m_>> \033[0m')
message : str = input('\n\033[35m[#] \033[92menter link post or message \033[35m_>> \033[0m')
num : int = input('\n\033[35m[!] \033[92menter number for send report \033[35m_>> \033[20;37m')
num = int(num)
if methods == '0':
    ide = message[:].split('/')
    __id__ = ide[5]
if methods == '1':
    ide = message[:].split('/')
    __id__ = ide[4]
else:
    ide = message[:].split('/')
    if ide == ide[5]:
        ide = message[:].split('/')
        __id__ = ide[5]
    elif ide == ide[4]:
        ide = message[:].split('/')
        __id__ = ide[4]
# id list int
__id__ = int(__id__)
_id_ : list = [__id__]
# ..........
numbr : int = int(0)
print('\n'*20)
def runing():
    for i in range(num):
        try:
            Report(name, api_id, api_hash, target, message, _id_)
            print('\033[93m[+] \033[92msended \033[31m!')
        except:
            pass
if __name__ == '__main__':
    runing()