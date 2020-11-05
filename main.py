import discord
from colorama import Fore

token = "Your token here"

lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLACK_EX
class TokenChecker(discord.Client):
  async def on_connect(self): 
      print(f"""{lb}Username  {lr}: {client.user.name}
{lb}Discriminator  {lr}: #{client.user.discriminator}
{lb}ID  {lr}: {client.user.id}
{lb}Email  {lr}: {client.user.email}
{lb}Guilds  {lr}: {len(client.guilds)}
{lb}Friends  {lr}: {len(client.user.friends)}
{lb}Avatar  {lr}: {client.user.avatar_url}
{lb}Creation Date  {lr}: {client.user.created_at}
{lb}2FA  {lr}: {client.user.mfa_enabled}
{lb}Verified? {lr}: {client.user.verified}
{lb}Nitro? {lr}: {client.user.premium_type}
      """)
      for guild in client.guilds:
        file = open(f"Guilds.txt", 'a')
        file.write(f"{guild.name}  ] | [  {guild.id}\n") 
      for user in client.user.friends:
        file = open(f"Friends.txt", 'a')
        file.write(f"{user.name}#{user.discriminator}  ] | [  {user.id}\n")



client = TokenChecker()
client.run(token, bot = False)
