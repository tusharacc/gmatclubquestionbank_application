
__author__ = 'Tushar Saurabh'

import requests
import logging
from bs4 import BeautifulSoup
#from enum import Enum


def prepare_string(str, length):
    in_str_len = len(str)
    output_str = str
    for x in range(1, (length - in_str_len)):
        output_str += " "
    return output_str

logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)
file = open('link_detail.txt','r')
out_fl = open('question_detail.txt','w',encoding='utf-8')
QUESTION_TYPE = 'CR'

for line in file:
    input_question_type = line[0:15]
    input_question_topic = line[16:200]
    input_question_link = line[213:499]
    logging.debug(input_question_topic+" "+input_question_type+" "+input_question_link)
    print(input_question_link)
    if input_question_type[0:2]==QUESTION_TYPE:

        res = requests.get(input_question_link.strip())
        try:
            res.raise_for_status()
            soup = BeautifulSoup(res.text,'html.parser')
            all_response = soup.find_all('div',class_='item text')
            #logging.debug("Tushar +" +all_response[0])
            if len(all_response[0].select('.downRow')) > 0:
                print('tushar')
                get_question = all_response[0].getText()
                answer_div = all_response[0].select('.downRow')
                answer = answer_div[0].getText()
                question_type = prepare_string(input_question_type,15)
                question_topic = prepare_string(input_question_topic,200)
                question_answer = prepare_string(answer,10)
                question_question = prepare_string(get_question,2000)
                out_fl.write(question_type+question_topic+question_answer+question_question+'\n')
            exit(1)
        except Exception as ex:
            print('There was a problem: %s' % (ex))


file.close()
out_fl.close()
