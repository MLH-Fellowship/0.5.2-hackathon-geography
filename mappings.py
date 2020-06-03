# plus_codes_list = [2, 3, 4, 5, 6, 7, 8, 9, 'C', 'F', 'G', 'H', 'J', 'M', 'P',
#                    'Q', 'R', 'V', 'W', 'X']
# words_list = []
#
# words_file = open('../words.txt', 'r')
# lines = words_file.readlines()
# for line in lines:
#     words_list.append("'" + line.strip() + "'")
#
# i = 0
# j = 0
# k = 0
#
# while i < len(plus_codes_list):
#     while j < len(plus_codes_list):
#         print("'" + str(plus_codes_list[i]) + str(plus_codes_list[j]) + "'" +
#               ": " + words_list[k] + ',')
#         j += 1
#         k += 1
#     i += 1
#     j = 0
#
# m = 0
# while k < len(words_list) and m < len(plus_codes_list):
#     print(f"'{plus_codes_list[m]}': {words_list[k]},")
#     m += 1
#     k += 1

map = {
    '22': 'find',
    '23': 'work',
    '24': 'part',
    '25': 'take',
    '26': 'place',
    '27': 'made',
    '28': 'live',
    '29': 'where',
    '2C': 'after',
    '2F': 'back',
    '2G': 'little',
    '2H': 'only',
    '2J': 'round',
    '2M': 'year',
    '2P': 'came',
    '2Q': 'show',
    '2R': 'every',
    '2V': 'good',
    '2W': 'give',
    '2X': 'under',
    '32': 'name',
    '33': 'very',
    '34': 'through',
    '35': 'just',
    '36': 'form',
    '37': 'sentence',
    '38': 'great',
    '39': 'think',
    '3C': 'help',
    '3F': 'low',
    '3G': 'line',
    '3H': 'differ',
    '3J': 'turn',
    '3M': 'cause',
    '3P': 'much',
    '3Q': 'mean',
    '3R': 'before',
    '3V': 'move',
    '3W': 'right',
    '3X': 'same',
    '42': 'tell',
    '43': 'does',
    '44': 'three',
    '45': 'want',
    '46': 'well',
    '47': 'also',
    '48': 'play',
    '49': 'small',
    '4C': 'home',
    '4F': 'read',
    '4G': 'hand',
    '4H': 'port',
    '4J': 'large',
    '4M': 'spell',
    '4P': 'even',
    '4Q': 'land',
    '4R': 'here',
    '4V': 'must',
    '4W': 'high',
    '4X': 'such',
    '52': 'follow',
    '53': 'change',
    '54': 'went',
    '55': 'light',
    '56': 'kind',
    '57': 'need',
    '58': 'house',
    '59': 'picture',
    '5C': 'again',
    '5F': 'animal',
    '5G': 'point',
    '5H': 'mother',
    '5J': 'world',
    '5M': 'near',
    '5P': 'build',
    '5Q': 'self',
    '5R': 'earth',
    '5V': 'father',
    '5W': 'head',
    '5X': 'stand',
    '62': 'page',
    '63': 'should',
    '64': 'country',
    '65': 'found',
    '66': 'answer',
    '67': 'school',
    '68': 'grow',
    '69': 'study',
    '6C': 'still',
    '6F': 'learn',
    '6G': 'plant',
    '6H': 'cover',
    '6J': 'food',
    '6M': 'four',
    '6P': 'between',
    '6Q': 'state',
    '6R': 'keep',
    '6V': 'never',
    '6W': 'last',
    '6X': 'thought',
    '72': 'city',
    '73': 'tree',
    '74': 'cross',
    '75': 'farm',
    '76': 'hard',
    '77': 'start',
    '78': 'might',
    '79': 'story',
    '7C': 'draw',
    '7F': 'left',
    '7G': 'late',
    '7H': 'while',
    '7J': 'press',
    '7M': 'close',
    '7P': 'night',
    '7Q': 'real',
    '7R': 'life',
    '7V': 'north',
    '7W': 'open',
    '7X': 'seem',
    '82': 'together',
    '83': 'next',
    '84': 'white',
    '85': 'children',
    '86': 'begin',
    '87': 'walk',
    '88': 'example',
    '89': 'ease',
    '8C': 'paper',
    '8F': 'group',
    '8G': 'always',
    '8H': 'music',
    '8J': 'those',
    '8M': 'both',
    '8P': 'mark',
    '8Q': 'often',
    '8R': 'letter',
    '8V': 'until',
    '8W': 'mile',
    '8X': 'river',
    '92': 'feet',
    '93': 'care',
    '94': 'second',
    '95': 'book',
    '96': 'carry',
    '97': 'took',
    '98': 'science',
    '99': 'room',
    '9C': 'friend',
    '9F': 'began',
    '9G': 'idea',
    '9H': 'fish',
    '9J': 'mountain',
    '9M': 'stop',
    '9P': 'once',
    '9Q': 'base',
    '9R': 'hear',
    '9V': 'horse',
    '9W': 'sure',
    '9X': 'watch',
    'C2': 'color',
    'C3': 'face',
    'C4': 'wood',
    'C5': 'main',
    'C6': 'enough',
    'C7': 'plain',
    'C8': 'girl',
    'C9': 'usual',
    'CC': 'young',
    'CF': 'ready',
    'CG': 'above',
    'CH': 'ever',
    'CJ': 'list',
    'CM': 'though',
    'CP': 'feel',
    'CQ': 'talk',
    'CR': 'bird',
    'CV': 'soon',
    'CW': 'body',
    'CX': 'family',
    'F2': 'direct',
    'F3': 'pose',
    'F4': 'leave',
    'F5': 'song',
    'F6': 'measure',
    'F7': 'door',
    'F8': 'product',
    'F9': 'black',
    'FC': 'short',
    'FF': 'numeral',
    'FG': 'class',
    'FH': 'wind',
    'FJ': 'question',
    'FM': 'happen',
    'FP': 'complete',
    'FQ': 'ship',
    'FR': 'area',
    'FV': 'half',
    'FW': 'rock',
    'FX': 'order',
    'G2': 'fire',
    'G3': 'south',
    'G4': 'problem',
    'G5': 'piece',
    'G6': 'told',
    'G7': 'knew',
    'G8': 'pass',
    'G9': 'since',
    'GC': 'whole',
    'GF': 'king',
    'GG': 'space',
    'GH': 'heard',
    'GJ': 'best',
    'GM': 'hour',
    'GP': 'better',
    'GQ': 'true',
    'GR': 'during',
    'GV': 'hundred',
    'GW': 'five',
    'GX': 'remember',
    'H2': 'step',
    'H3': 'early',
    'H4': 'hold',
    'H5': 'west',
    'H6': 'ground',
    'H7': 'interest',
    'H8': 'reach',
    'H9': 'fast',
    'HC': 'verb',
    'HF': 'sing',
    'HG': 'listen',
    'HH': 'table',
    'HJ': 'travel',
    'HM': 'less',
    'HP': 'morning',
    'HQ': 'simple',
    'HR': 'several',
    'HV': 'vowel',
    'HW': 'toward',
    'HX': 'against',
    'J2': 'pattern',
    'J3': 'slow',
    'J4': 'center',
    'J5': 'love',
    'J6': 'person',
    'J7': 'money',
    'J8': 'serve',
    'J9': 'appear',
    'JC': 'road',
    'JF': 'rain',
    'JG': 'rule',
    'JH': 'govern',
    'JJ': 'pull',
    'JM': 'cold',
    'JP': 'notice',
    'JQ': 'voice',
    'JR': 'unit',
    'JV': 'power',
    'JW': 'town',
    'JX': 'fine',
    'M2': 'certain',
    'M3': 'fall',
    'M4': 'lead',
    'M5': 'dark',
    'M6': 'machine',
    'M7': 'note',
    'M8': 'wait',
    'M9': 'plan',
    'MC': 'figure',
    'MF': 'star',
    'MG': 'noun',
    'MH': 'field',
    'MJ': 'rest',
    'MM': 'correct',
    'MP': 'able',
    'MQ': 'pound',
    'MR': 'done',
    'MV': 'beauty',
    'MW': 'drive',
    'MX': 'stood',
    'P2': 'contain',
    'P3': 'front',
    'P4': 'teach',
    'P5': 'week',
    'P6': 'final',
    'P7': 'gave',
    'P8': 'green',
    'P9': 'quick',
    'PC': 'develop',
    'PF': 'ocean',
    'PG': 'warm',
    'PH': 'free',
    'PJ': 'minute',
    'PM': 'strong',
    'PP': 'special',
    'PQ': 'mind',
    'PR': 'behind',
    'PV': 'clear',
    'PW': 'tail',
    'PX': 'produce',
    'Q2': 'fact',
    'Q3': 'street',
    'Q4': 'inch',
    'Q5': 'multiply',
    'Q6': 'nothing',
    'Q7': 'course',
    'Q8': 'stay',
    'Q9': 'wheel',
    'QC': 'full',
    'QF': 'force',
    'QG': 'blue',
    'QH': 'object',
    'QJ': 'decide',
    'QM': 'surface',
    'QP': 'deep',
    'QQ': 'moon',
    'QR': 'island',
    'QV': 'foot',
    'QW': 'system',
    'QX': 'busy',
    'R2': 'test',
    'R3': 'record',
    'R4': 'boat',
    'R5': 'common',
    'R6': 'gold',
    'R7': 'possible',
    'R8': 'plane',
    'R9': 'stead',
    'RC': 'wonder',
    'RF': 'laugh',
    'RG': 'thousand',
    'RH': 'check',
    'RJ': 'game',
    'RM': 'shape',
    'RP': 'equate',
    'RQ': 'miss',
    'RR': 'brought',
    'RV': 'heat',
    'RW': 'snow',
    'RX': 'tire',
    'V2': 'bring',
    'V3': 'distant',
    'V4': 'fill',
    'V5': 'east',
    'V6': 'paint',
    'V7': 'language',
    'V8': 'among',
    'V9': 'grand',
    'VC': 'ball',
    'VF': 'wave',
    'VG': 'drop',
    'VH': 'heart',
    'VJ': 'present',
    'VM': 'heavy',
    'VP': 'dance',
    'VQ': 'engine',
    'VR': 'position',
    'VV': 'wide',
    'VW': 'sail',
    'VX': 'material',
    'W2': 'size',
    'W3': 'vary',
    'W4': 'settle',
    'W5': 'speak',
    'W6': 'weight',
    'W7': 'general',
    'W8': 'matter',
    'W9': 'circle',
    'WC': 'pair',
    'WF': 'include',
    'WG': 'divide',
    'WH': 'syllable',
    'WJ': 'felt',
    'WM': 'perhaps',
    'WP': 'pick',
    'WQ': 'sudden',
    'WR': 'count',
    'WV': 'square',
    'WW': 'reason',
    'WX': 'length',
    'X2': 'represent',
    'X3': 'subject',
    'X4': 'region',
    'X5': 'energy',
    'X6': 'hunt',
    'X7': 'probable',
    'X8': 'brother',
    'X9': 'ride',
    'XC': 'cell',
    'XF': 'believe',
    'XG': 'fraction',
    'XH': 'forest',
    'XJ': 'race',
    'XM': 'window',
    'XP': 'store',
    'XQ': 'summer',
    'XR': 'train',
    'XV': 'sleep',
    'XW': 'prove',
    'XX': 'lone',
    '2': 'exercise',
    '3': 'wall',
    '4': 'catch',
    '5': 'mount',
    '6': 'wish',
    '7': 'board',
    '8': 'winter',
    '9': 'written',
    'C': 'wild',
    'F': 'instrument',
    'G': 'kept',
    'H': 'glass',
    'J': 'grass',
    'M': 'edge',
    'P': 'sign',
    'Q': 'visit',
    'R': 'past',
    'V': 'soft',
    'W': 'bright',
    'X': 'weather',
}

word_to_plus_code_mapping = {v: k for k, v in map.items()}