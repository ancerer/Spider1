import re
from bs4 import BeautifulSoup
from urllib import request, parse


if '__name__' == '__main__':
    ip = 'http://www.iqiyi.com/v_19rrb2yq04.html?fc=8b62d5327a54411b#vfrm=19-9-0-1'
    get_url = 