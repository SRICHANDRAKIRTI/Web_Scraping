Web Scraping - Books to Scrape

This project demonstrates basic web scraping using Python, Requests, BeautifulSoup, and Pandas.
The script scrapes image details (source, alt text, and thumbnail class) from the Books to Scrape
 website and saves the data into a CSV file.

📂 Project Structure
.
├── scraping.py          # Python script to scrape data
├── scrapping_data.csv   # Output dataset (scraped results)
└── README.md            # Project documentation

⚙️ Requirements

Make sure you have Python installed (>=3.7).
Install the required libraries using:

pip install requests beautifulsoup4 pandas

▶️ How to Run

Clone this repository:

git clone https://github.com/your-username/web-scraping-books.git
cd web-scraping-books


Run the script:

python scraping.py


The script will:

Fetch data from Books to Scrape

Extract image information (src, alt, thumbnail class)

Save the results into scrapping_data.csv
