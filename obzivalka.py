# огромное спасибо за скрипт https://github.com/PSPshnik
#.tralka <кол-во слов> <Сколько капса(в %)> <Имя обидчика>
from .. import loader, utils
import logging
import random

version = 4.8
sentence_min = 3
sentence_max = 10
# paragraph_min = 10
# paragraph_max = 20
print_length = False

m = ['некультурный', 'необразованный',
     'гороховый', 'мудовый', 'глупенький',
     'малолетний', 'ебучий', 'гнилой',
     'собачий', 'ссаный', 'моржовый',
     'вредный', 'прибабахнутый', 'ебаный',
     'волшебный', 'сказочный', 'маленький',
     'приёмный', 'сральный', 'пердёжный',
     'обоссанный', 'обосранный', 'чёртов',
     'грязный', 'тупой', 'нищий', 'родной', 'мусорный',
     'дегенеративный',
     'распроклятый', 'турецкий', 'блядский',
     'ёбаный', 'хуев', 'хуёвый', 'ебанутый',
     'ёбнутый', 'грязный', 'зелёный', 'сукин',
     'лысый', 'пожилой', 'вонючий', 'чокнутый']

f = ['некультурная', 'необразованная',
     'гороховая', 'мудовая', 'глупенькая',
     'малолетняя', 'ебучая', 'гнилая',
     'собачья', 'ссаная', 'моржовая',
     'вредная', 'прибабахнутая', 'ебаная',
     'волшебная', 'сказочная', 'маленькая',
     'приёмная', 'сральная', 'пердёжная',
     'обоссанная', 'обосранная', 'чёртова',
     'грязная', 'тупая', 'нищая',
     'родная', 'мусорная', 'дегенеративная',
     'распроклятая', 'турецкая', 'блядская',
     'ёбаная', 'хуева', 'хуёвая', 'ебанутая',
     'ёбнутая', 'грязная', 'зелёная', 'сукина',
     'лысая', 'пожилая', 'вонючая', 'чокнутая']

s = ['некультурное', 'необразованное',
     'гороховое', 'мудовое', 'глупенькое',
     'малолетнее', 'ебучее', 'гнилое',
     'собачье', 'ссаное', 'моржовое',
     'вредное', 'прибабахнутое', 'ебаное',
     'волшебное', 'сказочное', 'маленькое',
     'приёмное', 'сральное', 'пердёжное',
     'обоссанное', 'обосранное', 'чёртово', 'грязное',
     'тупое', 'нищее', 'родное', 'мусорное', 'дегенеративное',
     'распроклятое', 'турецкое', 'блядское',
     'ёбаное', 'хуево', 'хуёвое', 'ебанутое',
     'ёбнутое', 'грязное', 'зелёное', 'сукино',
     'лысое', 'пожилое', 'вонючее', 'чокнутое']

k = ['из жопы', 'в ловушке', 'в бане',
     'на хуе', 'в дурке', 'из стула', 'в дурке ебаной',
     'в хуипе', 'в запечатанной колоде']

n = ['негра', 'джокера', 'тупого говна', 'хуйни ебаной',
     'хуя', 'феминизма', 'говна',
     'от народа', 'хуйни', 'Навального',
     'ловушкера', 'Путина', 'русского народа', 'вонючки', 'с функцией жопа']

o = ['пиздец', 'блять', 'попался в ловушку',
     'тебя забайтили', 'ловушка джокера', 'тебе бан',
     'фак ю', 'убейся', 'соси',
     'ёбаный твой рот', 'срал я на тебя',
     'убейся об стену', 'соси пизду', 'у тебя хуй вместо носа',
     'купи мою подписку на ютубе',
     'хуй соси', 'губой тряси', 'я съел деда',
     'насрал в пизду',
     '22 июня 1642 года Карл Первый поднял королевский штандарт (королевский флаг), что по английским традициям означало объявление войны',
     'мне этот мир абсолютно понятен',
     'я был на этой планете бесконечным множеством',
     'но тебе этого не понять',
     'иди преисполняться в гранях каких-то',
     'пиздуй - бороздуй',
     'бредишь', 'вот я какну и смываю, и ты так делай',
     'не надо шутить с войной',
     'твою дочку ебут', 'залупаешься',
     'хули ты пиздишь', 'поцелуй лошадиную сраку',
     'распронаёб тебя', 'ъеь', 'ьуь', 'аье',
     'какого хуя они в другом порядке разложены',
     'ай фак ю булщит щит',
     'он за углом сидит и тебе на голову дрочит',
     'армяне в нарды играют', 'жирняк гай',
     'иди сюда, попробуй меня трахнуть, я тебя сам трахну',
     'что ты там делаешь', 'беги за горизонт',
     'попал в дурку ебаную', 'был бы ты человек', 'нахуй',
     'запомни', 'хули ты сюда лезешь',
     'высрана твоя морда', 'возьми салфетку',
     'я бы никому не проиграл',
     'иди нахуй', 'иди',
     'я тебя ебал, гад, срать на нас говна',
     'я тебя ебал гадить нас срать так',
     'держи в курсе', 'несёшь хуйню какую-то',
     'русские вперёд']

d = ['бекон', 'сыр', 'пенис', 'член',
     'мудозвон', 'лицемер', 'лжец',
     'хуй', 'гомогей', 'чай', 'рукоблуд',
     'долбан', 'пидорас', 'сын', 'козёл',
     'газ', 'фашист', 'пососатель',
     'дегенерат', 'спермобак', 'долбоёб',
     'клоун', 'паразит', 'письколёт',
     'мудак', 'спидозник', 'пудж', 'кремлебот',
     'объебос', 'дурачок', 'хуебес', 'пиздолёт',
     'педик', 'педик - медведик', 'дебил', 'дифичент',
     'кок сакер', 'пиздабол', 'аутист', 'гадёныш', 'выблядок',
     'глиномес', 'даун', 'хер', 'булщит', 'засранец',
     'инвалид', 'дурак', 'болван',
     'минетчик', 'онанист', 'напёрдыш',
     'чилипиздрик', 'пиздюк', 'гей', 'ловушкер',
     'пендос', 'наркоман', 'алкаш', 'жиробас',
     'рак', 'укурок', 'крокодил', 'ебальник',
     'секс-раб', 'потомок', 'дрыщ',
     'урод', 'карлик', 'дед инсайд', 'волк',
     'калыван', 'либераст', 'шакал',
     'педофил', 'бомж', 'пингвин', 'жираф',
     'огурец', 'салат', 'лук', 'картофель',
     'деградант', 'спам', 'человек', 'гуманитарий',
     'язык', 'стол', 'PEP-8', 'ебалай', 'враг', 'недруг', 'супостат',
     'кретин', 'козолуп', 'свинарь',
     'униженец', 'опущенец', 'муравей',
     'дятел', 'козёл', 'жирняк', 'говноед',
     'чёрт', 'суслик', 'идиот', 'жлоб', 'мерзавец',
     'негодяй', 'подлец', 'ублюдок', 'гад',
     'гавкошмыг', 'чикибамбонатор', 'чикибамбог',
     'джокер', 'жмых', 'жмышок', 'жмышонок',
     'куколд', 'ебалай', 'ушлёпок',
     'хуесос', 'членосос', 'чикибамбонёнок',
     'чикибан', 'чикибомбастер', 'чайник',
     'чикибамбонизатор', 'чикибамбог']

dd = ['куколда', 'хуйолда', 'мудила', 'блядина', 'гнида',
      'пидрила', 'тварь', 'сука', 'сперма', 'пидорасина',
      'либераха', 'срака', 'жопа', 'петушара', 'залупа',
      'хуета', 'пупа', 'петька', 'блядь', 'елда', 'тряпка',
      'яма', 'хуемразь', 'срань', 'мошонка', 'ссанина',
      'вагина', 'пизда', 'пососательница',
      'ловушка', 'паста', 'макаронина',
      'жиробасина', 'радфемка', 'шлюха', 'прошмандовка',
      'жируха', 'доска', 'уродина',
      'плоскодонка', 'скотина', 'омега',
      'черешня', 'ватрушка', 'шишка',
      'ракушка', 'свинья', 'какашка',
      'гнилушка', 'лягушка', 'свинушка',
      'картошка', 'волчара', 'дочь', 'пешка',
      'давалка', 'пососательница',
      'колбаса', 'собака', 'мохнатка', 'жижа',
      'какашка', 'какуля', 'душа', 'вражина',
      'падла', 'болезнь', 'бумажка', 'вонючка',
      'тень', 'гадина', 'чикибамбони',
      'микробамбони', 'мышь', 'мразь',
      'мразина', 'мразота']

ddd = ['удобрение', 'уёбище', 'ебло', 'хуйло',
       'чудище', 'говно', 'яблоко', 'животное',
       'дерьмо', 'блядотище', 'дитя', 'порождение',
       'очко', 'растение', 'ебало', 'ведро',
       'мудило', 'хуепучило']

gens = ['03', '14', '25', '8',
        '06', '16', '26', '30',
        '41', '52', '303', '330', '0',
        '414', '441', '1', '8',
        '525', '552', '2', '067',
        '167', '267', '306', '416',
        '526', '07', '8', '8', '8',
        '17', '27', '8', '8', '8',
        '307', '417', '527', '8', '8',
        '3067', '4167', '5267']

array = [d, dd, ddd, m, f, s, k, n, o]


def generate(word_count: int, caps_rate: int, name: str):
    res = []
    priv = ''
    if name:
        priv += f'Привет, {name}! '
    caps_rate %= 100
    priv += 'Ты, '
    word_count_now = 0
    while word_count_now < word_count:
        tempi = word_count + 1
        while word_count_now + tempi > word_count:
            random.seed()
            y = random.choice(gens)
            x = []
            for j in y:
                x.append(random.choice(array[int(j)]))
            x = ' '.join(x)
            tempi = len(x.split())
        res.append(x)
        word_count_now += tempi
    res = ', '.join(res)
    res = res.split()
    count = 0
    kek = random.randint(sentence_min, sentence_max)
    for v in range(len(res)):
        if res[v].endswith(','):
            count += 1
            if count % kek == 0:
                count = 0
                random.seed()
                kek = random.randint(sentence_min, sentence_max)
                res[v] = res[v][:-1] + '.'
                if v < len(res) - 1:
                    res[v + 1] = res[v + 1][0].upper() + res[v + 1][1:]
    res[0] = priv + res[0]
    res = ' '.join(res).split()
    for v in range(len(res)):
        random.seed()
        z = random.randint(0, 99)
        if z < caps_rate:
            res[v] = res[v].upper()
    return ' '.join(res) + '.'
# КТО ТО ЭТО ЕЩЁ ЧИТАЕТ?


logger = logging.getLogger(__name__)


def register(cb):
    cb(Tralka())


class Tralka(loader.Module):
    """Generates pastes"""

    def __init__(self):
        self.name = ("Pastes")
        self._me = None
        self._ratelimit = []

    async def client_ready(self, client, db):
        self._db = db
        self._client = client
        self._me = await client.get_me()

    async def tralkacmd(self, message):
        """.tralka <word_count> <caps_rate (in %)> <recepient name>"""
        args = utils.get_args(message)
        chatid = str(message.chat_id)
        if len(args) < 2:
            await utils.answer(message, "Проверь, ты всё указал правильно?")
        elif len(args) == 2:
            await utils.answer(message, generate(int(args[0]), int(args[1]), None))
        else:
            await utils.answer(message, generate(int(args[0]), int(args[1]), args[2]))
