import pyshorteners

def shorten_url(long_url):
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(long_url)
    return short_url


long_url = input("Enter the URL to shorten: ")
shortened_url = shorten_url(long_url)
print("Shortened URL:", shortened_url)
