import telebot
from telebot import types, TeleBot

Token = '5065022973:AAFaDA_uq54vEF9jHoDPNRBiAWqoDfCFNRQ'
bot = telebot.TeleBot("5222661077:AAGytBJpA4I62AlXyvTrUQV_QH7M9jBI42k")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет, на связи АСИ! Специально для тебя мы подготовили бота, который покажет "
                                      "тебе, что строительство и проектирование это занимательно и увлекательно!")
    photo = open('F:\PycharmProjects\PrOrMaket2\Picture\logoASI.jpg', 'rb')
    bot.send_photo(message.chat.id, photo=photo)
    bot.send_message(message.chat.id,
                     "Представим, что вам предлагают принять участие в проектировании жилого дома. В  "
                     "зависимости от региона, на участке может быть представлен разные виды грунта, от"
                     " которых зависит вид фундамента нашего дома")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Фундамент')
    item2 = types.KeyboardButton('Стены')
    item3 = types.KeyboardButton('Крыша')
    item4 = types.KeyboardButton('Коммуникации')
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, "Итак, нам даны на выбор следующие варианты разработки,"
                                      "с чего начнем?", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def pick_answer(message):
    if message.text == 'Фундамент':
        bot.send_message(message.chat.id, "Отлично, наш фундамент в зависимости от грунта может быть: ленточным,"
                                          "столбчатым, плитным или свайным. ")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Супесь')
        item2 = types.KeyboardButton('Глина')
        item3 = types.KeyboardButton('Скальный')
        item4 = types.KeyboardButton('Суглинок')
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id, "Давай определим, какой вид грунта представлен на нашем участке.",
                         reply_markup=markup)
    elif message.text == 'Глина':
        bot.send_message(message.chat.id, "Отлично, наш фундамент будет свайным"
                                          "Свайный фундамент позволяет нам строить дома высотой более 16 этажей.")
        photo = open("F:\PycharmProjects\PrOrMaket2\Picture\svayny_fundament.jpg", 'rb')
        bot.send_photo(message.chat.id, photo=photo)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('до 5.')
        item2 = types.KeyboardButton('до 9.')
        item3 = types.KeyboardButton('до 16.')
        item4 = types.KeyboardButton('более 16.')
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id, "Какова этажность твоего проекта?", reply_markup=markup)
    elif message.text == 'Скальный':
        bot.send_message(message.chat.id, "Отлично, наш фундамент будет либо плитным, либо свайным."
                                          " Свайный фундамент позволяет нам строить дома высотой более 16 этажей.")
        photo = open("F:\PycharmProjects\PrOrMaket2\Picture\plitny_fundament.jpg", 'rb')
        bot.send_photo(message.chat.id, photo=photo)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('до 5')
        item2 = types.KeyboardButton('до 9')
        item3 = types.KeyboardButton('до 16')
        item4 = types.KeyboardButton('более 16')
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id, "Какова этажность твоего проекта?", reply_markup=markup)
    elif message.text == 'Супесь':
        bot.send_message(message.chat.id, "Отлично, наш фундамент будет либо ленточным, либо столбчатым."
                                          "Ленточный фундамент позволяет вести застройку до 5 этажей, столбчатый до 9.")
        photo = open("F:\PycharmProjects\PrOrMaket2\Picture\lentochny_fundament.jpg", 'rb')
        bot.send_photo(message.chat.id, photo=photo)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('до 5')
        item2 = types.KeyboardButton('до 9')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, "Какова этажность твоего проекта?", reply_markup=markup)
    elif message.text == 'Суглинок':
        bot.send_message(message.chat.id, "Отлично, наш фундамент будет либо ленточным, либо столбчатым."
                                          "Ленточный фундамент позволяет вести застройку до 5 этажей, столбчатый до 9.")
        photo = open("F:\PycharmProjects\PrOrMaket2\Picture\lentochny_fundament.jpg", 'rb')
        bot.send_photo(message.chat.id, photo=photo)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('до 5')
        item2 = types.KeyboardButton('до 9')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, "Какова этажность твоего проекта?", reply_markup=markup)
    elif message.text == 'до 5.':
        bot.send_message(message.chat.id, "Отлично, такая комбинация грунта и этажности дает нам возможность"
                                          " проектирования функционирующего подвального помещения")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Да.')
        item2 = types.KeyboardButton('Нет.')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, "Будем ли мы делать подвал?", reply_markup=markup)
    elif message.text == 'до 9.':
        bot.send_message(message.chat.id, "Отлично, такая комбинация грунта и этажности дает нам возможность"
                                          " проектирования функционирующего подвального помещения")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Да.')
        item2 = types.KeyboardButton('Нет.')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, "Будем ли мы делать подвал?", reply_markup=markup)
    elif message.text == 'Да.':
        bot.send_message(message.chat.id, "Разработка основания здания завершена, теперь мы можем приступить к "
                                          "следующим этапам разработки.")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('/start')
        markup.add(item1)
        bot.send_message(message.chat.id, "Чтобы продолжить разработку, вернемся в начало всего "
                                          "с помощью этой кнопки", reply_markup=markup)
    elif message.text == 'Нет.':
        bot.send_message(message.chat.id, "Разработка основания здания завершена, теперь мы можем приступить к "
                                          "следующим этапам разработки.")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('/start')
        markup.add(item1)
        bot.send_message(message.chat.id, "Чтобы продолжить разработку, вернемся в начало всего "
                                          "с помощью этой кнопки", reply_markup=markup)
    elif message.text == 'до 5':
        bot.send_message(message.chat.id, "Такая комбинация грунта и этажности не дает нам возможность"
                                          " проектирования функционирующего подвального помещения")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('/start')
        markup.add(item1)
        bot.send_message(message.chat.id, "Разработка основания здания завершена, теперь мы можем приступить к "
                                          "следующим этапам разработки.Чтобы продолжить разработку, вернемся в начало"
                                          " всего с помощью этой кнопки", reply_markup=markup)
    elif message.text == 'до 9':
        bot.send_message(message.chat.id, "Такая комбинация грунта и этажности не дает нам возможность"
                                          " проектирования функционирующего подвального помещения")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('/start')
        markup.add(item1)
        bot.send_message(message.chat.id, "Разработка основания здания завершена, теперь мы можем приступить к "
                                          "следующим этапам разработки.Чтобы продолжить разработку, вернемся в начало"
                                          " всего с помощью этой кнопки", reply_markup=markup)
    elif message.text == 'до 16':
        bot.send_message(message.chat.id, "Такая комбинация грунта и этажности не дает нам возможность"
                                          " проектирования функционирующего подвального помещения")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('/start')
        markup.add(item1)
        bot.send_message(message.chat.id, "Разработка основания здания завершена, теперь мы можем приступить к "
                                          "следующим этапам разработки.Чтобы продолжить разработку, вернемся в начало"
                                          " всего с помощью этой кнопки", reply_markup=markup)
    elif message.text == 'более 16':
        bot.send_message(message.chat.id, "Такая комбинация грунта и этажности не дает нам возможность"
                                          " проектирования функционирующего подвального помещения")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('/start')
        markup.add(item1)
        bot.send_message(message.chat.id, "Разработка основания здания завершена, теперь мы можем приступить к "
                                          "следующим этапам разработки.Чтобы продолжить разработку, вернемся в начало"
                                          " всего с помощью этой кнопки", reply_markup=markup)
    elif message.text == 'до 16.':
        bot.send_message(message.chat.id, "Такая комбинация грунта и этажности не дает нам возможность"
                                          " проектирования функционирующего подвального помещения")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('/start')
        markup.add(item1)
        bot.send_message(message.chat.id, "Разработка основания здания завершена, теперь мы можем приступить к "
                                          "следующим этапам разработки.Чтобы продолжить разработку, вернемся в начало"
                                          " всего с помощью этой кнопки", reply_markup=markup)
    elif message.text == 'более 16.':
        bot.send_message(message.chat.id, "Такая комбинация грунта и этажности не дает нам возможность"
                                          " проектирования функционирующего подвального помещения")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('/start')
        markup.add(item1)
        bot.send_message(message.chat.id, "Разработка основания здания завершена, теперь мы можем приступить к "
                                          "следующим этапам разработки.Чтобы продолжить разработку, вернемся в начало"
                                          " всего с помощью этой кнопки", reply_markup=markup)
    elif message.text == 'Стены':
        bot.send_message(message.chat.id, "Отлично, наши стены в зависимости от климата должны иметь слой утеплителя. ")
        photo = open("F:\PycharmProjects\PrOrMaket2\Picture\Razrez.jpg", 'rb')
        bot.send_photo(message.chat.id, photo=photo)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item5 = types.KeyboardButton('+5-0')
        item6 = types.KeyboardButton('-10')
        item7 = types.KeyboardButton('-20')
        markup.add(item5, item6, item7)
        bot.send_message(message.chat.id, "Какова средняя температура зимы в регионе, в котором наше здание будет"
                                          " находиться?", reply_markup=markup)
    elif message.text == '+5-0':
        bot.send_message(message.chat.id, "В таком климате утепление здания не имеет существенной роли. ")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item5 = types.KeyboardButton('дo 5')
        item6 = types.KeyboardButton('дo 9')
        item7 = types.KeyboardButton('дo 16')
        item8 = types.KeyboardButton('болеe 16')
        markup.add(item5, item6, item7, item8)
        bot.send_message(message.chat.id, "При проектировке здания важно помнить какие изначальные условия тебе "
                                          "поставлены и что из них следует, вспомни сколько этажей будет в твоем"
                                          " здании?", reply_markup=markup)
    elif message.text == '-10':
        bot.send_message(message.chat.id, "В таком климате утепление здания имеет существенную роль. ")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item5 = types.KeyboardButton('дo 5')
        item6 = types.KeyboardButton('дo 9')
        item7 = types.KeyboardButton('дo 16')
        item8 = types.KeyboardButton('болеe 16')
        markup.add(item5, item6, item7, item8)
        bot.send_message(message.chat.id, "При проектировке здания важно помнить какие изначальные условия тебе "
                                          "поставлены и что из них следует, вспомни сколько этажей будет в твоем"
                                          " здании?", reply_markup=markup)
    elif message.text == '-20':
        bot.send_message(message.chat.id, "В таком климате утепление здания имеет существенную роль. ")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item5 = types.KeyboardButton('дo 5')
        item6 = types.KeyboardButton('дo 9')
        item7 = types.KeyboardButton('дo 16')
        item8 = types.KeyboardButton('болеe 16')
        markup.add(item5, item6, item7, item8)
        bot.send_message(message.chat.id, "При проектировке здания важно помнить какие изначальные условия тебе "
                                          "поставлены и что из них следует, вспомни сколько этажей будет в твоем"
                                          " здании?", reply_markup=markup)
    elif message.text == 'дo 5':
        bot.send_message(message.chat.id, "Такая этажность дает возможность использовать при строительстве такие"
                                          "строительные материалы, как: кирпич, керамические блоки, газобетон, "
                                          "панельные стены, древесина")
        photo = open("F:\PycharmProjects\PrOrMaket2\Picture\drevesina.jpg", 'rb')
        bot.send_photo(message.chat.id, photo=photo)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item5 = types.KeyboardButton('Дорого')
        item6 = types.KeyboardButton('Дешево')
        markup.add(item5, item6)
        bot.send_message(message.chat.id, "Строиматериалы какой цены ты собираешься "
                                          "покупать?", reply_markup=markup)
    elif message.text == 'дo 9':
        bot.send_message(message.chat.id, "Такая этажность дает возможность использовать при строительстве такие"
                                          "строительные материалы, как: кирпич, керамические блоки, газобетон,"
                                          " панельные стены")
        photo = open("F:\PycharmProjects\PrOrMaket2\Picture\gazobeton.jpg", 'rb')
        bot.send_photo(message.chat.id, photo=photo)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item5 = types.KeyboardButton('Дорого')
        item6 = types.KeyboardButton('Дешево')
        markup.add(item5, item6)
        bot.send_message(message.chat.id, "Строиматериалы какой цены ты собираешься "
                                          "покупать?", reply_markup=markup)
    elif message.text == 'дo 16':
        bot.send_message(message.chat.id, "Такая этажность дает возможность использовать при строительстве такие"
                                          "строительные материалы, как: кирпич, монолитный бетон")
        photo = open("F:\PycharmProjects\PrOrMaket2\Picture\kirpichnaya_stena.jpg", 'rb')
        bot.send_photo(message.chat.id, photo=photo)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item5 = types.KeyboardButton('Дорого')
        item6 = types.KeyboardButton('Дешево')
        markup.add(item5, item6)
        bot.send_message(message.chat.id, "Строиматериалы какой цены ты собираешься "
                                          "покупать?", reply_markup=markup)
    elif message.text == 'болеe 16':
        bot.send_message(message.chat.id, "Такая этажность дает возможность использовать при строительстве такие"
                                          "строительные материалы, как: кирпич, монолитный бетон")
        photo = open("F:\PycharmProjects\PrOrMaket2\Picture\monolitny.jpg", 'rb')
        bot.send_photo(message.chat.id, photo=photo)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item5 = types.KeyboardButton('Дорого')
        item6 = types.KeyboardButton('Дешево')
        markup.add(item5, item6)
        bot.send_message(message.chat.id, "Строиматериалы какой цены ты собираешься "
                                          "покупать?", reply_markup=markup)
    elif message.text == 'Дорого':
        bot.send_message(message.chat.id, "Дорогими строительными материалами считаются: кирпич, древесина")
        photo = open("F:\PycharmProjects\PrOrMaket2\Picture\drevesina.jpg", 'rb')
        bot.send_photo(message.chat.id, photo=photo)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item5 = types.KeyboardButton('Быстро')
        item6 = types.KeyboardButton('Долго')
        markup.add(item5, item6)
        bot.send_message(message.chat.id, "С какой скоростью будут возводиться стены?", reply_markup=markup)
    elif message.text == 'Дешево':
        bot.send_message(message.chat.id, "Дешевыми строительными материалами считаются: керамические блоки, газобетон,"
                                          " монолитный бетон, панельные стены")
        photo = open("F:\PycharmProjects\PrOrMaket2\Picture\panelny.jpg", 'rb')
        bot.send_photo(message.chat.id, photo=photo)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item5 = types.KeyboardButton('Быстро')
        item6 = types.KeyboardButton('Долго')
        markup.add(item5, item6)
        bot.send_message(message.chat.id, "С какой скоростью будут возводиться стены?", reply_markup=markup)
    elif message.text == 'Быстро':
        bot.send_message(message.chat.id, "Керамические блоки, газобетон, древесина, монолитный бетон,"
                                          " панельные стены - именно эти строительные материалы позволяют поддерживать"
                                          " высокую скорость возведения строительных конструкций.")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item5 = types.KeyboardButton('/start')
        markup.add(item5)
        bot.send_message(message.chat.id, "На этом проектирование стен заканчивается,"
                                          "приступим к другим этапам. Чтобы продолжить разработку, вернемся в начало"
                                          " всего с помощью этой кнопки", reply_markup=markup)
    elif message.text == 'Долго':
        bot.send_message(message.chat.id, "Кирпич - материал, использование которого требует большого количества"
                                          " времени и усилий строителей")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item5 = types.KeyboardButton('/start')
        markup.add(item5)
        bot.send_message(message.chat.id, "На этом проектирование стен заканчивается,"
                                          "приступим к другим этапам. Чтобы продолжить разработку, вернемся в начало"
                                          " всего с помощью этой кнопки", reply_markup=markup)
    elif message.text == 'Крыша':
        bot.send_message(message.chat.id, "Скат крыши - важный показатель. Именно благодаря скату возможен отвод воды"
                                          " с самого верха сооружения")
        photo = open("F:\PycharmProjects\PrOrMaket2\Picture\skat_krishi.jpg", 'rb')
        bot.send_photo(message.chat.id, photo=photo)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item9 = types.KeyboardButton('Много')
        item10 = types.KeyboardButton('Мало')
        markup.add(item9, item10)
        bot.send_message(message.chat.id, "Сколько осадков выпадает в твоем регионе?", reply_markup=markup)
    elif message.text == 'Много':
        bot.send_message(message.chat.id, "Учитывая такой объем осадков нашему зданию необходим скат крыши"
                                          " имеющий некоторый угол")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item9 = types.KeyboardButton('менее 5')
        item10 = types.KeyboardButton('менее 9')
        item11 = types.KeyboardButton('менее 16')
        item12 = types.KeyboardButton('бoлee 16')
        markup.add(item9, item10, item11, item12)
        bot.send_message(message.chat.id, "Для проектирования водостока необходимо вспомнить нашу этажность,"
                                          " итак сколько же мы заложили этажей в наше здание?", reply_markup=markup)
    elif message.text == 'Мало':
        bot.send_message(message.chat.id, "Учитывая такой объем осадков нашему зданию необходим скат крыши"
                                          "имеющий некоторый угол")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item9 = types.KeyboardButton('менее 5')
        item10 = types.KeyboardButton('менее 9')
        item11 = types.KeyboardButton('менее 16')
        item12 = types.KeyboardButton('бoлee 16')
        markup.add(item9, item10, item11, item12)
        bot.send_message(message.chat.id, "Для проектирования водостока необходимо вспомнить нашу этажность,"
                                          " итак сколько же мы заложили этажей в наше здание?", reply_markup=markup)
    elif message.text == 'менее 5':
        bot.send_message(message.chat.id, "Такая этажность позволяет разместить водосток снаружи здания")
        photo = open("F:\PycharmProjects\PrOrMaket2\Picture\livnevka.jpg", 'rb')
        bot.send_photo(message.chat.id, photo=photo)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item5 = types.KeyboardButton('/start')
        markup.add(item5)
        bot.send_message(message.chat.id, "На этом облегченное проектирование крыши заканчивается,"
                                          "приступим к другим этапам. Чтобы продолжить разработку, вернемся в начало"
                                          " всего с помощью этой кнопки", reply_markup=markup)
    elif message.text == 'менее 9':
        bot.send_message(message.chat.id, "Такая этажность вынуждает нас разместить водосток внутри здания")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item5 = types.KeyboardButton('/start')
        markup.add(item5)
        bot.send_message(message.chat.id, "На этом облегченное проектирование крыши заканчивается,"
                                          "приступим к другим этапам. Чтобы продолжить разработку, вернемся в начало"
                                          " всего с помощью этой кнопки", reply_markup=markup)
    elif message.text == 'менее 16':
        bot.send_message(message.chat.id, "Такая этажность вынуждает нас разместить водосток внутри здания")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item5 = types.KeyboardButton('/start')
        markup.add(item5)
        bot.send_message(message.chat.id, "На этом облегченное проектирование крыши заканчивается,"
                                          "приступим к другим этапам. Чтобы продолжить разработку, вернемся в начало"
                                          " всего с помощью этой кнопки", reply_markup=markup)
    elif message.text == 'бoлee 16':
        bot.send_message(message.chat.id, "Такая этажность вынуждает нас разместить водосток внутри здания")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item5 = types.KeyboardButton('/start')
        markup.add(item5)
        bot.send_message(message.chat.id, "На этом облегченное проектирование крыши заканчивается,"
                                          "приступим к другим этапам. Чтобы продолжить разработку, вернемся в начало"
                                          " всего с помощью этой кнопки", reply_markup=markup)
    elif message.text == 'Коммуникации':
        bot.send_message(message.chat.id, "Наше здание должно иметь подключение к инженерным сетям, а также иметь"
                                          " уточненное местоположение, относительно сложных участков городской "
                                          " инфраструктуры ")
        photo = open("F:\PycharmProjects\PrOrMaket2\Picture\Vodoochistnie.jpg", 'rb')
        bot.send_photo(message.chat.id, photo=photo)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item14 = types.KeyboardButton('Гражданское')
        item15 = types.KeyboardButton('Промышленное')
        markup.add(item14, item15)
        bot.send_message(message.chat.id, "Для определения того, как будут подключены инженерные сети в нашем "
                                          " сооружении, определим предназначение нашего здания.", reply_markup=markup)
    elif message.text == 'Гражданское':
        bot.send_message(message.chat.id, "Наше здание должно иметь подключение к инженерным сетям общего пользования")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item18 = types.KeyboardButton('2 - 5 метров')
        item19 = types.KeyboardButton('10 метров')
        item20 = types.KeyboardButton('20+ метров')
        markup.add(item18, item19, item20)
        bot.send_message(message.chat.id, "Определим дальность нашего здания от автомобильных дорог общего пользования"
                                          " и необходимость создания каких-либо заграждений, для уменьшения шума",
                         reply_markup=markup)
    elif message.text == 'Промышленное':
        bot.send_message(message.chat.id, "У нашего здания должны присутствовать свои независимые очистные сооружения")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item14 = types.KeyboardButton('2 - 5 метров')
        item15 = types.KeyboardButton('10 метров')
        item16 = types.KeyboardButton('20+ метров')
        markup.add(item14, item15, item16)
        bot.send_message(message.chat.id, "Определим дальность нашего здания от автомобильных дорог общего пользования"
                                          " и необходимость создания каких-либо заграждений, для уменьшения шума",
                         reply_markup=markup)
    elif message.text == '2 - 5 метров':
        bot.send_message(message.chat.id, "При такой близости к автомагистрали возведение здания невозможно."
                                          " Необходимо увеличить расстояние между зданием и дорогой")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item14 = types.KeyboardButton('менее 5 этажей')
        item15 = types.KeyboardButton('менее 9 этажей')
        item16 = types.KeyboardButton('менее 16 этажей')
        item17 = types.KeyboardButton('более 16 этажей')
        markup.add(item14, item15, item16, item17)
        bot.send_message(message.chat.id, "В зависимости от этажности, определяют необходимость установки лифтов,"
                                          " а также их количество на подъезд", reply_markup=markup)
    elif message.text == '10 метров':
        bot.send_message(message.chat.id, "Такое расстояние до автомагистрали вынуждает использовать в качестве "
                                          " шумоподавления зеленые насаждения")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item14 = types.KeyboardButton('менее 5 этажей')
        item15 = types.KeyboardButton('менее 9 этажей')
        item16 = types.KeyboardButton('менее 16 этажей')
        item17 = types.KeyboardButton('более 16 этажей')
        markup.add(item14, item15, item16, item17)
        bot.send_message(message.chat.id, "В зависимости от этажности, определяют необходимость установки лифтов,"
                                          " а также их количество на подъезд", reply_markup=markup)
    elif message.text == '20+ метров':
        bot.send_message(message.chat.id, "В таком случае шумоподавление необязательно, но организовать связь "
                                          " с магистралью необходимо в любом случае.")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item14 = types.KeyboardButton('менее 5 этажей')
        item15 = types.KeyboardButton('менее 9 этажей')
        item16 = types.KeyboardButton('менее 16 этажей')
        item17 = types.KeyboardButton('более 16 этажей')
        markup.add(item14, item15, item16, item17)
        bot.send_message(message.chat.id, "В зависимости от этажности, определяют необходимость установки лифтов,"
                                          " а также их количество на подъезд", reply_markup=markup)
    elif message.text == 'менее 5 этажей':
        bot.send_message(message.chat.id, "Установка лифта будет нецелесообразной")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('/start')
        markup.add(item1)
        bot.send_message(message.chat.id, "На этом можно завершить разработку коммуникаций в здании, теперь мы можем "
                                          " приступить к следующим этапам разработки.Чтобы продолжить разработку, "
                                          " вернемся в начало всего с помощью этой кнопки", reply_markup=markup)
    elif message.text == 'менее 9 этажей':
        bot.send_message(message.chat.id, "В данном случае необходимо установить один лифт на подъезд")
        photo = open("F:\PycharmProjects\PrOrMaket2\Picture\Lift.jpg", 'rb')
        bot.send_photo(message.chat.id, photo=photo)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('/start')
        markup.add(item1)
        bot.send_message(message.chat.id, "На этом можно завершить разработку коммуникаций в здании, теперь мы можем "
                                          " приступить к следующим этапам разработки.Чтобы продолжить разработку, "
                                          " вернемся в начало всего с помощью этой кнопки", reply_markup=markup)
    elif message.text == 'менее 16 этажей':
        bot.send_message(message.chat.id, "В данном случае необходима установка не менее двух лифтов")
        photo = open("F:\PycharmProjects\PrOrMaket2\Picture\Lift.jpg", 'rb')
        bot.send_photo(message.chat.id, photo=photo)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('/start')
        markup.add(item1)
        bot.send_message(message.chat.id, "На этом можно завершить разработку коммуникаций в здании, теперь мы можем "
                                          " приступить к следующим этапам разработки.Чтобы продолжить разработку, "
                                          " вернемся в начало всего с помощью этой кнопки", reply_markup=markup)
    elif message.text == 'более 16 этажей':
        bot.send_message(message.chat.id, "В данном случае необходима установка не менее трех лифтов")
        photo = open("F:\PycharmProjects\PrOrMaket2\Picture\Lift.jpg", 'rb')
        bot.send_photo(message.chat.id, photo=photo)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('/start')
        markup.add(item1)
        bot.send_message(message.chat.id, "На этом можно завершить разработку коммуникаций в здании, теперь мы можем "
                                          " приступить к следующим этапам разработки.Чтобы продолжить разработку, "
                                          " вернемся в начало всего с помощью этой кнопки", reply_markup=markup)



# 44 условия лол
bot.polling(none_stop=True, interval=0)
