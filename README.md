News Headline Web Scraper - It is simple Python script that scrapes top headlines from a news website and saves them into a .txt file.

Tools Used,
Python - requests (for fetching HTML) , BeautifulSoup (for parsing and extracting text)

This program fetches the HTML of BBC News
extracts all <h3> tag content using requests and BeautifulSoup and
saves them line by line to headlines.txt

Input from website
<h3>Breaking News: Market crashes</h3>
<h3>     </h3>             
<h3>Technology Update</h3>
<h3></h3>                
<h3>World Leaders Meet</h3>

Output:
Breaking News: Market crashes
Technology Update
World Leaders Meet
