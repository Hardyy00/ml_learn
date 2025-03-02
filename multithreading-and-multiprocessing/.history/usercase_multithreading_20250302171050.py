'''
Real-World Example : Multithreading for I/O-bound tasks
Scenario : Web Scraping

Web Scraping often involves making numerous network requests to fetch web pages. These tasks are I/0 bound because they spend a lot of time waiting for responses from servers. Multithreading can significantly improve the performance by allowing multiple web pages to be fetched concurrently

'''
'''



'''

import threading
import requests
from bs4 import BeautifulSoup  # beautiful soup 4

url = [
    
    'https://python.langchain.com/docs/introduction/',

'https://python.langchain.com/api_reference/core/index.html',

'https://python.langchain.com/api_reference/experimental/index.html'
]
