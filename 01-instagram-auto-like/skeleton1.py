import time
import random
from selenium import webdriver
from urllib.parse import quote


id = 'id'
password = 'password'

timeline_like_count = 120
hash_tags = ['코딩', '빅데이터','보아즈']
hash_tags_count = 60

browser = webdriver.Chrome('chromedriver')
browser.get('https://instagram.com/')

def login(id, password):
    '''
    인스타그램 로그인 구현
    '''
    pass

def timeline_like(timeline_like_count):
    '''
    타임라인 좋아요 구현
    '''
    pass

def hash_tags_like(hash_tags, hash_tags_count):
    '''
    해시태그 좋아요 구현
    '''
    pass


login(id, password)
timeline_like(timelinke_like_count)
hash_tags_like(hash_tags, hash_tags_count)

browser.quit()
