import requests, bs4
import time
keyword = 'python+programming'
for i in range(0, 100, 10):
    time.sleep(5)
    url = f'https://www.google.com/search?q={keyword}&rlz=1C1GCEA_enIR914IR914&oq=python&aqs=chrome.2.69i57j0l7.3983j0j7&sourceid=chrome&ie=UTF-8&start={i}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.content
        parser = bs4.BeautifulSoup(data, features="html.parser")
        a_tags = parser.find_all('a')
        for tag in a_tags:
            try:
               link = tag['href']
               if ('google' not in link and 'youtube' not in link) and ('http://' in link or 'https://' in link):
                   if link.startswith('/url?q='):
                        link = link[7:]
                   print(link)
            except:
                pass
