'''
Real-World Example : Multithreading for I/O-bound tasks
Scenario : Web Scraping

Web Scraping often involves making numerous network requests to fetch web pages. These tasks are I/0 bound because they spend a lot of time waiting for responses from servers. Multithreading can significantly improve the performance by allowing multiple web pages to be fetched concurrently

'''

import threading
import requests
from bs4 import BeautifulSoup  # beautiful soup 4

urls = [
    
    'https://python.langchain.com/docs/introduction/',

'https://python.langchain.com/api_reference/core/index.html',

'https://python.langchain.com/api_reference/experimental/index.html'
]


def fetch_content(url):
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f'fetched {len(soup.text)}')
    
    
threads = []

for url in urls:
    
    thread = threading.Thread(target=fetch_content, args=(url,)) 
    threads.append(thread)
    thread.start()
    
    
for thread in threads :
    thread.join()
    
    
print("All web pages fetched")        
       

