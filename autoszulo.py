"""
A module to fill in a certain online form automatically.
"""

import argparse
import time
import sys

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tkinter import simpledialog

PYTHONWAIT = 0.2
SELENIUMWAIT = 2

DEFAULT_NUMBER_OF_FILLS = 3
DEFAULT_LINK = 'https://szuloikerdoiv1.unipoll.hu/PagesForResponse/normalsurvey/response?surveyid=20124780'

START_BUTTON =     "//button[@class='mat-ripple mat-tooltip-trigger start-btn']"
EXIT_BUTTON =      "//button[@class='mat-ripple header__btn header__btn--exit ng-star-inserted']"
CANCEL_BUTTON =    "//button[@class='mat-ripple dialog__button dialog__button--cancel ng-star-inserted']"
NEXT_PAGE_BUTTON = "//button[@class='mat-ripple mat-tooltip-trigger paginator__btn' and @icon='next']"
SUBMIT1_BUTTON =   "//button[@class='mat-ripple submit__button ng-tns-c117-0']"
SUBMIT2_BUTTON =   "//button[@class='mat-ripple dialog__button dialog__button--ok ng-star-inserted']"

TEXTAREA = "//textarea[@maxlength='4000']"
TEXT = """1. Érdemi és nyilvános párbeszédet az oktatás megújításáról! Hiteles tájékoztatást a kormány és a közmédia részéről!
    2. Szüntessék meg a pedagógusok lejáratását, az oktatási szereplők megfélemlítését! A kirúgott vagy leváltott tanárokat azonnal helyezzék vissza! Megbecsülést a pedagógusoknak!
    3. Érdekérvényesítő sztrájkjogot a pedagógusoknak!
    4. Felelős, hozzáértő oktatásirányítást! Önálló oktatási minisztériumot!
    5. Kisebb terhelést a diákoknak és a pedagógusoknak!
    6. Esélyteremtő, minőségi oktatást és nevelést mindenkinek – az óvodától az egyetemig!
    7. Versenyképes és értékálló bérezést az oktatásban dolgozóknak!
    8. Minőségi, 21. századi környezetet a tanuláshoz és a tanításhoz, neveléshez!
    9. Szakmai szabadságot és támogatást az oktatásban! Korszerű nemzeti alaptantervet! Szabad tankönyvválasztást!"""


def fill_in(url):
    """Fill in a certain online form automatically."""


    def click(xpath):
        """Search for an element by `xpath`, wait, click, wait."""
        WebDriverWait(browser, SELENIUMWAIT).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
        time.sleep(PYTHONWAIT)


    def next_page(click_somewhere=True):
        """Go to next page."""
        # need to do something first
        if click_somewhere:
            click(EXIT_BUTTON)
            click(CANCEL_BUTTON)
        click(NEXT_PAGE_BUTTON)


    # start Firefox
    browser = webdriver.Firefox()
    time.sleep(PYTHONWAIT)

    # home page
    browser.get(url)
    time.sleep(PYTHONWAIT)

    # go to page#1
    click(START_BUTTON)

    # go to page#6
    for i in range(5): next_page()

    # write in text
    text_answer = browser.find_element(By.XPATH, TEXTAREA)
    text_answer.send_keys(TEXT)
    time.sleep(PYTHONWAIT)

    # go to page#7
    next_page(click_somewhere=False)

    # submit data
    click(SUBMIT1_BUTTON)
    click(SUBMIT2_BUTTON)
    time.sleep(PYTHONWAIT)

    # quit Firefox
    browser.quit()


def format_url(url):
    """Convert `url` to canonical format."""
    return url.replace('Survey.aspx?SurveyId',
        'PagesForResponse/normalsurvey/response?surveyid')


def main():
    """Main."""
    args = get_args()

    number_of_fills = args.number_of_fills
    url = args.link

    if getattr(sys, 'frozen', False):  # if we are running under PyInstaller
        number_of_fills = simpledialog.askinteger("Gyermekek száma", "Hány gyermekre töltse ki a program a kérdőívet?")
        url = simpledialog.askstring("Kérdőív link", "Adja meg a linket, amit a Krétában kapott a kérdőívhez:")

    url = format_url(url)

    for i in range(number_of_fills):
        fill_in(url)


def get_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        '-n', '--number-of-fills',
        help='Fill in the form this much times.',
        type=int,
        default=DEFAULT_NUMBER_OF_FILLS
    )
    parser.add_argument(
        '-l', '--link',
        help='Use this URL to access the form.',
        type=str,
        default=DEFAULT_LINK
    )
    return parser.parse_args()


if __name__ == '__main__':
    main()

