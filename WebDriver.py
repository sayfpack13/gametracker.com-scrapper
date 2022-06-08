from selenium import webdriver

def SetupWebDriver(options,os="linux"):
    if(os=="linux"):
        driver = webdriver.Chrome(executable_path="chromedriver/stable/chromedriver", options=options)
    else:
        driver = webdriver.Chrome(executable_path='C:/webdriver/chromedriver.exe', options=options)


    return driver

def SetupWebDriverOptions(silent):
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-notifications')
    options.add_argument("--mute-audio")
    if silent==True:
        options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    #options.add_argument("user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1")
    return options