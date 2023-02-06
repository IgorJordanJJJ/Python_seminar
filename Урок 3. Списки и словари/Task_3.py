#В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;B, C, M, P – 3 очка;F, H, V, W, Y – 4 очка;K – 5 очков;J, X – 8 очков;Q, Z – 10 очков.
# А русские буквы оцениваются так:А, В, Е, И, Н, О, Р, С, Т – 1 очко;Д, К, Л, М, П, У – 2 очка;Б, Г, Ё, Ь, Я – 3 очка
# ;Й, Ы – 4 очка;Ж, З, Х, Ц, Ч – 5 очков;Ш, Э, Ю – 8 очков;Ф, Щ, Ъ – 10 очков.Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
#Пример
#ноутбук
#12



# scrabble_english_points = {
#     'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
#     'D': 2, 'G': 2,
#     'B': 3, 'C': 3, 'M': 3, 'P': 3,
#     'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
#     'K': 5,
#     'J': 8, 'X': 8,
#     'Q': 10, 'Z': 10
# }

# scrabble_russian_points = {
#     'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
#     'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
#     'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
#     'Й': 4, 'Ы': 4,
#     'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
#     'Ш': 8, 'Э': 8, 'Ю': 8,
#     'Ф': 10, 'Щ': 10, 'Ъ': 10
# }

# word = input("Enter word: ")

# if all(c in scrabble_english_points for c in word.upper()):
#     points = sum(scrabble_english_points[c] for c in word.upper())
# elif all(c in scrabble_russian_points for c in word):
#     points = sum(scrabble_russian_points[c] for c in word)
# else:
#     print("Invalid word")
#     exit()

# print("The word costs", points, "points in Scrabble.")

# def score_word(word):
#     score = 0
#     for letter in word:
#         letter = letter.upper()
#         if letter in 'AEIOULNRST':
#             score += 1
#         elif letter in 'DG':
#             score += 2
#         elif letter in 'BCMP':
#             score += 3
#         elif letter in 'FHVWY':
#             score += 4
#         elif letter in 'K':
#             score += 5
#         elif letter in 'JX':
#             score += 8
#         elif letter in 'QZ':
#             score += 10
#     return score

# def score_russian_word(word):
#     score = 0
#     for letter in word:
#         letter = letter.upper()
#         if letter in 'АВЕИНОРСТ':
#             score += 1
#         elif letter in 'ДКЛМПУ':
#             score += 2
#         elif letter in 'БГЁЬЯ':
#             score += 3
#         elif letter in 'ЙЫ':
#             score += 4
#         elif letter in 'ЖЗХЦЧ':
#             score += 5
#         elif letter in 'ШЭЮ':
#             score += 8
#         elif letter in 'ФЩЪ':
#             score += 10
#     return score

# def get_word_score(word):
#     score = 0
#     if all(letter.isascii() for letter in word):
#         score = score_word(word)
#     elif all(letter.isalpha() for letter in word):
#         score = score_russian_word(word)
#     else:
#         print("Error: Invalid word")
#         return
#     return score

# word = input("Enter a word: ")
# word_score = get_word_score(word)

# if word_score is not None:
#     print("The score for the word '" + word + "' is: " + str(word_score))

def calculate_word_value(word, language):
    english_letters_values = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1, 'D': 2, 'G': 2, 'B': 3, 'C': 3, 'M': 3, 'P': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'K': 5, 'J': 8, 'X': 8, 'Q': 10, 'Z': 10}
    russian_letters_values = {'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1, 'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2, 'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3, 'Й': 4, 'Ы': 4, 'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5, 'Ш': 8, 'Э': 8, 'Ю': 8, 'Ф': 10, 'Щ': 10, 'Ъ': 10}
    
    if language.upper() == 'ENGLISH':
        letters_values = english_letters_values
    elif language.upper() == 'RUSSIAN':
        letters_values = russian_letters_values
    else:
        return 'Invalid language selected'

    word_value = 0
    for letter in word:
        word_value += letters_values.get(letter.upper(), 0)
    
    return word_value

word = input('Enter a word: ')
language = input('Enter the language (English or Russian): ')

word_value = calculate_word_value(word, language)
print('Word value:', word_value)