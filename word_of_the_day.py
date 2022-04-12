import random
import datetime

def make_dic(new_file):    # string is taken in, returned to dict.
    new_Dic = {}
    for i in range(97, 123):    # key value pair is appended to dict. with keys as ascii dec codes (97=122) are on an empty list
        new_Dic[chr(i)] = []

    file = open(new_file)  # dictionary then gets populated
    for line in file:
        new_Dic[line[0]].append(line.strip())
    file.close()
    return new_Dic

def get_word_of_the_giorno(giorno):     # int for day is returned with string after it's sequestered
    wordsDic = make_dic("words.txt")
    if giorno <= 26:    # day(giorno) is within range of 26
        giorno = giorno - 1
    else:
        giorno = (giorno % 26) - 1

    return random.choice(wordsDic[giorno])


if __name__ == '__main__':
  print(get_word_of_the_giorno(datetime.datetime.today().day))