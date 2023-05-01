import discord

bot = discord.bot()

token = "MTEwMjU1MDI4NTY5MzQ5MzI2OA.GQ4ymO.ofxeF-CoJD8x3BjuNbIRu-uo4W_HuIIa08Ugc4"


@bot.event
async def on_ready():
    print("봇이 작동합니다.")
    

@bot.slash_command(guild_ids=[1089147112723333220], description = "Check bot's response latency")
async def ping(ctx):
    embed = discord.Embed(
        title="Pong!", description=f"Delay: {bot.latency} seconds", color=0xFFFFFF)
    embed.set_footer(text="Embed Footer")
    await ctx.respond(embed=embed)

bot.run(token)
