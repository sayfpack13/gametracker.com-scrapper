import random
import time
import WebDriver
from selenium.webdriver.common.by import By

def username_scrapper(MAX_PAGES):

    userlist_url = "https://www.gametracker.com/search/cs/?search_by=online_player&searchpge="
    visited_pages = []
    username_list = []
    counter = 0

    # START HERE
    driver_options = WebDriver.SetupWebDriverOptions(True)
    driver = WebDriver.SetupWebDriver(driver_options, "windows")

    while (counter < MAX_PAGES):

        page_num = random.randrange(1, 500)
        if (visited_pages.__contains__(page_num)):
            continue

        visited_pages.append(page_num)

        driver.get(userlist_url + str(page_num))
        print("Job: " + str(counter + 1)+ ", User list Page: " + str(page_num) )

        # get all <a> elements
        a_tags = driver.find_elements(By.TAG_NAME, 'a')

        for a_tag in a_tags:
            if a_tag.get_attribute("href").__contains__("player/"):
                username_list.append(a_tag.text)

        counter += 1

    # save username list

    timestamp = round(time.time())
    # filename="usernames-"+str(timestamp)+".txt"
    filename = "usernames.txt"
    print("saving data to '"+filename+"' ...")

    textfile = open(filename, "w", encoding="utf-8")
    for user in username_list:
        textfile.write(user + "\n")

    print("==================done username scrap==================")

    textfile.close()
    driver.close()