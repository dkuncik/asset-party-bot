# Asset Party Bot
Automated Raffle Entry Script

## Description
This Python script automates the process of entering a raffle on a specific website. It utilizes web scraping techniques and the Selenium library to interact with the website's interface and perform the necessary actions.

The script starts by checking if the user is already logged in to the website. If not, it prompts the user to log in by displaying a QR code that needs to be scanned using an authentication app. Once logged in, the script retrieves the necessary session cookies and stores them in a file for future use.

After ensuring the user is logged in, the script navigates to the raffle entry page and checks if the user has already entered the raffle. If not, it clicks the entry button and retrieves the raffle schedule information. It then waits for a specific period of time before attempting to enter the raffle again.

While the script is running, it continuously checks if the user has won the raffle by scraping the website's page. If a winner is found, the script displays the winner's name.

In case of any errors or exceptions, the script attempts to refresh the web page and continue execution.

## Prerequisites 
Before running the script, make sure you have the following dependencies installed:

- Python (version 3.6 or higher)
- Selenium library (pip install selenium)
- BeautifulSoup library (pip install beautifulsoup4)

You will also need to download the Chrome WebDriver for Selenium. Ensure that the downloaded WebDriver is compatible with your Chrome browser version.

## Usage

1. Clone the repository:
```shell
git clone https://github.com/VaporDotDev/asset-party-bot
```
2. Navigate to the project directory:
```shell
cd automated-raffle-script
```
3. Install the required dependencies:
```shell
pip install -r requirements.txt
```
4. Download the Chrome WebDriver and place it in the project directory.
5. Run the script:
```shell
python raffle_script.py
```
7. Follow the on-screen instructions to log in and perform the raffle entry.

__Note:__ Ensure that you have a stable internet connection while running the script.
