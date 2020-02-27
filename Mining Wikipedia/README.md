# Mining Wikipedia
The `wiki_query.py` program is used for mining the web page contents of Wikipedia. It takes a search term as argument and prints the content of the Wikipedia page for that term.

## Design
This program defines only one function called `get_content` that requires one and <em>only</em> one input argument which represents the Wikipedia term to search for.

The function uses the argument to produce the corresponding url for the term using **UTF 8** encoding. The web page is opened using the `urllib` library and then parsed with the `BeautifulSoup` library.

The `try-except` structure in the function is used to capture the error when the input argument doesn't have a valid Wikipedia page, in which case an error message `*SITE NOT FOUND*` will be shown. Otherwise, the function will find every `<p>` under the `mw-parser-output` class and print the page content.

## Usage
Call only one argument to the program script, e.g.:  

    $ python3 wiki_query.py ankylosaurus

When the term to search has more than one word (i.e. `New Year`), use an underscore to replace the space(s) (i.e. `New_Year`), e.g.:

    $ python3 wiki_query.py New_Year

The first letter of each word can be either uppercase or lowercase, since Wikipedia doesn't differentiate between them. In other words, all of the following commands will print the content of the same Wikipedia page:

    $ python3 wiki_query.py New_Year
    $ python3 wiki_query.py new_year
    $ python3 wiki_query.py New_year
    $ python3 wiki_query.py new_Year
