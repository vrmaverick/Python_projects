from translate import Translator
languages = {
    1: {'name': 'English', 'code': 'en'},
    2: {'name': 'Chinese', 'code': 'zh'},
    3: {'name': 'Spanish', 'code': 'es'},
    4: {'name': 'Hindi', 'code': 'hi'},
    5: {'name': 'Arabic', 'code': 'ar'},
    6: {'name': 'Bengali', 'code': 'bn'},
    7: {'name': 'Russian', 'code': 'ru'},
    8: {'name': 'Portuguese', 'code': 'pt'},
    9: {'name': 'Indonesian', 'code': 'id'},
    10: {'name': 'Urdu', 'code': 'ur'},
    11: {'name': 'German', 'code': 'de'},
    12: {'name': 'Japanese', 'code': 'ja'},
    13: {'name': 'Swahili', 'code': 'sw'},
    14: {'name': 'Telugu', 'code': 'te'},
    15: {'name': 'Marathi', 'code': 'mr'},
    16: {'name': 'Turkish', 'code': 'tr'},
    17: {'name': 'Tamil', 'code': 'ta'},
    18: {'name': 'French', 'code': 'fr'},
    19: {'name': 'Vietnamese', 'code': 'vi'},
    20: {'name': 'Korean', 'code': 'ko'},
    21: {'name': 'Italian', 'code': 'it'},
    22: {'name': 'Persian', 'code': 'fa'},
    23: {'name': 'Polish', 'code': 'pl'},
    24: {'name': 'Ukrainian', 'code': 'uk'},
    25: {'name': 'Malayalam', 'code': 'ml'},
    26: {'name': 'Kannada', 'code': 'kn'},
    27: {'name': 'Gujarati', 'code': 'gu'},
    28: {'name': 'Thai', 'code': 'th'},
    29: {'name': 'Romanian', 'code': 'ro'},
    30: {'name': 'Dutch', 'code': 'nl'},
    31: {'name': 'Swedish', 'code': 'sv'},
    32: {'name': 'Czech', 'code': 'cs'},
    33: {'name': 'Greek', 'code': 'el'},
    34: {'name': 'Danish', 'code': 'da'},
    35: {'name': 'Finnish', 'code': 'fi'},
    36: {'name': 'Hungarian', 'code': 'hu'},
    37: {'name': 'Norwegian', 'code': 'no'},
    38: {'name': 'Hebrew', 'code': 'he'},
    39: {'name': 'Slovak', 'code': 'sk'},
    40: {'name': 'Catalan', 'code': 'ca'},
    41: {'name': 'Lithuanian', 'code': 'lt'},
    42: {'name': 'Slovenian', 'code': 'sl'},
    43: {'name': 'Irish', 'code': 'ga'},
    44: {'name': 'Estonian', 'code': 'et'},
    45: {'name': 'Icelandic', 'code': 'is'},
    46: {'name': 'Latvian', 'code': 'lv'},
    47: {'name': 'Croatian', 'code': 'hr'},
    48: {'name': 'Bosnian', 'code': 'bs'},
    49: {'name': 'Serbian', 'code': 'sr'},
    50: {'name': 'Albanian', 'code': 'sq'},
    51: {'name': 'Macedonian', 'code': 'mk'},
    52: {'name': 'Malay', 'code': 'ms'},
    53: {'name': 'Bulgarian', 'code': 'bg'},
    54: {'name': 'Afrikaans', 'code': 'af'},
    55: {'name': 'Georgian', 'code': 'ka'},
    56: {'name': 'Belarusian', 'code': 'be'},
    57: {'name': 'Armenian', 'code': 'hy'},
    58: {'name': 'Kurdish', 'code': 'ku'},
    59: {'name': 'Luxembourgish', 'code': 'lb'},
    60: {'name': 'Basque', 'code': 'eu'},
    61: {'name': 'Mongolian', 'code': 'mn'},
    62: {'name': 'Azerbaijani', 'code': 'az'},
    63: {'name': 'Uzbek', 'code': 'uz'},
    64: {'name': 'Amharic', 'code': 'am'},
    65: {'name': 'Farsi', 'code': 'fa'},
    66: {'name': 'Gaelic', 'code': 'gd'},
    67: {'name': 'Kazakh', 'code': 'kk'},
    68: {'name': 'Pashto', 'code': 'ps'},
    69: {'name': 'Nepali', 'code': 'ne'},
    70: {'name': 'Burmese', 'code': 'my'},
    71: {'name': 'Zulu', 'code': 'zu'},
    72: {'name': 'Yoruba', 'code': 'yo'},
    73: {'name': 'Haitian Creole', 'code': 'ht'},
    74: {'name': 'Cebuano', 'code': 'ceb'},
    75: {'name': 'Javanese', 'code': 'jv'},
    76: {'name': 'Malagasy', 'code': 'mg'},
    77: {'name': 'Somali', 'code': 'so'},
    78: {'name': 'Uighur', 'code': 'ug'},
    79: {'name': 'Galician', 'code': 'gl'},
    80: {'name': 'Tajik', 'code': 'tg'},
    81: {'name': 'Sinhala', 'code': 'si'},
    82: {'name': 'Hausa', 'code': 'ha'},
    83: {'name': 'Sundanese', 'code': 'su'},
    84: {'name': 'Kannada', 'code': 'kn'},
    85: {'name': 'Igbo', 'code': 'ig'},
    86: {'name': 'Xhosa', 'code': 'xh'},
    87: {'name': 'Maltese', 'code': 'mt'},
    88: {'name': 'Yiddish', 'code': 'yi'},
    89: {'name': 'Maori', 'code': 'mi'},
    90: {'name': 'Hmong', 'code': 'hmn'},
    91: {'name': 'Corsican', 'code': 'co'},
    92: {'name': 'Kyrgyz', 'code': 'ky'},
    93: {'name': 'Sesotho', 'code': 'st'},
    94: {'name': 'Khmer', 'code': 'km'},
    95: {'name': 'Scots Gaelic', 'code': 'gd'},
    96: {'name': 'Hawaiian', 'code': 'haw'},
    97: {'name': 'Shona', 'code': 'sn'},
    98: {'name': 'Frisian', 'code': 'fy'},
    99: {'name': 'Lao', 'code': 'lo'},
    100: {'name': 'Samoan', 'code': 'sm'}
}
fi=input("enter the file name with correct path .txt extension : ")
print("Top 30 Languages:")
for num, language in languages.items():
    print(f"{num}. {language['name']}")

while True:
    try:
        choice = int(input("Enter the number corresponding to the language: "))
        if choice in languages:
            print(f"ISO 639-1 Code: {languages[choice]['code']}")
            c = languages[choice]['code']
            translator=Translator(to_lang=c)
            try:
                with open(fi, mode='r') as my_text:
                    print("Original text : ")
                    print(my_text.read())
                    my_text.seek(0)
                    text = my_text.read()
                    trans=translator.translate(text)
                    print("Translate text : ")
                    print(trans)
            except FileNotFoundError as err:
                    print('file not found check file path')
                    raise err
            break
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")


