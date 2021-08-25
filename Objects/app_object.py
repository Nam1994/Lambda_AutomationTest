class Integration_Object:
    def __init__(self, title, url):
        self.title = title
        self.url = url

    def __str__(self):
        return "title is: {}, url is: {} ".format(self.title, self.url)
