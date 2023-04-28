directions = {
    1: 'Естественнонаучная',
    2: 'Социально-гуманитарная',
    3: 'Техническая',
    4: 'Туристско-краеведческая',
    5: 'Физкультурно-спортивная',
    6: 'Художественная',
}

profiles = {
    'Естественнонаучная': [
        'Аквариумистика',
        'Астрономия',
        'Биология',
        'География',
        'Геология',
        'Животноводство',
        'Здоровье и медицина',
        'Зоология',
        'Информатика',
        'Коневодство и верховая езда',
        'Лесничество',
        'Математика',
        'Методология исследования',
        'Растениеводство',
        'Фермерство',
        'Физика',
        'Химия',
        'Экология',
    ],
    'Социально-гуманитарная': [
        'Безопасное поведение',
        'Безопасность дорожного движения / ЮИД',
        'Библиотечное дело',
        'Военно-патриотическое воспитание',
        'Волонтерство',
        'Гражданско-патриотическое воспитание',
        'Духовно-нравственное воспитание',
        'Журналистика и СМИ',
        'Здоровый образ жизни',
        'Иностранный язык',
        'История',
        'Кулинария',
        'Логопедия',
        'Маркетинг',
        'Менеджмент',
        'Организация досуга',
        'Педагогика',
        'Подготовка к школе',
        'Политология',
        'Проектная деятельность',
        'Профориентация',
        'Психология',
        'Религиоведение, теология',
        'Риторика',
        'Российское движение школьников',
        'Социальная адаптация',
        'Социальное воспитание',
        'Социология',
        'Спортивное воспитание',
        'Ученическое самоуправление или школа актив',
        'Фольклористика',
        'Экономика',
        'Экскурсоведение',
        'Этика',
        'Этнокультурное образование',
        'Юриспруденция',
        'Языки народов России (кроме русского)',
        'Языкознание (русский язык)',
    ],
    'Техническая': [
        '3D-моделирование и прототипирование',
        'Автотехника',
        'Графическая документация',
        'Инженерный',
        'Картинг',
        'Компьютерная графика',
        'Компьютерные технологии',
        'Конструирование',
        'Моделизм',
        'Моделирование',
        'Морское дело',
        'Мототехника',
        'Музыкальные технологии',
        'Мультимедийные презентации',
        'Мультипликация и кинопроизводство',
        'Научно-технический',
        'Обработка древесины',
        'Обработка металла',
        'Обслуживание вычислительной и мультимедиа техники',
        'Обслуживание и ремонт бытовой техники',
        'Обслуживание и ремонт транспортных средств',
        'Программирование',
        'Проектирование',
        'Радиотехника',
        'Радиоэлектроника',
        'Робототехника',
        'Сельскохозяйственная техника',
        'Спортивно-технический',
        'Техническое обслуживание и ремонт зданий',
        'Техническое творчество',
        'Фотография',
        'Электроника',
        'Электротехника и энергетика',
    ],
    'Туристско-краеведческая': [
        'Археология',
        'Архивное дело',
        'Велосипедный туризм',
        'Водный туризм',
        'Горный туризм',
        'Краеведение',
        'Лыжный туризм',
        'Музейное дело',
        'Ориентирование на местности',
        'Пеший туризм',
        'Поисково-спасательные работы',
        'Спелеотуризм',
        'Спортивный туризм',
        'Экологический туризм',
        'Этнический',
    ],
    'Физкультурно-спортивная': [
        'Автоспорт',
        'Адаптивная физкультура и спорт',
        'Айкидо',
        'Армреслинг',
        'Арнис (эксрима)',
        'Бадминтон',
        'Баскетбол',
        'Бег по шоссе и/или кроссы',
        'Беговые дисциплины легкой атлетики',
        'Биатлон',
        'Бильярд',
        'Бокс',
        'Велоспорт',
        'Вовинам',
        'Водные виды спорта',
        'Военно-спортивное многоборье',
        'Волейбол',
        'Вольная борьба',
        'Гандбол',
        'Гимнастика',
        'го',
        'Гребля',
        'Греко-римская борьба',
        'Дартс',
        'Дельтпланеризм',
        'Детский фитнесс',
        'Джиу-джитсу',
        'Дзюдо',
        'Йога',
        'Капоэйра',
        'Карате',
        'Кёрлинг',
        'Киберспорт',
        'Кикбоксинг',
        'Классическая борьба',
        'Кобудо',
        'Конный спорт',
        'Конькобежные виды спорта',
        'Крав-Мага',
        'Кудо',
        'Куреш',
        'Кэндо',
        'Лапта',
        'Легкоатлетические многоборья',
        'Ледолазание',
        'Лыжные виды спорта',
        'Мотоспорт',
        'Настольный теннис',
        'Национальные виды спорта',
        'Оздоровительная физкультура',
        'ОФП (общая физическая подготовка)',
        'Парапланеризм',
        'Парашютный спорт',
        'Парусный спорт',
        'Пауэрлифтинг',
        'Пейнтбол',
        'Плавание',
        'Планеризм',
        'Подвижные игры',
        'Пожарно-прикладной спорт',
        'Прыжки на батуте',
        'Пулевая стрельба',
        'Регби',
        'Роликовые коньки',
        'Рукопашный бой',
        'Самбо',
        'Санный спорт, бобслей, скелетон',
        'Сёрфинг',
        'Скалолазание',
        'Скейтбординг',
        'Сноубординг',
        'Современное пятиборье',
        'Спелеотехника',
        'Спортивная акробатика',
        'Спортивная ходьба',
        'Спортивная хореография',
        'Спортивное ориентирование',
        'Страйкбол',
        'Стрельба из лука',
        'Сумо',
        'Тайский бокс (муай-тай)',
        'Танцевальный спорт',
        'Теннис (лаун-теннис)',
        'Технические дисциплины лёгкой атлетики',
        'Тхэквондо',
        'Тяжёлая атлетика',
        'Ушу',
        'Фехтование',
        'Фигурное катание (на коньках)',
        'Фитнес',
        'Флорбол',
        'Футбол',
        'Футзал',
        'Хапкидо',
        'Хоккей',
        'Шахматы',
        'Шашки',
    ],
    'Художественная': [
        'Аппликация',
        'Бамбукоплетение',
        'Батик',
        'Берёста',
        'Бисероплетение',
        'Бумагопластика',
        'Валяние',
        'Визаж и эстетика',
        'Витраж',
        'Вокал и/или хоровое пение',
        'Вышивание',
        'Вязание',
        'Гончарное дело',
        'Графика',
        'Декламация',
        'Декоративно-прикладное искусство (смешанные техники)',
        'Декупаж',
        'Дизайн',
        'Живопись',
        'Золотное шитьё',
        'Изобразительное искусство',
        'Кондитерское искусство',
        'Кружевоплетение',
        'Литературное творчество',
        'Лозоплетение',
        'Лоскутное шитьё (пэчворк, квилтинг)',
        'Макраме',
        'Мастерство краснодеревщика',
        'Мода и дизайн одежды',
        'Мозаика',
        'Музыкальная грамота',
        'Музыкальные инструменты',
        'Набивка ткани',
        'Парикмахерское искусство',
        'Песочная анимация (рисование песком)',
        'Пирография (выжигание)',
        'Режиссура',
        'Ритмика',
        'Роспись',
        'Скрапбукинг',
        'Скульптура и/или лепка',
        'Слушание музыки',
        'Современное искусство (граффити, стрит-арт и т.д.)',
        'Театральное искусство',
        'Ткачество',
        'Фотоискусство',
        'Хореография',
        'Художественная ковка',
        'Художественная резьба',
        'Цирковое искусство',
        'Чеканка',
        'Ювелирное дело',
    ]
}
