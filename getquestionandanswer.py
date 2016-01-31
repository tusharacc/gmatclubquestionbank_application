'''
The program takes the input file created by 'questionlink.py' and creates a JSON of questions and answers for a
particular section.

JSON Structure = [{'question_type':'CR','question':'html','answer':'A','used':'No','response':'NA'}]
question_type can be high, medium or low for each section
used is used to identify if the question has been displayed to audience
response will store whether user response was correct or not

The program output is stored in "section_complexity_question_detail.txt".

To download questions for SC, change the variable QUESTION_TYPE to SC_HIGH or SC_LOW or SC_MEDIUM as appropriate.
'''

__author__ = 'Tushar Saurabh'

import requests
import logging
from bs4 import BeautifulSoup
import json
#from enum import Enum


def prepare_string(str, length):
    in_str_len = len(str)
    output_str = str
    for x in range(1, (length - in_str_len)):
        output_str += " "
    return output_str


QUESTION_TYPE = 'SC_HIGH'
question_json_array = []

logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)
file = open('link_detail.txt','r',encoding='utf-8')
out_fl = open(QUESTION_TYPE.lower()+'_question_detail.txt','w',encoding='utf-8')
question_collected = 0
question_rejected = 0
for line in file:
    question_json = {}
    input_question_type = line[0:15]
    input_question_topic = line[16:200]
    input_question_link = line[213:499]
    logging.debug(input_question_topic+" "+input_question_type+" "+input_question_link)
    print(input_question_link)
    if input_question_type[0:len(QUESTION_TYPE)]==QUESTION_TYPE:

        res = requests.get(input_question_link.strip())
        try:
            res.raise_for_status()
            soup = BeautifulSoup(res.text,'html.parser')
            all_response = soup.find_all('div',class_='item text',limit=1)
            #logging.debug(all_response[0])
            #logging.debug("Tushar +" +all_response[0])
            if len(all_response[0].select('.downRow')) > 0:
                question_collected += 1
                answer_div = all_response[0].select('.downRow')
                answer = answer_div[0].getText()
                all_response[0].div.decompose()
                p_elem = all_response[0].select('p')
                if len(p_elem) > 0:
                    all_response[0].p.decompose()
                logging.debug(all_response[0])
                question_json['question_type'] = input_question_type
                question_json['question'] = all_response[0].prettify().replace('\n','')
                question_json['answer'] = answer
                question_json['used'] = 'No'
                question_json['response'] = 'NA'
                logging.debug("JSON Onject" + str(question_json))
                question_json_array.append(question_json)
                '''
                question_type = prepare_string(input_question_type,15)
                question_topic = prepare_string(input_question_topic,200)
                question_answer = prepare_string(answer,10)
                question_question = prepare_string(all_response[0].prettify().replace('\n',''),2000)

                out_fl.write(question_answer+question_question+'\n')
                '''
            else:
                question_rejected += 1
            '''
            if question_collected > 25:
                json.dump(question_json_array,out_fl)
                exit(1)
            '''
        except Exception as ex:
            print('There was a problem: %s' % (ex))

json.dump(question_json_array,out_fl)
print('The questions accepted: %s & the question rejected %s' % (question_collected,question_rejected ))
file.close()
out_fl.close()
