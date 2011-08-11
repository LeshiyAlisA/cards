#-*- coding: utf-8 -*-
__author__ = 'leshiy'
import urllib
import html5lib
from html5lib import treebuilders
from xml.etree import cElementTree
from lxml import etree
from html5lib import treebuilders, sanitizer


class translate:

    def test(self,word):
        url1='http://lingvo.yandex.ru/table/%D1%81%20%D0%B0%D0%BD%D0%B3%D0%BB%D0%B8%D0%B9%D1%81%D0%BA%D0%BE%D0%B3%D0%BE/'
        url2='http://lingvo.yandex.ru/'+word+'/%D1%81%20%D0%B0%D0%BD%D0%B3%D0%BB%D0%B8%D0%B9%D1%81%D0%BA%D0%BE%D0%B3%D0%BE/'

        u=urllib.urlopen('http://lingvo.yandex.ru/'+word+'/%D1%81%20%D0%B0%D0%BD%D0%B3%D0%BB%D0%B8%D0%B9%D1%81%D0%BA%D0%BE%D0%B3%D0%BE/')
        str=u.read()
        parser = html5lib.HTMLParser(tree=treebuilders.getTreeBuilder('dom'),tokenizer=sanitizer.HTMLSanitizer)
        dom = parser.parse(str)

        for elem in dom.getElementsByTagName('li'):
            if elem.hasAttribute('class'):
                if elem.getAttribute('class')=='b-translate-answer__lan__item b-translate-answer__lan__cur':
                    
                    for child in elem.childNodes:
                        if child.nodeType==3:
                            print child.data.strip()

        for elem in dom.getElementsByTagName('span'):
            if elem.hasAttribute('class'):
                if elem.getAttribute('class')=='b-translate__tr':
                    for child in elem.childNodes:
                        if child.nodeType==3:
                            print child.data.strip()




      




