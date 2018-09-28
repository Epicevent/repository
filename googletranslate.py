import sys
from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen


def translate(word):
    data = {'sl': 'ko', 'tl': 'en', 'text': 'word'}
    data['text'] = word

    querystring = urllib.parse.urlencode( data )
    request =  urllib.request.Request( 'http://www.translate.google.com' + '?' + querystring )

    request.add_header( 'User-Agent',
                        'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11' )
    opener = urllib.request.build_opener()
    feeddata = opener.open( request ).read()
    soup = BeautifulSoup( feeddata )
    return soup.find( 'span', id="result_box" ).get_text()


word = input( '번역할 문장을 입력하세요. : ' )
print (translate(  word ))