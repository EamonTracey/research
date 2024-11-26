# TODO: fix

import ndcctools.taskvine as vine

def fetch_content(url):
    import requests
    response = requests.get(url)
    return response


urls = [
        "https://apnews.com",
        "https://nytimes.com",
        "https://wsj.com",
        "https://axios.com",
        "https://nbcnews.com",
        "https://cnn.com",
        "https://abcnews.com",
        "https://washingtonpost.com",
        "https://reuters.com",
]

manager = vine.FuturesExecutor(factory=False)
contents = [manager.submit(fetch_content, url) for url in urls]

for content in vine.futures.as_completed(contents):
    print(content)
