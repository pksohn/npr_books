# NPR Book Concierge scraper

Small scraper to download a list of books from NPR's fantastic annual
[Book Concierge](http://apps.npr.org/best-books-2016/). CSV files
in the repo are the full book lists from 2013-2016 with a small
subset of available data fields. 

To download the data, clone the repository and run:

```
python books.py
```

To view books in a Pandas DataFrame object:

```
import books
df = books.Books(2016).to_frame()
print df.head()

|   | author                              | title                                             | text                                              | tags                                              | isbn       | isbn13        |
|---|-------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|------------|---------------|
| 0 | Mona Awad                           | 13 Ways Of Looking At A Fat Girl: Fiction         | The title of this book might be off-putting — ... | [staff-picks, book-club-ideas, identity-and-cu... | 0143128485 | 9780143128489 |
| 1 | Eric Ripert, with Veronica Chambers | 32 Yolks: From My Mother's Table To Working Th... | <em>32 Yolks</em> is as much a peek into the c... | [staff-picks, biography-and-memoir, book-club-... | 0812992989 | 9780812992984 |
| 2 | Sonali Dev                          | A Change Of Heart                                 | A change of pace from last year's <em>A Bollyw... | [identity-and-culture, lets-talk-about-sex, lo... | 1496705742 | 9781496705747 |
| 3 | Oliver Jeffers and Sam Winston      | A Child Of Books                                  | It begins: "I am a child of books. I come from... | [staff-picks, kids-books]                         | 0763690775 | 9780763690779 |
| 4 | Brian Evenson                       | A Collapse Of Horses: A Collection Of Stories     | Brian Evenson's unsettling collection plumbs t... | [poetry, science-fiction-and-fantasy, seriousl... | 1566894131 | 9781566894135 |
```


From here you can subset data in interesting ways. For example,
to see all books that are tagged as staff picks:

```
staff_picks = df.apply(lambda row: 'staff-picks' in row.tags, axis=1)
print df[staff_picks].head()

|   | author                              | title                                             | text                                              | tags                                              | isbn       | isbn13        |
|---|-------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|------------|---------------|
| 0 | Mona Awad                           | 13 Ways Of Looking At A Fat Girl: Fiction         | The title of this book might be off-putting — ... | [staff-picks, book-club-ideas, identity-and-cu... | 0143128485 | 9780143128489 |
| 1 | Eric Ripert, with Veronica Chambers | 32 Yolks: From My Mother's Table To Working Th... | <em>32 Yolks</em> is as much a peek into the c... | [staff-picks, biography-and-memoir, book-club-... | 0812992989 | 9780812992984 |
| 3 | Oliver Jeffers and Sam Winston      | A Child Of Books                                  | It begins: "I am a child of books. I come from... | [staff-picks, kids-books]                         | 0763690775 | 9780763690779 |
| 5 | Amor Towles                         | A Gentleman In Moscow: A Novel                    | Count Alexander Rostov is a resourceful man wh... | [staff-picks, historical-fiction, love-stories... | 0670026190 | 9780670026197 |
| 6 | Louise Penny                        | A Great Reckoning: A Novel                        | In Louise Penny's 12th Chief Inspector Gamache... | [staff-picks, mysteries-and-thrillers]            | 1250022134 | 9781250022134 |
```