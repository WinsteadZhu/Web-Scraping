#!/usr/bin/env python
# -*- coding: utf-8 -*-


import urllib.parse
import urllib.request
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import unicodedata
import sys


# Define a function that takes a wikipedia search term as an argument
def get_content(term):

    # Retrieve url and deal with non-ASCII characters
    prefix = 'https://en.wikipedia.org/wiki'
    link = '/'.join((prefix, term))
    link = urllib.parse.quote(link.encode('utf8'), ':/')
    
    try:
        # Get HTML from web page
        html_body = urllib.request.urlopen(link)
    
        # Parse HTML with BS
        soup = BeautifulSoup(html_body,'html.parser')
        
    except HTTPError:
        print('*SITE NOT FOUND*')
    
    else:
        # Select appropriate element for content
        content = soup.select('.mw-parser-output p')
            
        # Go through every <p> that BS finds, extract the text, and clean it
        contents = [unicodedata.normalize("NFKD", elem.get_text()) for elem in content]
        
        # Go through list of <p>'s and join them into a single string
        wiki_content = ' '.join(contents)
        
        # Print Wiki web page content
        print(wiki_content)

# Enable calling argument(s)
first_arg = sys.argv[1]

get_content(first_arg)



