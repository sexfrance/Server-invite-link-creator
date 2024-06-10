import discord
from colorama import Fore, Style

intents = discord.Intents.default()
intents.guilds = True
bot = discord.Bot(intents=intents)

def colored_input(color, prompt):
    print(color + prompt + Style.RESET_ALL, end='')
    return input()

@bot.event
async def on_ready():
    print(Fore.LIGHTBLUE_EX + f'Connected as {bot.user}!' + Style.RESET_ALL)
    await list_servers()

async def list_servers():
    guilds = bot.guilds
    if not guilds:
        print(Fore.RED + "No server found." + Style.RESET_ALL)
        return
    print(Fore.LIGHTBLUE_EX + "Available servers:" + Style.RESET_ALL)
    for i, guild in enumerate(guilds):
        print(f"{i + 1}. {guild.name} ({guild.id}) - {guild.member_count} members")
    server_index = int(colored_input(Fore.LIGHTBLUE_EX, "Enter the server number for which you want to create an invite link:")) - 1
    if 0 <= server_index < len(guilds):
        server = guilds[server_index]
        channel = server.text_channels[0]  # Get the first text channel of the server
        invite = await channel.create_invite(max_age=0, max_uses=0)
        print(Fore.LIGHTBLUE_EX + f"Create invite for server: {server.name} ({server.id}): {invite}" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Invalid server number." + Style.RESET_ALL)

if __name__ == "__main__":
    bot_token = colored_input(Fore.CYAN, "Bot token : ")
    bot.run(bot_token)
