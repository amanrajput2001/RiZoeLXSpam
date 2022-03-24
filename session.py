from telethon.sessions import StringSession
from telethon.sync import TelegramClient


print(
    """┏━━┓━━┏━━━┓━━━━━━━━┏┓━\n┃┏┓┃┏┓┃┏━┓┃━━━━━━━━┃┃━\n┃┗┛┃┗┛┗┛━┛┃┏━━┓┏━━┓┃┃━\n┃━━┛┏┓┃┏━┏┓┃┏┓┃┃┏┓┃┃┃━\n┃┃┃┃┃┃┃┗━┛┃┃┗┛┃┃┃━┫┃┗━┓\n┗┛┗┛┗┛┗━━━┛┗━━┛┗━━┛┗━━┛"""
)

print("\n • Telethon Session •")

print("\n\nEnter Your Valid Details To Continue!\n\n")

        
APP_ID = int(input("18137747"))
API_HASH = input("27ac967e8b647863db2c2fcd97b5f166")


try:
   with TelegramClient(StringSession(), APP_ID, API_HASH) as RiZoeL:
       print("\nSTRING SESSION GENERATE SUCCESSFULLY CHECK SAVED MASSAGE")
       RiZoeL.send_message("me", f"**RiZoeL X Spam Session :**\n\n`{RiZoeL.session.save()}`\n\n__Do not share this anywhere!!__")
       
except Exception as e:
    print(f"{e}") 
