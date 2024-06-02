# Twitter Trends Scraper

This project is a web scraper designed to extract the top trending topics from Twitter using Selenium WebDriver. The scraper automates the login process, navigates to the trending page, and collects the top trending topics.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have Python 3.x installed on your machine.
- You have pip (Python package installer) installed.
- You have Google Chrome installed.
- You have downloaded the ChromeDriver executable and placed it in a known directory. Ensure the ChromeDriver version matches your installed Chrome browser version. [Download ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/twitter-trends-scraper.git
   cd twitter-trends-scraper
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required Python packages:

   ```bash
   pip install selenium
   ```

## Usage

1. Update the path to the ChromeDriver executable in the script. Replace `'C:/chromedriver.exe'` with the actual path to your `chromedriver.exe`.

2. Open the `main.py` file and update the Twitter login credentials (`username` and `password`) with your actual Twitter account credentials.

3. Run the script:

   ```bash
   python main.py
   ```
