from autoscraper import AutoScraper

url = 'https://finance.yahoo.com/quote/AAPL/'

wanted_list = ["124.81"]

scraper = AutoScraper()
"""
# Here we can also pass html content via the html parameter instead of the url (html=html_content)

result = scraper.build(url, wanted_list)
print(result)
"""
proxies = {
    "http": 'http://127.0.0.1:1087',
    "https": 'https://127.0.0.1:1087',
}

result = scraper.build(url, wanted_list, request_args=dict(proxies=proxies))
print(result)

# Now we can get the price of any symbol:
res = scraper.get_result_exact('https://finance.yahoo.com/quote/MSFT/')
print(res)