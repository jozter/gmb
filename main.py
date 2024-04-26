from backround import keep_alive
import telebot
from telebot import types

bot = telebot.TeleBot('6353092152:AAFGp49Tarh49CO3pzkHC50JYiMzHdexBqY')

user_id_file = open("user_id_file.txt", "r")
users_id = set()
for line in user_id_file.readlines():
  users_id.add(line.strip())
user_id_file.close()

# Часто задаваемые вопросы - наполнение
faq = ['Кто мы такие?', 
       'Чем мы занимаемся?', 
       'Мы в соц. сетях',
      'Присоединяйся к движению!']
faq_answers = ['''Привет, мы - Экологический клуб «Green MISIS»\!🪴
Наша команда с 2021 года работает над повышением осведомленности сотрудников и студентов в вопросах экологии и помогает им прийти к экологичному образу жизни, а университету — к устойчивому развитию\.''',
               '''Мы реализуем немало важных «зеленых» проектов:
• цикл лекций «ЭКОшкола»
• РСО на территории Точки кипения – Коммуны
• акции по сбору вторсырья «Из офиса — на переработку» 
• своп\-вечеринки «СВОП: подари одежде новую жизнь» 
• буккроссинг
С 2022 года проводим ежегодно экологический фестиваль «ЭКОфест»\!🌱 ''',
              '''[*Мы в ВК*](https://vk.com/greenmisis)
[*Мы в Telegram*](https://t.me/greenmisis)''',
    '''Присоединяйся к движению\!🪴
Понимаешь, что хочешь как\-то повлиять на будущее планеты, но не знаешь как\? Присоединяйся к нам, где мы вместе движемся к лучшему будущему\. Мы рады новым участникам\!
Наша цель — вдохновить людей, чтобы они изменили себя, а дальше — целый мир\!
Подписывайся на Green MISIS в социальных сетях, чтобы узнавать больше об экологии и не пропускать важные мероприятия\!
[*Вступление в Green MISIS*](https://docs.google.com/forms/d/e/1FAIpQLSfhh8TeQe4y_xUCEXUzJHtuHJihPIl6PzEmBfdf9inqh8cWmg/viewform)''']
faq_dict = {}
for i in range(len(faq)):
  faq_dict[faq[i]] = faq_answers[i]

# Узнать о правилах подготовки вторсырья 
sec_mats = ['Стекло', 'Макулатура ', 'Пластик']
sm_answers = ['''*Стекло*\n
- Ополосните от остатков жидкости
- Снимите крышки\n''', '''*Макулатура*\n
- Проверьте бумагу на наличие плёнки (надорвите край, если пленка не тянется и не видна,то можно сдавать) 
- Удалите металлические пружины и пластиковые включения
- Уберите скотч\n
*Не принимаем*\n
- Жирная/грязная бумага 
- Чеки (сдаются отдельно)
- Тетрапак (сдается отдельно)
- Бумажные стаканы/посуда 
- Бумажные салфетки/полотенца\n
''', '''*Пластик*\n
- Ополосните от остатков пищи и химии
- Снимите термоусадочную упаковку (плотно прилегает по форме тары)
- Компактно сложите
- Снимите крышки (сдаются отдельно для проекта «Добрые крышечки»)\n
*Не принимаем*\n
- Пластик с маркировкой 7 Other\n''']

sm_dict = {}
for i in range(len(sec_mats)):
  sm_dict[sec_mats[i]] = sm_answers[i]

#Советы по экологической гигиене
advice = '''Начните вести zero-waste образ жизни ♻️

♻️ Zero-waste –  это набор принципов, направленных на сведение к минимальному количеству мусора посредством многоразового использования предметов и вещей. Проще говоря, все материалы используются эффективно и ничего не выбрасывается.

♻️ Постепенно вводите сортировку в свою жизнь.
В качестве эксперимента попробуйте собрать всё потенциальное вторсырье за несколько дней в один пакет, а потом сверьте содержимое с табличкой принимаемых маркировок экоцентром.

♻️ Избегайте «биоразлагаемых» пакетов
В современном мире существует два типа «биоразлагаемых» пакетов
Оксоразлагаемые
Это пакеты из обычного пластика, покрытого сверху специальным раствором, ускоряющим процесс окисления и распада полимера под действием солнечного света, тепла и кислорода, содержащегося в воздухе. Чаще всего применяется добавка, известная под названием d2w, из-за которой упаковку невозможно переработать. Гидробиоразлагаемые.
Это более продвинутая технология, основанная на использовании специальных полимеров, созданных из природных компонентов. Наиболее распространены упаковочные материалы из крахмала, реже — из сои, пшеницы, сахарного тростника.
На производство этой упаковки идут пищевые продукты, что в условиях средней жизни пакета в 12–16 минут просто нерационально.

♻️ Решающим фактом против является то, что  в России не существует механизмов правильной утилизации этих видов отходов. В итоге, пакеты попадают на свалки, где разлагаются на микропластик и метан.'''

communa_containers = ['com_glass', 'com_plastic', 'com_macul', 'com_bat', 'com_tops', 'com_stac']
communa_containers_dict = {'com_glass':'Стекло', 'com_plastic': 'Пластик', 'com_macul':'Макулатура', 'com_bat':'Батарейки', 'com_tops':'Крышки', 'com_stac':'Стаканчики'}

@bot.message_handler(commands=['start', 'help'])
def start(message):
  global users_id
  user_id = message.chat.id
  start_markup = types.InlineKeyboardMarkup(row_width=1)
  if str(user_id) not in users_id:
    user_id_file = open("user_id_file.txt",  "a")
    user_id_file.write(str(user_id) + '\n')
    users_id.add(str(user_id))
    user_id_file.close()
  faq_but = types.InlineKeyboardButton("Узнать об экоклубе Green MISIS",
                                       callback_data='faq')
  ask_but = types.InlineKeyboardButton('Остались вопросы?',
                                       callback_data='ask')
  bin_but = types.InlineKeyboardButton('Контейнер заполнен',
                                       callback_data='bin')
  #gig_but = types.InlineKeyboardButton('Х привычек, которые сделают тебя eco-friendly',callback_data='gig')
  sm_but = types.InlineKeyboardButton('Подготовка вторсырья от А до Я',
                                       callback_data='sm')
  start_markup.add(bin_but, sm_but,  faq_but, ask_but)
  bot.send_message(message.chat.id,
                   ''' Привет, это бот *Green MISIS!* 
Здесь ты можешь сообщить о заполненном контейнере, приобщиться к сортировке вторсырья, а также познакомиться с нашим студенческим объединением.''',
                   reply_markup=start_markup, parse_mode="Markdown")


@bot.callback_query_handler(func=lambda call: call.data == 'faq')
def get_func_faq(call):
  global faq
  faq_markup = types.InlineKeyboardMarkup(row_width=1)
  faq_buts= []
  for i in range(len(faq)):
    faq_buts.append(types.InlineKeyboardButton(faq[i], callback_data=faq[i]))
    faq_markup.add(faq_buts[i])
  bot.send_message(call.message.chat.id, "Что вы хотите узнать?", reply_markup=faq_markup)
  return

@bot.callback_query_handler(func=lambda call: call.data in faq)
def get_func_q(call):
  #bot.send_message(call.message.chat.id, call.data)

  if call.data == 'Кто мы такие?':
    bot.send_message(call.message.chat.id, '''Привет, мы - Экологический клуб «Green MISIS»!\n Наша команда с 2021 года работает над повышением осведомленности сотрудников и студентов в вопросах экологии и помогает им прийти к экологичному образу жизни, а университету — к устойчивому развитию.''')
  else:
    bot.send_message(call.message.chat.id, faq_dict[call.data], parse_mode='MarkdownV2')
  return

@bot.callback_query_handler(func=lambda call: call.data == 'gig')
def get_func_gig(call):
  global advice
  bot.send_message(call.message.chat.id, advice)
  return

@bot.callback_query_handler(func=lambda call: call.data == 'sm')
def get_func_sm(call):
  global sec_mats
  sm_markup = types.InlineKeyboardMarkup(row_width=1)
  sm_buts= []
  for i in range(len(sec_mats)):
    sm_buts.append(types.InlineKeyboardButton(sec_mats[i], callback_data=sec_mats[i]))
    sm_markup.add(sm_buts[i])
  bot.send_message(call.message.chat.id, 'Основное правило: _вторсырье должно быть чистым и сухим!_\nКакой вид вторсырья вас интересует?', reply_markup=sm_markup, parse_mode="Markdown")
  return

@bot.callback_query_handler(func=lambda call: call.data in sec_mats)
def get_func_sm1(call):
  bot.send_message(call.message.chat.id, (sm_dict[call.data]), parse_mode="Markdown")

  call.data = ''

@bot.callback_query_handler(func=lambda call: call.data == 'ask')
def get_func_ask(call):
  ask_markup = types.InlineKeyboardMarkup()
  call.data = 'new_q'
  bot.send_message(call.message.chat.id,
                   "Напишите нам вопрос и мы ответим на него",
                   reply_markup=ask_markup)

  @bot.message_handler(content_types=['text'])
  def get_message(message):
    global new_quest
    q_person_id_file = open("q_person_id.txt", "r")
    q_person_id = q_person_id_file.readlines()
    new_quest = message.text
    this_user_username = message.from_user.username
    bot.send_message(
      q_person_id[-1],
      f'Вопрос от пользователя  @{this_user_username}: ' + str(new_quest))
    bot.send_message(
      call.message.chat.id,
      'Спасибо за вопрос. Активисты экололгического клуба Green MISIS скоро ответят вам.🌿'
    )
    q_person_id_file.close()
  return


@bot.callback_query_handler(func=lambda call: call.data == 'bin')
def get_func_bin(call):
  bin_markup = types.InlineKeyboardMarkup(row_width=1)
  g1_but = types.InlineKeyboardButton('Горняк-1', callback_data='g1')
  b_but = types.InlineKeyboardButton('Корпус Б', callback_data='campus_b')
  comm_but = types.InlineKeyboardButton('Точка кипения Коммуна', callback_data='communa')
  m3_but = types.InlineKeyboardButton('Металлург-3', callback_data='m3')
  media_center_but = types.InlineKeyboardButton('Медиацентр', callback_data='mc')
  bin_markup.add(comm_but, b_but, g1_but, m3_but, media_center_but)
  bot.send_message(call.message.chat.id, "Выбери местоположение контейнера", reply_markup=bin_markup)

@bot.callback_query_handler(func=lambda call: call.data == 'communa')
def get_func_communa_containers(call):
  communa_markup = types.InlineKeyboardMarkup(row_width=1)
  glass_but = types.InlineKeyboardButton('Стекло', callback_data='com_glass')
  plastic_but = types.InlineKeyboardButton('Пластик', callback_data='com_plastic')
  paper_but = types.InlineKeyboardButton('Макулатура', callback_data='com_macul')
  batary_but = types.InlineKeyboardButton('Батарейки', callback_data='com_bat')
  tops_but = types.InlineKeyboardButton('Крышки', callback_data='com_tops')
  stacs_but = types.InlineKeyboardButton('Стаканчики', callback_data='com_stac')
  communa_markup.add(glass_but, plastic_but, paper_but, batary_but, tops_but, stacs_but)
  bot.send_message(call.message.chat.id, 'Выбери контейнер', reply_markup=communa_markup)

@bot.callback_query_handler(func=lambda call: call.data == 'g1')
def get_func_g1_containers(call):
  g1_markup = types.InlineKeyboardMarkup(row_width=1)
  t_but = types.InlineKeyboardButton('Крышки', callback_data='g1_tops')
  b_but = types.InlineKeyboardButton('Батарейки', callback_data='g1_bats')
  g1_markup.add(t_but, b_but)
  bot.send_message(call.message.chat.id, "Выбери контейнер", reply_markup=g1_markup)
  
@bot.callback_query_handler(func=lambda call: call.data == 'm3')
def get_func_m3_containers(call):
  m3_markup = types.InlineKeyboardMarkup(row_width=1)
  t_but = types.InlineKeyboardButton('Крышки', callback_data='m3_tops')
  b_but = types.InlineKeyboardButton('Батарейки', callback_data='m3_bats')
  m3_markup.add(t_but, b_but)
  bot.send_message(call.message.chat.id, "Выбери контейнер", reply_markup=m3_markup)

@bot.callback_query_handler(func=lambda call: call.data == 'campus_b')
def get_func_campus_b_containers(call):
  campus_b_markup = types.InlineKeyboardMarkup(row_width=1)
  t_but = types.InlineKeyboardButton('Крышки', callback_data='campus_b_tops')
  campus_b_markup.add(t_but)
  bot.send_message(call.message.chat.id, "Выбери контейнер", reply_markup=campus_b_markup)

@bot.callback_query_handler(func=lambda call: call.data == 'mc')
def get_func_mediacenter_containers(call):
  mediacenter_markup = types.InlineKeyboardMarkup(row_width=1)
  t_but = types.InlineKeyboardButton('Стаканчики', callback_data='mc_tops')
  mediacenter_markup.add(t_but)
  bot.send_message(call.message.chat.id, "Выбери контейнер", reply_markup=mediacenter_markup)

@bot.callback_query_handler(
  func=lambda call: call.data in communa_containers or call.data in  ['g1_tops', 'g1_bats', 'm3_tops', 'm3_bats', 'campus_b_tops', 'mc_tops'])
def get_func_all_bin(call):
  if call.data in communa_containers:
    d_bin_person_id_file = open("d_bin_person_id.txt", "r")
    d_bin_person_id = d_bin_person_id_file.readlines()
    bot.send_message(d_bin_person_id[-1], "В Точке кипения Коммуна заполнен контейнер " + communa_containers_dict[call.data])
    bot.send_message(call.message.chat.id, "Спасибо! Мы освободим его в ближайшее время")
    d_bin_person_id_file.close()
  elif call.data == 'campus_b_tops':
    b_bin_person_id_file = open("b_bin_person_id.txt", "r")
    b_bin_person_id = b_bin_person_id_file.readlines()
    bot.send_message(b_bin_person_id[-1], "Контейнер с крышечками в корпусе Б заполнен")
    bot.send_message(call.message.chat.id, "Спасибо! Мы освободим его в ближайшее время")
    b_bin_person_id_file.close()
  elif call.data == 'g1_tops':
    g1_bin_person_id_file = open("g1_bin_person_id.txt", "r")
    g1_bin_person_id = g1_bin_person_id_file.readlines()            
    bot.send_message(g1_bin_person_id[-1], "Контейнер с крышечками в Г1 заполнен")
    bot.send_message(call.message.chat.id, "Спасибо! Мы освободим его в ближайшее время")
  elif call.data == 'g1_bats':
    g1_bin_person_id_file = open("g1_bin_person_id.txt", "r")
    g1_bin_person_id = g1_bin_person_id_file.readlines()            
    bot.send_message(g1_bin_person_id[-1], "Контейнер с батарейками в Г1 заполнен")
    bot.send_message(call.message.chat.id, "Спасибо! Мы освободим его в ближайшее время")
    g1_bin_person_id_file.close()
  elif call.data == 'mc_tops':
    mc_bin_person_id_file = open("d_bin_person_id.txt", "r")
    mc_bin_person_id = mc_bin_person_id_file.readlines()
    bot.send_message(mc_bin_person_id[-1], "Контейнер в медиаценре заполнен")
    bot.send_message(call.message.chat.id, "Спасибо! Мы освободим его в ближайшее время")
    mc_bin_person_id_file.close()
  elif call.data == 'm3_tops':
    m_bin_person_id_file = open("m_bin_person_id.txt", "r")
    m_bin_person_id = m_bin_person_id_file.readlines()
    bot.send_message(m_bin_person_id[-1], "Контейнер с крышечками в М3 заполнен")
    bot.send_message(call.message.chat.id, "Спасибо! Мы освободим его в ближайшее время")
    m_bin_person_id_file.close()
  elif call.data == 'm3_bats':
    m_bin_person_id_file = open("mc_bin_person_id.txt", "r")
    m_bin_person_id = m_bin_person_id_file.readlines()
    bot.send_message(m_bin_person_id[-1], "Контейнер в М3 с батарейками заполнен")
    bot.send_message(call.message.chat.id, "Спасибо! Мы освободим его в ближайшее время")
    m_bin_person_id_file.close()

  else:
    bot.send_message(call.message.chat.id, "Я тебя не понимаю")
    
  call.data = ''


@bot.message_handler(commands=['change_person'])
def change_person(message):
  secret_markup = types.InlineKeyboardMarkup(row_width=1)
  q_but = types.InlineKeyboardButton(
    'человек, ответственный за ответы на вопросы',
    callback_data='change_person_q')
  b_but = types.InlineKeyboardButton(
    'человек, ответственный за контейнер с крышечками в Б',
    callback_data='change_person_b')
  d_but = types.InlineKeyboardButton(
    'человек, ответственный за контейнер с крышечками в Точке кипения Коммуна',
    callback_data='change_person_d')
  m_but = types.InlineKeyboardButton(
    'человек, ответственный за контейнер с крышечками в М3',
    callback_data='change_person_m')
  g_but = types.InlineKeyboardButton(
    'человек, ответственный за контейнер с крышечками в Г1',
    callback_data='change_person_g')
  secret_markup.add(q_but, d_but, b_but, g_but, m_but)
  bot.send_message(message.chat.id,
                   "Кем вы хотите стать?",
                   reply_markup=secret_markup)


@bot.callback_query_handler(func=lambda call: call.data == "change_person_g")
def get_func_bin_g(call):
  g1_bin_id_file = open("g1_bin_person_id.txt",  "a")
  g1_bin_id_file.write(str(call.message.chat.id) + '\n')
  g1_bin_id_file.close()
  bot.send_message(
    call.message.chat.id,
    'Поздравляю! Теперь вам будут приходить сообщения когда контейнер в Г1 заполнится'
  )
  call.data = ''


@bot.callback_query_handler(func=lambda call: call.data == "change_person_b")
def get_func_bin_b(call):
  b_bin_id_file = open("b_bin_person_id.txt",  "a")
  b_bin_id_file.write(str(call.message.chat.id) + '\n')
  b_bin_id_file.close()
  bot.send_message(
    call.message.chat.id,
    'Поздравляю! Теперь вам будут приходить сообщения когда контейнер в Б заполнится'
  )
  call.data = ''


@bot.callback_query_handler(func=lambda call: call.data == "change_person_m")
def get_func_bin_m(call):
  m_bin_id_file = open("m_bin_person_id.txt",  "a")
  m_bin_id_file.write(str(call.message.chat.id) + '\n')
  m_bin_id_file.close()
  bot.send_message(
    call.message.chat.id,
    'Поздравляю! Теперь вам будут приходить сообщения когда контейнер в M3 заполнится'
  )
  call.data = ''


@bot.callback_query_handler(func=lambda call: call.data == "change_person_d")
def get_func_bin_d(call):
  d_bin_id_file = open("d_bin_person_id.txt",  "a")
  d_bin_id_file.write(str(call.message.chat.id) + '\n')
  d_bin_id_file.close()
  bot.send_message(
    call.message.chat.id,
    'Поздравляю! Теперь вам будут приходить сообщения когда контейнер в Доме коммуне заполнится'
  )
  call.data = ''


@bot.callback_query_handler(func=lambda call: call.data == "change_person_q")
def get_func_bin_q(call):
  q_person_id_file = open("q_person_id.txt",  "a")
  q_person_id_file.write(str(call.message.chat.id) + '\n')
  q_person_id_file.close()
  bot.send_message(
    call.message.chat.id, 'Поздравляю! Теперь вам будут приходить вопросы от пользователей')
  call.data = ''

@bot.message_handler(commands=['add_sending'])
def add_sending(message):
  bot.send_message(message.chat.id, 'Пришлите текст')
  bot.register_next_step_handler(message, add_sending1)

def add_sending1(message):
  global sending_text
  sending_text = str(message.text)
  bot.send_message(message.chat.id, 'Пришлите фото')
  bot.register_next_step_handler(message, get_user_photo)

@bot.message_handler(content_type=['photo'])
def get_user_photo(message):
  global sending_text, photo
  if str(message.text) != 'None': 
    bot.send_message(message.chat.id, "Необходимо прислать сообщение без текста. Начните заново с команды /add_sending")
    return
  else:
    photo = message.photo[0].file_id
    bot.send_message(message.chat.id, 'Вот так будет выглядеть рассылка')
    bot.send_photo(message.chat.id, photo, sending_text)
    bot.send_message(message.chat.id, 'Выполнить? Для отмены рассылки напишите "Нет"')
    bot.register_next_step_handler(message, do_sending)
  
def do_sending(message):
  global photo
  if str(message.text).lower() == 'нет': return
  for user in users_id:
    bot.send_photo(user, photo, sending_text)
  bot.send_message(message.chat.id, 'Рассылка завершена')
  
  

keep_alive()
bot.polling(none_stop=True)
