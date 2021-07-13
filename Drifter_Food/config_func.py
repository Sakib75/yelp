import json
import csv
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class FileNaming:
    """ A class used for input/output file naming
    ...
    Attributes
    ----------
    competitor_code: str
            competitor code
    file_format: default csv
            format of the output or input file

    Methods
    -------
    spider_output_final():
            the method returns spider output (no duplicates) filename
    spider_output_row():
            the method returns spider output (with duplicates) filename
    scraper_output_raw():
            the method returns scraper output filename
    """

    def __init__(self, competitor_code: str, file_format="csv"):
        self.competitor_code = competitor_code,
        self.file_format = file_format

    def spider_output_final(self):
        return f"BDG-{self.competitor_code[0]}-{datetime.now().strftime('%y')}{datetime.now().strftime('%m')}-target-urls.{self.file_format}"

    def spider_output_raw(self):
        return f"BDG-{self.competitor_code[0]}-{datetime.now().strftime('%y')}{datetime.now().strftime('%m')}-clean-data.{self.file_format}"

    def scraper_output_raw(self):
        return f"BDG-{self.competitor_code[0]}-{datetime.now().strftime('%y')}{datetime.now().strftime('%m')}-raw-data.{self.file_format}"


def config_import_reader(name: str) -> dict:
    """
    The function reads website information from config_import.json and returns it as a dict
    """
    current_file_path = os.path.dirname(os.path.abspath(__file__))
    with open(current_file_path + "/config_import.json") as file:
        config = json.load(file)
        for website in config["config"]:

            if website["name"].lower() == name.lower():
                return website


def remove_duplicates(initial_filename: str, final_filename: str):
    """
    Reading file from the directory "3-clean-data",
    removing duplicates and writing in new final file,
    saving the new file in the directory "1-target-urls"

    :param initial_filename:
    :param final_filename:
    :return:
    """
    unique_urls = set()
    input()
    with open(f'3-clean-data/{initial_filename}', newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        for row in reader:
            unique_urls.add(row["link"])

    csv_dict = {"link": None}
    with open(f'1-target-urls/{final_filename}', "a", newline="", encoding="utf-8-sig") as file:
        w = csv.DictWriter(file, csv_dict.keys())
        if file.tell() == 0:
            w.writeheader()
        for url in unique_urls:
            w.writerow({"link": url})


def open_in_browser():
    """
    Opening Firefox browser
    """
    driver_profile = webdriver.FirefoxProfile()
    driver_profile.set_preference('dom.webdriver.enabled', False)
    driver_profile.set_preference('useAutomationExtension', False)
    driver_profile.update_preferences()
    desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
    driver = webdriver.Firefox(firefox_profile=driver_profile,
                               desired_capabilities=desired_capabilities,
                               executable_path="geckodriver.exe")

    return driver


def open_in_headless_browser():
    """
    Opening Firefox headless browser
    """
    driver_profile = webdriver.FirefoxProfile()
    options = FirefoxOptions()
    options.add_argument('--headless')
    driver_profile.set_preference('dom.webdriver.enabled', False)
    driver_profile.set_preference('useAutomationExtension', False)
    driver_profile.update_preferences()
    desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
    driver = webdriver.Firefox(firefox_profile=driver_profile, options=options,
                               desired_capabilities=desired_capabilities,
                               executable_path='geckodriver.exe')
    driver.maximize_window()

    return driver
