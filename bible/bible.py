import pandas as pd

bible_path = r"C:\\GitHub\\worship_assistant\\bible\\"
book_dict = {1: ['창세기', '창'], 2: ['출애굽기', '출'], 3: ['레위기', '레'], 4: ['민수기', '민'], 5: ['신명기', '신'], 6: ['여호수아', '수'], 7: ['사사기', '삿'], 8: ['룻기', '룻'], 9: ['사무엘상', '삼상'], 10: ['사무엘하', '삼하'], 11: ['열왕기상', '왕상'], 12: ['열왕기하', '왕하'], 13: ['역대상', '대상'], 14: ['역대하', '대하'], 15: ['에스라', '스'], 16: ['느헤미야', '느'], 17: ['에스더', '에'], 18: ['욥기', '욥'], 19: ['시편', '시'], 20: ['잠언', '잠'], 21: ['전도서', '전'], 22: ['아가', '아'], 23: ['이사야', '사'], 24: ['예레미야', '렘'], 25: ['예레미야애가', '애'], 26: ['에스겔', '겔'], 27: ['다니엘', '단'], 28: ['호세아', '호'], 29: ['요엘', '욜'], 30: ['아모스', '암'], 31: ['오바댜', '옵'], 32: ['요나', '욘'], 33: ['미가', '미'], 34: ['나훔', '나'], 35: ['하박국', '합'], 36: ['스바냐', '습'], 37: ['학개', '학'], 38: ['스가랴', '슥'], 39: ['말라기', '말'], 40: ['마태복음', '마'], 41: ['마가복음', '막'], 42: ['누가복음', '눅'], 43: ['요한복음', '요'], 44: ['사도행전', '행'], 45: ['로마서', '롬'], 46: ['고린도전서', '고전'], 47: ['고린도후서', '고후'], 48: ['갈라디아서', '갈'], 49: ['에베소서', '엡'], 51: ['골로새서', '골'], 52: ['데살로니가전서', '살전'], 53: ['데살로니가후서', '살후'], 54: ['디모데전서', '딤전'], 55: ['디모데후서', '딤후'], 56: ['디도서', '딛'], 57: ['빌레몬서', '빌'], 58: ['히브리서', '히'], 59: ['야고보서', '약'], 60: ['베드로전서', '벧전'], 61: ['베드로후서', '벧후'], 62: ['요한일서', '요1'], 63: ['요한이서', '요2'], 64: ['요한삼서', '요3'], 65: ['유다서', '유'], 66: ['요한계시록', '계']}
entry = 'kjv 창 1 1'

def book_key(input):
    for key, values in book_dict.items():
        if input in values:
            return str(key)
    return None

def csv_format(input):
    if len(input) == 1:
        output = '00'+input
    elif len(input) == 2:
        output = '0'+input
    return output

def find_scripture(bible, query):
    df = pd.read_csv(bible_path+bible+'.csv', encoding='CP949')
    scripture = df[df['id'] == int(query)]['t'].values[0]
    return scripture


def scripture(entry):
    # entry = input('bible(gae/kjv) | book | ch | verse 1 \n')

    input_dict = {
        'bible': entry.split()[0],
        'book': entry.split()[1],
        'ch': entry.split()[2],
        'verse1': entry.split()[3],
        # 'verse2': entry.split()[4]
    }

    bible = input_dict['bible']
    df = pd.read_csv(bible_path+bible+'.csv', encoding='CP949')
    book = book_key(input_dict['book'])
    chapter = csv_format(input_dict['ch'])
    verse1 = csv_format(input_dict['verse1'])
    query = book+chapter+verse1

    scripture = find_scripture(bible, query)

    print(scripture)

    output_dict = {
        'user_input': f'{book_dict[int(book)][0]} {input_dict["ch"]}장 {input_dict["verse1"]}절',
        'bible': bible,
        'query': int(query),
        'scripture': scripture
    }

    return output_dict

if __name__ == '__main__':
    scripture(entry)
