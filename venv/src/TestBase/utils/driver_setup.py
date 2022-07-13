from appium import  webdriver

desired_caps = {
  "platformName": "Android",
  "platformVersion": "11",
  "deviceName": "Galaxy A30",
  "udid": "R58M61X94KE",
  "appPackage": "com.google.android.youtube",
  "appActivity": "com.google.android.apps.youtube.app.watchwhile.WatchWhileActivity"
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

