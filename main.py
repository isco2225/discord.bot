import discord
from discord.ext import commands
import random
from data.culture_data import cultures
from data.joke_data import jokes
from data.key_value import responses
from data.key_value import learnEnglish
#bu listelerin seviyesi olacak (kolay-orta-zor-çok zor).
#github ortak proje oluşturulacak.
#ses kanallarında ses kullanabilme kullanıcı ses odasına girdiğinde bot gelir ve ona bir şeyler söyler ve çıkar.

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)
token = 'MTE4MzQwNTU4ODYxNzYyNTY0MQ.GnExYB.xXJgOoOMbz15cM3VtABWg1BP7OnR-Dqot6uhuk'
@bot.event
async def on_ready():
    print(f'hazırız şefim {bot.user}')
@bot.event
async def on_message(message):
    # bot kendi mesajlarını dikkate almaz.
    if message.author == bot.user:
        return
    # Mesajın içeriğini küçük harfe çevirerek kontrol ediyoruz
    content_lower = message.content.lower()

    # İngilizce öğrenme kısmı
    if content_lower.startswith('!ingilizce'):
        # Rastgele bir İngilizce kelime seç
        random_english_word = random.choice(list(learnEnglish.keys()))
        await message.channel.send(f"İngilizce kelimen: {''.join(random_english_word)}")
#2225
        def check(m):
            # Doğru cevabın kontrolü
            return m.author != bot.user and m.channel == message.channel and m.content.lower() in learnEnglish[
                random_english_word]
        try:
            user_response = await bot.wait_for('message', check=check, timeout=15)
            await message.channel.send(f"Aferin! {user_response.author.mention}, doğru cevap.")
        except TimeoutError:
            await message.channel.send(
                f"Üzgünüm, zaman doldu. Doğru cevap: {''.join(learnEnglish[random_english_word][0])}")

    for keyword, responses_list in responses.items():
        if content_lower.startswith(keyword):
            # Rastgele bir yanıt seç
            selected_response = random.choice(responses_list)
            await message.channel.send(selected_response)
            break
    if content_lower.startswith('şaka yap') | content_lower.startswith('sıkıldım') | content_lower.startswith('canım sıkıldı') | content_lower.startswith('şaka') | content_lower.startswith('saka'):
        selected_joke = random.choice(jokes)
        await message.channel.send(selected_joke)
    elif content_lower.startswith('genel kültür') | content_lower.startswith('bilgi'):
        select_culture = random.choice(cultures)
        await message.channel.send(select_culture)


    await bot.process_commands(message)

bot.run(token)


