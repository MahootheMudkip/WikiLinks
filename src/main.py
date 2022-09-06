from urllib import response
import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re 

# just for now
ssl._create_default_https_context = ssl._create_unverified_context

# Request 1 wikipedia page 
page_name = "1957 Cincinnati Bearcats football team"
url = ("https://en.wikipedia.org/wiki/" + page_name).replace(' ', '_')
response = urlopen(url)
raw_html = response.read().decode("utf-8")
webpage = BeautifulSoup(raw_html, "html.parser")

# taking a look at what html looks like
with open('webpage.html', 'w') as f:
    f.write(webpage.prettify())

# finding links to wikipedia pages
links = webpage.find_all('a', href=re.compile('^/wiki/'))
with open('links.html', 'w') as f:
    for link in links:
        name = link.get('title')
        if name == None or ':' in link.get('href'):
            links.remove(link)
        else:
            f.write(f'{link}\n')
            f.write(name + '\n')
            f.write('\n')
            

