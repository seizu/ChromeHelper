*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${CONFIG CHROMEDRIVER EXE}  %{USERPROFILE}/Documents/robotframework/webdriver/chromedriver103.exe
${CONFIG CHROMEDRIVER LOG}  ${CURDIR}/chromedriver_log.txt


##################################################################################################################
## Run chrome with argument --remote-debugging-port=9222
## e.g. for windows  "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222
##################################################################################################################

*** Test Cases ***
Chrome Browser Attach Test
    ${ctx}=           Get Library Instance    SeleniumLibrary
    Import Library    ${CURDIR}/ChromeHelperLibrary.py    ${ctx}
    Attach Chrome    chrome_driver=${CONFIG CHROMEDRIVER EXE}    debugger_address=127.0.0.1:9222    log_path=${CONFIG CHROMEDRIVER LOG}
    Go To   https://stackoverflow.com
