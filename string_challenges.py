# Вывести последнюю букву в слове
def output_last_letter():
   return word[-1]

word = 'Архангельск'
print('Последняя буква слова-',output_last_letter(),'\n')

# Вывести количество букв "а" в слове
def output_len_word():
   return len(word_1)

word_1 = 'Архангельск'
print('Количество букв в слов-',output_len_word(),'\n')


# Вывести количество гласных букв в слове
def calculate_vowel_letters():
    count_vowel = 0
    for letter in vowel_letters:
        if letter in word_2:
             count_vowel += 1
    return count_vowel

vowel_letters = 'А, а, е, ё, и, о, у, ы, э, ю, я'
word_2 = 'Архангельск'
print('Количество гласных букв в слове-',calculate_vowel_letters(),'\n')

# Вывести количество слов в предложении
def output_len_words():
   return len(sentence.split())

sentence = 'Мы приехали в гости'
print('Количество слов в предложении -',output_len_words(),'\n')

# Вывести первую букву каждого слова на отдельной строке
def output_first_letter():
   for word in sentence_1.split():
       print('Первая буква в слове',word,'-',word[0])

sentence_1 = 'Мы приехали в гости'
output_first_letter()
print()

# Вывести усреднённую длину слова в предложении
def calc_average_word():
    return round((len(sentence_2)/len(sentence_2.split())),1)

sentence_2 = 'Мы приехали в гости'
print('Усреднённая длина слова-',calc_average_word())

