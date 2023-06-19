import os
import pickle
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def check_login():
    try:
        driver.find_element(By.XPATH, "//div[@class='section user']")
    except:
        return False
    return True


def check_entered():
    try:
        driver.find_element(By.XPATH, "//img[@title='Dom']")
        return True
    except:
        return False


def cleanup():
    was_Cleaned = False
    screenshots_folder = "Screenshots"
    print("<#> Attempting cleanup...")
    for filename in os.listdir(screenshots_folder):
        if filename in os.listdir(screenshots_folder):
            file_path = os.path.join(screenshots_folder, filename)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                    was_Cleaned = True
            except Exception as e:
                print(f"Failed to delete file: {file_path}. Exception: {e}")
    if was_Cleaned:
        print("<#> Screenshots cleaned")
    else:
        print("<#> Nothing to be cleaned!")


options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920,1080')

url = "https://asset.party/get/developer/preview"

driver = webdriver.Chrome(options=options)

try:
    try:
        driver.get(url)
    except:
        print("<#> The web-page is down.")

    try:
        print("<#> Attempting to regain session.")
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
        print("<#> Session found.")
    except:
        print("<#> Session lost, please re-login.")

    try:
        driver.get(url)
        logged_In = check_login()
    except:
        print("<#> The web-page is down.")

    cleanup()

    if not logged_In:
        url_login = "https://steamcommunity.com/openid/login?openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid" \
                    ".mode=checkid_setup&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select" \
                    "&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.return_to" \
                    "=https%3A%2F%2Fasset.party%2F.login%2F&openid.realm=https%3A%2F%2Fasset.party"
        driver.get(url_login)

        while not logged_In:
            soup = BeautifulSoup(driver.page_source, 'html.parser')

            time.sleep(1)

            driver.save_screenshot("Screenshots/AUTH-QR-CODE.png")
            print("<#> Please scan the QR Code: Screenshots/AUTH-QR-CODE.png")

            time.sleep(20)

            form = soup.find('form', {'name': 'loginForm'})
            if form:
                print("\n<#> Form found...")
                try:
                    print("<#> Attempting log-in...\n")
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='submit']"))) \
                        .click()
                    cleanup()
                    pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
                    logged_In = check_login()
                except:
                    logged_In = check_login()
    elif logged_In:
        print("<#> Script is running.\n")
        time.sleep(5)
        while logged_In:
            raffle_Entered = check_entered()
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            if not raffle_Entered:
                try:
                    WebDriverWait(driver, 0).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[@class='button is-large is-primary']"))) \
                        .click()
                    schedule_text = soup.find_all("span", {"class": "tag"})[1].text.split(" ", 1)[1]
                    print("<#> Entering at: ", schedule_text)
                    time.sleep(5)
                except Exception as e:
                    print("<#> Failed to enter... Retrying. ", e)

            try:
                winner = soup.find_all("span", {"class": "tag"})[4].text.split(" ", 1)[1]
                print(winner)
            except:
                pass

except Exception as e:
    print("An error occurred: ", e)
    driver.refresh()
