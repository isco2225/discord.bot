import discord
import random
from discord.ext import commands
from data.culture_data import cultures
from data.joke_data import jokes
from data.key_value import responses
from data.key_value import learnEnglish_a1, learnEnglish_a2, learnEnglish_b1, learnEnglish_b2

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
    for keyword, learn_dict in [('!ingilizce a1', learnEnglish_a1),
                                ('!ingilizce a2', learnEnglish_a2),
                                ('!ingilizce b1', learnEnglish_b1),
                                ('!ingilizce b2', learnEnglish_b2)]:
        if content_lower.startswith(keyword):
            await check_user_response(bot, message, learn_dict)
            return

    for keyword, responses_list in responses.items():
        if content_lower.startswith(keyword):
            # Rastgele bir yanıt seç
            selected_response = random.choice(responses_list)
            await message.channel.send(selected_response)
            return

    if content_lower.startswith('şaka yap') or content_lower.startswith('sıkıldım') or content_lower.startswith('canım sıkıldı') or content_lower.startswith('şaka') or content_lower.startswith('saka'):
        selected_joke = random.choice(jokes)
        await message.channel.send(selected_joke)
    elif content_lower.startswith('genel kültür') or content_lower.startswith('bilgi'):
        select_culture = random.choice(cultures)
        await message.channel.send(select_culture)

    await bot.process_commands(message)

async def check_user_response(bot, message, learn_dict):
    random_english_word, correct_answer = get_random_word(learn_dict)
    await message.channel.send(f"İngilizce kelimen: {''.join(random_english_word)}")

    def check(m):

        return m.author != bot.user and m.channel == message.channel and m.content.lower() in correct_answer



    try:
        user_response = await bot.wait_for('message', check=check, timeout=15)

        await message.channel.send(f"Aferin lan {user_response.author.mention}, doğru cevap.")
    except TimeoutError:
        await message.channel.send(f"Üzgünüm, zaman doldu. Doğru cevap: {''.join(correct_answer[0])}")

def get_random_word(learn_dict):
    random_word = random.choice(list(learn_dict.keys()))
    return random_word, learn_dict[random_word]

bot.run(token)
