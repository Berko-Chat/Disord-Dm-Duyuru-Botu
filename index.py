import discord
from discord.ext import commands
import os

# Gerekli intentleri ayarlıyoruz
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Bot prefix'i ve intentleri ayarlıyoruz
bot = commands.Bot(command_prefix="!", intents=intents)

# Bot hazır olduğunda bu mesajı gösterecek
@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} olarak giriş yaptı!')

# !duyuru komutunun sadece yöneticiler tarafından kullanılmasını sağlıyoruz
@bot.command()
@commands.has_permissions(administrator=True)
async def duyuru(ctx, *, mesaj):
    # Sunucudaki tüm üyeleri al
    for member in ctx.guild.members:
        # Botları atla
        if member.bot:
            continue
        try:
            # Üyeye DM gönder
            await member.send(mesaj)
            print(f'{member.name} adlı kullanıcıya mesaj gönderildi.')
        except Exception as e:
            print(f'{member.name} adlı kullanıcıya mesaj gönderilemedi. Hata: {e}')

    # Komut kullanan kişiye bildirim gönder
    await ctx.send('Duyuru tüm üyelere gönderildi!')

# Yönetici olmayan biri komutu kullanmaya çalışırsa hata mesajı
@duyuru.error
async def duyuru_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('Bu komutu kullanmak için yeterli yetkiniz yok!')

# Botunuzu başlatmak için token girin
bot.run('MTI3NTAzMzQ5Mzc1MDkzOTY2OQ.Gvz9Mm.wBwTb0RzBWoocJAQeOzNsk7uvjDzpWDr4_k2hE')
