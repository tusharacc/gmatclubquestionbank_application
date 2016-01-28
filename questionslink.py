'''
The code will download link & topic of questions from GMATCLUB.com.
Currently it is downloading questions for CR,SC,PS & DS and 100 questions per difficulty level(600-, 600-700 & 700+

If User needs to get more than 100 question, please include the additional links in list links.
Please note, even links could be automated, however I hardcoded to avoid additional logic.

'''


__author__ = 'Tushar Saurabh'

import requests
import logging
from bs4 import BeautifulSoup
from enum import Enum


class ID(Enum):
    DS_HIGH = 180
    DS_MEDIUM = 222
    DS_LOW = 223
    PS_HIGH = 187
    PS_MEDIUM = 216
    PS_LOW = 217
    CR_HIGH = 168
    CR_MEDIUM = 226
    CR_LOW = 227
    SC_HIGH = 172
    SC_MEDIUM = 231
    SC_LOW = 232


MAXIMUM_TOPIC = 100


def prepare_string(str, length):
    in_str_len = len(str)
    output_str = str
    for x in range(1, (length - in_str_len)):
        output_str += " "
    return output_str

logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)
file = open('link_detail.txt', 'w',encoding='utf-8')
for id in ID:

    links = {'http://gmatclub.com/forum/search.php?search_id=tag&tag_id=' + str(id.value),
             'http://gmatclub.com/forum/search.php?st=0&sk=t&sd=d&sr=topics&search_id=tag&tag_id=' + str(
                 id.value) + '&similar_to_id=0&search_tags=any&search_id=tag&start=50',
             'http://gmatclub.com/forum/search.php?st=0&sk=t&sd=d&sr=topics&search_id=tag&tag_id=' + str(
                 id.value) + '&similar_to_id=0&search_tags=any&search_id=tag&start=100',
             'http://gmatclub.com/forum/search.php?st=0&sk=t&sd=d&sr=topics&search_id=tag&tag_id=' + str(
                 id.value) + '&similar_to_id=0&search_tags=any&search_id=tag&start=150',
             'http://gmatclub.com/forum/search.php?st=0&sk=t&sd=d&sr=topics&search_id=tag&tag_id=' + str(
                 id.value) + '&similar_to_id=0&search_tags=any&search_id=tag&start=200',
             'http://gmatclub.com/forum/search.php?st=0&sk=t&sd=d&sr=topics&search_id=tag&tag_id=' + str(
                 id.value) + '&similar_to_id=0&search_tags=any&search_id=tag&start=250',
             'http://gmatclub.com/forum/search.php?st=0&sk=t&sd=d&sr=topics&search_id=tag&tag_id=' + str(
                 id.value) + '&similar_to_id=0&search_tags=any&search_id=tag&start=300'}

    topic_count = 0

    for link in links:
        res = requests.get(link)
        end_of_file = False
        try:
            res.raise_for_status()
            soup = BeautifulSoup(res.text,'html.parser')
            all_topics = soup.select('tbody tr')
            num_of_elements = len(all_topics)
            logging.debug(all_topics)

#In below For statement, the end is hardcoded, it should be num_of_elements, however I was not able to handle End of
# Webpage scenario hence hardcoded.
            for x in range(0, 96, 2):
                if all_topics[x].get('class') == 'sub_caption':
                    end_of_file = True
                    break
                all_td_element = all_topics[x].select('td')
                logging.debug(all_td_element)
                if len(all_td_element[2]) > 1:
                    topic_count += 1
                    table_element = all_topics[x].select('.column2Table')
                    a_tag = table_element[0].select('a')
                    topic = a_tag[1].getText().strip("\n")
                    link = a_tag[1].get('href').strip("\n")
                    section_str = prepare_string(id.name, 15)
                    topic_str = prepare_string(topic, 200)
                    link_str = prepare_string(link, 500)
                    file.write(section_str + topic_str + link_str +"\n")
                if topic_count >= MAXIMUM_TOPIC or x > 98:
                    break

            if topic_count >= MAXIMUM_TOPIC or end_of_file :
                break

        except Exception as exc:
            print(all_td_element)
            print('There was a problem: %s' % (exc))
            exit(1)
file.close()