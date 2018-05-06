# -*- coding: utf-8 -*-
import os
import requests
from bs4 import BeautifulSoup
from user_agent import generate_user_agent, generate_navigator
import time


def get_mbp_price():
    """获取 macbook pro 价格插件"""
    url = 'https://item.m.jd.com/product/4331185.html?sid=849cd8141eb52424e07ff3078b807ba0'
    try:
        headers = {'user-agent': generate_user_agent()}
        req = requests.get(url, headers=headers, timeout=6)
        soup = BeautifulSoup(req.text, 'lxml').find('div', class_='page-content')
        title = soup.find('span', class_='title-text').text
        try:
            price = soup.find('span', class_='seckill-big-price').text
        except:
            price = soup.find('span', class_='big-price').text
        return {
            'code': 0,
            'type': 'macbookpro',
            'date': time.strftime("%Y-%m-%d", time.localtime()),
            'content': {
                'title': title,
                'price': price
            }
        }
    except Exception as error:
        print(error)
        return {"code": -1}


def setup(app):
    print('-> Setting up : ' + __file__)
    app.register_function('get_mbp_price', get_mbp_price)
