from bs4 import BeautifulSoup

class WebScarper:
    def __init__(self, html_file):
        self.soup = BeautifulSoup()
        self.html_file = html_file
        self.open_html()
        self.run()

    def open_html(self):
        with open(self.html_file) as fp:
            self.soup = BeautifulSoup(fp, "lxml")

    def run(self):
        print(self.soup.prettify())


if __name__ == "__main__":
    print("running...")

    # Add your HTML File
    WebScarper("index.html")