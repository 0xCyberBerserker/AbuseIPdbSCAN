# AbuseIPDB Scanner with a better JSON looking
So a friend of mine @Rafael and I were looking to make this thing even better.

Originally written by Mikebanks
https://github.com/mikebanks/AbuseIPdbSCAN

This is a python script that will parse IP addresses from files or manually interact with AbuseIPDB API. It will return the information about the IP into standard out in various outputs.

The main change is that it showed like this before
![AbuseDB1.png](AbuseDB1.png)

And now it's looking like this:

![AbuseDB2.png](AbuseDB2.png)

I think it's a more comfortable way to see the data.



## Installation

``` BASH
git clone https://github.com/mikebanks/AbuseIPdbSCAN.git
```

## Requirements

``` BASH
pip3 install -r requirements.txt
```
**IMPORTANT:** If you used the original version of the code made by the main author you should need to install **pprint** instead all the other packets so run this command:
``` BASH
pip3 install pprint
```

## AbuseIPDB API Key

In order to use the script you will need an API key. The AbuseIPDB API key information can be found here: deprecated, V2: <https://docs.abuseipdb.com/>

## Usage

Basic Commands:

Short Form    | Long Form     | Description
------------- | ------------- |-------------
-f            | --file        | parses IP Addresses from a single given file
-b            | --block       | lookup an IP block
-d            | --days        | take in the number of days in history to go back for IP reports. Default: 30 Days
-i            | --ip          | lookup a single IP address
-v            | --version     | displays version information
-cc           | --countrycode | select a country code to check IP range

Output commands:
Short Form    | Long Form     | Description
------------- | ------------- |-------------
-c            | --csv         | outputs items in comma seperated values
-j            | --json        | outputs items in json format (reccomended)
-l            | --jsonl       | outputs items in jsonl format (reccomended)
-t            | --tsv         | outputs items in tab seperated values (Default)
-x            | --translate   | by default categories are numbers, with this flag it will convert them to text


### Examples

* To search for reports on an IP address:

``python3 AbuseIPDB.py -i 1.1.1.1``

* To search for reports on an IP Block:

``python3 AbuseIPDB.py -b 1.1.1.0/24``

* To search a whole country IP range and translate the categories to names:

``python3 AbuseIPDB.py -cc nz -x``

