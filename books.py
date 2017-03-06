import json
import requests
from bs4 import BeautifulSoup
import pandas as pd


def download_books(year, csv_path, columns=None):

    books = Books(year)
    df = books.to_frame(columns=columns)
    df.to_csv(csv_path, index=False, encoding='utf=8')


class Books(object):

    def __init__(self, year):

        self.year = year
        self.url = 'http://apps.npr.org/best-books-{}/'.format(year)

    @property
    def script_text(self):
        url_text = requests.get(self.url).text
        soup = BeautifulSoup(url_text, 'lxml')

        # Find all script elements in page, filter for the one that includes
        # the 'window.BOOKS' variable
        scripts = soup.find_all('script')
        script_list = [element for element in scripts if
                       'window.BOOKS' in element.text]

        return script_list[0].text

    @property
    def books_json(self):

        # Get JSON from script text
        # Find matching brace to the first opening brace after BOOKS
        books_position = self.script_text.find('BOOKS')
        starting_brace = self.script_text[books_position:].find('[')
        text = self.script_text[books_position:][starting_brace:]

        opened = 1

        for position, char in enumerate(text):
            if char == '[':
                opened += 1
            if char == ']':
                opened -= 1
            if opened == 1 and char > 1:
                break

        filtered_text = text[:(position + 1)]

        return filtered_text

    def to_json(self):

        return json.loads(self.books_json)

    def to_frame(self, columns=None):

        json_data = self.to_json()
        df = pd.DataFrame(json_data)

        if columns:
            df = df[columns]

        return df


if __name__ == '__main__':

    columns = ['author', 'title', 'text', 'tags', 'isbn', 'isbn13']

    for year in [2016, 2015, 2014, 2013]:
        file_name = 'npr_books_{}.csv'.format(year)
        print 'Downloading books list for {}'.format(year)
        download_books(year, file_name, columns)
