![imgRepo/AbuseFiglet.png](imgRepo/AbuseFiglet.png)

# AbuseIPDB Scanner with a far better JSON looking and Automatic Screenshots by IP!

Originally written by Mikebanks
<https://github.com/mikebanks/AbuseIPdbSCAN/>

This is a python script that will parse IP addresses from files or manually interact with AbuseIPDB API. It will return the information about the IP into standard out in various outputs.

It works on Windows and Linux OS. 

## Changes

    The main change is that it showed like this before

![imgRepo/AbuseDB1.png](imgRepo/AbuseDB1.png)

    And now it's looking like this:

![imgRepo/AbuseDB2.png](imgRepo/AbuseDB2.png)

    I made another file called AbuseIpDBScreenshot.py that takes screenshots going to the webpage (http://abuseipdb.com/IP_GIVEN) and takes a screenshot in way that you can copy to the clipboard direclty.




## Installation

``` BASH
git clone https://github.com/JohnMorgan1234/AbuseIPdbSCAN.git
```
### Screenshots of the webpage analysis
<br/>
If you want to make a Screenshot the case in AbuseIPDB.com and you have GoogleChrome Installed now you can. There's a file called AbuseIpScreenshot.py that has the functions previously had the other script.
In case you have version 97 of google chrome just use it like that, if not:
Look at the version you have and download the same on here: <https://chromedriver.chromium.org/downloads/> so you can take all the advantages that this fork offers to you!
It's simple. Go to Options -> Help -> About Google Chrome

![imgRepo/ChromeVersion.png](imgRepo/ChromeVersion.png)

Now download the ChromeDriver of the same version of Google Chrome and move it to the folder called "chromedrivers"

**PS:** It would possibly be necessary to install a good adblocker on your google chrome web browser to make sure the screenshots are seen well.
Then when the Screenshot is taken your image viewer will pop up with your new screenshot!

## Requirements

``` BASH
pip3 install -r requirements.txt
```


## AbuseIPDB API Key

In order to use the script you will need an API key. The AbuseIPDB API key information can be found here: V2: <https://docs.abuseipdb.com/>

## Usage of the main script

Basic Arguments:

Short Form    | Long Form     | Description
------------- | ------------- |-------------
-i            | --ip          | lookup a single IP address ( **WORKING!!!** )
-f            | --file        | parses IP Addresses from a single given file (**Work In Progress**)
-b            | --block       | lookup an IP block (Currently not working)
-d            | --days        | take in the number of days in history to go back for IP reports. Default: 30 Days (Currently not working)
-v            | --version     | displays version information (Working)
-cc           | --countrycode | select a country code to check IP range (Currently not working)


## Usage of the ScreenShot script

Short Form    | Long Form     | Description
------------- | ------------- |-------------
-i            | --ip          | lookup a single IP address, goes to Abuseipdb.com/IP_Given and takes screenshot.


### Examples

* To search for reports on an IP address:

``` BASH
python3 AbuseIPDB.py -i 1.1.1.1
```
* And for taking a Screenshot directly :
```BASH
python3 AbuseIpDBScreenshot.py -i 1.1.1.1
```

[//]: <* To search for reports on an IP Block:> 

[//]: <``python3 AbuseIPDB.py -b 1.1.1.0/24``> 

[//]: <* To search a whole country IP range and translate the categories to names:>

[//]: <``python3 AbuseIPDB.py -cc nz -x``>


Thanks to the main author Mikebanks <https://github.com/mikebanks/> and my friends Pol & Rafael for giving me the advice with that awesome python libs!😁
