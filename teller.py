#!/usr/bin/python
# coding=utf-8

import sys
import time
import sqlite3
import telepot
from pprint import pprint
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from datetime import date, datetime, timedelta
import traceback

import noti


def replyAptData(name_param, user, pos_param):
    print(user, name_param, pos_param)
    res_list = noti.getData(name_param, pos_param)
    msg = ''
    for r in res_list:
        print(str(datetime.now()).split('.')[0], r)
        if len(r+msg)+1 > noti.MAX_MSG_LENGTH:
            noti.sendMessage(user, msg)
            msg = r+'\n'
        else:
            msg += r+'\n'
    if msg:
        noti.sendMessage(user, msg)
    else:
        noti.sendMessage(user, '해당하는 데이터가 없습니다.' )

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text':
        noti.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
        return

    text = msg['text']
    args = text.split(' ')

    if text.startswith('지갑') and len(args) > 1:
        print('try to 지갑', args[1])
        replyAptData('지갑', chat_id, args[1])
    elif text.startswith('쇼핑백') and len(args) > 1:
        print('try to 쇼핑백', args[1])
        replyAptData('쇼핑백', chat_id, args[1])
    elif text.startswith('서류봉투') and len(args) > 1:
        print('try to 서류봉투', args[1])
        replyAptData('서류봉투', chat_id, args[1])
    elif text.startswith('가방') and len(args) > 1:
        print('try to 가방', args[1])
        replyAptData('가방', chat_id, args[1])
    elif text.startswith('베낭') and len(args) > 1:
        print('try to 베낭', args[1])
        replyAptData('베낭', chat_id, args[1])
    elif text.startswith('핸드폰') and len(args) > 1:
        print('try to 핸드폰', args[1])
        replyAptData('핸드폰', chat_id, args[1])
    elif text.startswith('옷') and len(args) > 1:
        print('try to 옷', args[1])
        replyAptData('옷', chat_id, args[1])
    elif text.startswith('책') and len(args) > 1:
        print('try to 책', args[1])
        replyAptData('책', chat_id, args[1])
    elif text.startswith('파일') and len(args) > 1:
        print('try to 파일', args[1])
        replyAptData('파일', chat_id, args[1])
    elif text.startswith('기타') and len(args) > 1:
        print('try to 기타', args[1])
        replyAptData('기타', chat_id, args[1])
    else:
        noti.sendMessage(chat_id, '제대로된 명령어를 입력해주세요.\n'
                                  '분실물 [지하철코드] 명령을 입력하세요.\n'
                                  '분실물: 지갑, 쇼핑백, 서류봉투, 가방, 베낭, 핸드폰, 옷, 책, 파일, 기타\n'
                                  '지하철코드:  s1 - 지하철(1~4호선), s2 - 지하철(5~8호선), s3 - 코레일, s4 - 지하철(9호선)')