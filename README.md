# Github Archive

## Source : https://www.githubarchive.org/

Open-source developers all over the world are working on millions of projects:
writing code & documentation, fixing & submitting bugs, and so forth.
GitHub Archive is a project to record the public GitHub timeline, archive it,
and make it easily accessible for further analysis.

Each archive contains JSON encoded events as reported by the GitHub API.
You can download the raw data and apply own processing to it - e.g. write a
custom aggregation script.


## Starting with basic Github Archive script

test_src directory contains a python script (github_archive.py) to fetch Github archive data
published at particular date and time hour, We are taking date and time hour
from user as an input and storing the fetched Github archive data in file with
name format as "github_archive_dd_mm_yyyy_timehour.gz" in a current directory.

Example: Activity for 1/1/2015 @ 3PM

Run the Python Script,
$./github_archive.py

Enter the date in format 'dd/mm/yyyy' : 01/01/2015
Enter the time hour (1 - 24): 15
Github Archive URL : http://data.githubarchive.org/2015-01-01-15.json.gz
Downloading github_archive_01_01_2015_15.gz ...
Download Complete
HTTP status code : 200

You will find github_archive_01_01_2015_15.gz file in current directory
which contains JSON encoded events as reported by the GitHub API.
