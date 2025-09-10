import string
import random

class UrlShortener:
    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}
        self.base_url = "http://short.url/"
        self.code_length = 6

    def _generate_code(self):
        chars = string.ascii_letters + string.digits
        while True:
            code = ''.join(random.choices(chars, k=self.code_length))
            if code not in self.code_to_url:
                return code

    def shorten(self, long_url):
        if long_url in self.url_to_code:
            code = self.url_to_code[long_url]
        else:
            code = self._generate_code()
            self.url_to_code[long_url] = code
            self.code_to_url[code] = long_url
        return self.base_url + code

    def redirect(self, short_url):
        code = short_url.replace(self.base_url, "")
        return self.code_to_url.get(code)

shortener = UrlShortener()
short = shortener.shorten("https://www.amazon.com")
print(short)
print(shortener.redirect(short))