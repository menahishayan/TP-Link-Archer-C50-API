# Adding Support For Your Model

## Looking for maintainers
This project is no longer being maintained. If you'd like to work on it, let me know. Until then, there's no point following the steps below.

## How It Works
1. We're going to open up the router's web management page and figure out what internal requests the webpage is making (what commands it's sending to the router) to do the tasks in question.  
2. We're then going to look at that data and parse it into the format that we need so the API functions can replicate those commands

## Prerequisites 
1. Chrome or Safari (>=14.0)
2. Access to the router's web management page
3. Knowledge of Inspect Element / Network Monitoring

## Steps
### Setup
1. Go over to the router's web management page (don't log in yet)
2. Open the Inspect window > Network tab
3. Tick the "Preserve Log" checkbox and set the filter to "XHR"
### Recording
4. Click on various buttons in the web management page "About", "WAN Setup", "Dual Band", "WLAN", "2.4GHz", etc 
5. Once you've clicked on all the important options, finally click "Logout" and "Restart". (only do this if you have "Preserve Log" enabled)
### Export Captured Data
6. Right Click on the CGI files in the Inspect window's "Network" tab and export HAR
7. Compress the HARs into a ZIP/TAR
8. Create a new issue on this GitHub with the following template:
  - Title: [Model Name] Support Data
  - Description: (List of buttons clicked on in the router management page)
  - Attachment: Compressed file of your packet captures
  
