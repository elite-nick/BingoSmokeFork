import random
import time
import telebot
from background import keep_alive
import io
import os

api_key = os.environ['API_KEY']
yuri_id = os.environ['YURI']
mine_id = os.environ['MINE']
nikita_id = os.environ['NIKITA']
serega_id = os.environ['SEREGA']
misha_id = os.environ['MISHA']
group_id = os.environ['GROUP_ID']

bot = telebot.TeleBot(api_key)

cat_commands = ['жидкий кот', 'жидокот']
cat2o = {
    'head':
    'CAACAgIAAxkBAAEBe9JlLSQ7DZkard_-QJ5he7Vq1vyeBgACQQADKA9qFPDp0yN1HEZhMAQ',
    'body':
    'CAACAgIAAxkBAAEBe9RlLSQ9DONExbA87UHp9EkLA9Jg6AACNQADKA9qFFJR2Ut3d7AFMAQ',
    'tail':
    'CAACAgIAAxkBAAEBe9ZlLSQ_C-Ln9YpkZjUH5z7iyKKpqQACPwADKA9qFGqgL_9ebv15MAQ'
}

smoke_commands = [
    'курить', 'smoke', 'перекур', '/smoke', '🚬', 'перекур парни',
    '/smoke@bingosmoke_bot', 'дудеть', 'смоукать', 'курякать', 'куритя',
    'употреблять никотин', 'употреблять никитин',
    'пускать кол ечки серого дыма в этот хмурый стальной осенний день',
    'пускать колечки серого дыма в этот хмурый стальной осенний день',
    'курякекать', 'курититя', 'проебывать работу', 'керить', 'дудонить',
    'курьить', 'куренькать', 'дуденить', 'сосать дым',
    'получать удовольствие путем вдыхания продуктов испарения через электронное устройство для нагрева жидкости',
    'сосать', 'курить хочется', 'проёбывать работу', 'дуть', 'дымить',
    'бигсмоукать', 'smoking', "smoykat'", 'зайти под смоком в логово рошана',
    'куритькать', 'курилить', 'курить парни', 'куриииить', 'куриить',
    'курииить', 'дышать воздухом', "kyrit'", 'курить умоляю', 'умоляю курить',
    'совещание в курилке', 'курить бамбук', 'курияки', 'сосать чилееен',
    'го курить', 'сосать член', 'курить нахой', 'rehbnm', 'курим', 'согласую',
    'согласовано', 'парить', 'сосать дым  в направлении дома', 'дышать паром',
    'курить курить курить', 'жестко давить испарик копчением',
    'стрелять дудки', 'дудонькать', 'обсасывать мундштук на морозе',
    'чую пора курить', 'сукин ты сын, я в деле', 'куритьь', 'курить чилееен',
    'жрать', 'куриц'
]
no_commands = [
    'некурить', 'не курить', 'пропущу', 'пропусчу', 'вкс', 'на вкс',
    'пропустит', 'он пропустит', 'не пойду', 'проебывать курение',
    'пропустить', 'отправить на доработку', 'не согласую', 'несогласовано',
    'кушаю', 'кушает', 'обед', 'обэд', 'хаваю', 'созвон', 'вкс,  5 минут',
    'он на вкс', 'воздержание от курения', 'вкс,  10 минут', 'вкс,  15 минут'
]
home_commands = [
    'домой', 'дома', 'сегодня дома', 'сосать дым в направлении дома', 'ухожу',
    'лететь на курильной тяге домой', 'ушел домой', 'курить дома',
    'дома курить', 'сосать дома'
]
waiting_commands = [
    '5 сек', '5 сек гомосек', 'жду', 'выхажу околофутболить',
    'выхожу околофутболить', 'на улице', 'околофутбола', 'околофутбол',
    'около футбола', 'околофутболю'
]
catchup_commands = ['догоню', 'бегу']
woman_commands = ['стрелять дудки', 'стрелять']

auf_commands = ['ауф', '/auf', 'auf', '/ауф']
aue_commands = ['/aue', 'ауе', '/ауе', '/загадка']

ultimate = [
    'курить жестко хочу', 'курить хочу жестко', 'жестко курить хочу',
    'хочу жестко курить', 'хочу курить жестко', 'курить хочу пиздец',
    'пиздец курить хочется', 'пиздец курить хочу', 'курить пиздец хочу'
]
strong = ['жестко курить', 'курить жестко']

helps = ['help', '/help', 'хэлп', 'хелп']
all_commands = smoke_commands + auf_commands + aue_commands + ultimate + strong + no_commands

stickersYu = []
stickersSl = []
stickersCommon = []
stickersNo = []
stickersHome = []
stickersWait = []
stickersCatchup = []
query_one = ''

auf_replies = []
aue_replies = []
poop_replies = ['пися', 'попа', 'какащки', 'чилееен']
hook = [
    '@Azaz31', '@vosalaev', '@goodzonix', '@Bogdabvas', '@Laco99',
    '@ZharinoffM', '@IrinaKuz26', '@Lalalarew', '@devil_only9898'
]
ban_list = []

with io.open('inputs.txt', 'r', encoding='UTF-8') as f:
  for line in f.readlines():
    if line[0] == 'y':
      stickersYu.append(line.strip().split(' ')[1])
    elif line[0] == 's':
      stickersSl.append(line.strip().split(' ')[1])
    elif line[0] == 'a':
      auf_replies.append(line[2:])
    elif line[0] == 'r':
      aue_replies.append(line[2:].replace('Ответ', '\nОтвет'))
    elif line[0] == 'e':
      stickersCommon.append(line.strip().split(' ')[1])
    elif line[0] == 'n':
      stickersNo.append(line.strip().split(' ')[1])
    elif line[0] == 'h':
      stickersHome.append(line.strip().split(' ')[1])
    elif line[0] == 'w':
      stickersWait.append(line.strip().split(' ')[1])
    elif line[0] == 'c':
      stickersCatchup.append(line.strip().split(' ')[1])

with io.open('queries.txt', 'r', encoding='UTF-8') as f:
  for line in f.readlines():
    if line[0] == '1':
      query_one += line[2:]

with io.open('ban_file.txt', 'r', encoding='UTF-8') as f:
  for line in f.readlines():
      ban_list += str(line)

stickers = {mine_id: stickersSl, yuri_id: stickersYu}
replies = {'aue': aue_replies, 'auf': auf_replies, 'poop': poop_replies}


def send_sticker(chat_id, user_id, msg_id):
  try:
    bot.send_sticker(chat_id,
                     random.choice(stickers.get(user_id)),
                     reply_to_message_id=msg_id,
                     disable_notification=True)
  except TypeError:
    bot.send_sticker(chat_id,
                     random.choice(stickersCommon),
                     reply_to_message_id=msg_id,
                     disable_notification=True)


def send_message(msg_type, chat_id, msg_id):
  bot.send_message(chat_id,
                   text=random.choice(replies.get(msg_type)),
                   reply_to_message_id=msg_id,
                   disable_notification=True)


def get_photo(msg):
  photo = msg.photo[-1]
  file_id = photo.file_id
  file = bot.get_file(file_id)
  downloaded_file = bot.download_file(file.file_path)
  with open("downloaded_photo.jpg", "wb") as file:
    file.write(downloaded_file)


@bot.message_handler(content_types=['text', 'photo'])
def message_replier(message):
  current_time = int(time.time())
  msg_time = message.date
  user_id = str(message.from_user.id)

  if current_time - msg_time < 120 and message.content_type == 'text':
    if 'бан' in message.text and user_id == mine_id:
      ban = message.text.replace('бан ', '')
      if ban.lower() == 'юра':
        ban_list.append(yuri_id)
      elif ban.lower() == 'слава':
        ban_list.append(mine_id)
      elif ban.lower() == 'никита':
        ban_list.append(nikita_id)
      elif ban.lower() in ['серега', 'серёга']:
        ban_list.append(serega_id)
      elif ban.lower() == 'миша':
        ban_list.append(misha_id)
      with io.open('ban_file.txt', 'w', encoding='UTF-8') as f:
        for ban_id in ban_list:
          f.write(str(ban_id) + '\n')
      bot.send_message(mine_id, text=f'{ban} ЗАБАНЕН')
      return
    if 'прости' in message.text and user_id == mine_id:
      ban = message.text.replace('прости ', '')
      if ban.lower() == 'юра':
        ban_list.remove(yuri_id)
      elif ban.lower() == 'слава':
        ban_list.remove(mine_id)
      elif ban.lower() == 'никита':
        ban_list.remove(nikita_id)
      elif ban.lower() in ['серега', 'серёга']:
        ban_list.remove(serega_id)
      elif ban.lower() == 'миша':
        ban_list.remove(misha_id)
      with io.open('ban_file.txt', 'w', encoding='UTF-8') as f:
        for ban_id in ban_list:
          f.write(str(ban_id) + '\n')
      bot.send_message(mine_id, text=f'{ban} разбанен')
      return
    if message.text.lower() in all_commands and random.randint(0, 100) >= 95:
      send_message('poop', message.chat.id, message.message_id)
      return
    if 'бот отправь' in message.text and user_id == mine_id:
      bot.send_message(group_id, text=message.text.replace('бот отправь', ''))

    if message.text.lower() == 'отправь стикер' and user_id == mine_id:
      bot.send_sticker(group_id,
                       random.choice(stickersCommon),
                       disable_notification=True)
    if user_id in ban_list:
      bot.send_message(message.chat.id,
                       text='ТЫ ЗАБАНЕН',
                       reply_to_message_id=message.message_id,
                       disable_notification=True)
      return
    if message.text.lower(
    ) in smoke_commands or 'согласование' in message.text.lower():
      send_sticker(chat_id=message.chat.id,
                   user_id=user_id,
                   msg_id=message.message_id)

    elif message.text.lower() in helps:
      all_commands_str = '\n'.join(smoke_commands)
      bot.send_message(message.chat.id,
                       text=f'Список простых команд:\n{all_commands_str}',
                       reply_to_message_id=message.message_id,
                       disable_notification=True)

    elif message.text.lower() in cat_commands:
      if user_id == mine_id:
        k = 0
      elif user_id == yuri_id:
        k = 6
      else:
        k = random.randint(0, 5)
      bot.send_sticker(message.chat.id,
                       cat2o.get('head'),
                       reply_to_message_id=message.message_id,
                       disable_notification=True)
      for i in range(k):
        bot.send_sticker(message.chat.id,
                         cat2o.get('body'),
                         disable_notification=True)
      bot.send_sticker(message.chat.id,
                       cat2o.get('tail'),
                       disable_notification=True)

    elif message.text.lower() in aue_commands:
      send_message('aue', message.chat.id, message.message_id)

    elif message.text.lower() in auf_commands:
      send_message('auf', message.chat.id, message.message_id)

    elif message.text.lower() in ultimate:
      for k in range(4):
        bot.send_sticker(message.chat.id,
                         random.choice(stickersCommon + stickersYu +
                                       stickersSl),
                         reply_to_message_id=message.message_id,
                         disable_notification=True)
    elif message.text.lower() in strong:
      for k in range(2):
        bot.send_sticker(message.chat.id,
                         random.choice(stickersCommon + stickersYu +
                                       stickersSl),
                         reply_to_message_id=message.message_id,
                         disable_notification=True)
    elif message.text.lower() == 'пудж' or message.text.lower() == 'перепудж':
      if random.randint(0, 100) >= 98:
        pudge = 'пудж хукает ' + '@' + message.from_user.username + ' И НАЧИНАЕТ ЕГО ЖРАТЬ.\nТеперь ты не можешь идти курить потому что тебя СОЖРАЛИ'
      else:
        pudge = 'пудж хукает ' + random.choice(
            hook
        ) + ' авхазвахвхах чинчопа чинчопа\nТеперь ты открываешь дверь пропуском'
      bot.send_message(message.chat.id,
                       text=pudge,
                       reply_to_message_id=message.message_id,
                       disable_notification=True)
      bot.send_video(
          message.chat.id,
          'https://tenor.com/ru/view/pudge-пудж-виляетпопой-виляет-дота-gif-27008808',
          None,
          disable_notification=True)

    elif message.text.lower() in no_commands:
      bot.send_sticker(message.chat.id,
                       random.choice(stickersNo),
                       reply_to_message_id=message.message_id,
                       disable_notification=True)
    elif message.text.lower() in home_commands:
      bot.send_sticker(message.chat.id,
                       random.choice(stickersHome),
                       reply_to_message_id=message.message_id,
                       disable_notification=True)
    elif message.text.lower() in waiting_commands:
      bot.send_sticker(message.chat.id,
                       random.choice(stickersWait),
                       reply_to_message_id=message.message_id,
                       disable_notification=True)
    elif message.text.lower() in catchup_commands:
      bot.send_sticker(message.chat.id,
                       random.choice(stickersCatchup),
                       reply_to_message_id=message.message_id,
                       disable_notification=True)


keep_alive()
#bot.polling(none_stop=True, interval=0)
bot.infinity_polling()
