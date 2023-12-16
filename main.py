import discord
import random
from discord.ext import commands
from data.culture_data import cultures
from data.joke_data import jokes
from data.key_value import responses, learnEnglish_a1, learnEnglish_a2, learnEnglish_b1, learnEnglish_b2

# ses kanallarında ses kullanabilme kullanıcı ses odasına girdiğinde bot gelir ve ona bir şeyler söyler ve çıkar.

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

    async def choose(m):
        global random_english_word
        if content_lower.startswith('!ingilizce a1'):
            # Rastgele bir İngilizce kelime seç
            random_english_word = random.choice(list(learnEnglish_a1.keys()))
            await message.channel.send(f"İngilizce kelimen: {''.join(random_english_word)}")
            return m.author != bot.user and m.channel == message.channel and m.content.lower() in learnEnglish_a1[
                random_english_word]
            # İngilizce öğrenme kısmı
        elif content_lower.startswith('!ingilizce a2'):
            # Rastgele bir İngilizce kelime seç
            random_english_word = random.choice(list(learnEnglish_a2.keys()))
            await message.channel.send(f"İngilizce kelimen: {''.join(random_english_word)}")
            return m.author != bot.user and m.channel == message.channel and m.content.lower() in learnEnglish_a2[
                random_english_word]
        elif content_lower.startswith('!ingilizce b1'):
            # Rastgele bir İngilizce kelime seç
            random_english_word = random.choice(list(learnEnglish_b1.keys()))
            await message.channel.send(f"İngilizce kelimen: {''.join(random_english_word)}")
            return m.author != bot.user and m.channel == message.channel and m.content.lower() in learnEnglish_b1[
                random_english_word]
        elif content_lower.startswith('!ingilizce b2'):
            # Rastgele bir İngilizce kelime seç
            random_english_word = random.choice(list(learnEnglish_b2.keys()))
            await message.channel.send(f"İngilizce kelimen: {''.join(random_english_word)}")
            return m.author != bot.user and m.channel == message.channel and m.content.lower() in learnEnglish_b2[
                random_english_word]

        choose()
        try:
            user_response = await bot.wait_for('message', check=choose, timeout=15)
            await message.channel.send(f"Aferin! {user_response.author.mention}, doğru cevap.")
        except TimeoutError:
            await message.channel.send(
                f"Üzgünüm, zaman doldu. Doğru cevap: {''.join(learnEnglish_a1[random_english_word][0])}")

    for keyword, responses_list in responses.items():
        if content_lower.startswith(keyword):
            # Rastgele bir yanıt seç
            selected_response = random.choice(responses_list)
            await message.channel.send(selected_response)
            break
    if content_lower.startswith('şaka yap') | content_lower.startswith('sıkıldım') | content_lower.startswith(
            'canım sıkıldı') | content_lower.startswith('şaka') | content_lower.startswith('saka'):
        selected_joke = random.choice(jokes)
        await message.channel.send(selected_joke)
    elif content_lower.startswith('genel kültür') | content_lower.startswith('bilgi'):
        select_culture = random.choice(cultures)
        await message.channel.send(select_culture)

    await bot.process_commands(message)


bot.run(token)
