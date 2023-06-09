# Web Scraping MyAnimeList

This is a web scraping project that utilizes the *BeautifulSoup* library to scrape data from the "MyAnimeList" website. It allows you to extract information about anime titles, synopsis, genres, release date and more, directly from the seasonal anime listings on My Anime List.

## Installation and Prerequisites

*Python 3.x*: This project requires Python to be installed on your system. You can download it from the official Python website (https://www.python.org/downloads/).

*BeautifulSoup*: The BeautifulSoup library is required to parse and extract data from HTML. You can install it using pip with the following command:
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install BeautifulSoup.

```shell
   pip install bs4
```

## Getting Started

To start using the web scraper, follow the steps below:

1. Clone this repository or download the source code as a ZIP file and extract it to a directory of your choice.

2. Open a terminal or command prompt and navigate to the project directory.

3. Open the ```main.py``` file in a text editor of your choice.
4. Run the scraper by executing the following command in the terminal or command prompt:
```shell
   python main.py
```
5. The script will start scraping the top seasonal anime on MyAnimeList and display the extracted information in the console.

6. Once the scraping is complete, the script will save the scraped data to a file named ```top seasonal anime.csv``` in the project directory.

## Customization

* Extract more fields: The script currently extracts anime titles, synopsis, genres, release date, episode count and duration, links to watch the anime(or promotional video) and to get more information. You can modify the code to extract additional fields such as ratings, number of people watching, etc.

* Filter by status: By default, the script extracts all anime titles from the seasonal anime listings. If you want to filter by status (e.g., only completed anime), you can modify the script to include the desired filtering logic.

* Store data in a different format: The script currently saves the scraped data in a CSV file. If you prefer a different format such as JSON or Excel, you can modify the code to use the appropriate libraries for your desired format.

## Limitations
* Authentication: In order to watch the anime, you will have to login every time you click on the link that leads you to MALJapan to watch the anime.

* Rate Limiting: MyAnimeList may have rate limiting mechanisms in place to prevent excessive scraping. It's recommended to use the scraper responsibly and avoid making too many requests in a short period.

## License
This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License. Feel free to modify and distribute it according to your needs.

## Acknowledgement

This web scraping project was made possible thanks to the BeautifulSoup library. Special thanks to the developers and contributors of BeautifulSoup for creating such a powerful and user-friendly tool.

If you have any questions or encounter any issues, please feel free to reach out or submit a bug report in the GitHub repository. Happy scraping!

