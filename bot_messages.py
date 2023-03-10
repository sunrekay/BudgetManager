def start() -> str:
    '''Текст сообщения когда пользователь нажимает старт'''
    return '''Привет, я Финансовый помощник Джон. 
Давай перечислю то,что я умею:
    1. Со мной ты можешь создать финансовые правила,
которые помогут доходить до целей
например тратить на Кофе не более 3000 руб в месяц. 
Мы вместе достигнем этого результата! Тебе не нужно 
заморачиваться и ущемлять себя в тратах,я буду проводить
анализ,скидывать тебе результат,а ты принимать
решение соблюдаем правила или меняем правила.
    2. Заполнив календарь обязательства, ты  будь уверен/а,что 
Мы с тобой закроем все обязательства и даже начнем
откладывать. Помни о правиле “Сначала заплати себе”. 
Заплатить за кредиты,квартиру,комуналку. И отложить 10-20% от зп вполне реально! 
А потом съездить отдохнуть в турцию заблаговременно запланировав отпуск. 
У тебя все получится) 
    3. Все что тебе нужно вносить траты, я буду напоминать тебе 
в то время,которое ты скажешь. 
И так поехали!
'''
# end start_message()


def create_rule():
    '''Текст сообщения при создании финансового правила'''
    return '''Введите название категории для которой создадим правило.
Например: категория "отдых" в месяц "20.000" это будет значить,что вы не намерены тратить на отдых более 20.000 в месяц. 
'''
# end create_rule


def calendar():
    '''Текст начала обучения с "Календарь обязательств"'''
    return '''Отлично, правило создано
Теперь давай определимся с обязательствами
Нажми на кнопку "Календарь обязательств"
'''
# end calendar