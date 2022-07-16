import random
import time, requests, webbrowser
import sys as n
import time as mm
token = input('- التوكن يبعد كلبي 🌹 :  ')
ID = input('- الايدي مالتك ورده ❤️ :  ')
j = 1
b='QWERTYUIOPLKJHGFDSAZXCVBNM1234567809'
a = 'QWERTYUIOPLKJHGFDSAMNBVCXC'
n = '_'
length = 1
while True:
   u= ''.join(random.sample(b,length))
   r= ''.join(random.sample(a,length))
   k= ''.join(random.sample(b,length))
   n= ''.join(random.sample(n,length))
   AA=(k+k+k+k+k+k+k+u)
   A=(u+u+u+u+u+u+u+k)
   AAA=(u+n+u+n+k)
   AAAA=(u+n+k+n+r)
   AAAAA=(u+n+r+n+k)
   AAAAAA=(k+n+r+n+u)
   AAAAAAA=(k+n+u+n+r)
   AAAAAAAAA=(r+n+u+n+k)
   AHMad = AA , A , AAA , AAAA , AAAAA , AAAAAA , AAAAAAA , AAAAAAAAA
   user = str("".join(random.choice(AHMad)))
   url = f"https://t.me/{user}"
   req = requests.get(url)
   if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0: 
    print(f" [{j}] ✅ ☑️    >> [ {user} ]")
    try:
     req = requests.post(f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=-\n 𝗨𝗦𝗘𝗥 :  @{user} \n @K_A_Y -''')
    except NameError:
     pass
   else:
    print(f" [{j}] ⛔🚫 >> [ {user} ]")
   j += 1
