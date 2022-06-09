import WebDriver
import GameTrackerTools


def message_sender():
    username = "xxxxxxxxxxx"
    password = "xxxxxxxxxxxxx"
    usernames_file = open("usernames.txt", "r", encoding="utf8")
    subject_file = open("subject.txt", "r", encoding="utf8")
    message_file = open("message.txt", "r", encoding="utf8")
    sendmsg_url = "https://www.gametracker.com/account/manage/pmsend.php"

    # START HERE
    driver_options = WebDriver.SetupWebDriverOptions(True)
    driver = WebDriver.SetupWebDriver(driver_options, "windows")

    GameTrackerTools.Login(driver, username, password)
    GameTrackerTools.send_msg(driver, usernames_file, subject_file, message_file, sendmsg_url)

    print("==================done sending messages==================")

    message_file.close()
    subject_file.close()
    usernames_file.close()
    driver.close()
