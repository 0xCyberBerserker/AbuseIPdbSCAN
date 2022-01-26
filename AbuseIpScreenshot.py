#!/usr/bin/python3
import os
from telnetlib import IP
import os.path
import argparse
import urllib.request as urllib
import urllib.request as urlRequest
import urllib.parse as urlParse
import platform

from PIL import Image
from selenium import webdriver

import time

from selenium.webdriver.chrome.options import Options
from pygments import highlight, lexers, formatters
from pyfiglet import Figlet
from dotenv import load_dotenv

parser = argparse.ArgumentParser(
    description='This program utilizes the Abuse IP Database from: AbuseIPDB.com to perform queries about IP addresses and returns the output to standard out.'
)
# Inputs
required = parser.add_mutually_exclusive_group()

required.add_argument(
    "-i",
    "--ip",
    help="lookup a single IP address",
    action="store")
"""
required.add_argument(
    "-l",
    "--list",
    help="lookup a list of IPs",
    action="store")
"""
args = parser.parse_args()


def imgShow(IP):
    img="./AbuseIPDB_"+IP+'.png'
    if(platform.system() == "Windows"):
        os.system('start '+img)
    else:
        os.system("shotwell "+img)
     
def takeScreenshot(IP):
    URL = "https://www.abuseipdb.com/check/"+IP
    options = webdriver.ChromeOptions()
    options.headless = True
    if(platform.system() == "Windows"):
        #Windows
        driver = webdriver.Chrome("./chromedrivers/chromedriver.exe")
    else:
        #Linux
        driver = webdriver.Chrome("./chromedrivers/chromedriver")
    driver.get(URL)
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    #driver.set_window_size(S('Width'),S('Height'), driver.window_handles[0]) # May need manual adjustment
    driver.set_window_size(540,1800, driver.window_handles[0]) # Manual Adjusted, like a phone
    driver.find_element_by_tag_name('body').screenshot('AbuseIPDB_'+IP+'.png')
    driver.quit()

def main():
    if args.ip:
        takeScreenshot(args.ip)
        imgShow(args.ip)
    
        
    else:
        exit(
            "Error: one of the following arguments are required: -i/--ip, more work in progress")


if __name__ == '__main__':
    main()