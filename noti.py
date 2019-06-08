#!/usr/bin/python
# coding=utf-8

import sys
import time
import sqlite3
import telegram
from pprint import pprint
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from datetime import date, datetime, timedelta
import traceback
import jsonParsing
import telepot

#key = 'sea100UMmw23Xycs33F1EQnumONR%2F9ElxBLzkilU9Yr1oT4TrCot8Y2p0jyuJP72x9rG9D8CN5yuEs6AS2sAiw%3D%3D'#'여기에 API KEY를 입력하세요'
TOKEN = '889082229:AAHdaKayoSHvJLWE1Qq8yT8GBci-lXT-CeI'#'여기에 텔레그램 토큰을 입력하세요'
MAX_MSG_LENGTH = 300
baseurl = 'http://openAPI.seoul.go.kr:8088/4c566371676c64793334654f5a6a7a/json/SearchLostArticleService/1/5/'
bot = telepot.Bot(TOKEN)

def getData(name_param, pos_param):
    res_list = []

    res_body = jsonParsing.Lost_Article(name_param, pos_param)

    totalCount = len(res_body['SearchLostArticleService']['row'])
    for i in range(totalCount):
        row = res_body['SearchLostArticleService']['row'][i]['GET_DATE'] + ' ' \
              + res_body['SearchLostArticleService']['row'][i]['TAKE_PLACE'] + ' ' + res_body['SearchLostArticleService']['row'][i]['GET_NAME']
        if row:
            res_list.append(row.strip())
    return res_list

def sendMessage(user, msg):
    try:
        bot.sendMessage(user, msg)
    except:
        traceback.print_exc(file=sys.stdout)

def run(name_param, pos_param):
    conn = sqlite3.connect('logs.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS logs( user TEXT, log TEXT, PRIMARY KEY(user, log) )')
    conn.commit()

    user_cursor = sqlite3.connect('users.db').cursor()
    user_cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, location TEXT, PRIMARY KEY(user, location) )')
    user_cursor.execute('SELECT * from users')

    for data in user_cursor.fetchall():
        user, param = data[0], data[1]
        print(user, name_param, pos_param)
        res_list = getData(name_param, pos_param)
        msg = ''
        for r in res_list:
            try:
                cursor.execute('INSERT INTO logs (user,log) VALUES ("%s", "%s")'%(user,r))
            except sqlite3.IntegrityError:
                # 이미 해당 데이터가 있다는 것을 의미합니다.
                pass
            else:
                print( str(datetime.now()).split('.')[0], r )
                if len(r+msg)+1 > MAX_MSG_LENGTH:
                    sendMessage(user, msg)
                    msg = r+'\n'
                else:
                    msg += r+'\n'
        if msg:
            sendMessage(user, msg)
    conn.commit()

if __name__=='__main__':
    today = date.today()
    current_month = today.strftime('%Y%m')

    print('[',today,']received token :', TOKEN)

    pprint(bot.getMe())

    #run(current_month)
