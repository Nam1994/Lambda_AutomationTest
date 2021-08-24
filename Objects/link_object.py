class Object:
    def __init__(self, click, title, url):
        self.click = click
        self.title = title
        self.url = url

    def __str__(self):
        return "click is: {}, title is: {}, url is: {} ".format(self.click, self.title, self.url)
