#! python3
# searchpypi.py  - Opens several search results.
# reference: https://stackoverflow.com/questions/60590845/trouble-with-searchpyi-py-automate-the-boring-stuff-with-python

import requests, sys, webbrowser, bs4
print('Searching...')    # display text while downloading the search result page
res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# Open a browser tab for each result.
link_elems = soup.select('.package-snippet')
num_open = min(5, len(link_elems))
for i in range(num_open):
    url_to_open = 'https://pypi.org' + link_elems[i].get('href')
    print('Opening', url_to_open)
    webbrowser.open(url_to_open)
