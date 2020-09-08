from autoscraper import AutoScraper

url = 'https://stackoverflow.com/questions/2081586/web-scraping-with-python'

# We can add one or multiple candidates here.
# You can also put urls here to retrieve urls.
wanted_list = ["How to call an external command?"]

scraper = AutoScraper()
result = scraper.build(url, wanted_list)

for i in result:
    print(i)
"""
Here's the output:

[
    'How do I merge two dictionaries in a single expression in Python (taking union of dictionaries)?', 
    'How to call an external command?', 
    'What are metaclasses in Python?', 
    'Does Python have a ternary conditional operator?', 
    'How do you remove duplicates from a list whilst preserving order?', 
    'Convert bytes to a string', 
    'How to get line count of a large file cheaply in Python?', 
    "Does Python have a string 'contains' substring method?", 
    'Why is “1000000000000000 in range(1000000000000001)” so fast in Python 3?'
]
"""

# Now you can use the scraper object to get related topics of any stackoverflow page:
tem = scraper.get_result_similar('https://stackoverflow.com/questions/606191/convert-bytes-to-a-string')
print(tem)

# We can now save the built model to use it later. To save:

# Give it a file path
scraper.save('scrapers/yahoo-finance')
# And to load:

# scraper.load('scrapers/yahoo-finance')
