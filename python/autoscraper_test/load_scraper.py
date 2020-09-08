from autoscraper import AutoScraper

scraper = AutoScraper()

scraper.load('scrapers/yahoo-finance')

tem = scraper.get_result_similar('https://stackoverflow.com/questions/606191/convert-bytes-to-a-string')
print(tem)
