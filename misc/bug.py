import requests
import ndcctools.taskvine as vine

def fetch_content(url):
    # TODO: implement
    return url


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

manager = vine.FuturesExecutor(port=1357, factory=False)
contents = [manager.submit(fetch_content, url) for url in urls]

for content in vine.futures.as_completed(contents):
    print(content)
