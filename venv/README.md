# YouTube test cases via Appium Python

This repository contains test cases for YouTube 

## Dependences
1. Python and Pycharm 
2. Android sudio SDK and emulator
3. Appium binaries, Desktop client and Android emulator and Real device configuration
4. Install JDK (Java Development Kit) 
5. Install Eclipse
6. Install TestNg for Eclipse
7. Install Selenium Server JAR 
8. Appium Client Library
9. APK App Info



## Usage
###### For halp
```bash
python .\venv\run.py --help
```
###### For example
```bash
python .\venv\run.py --test Shorts_page  --allure No
```


## Warning
After running test you should fix ``` desired_caps ``` for your phone or emulator in ``` \venv\src\TestBase\utils\driver_setup.py ``` file.
Sometimes you can get error like this ```An element could not be located on the page using the given search parameters.``` In this case you must change ```SUBSCRIPTIONS``` locator in ``` venv\src\PageObject\constants\youtube_consts.py ```file.
