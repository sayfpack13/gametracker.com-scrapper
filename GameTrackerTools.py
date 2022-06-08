import time
from selenium.webdriver.common.by import By



def Login(driver, username, password):
    driver.get("https://www.gametracker.com/")

    username_field = driver.find_element(By.NAME, "username")
    username_field.send_keys(username)

    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys(password)

    driver.find_element(By.NAME, "submit").click()

    # check if logged in
    time.sleep(3)
    try:
        username_field = driver.find_element(By.NAME, "username")
        print("can't login !!")
        exit()
    except:
        print("loggedin !!")
        pass


def send_msg(driver, usernames_file, subject_file, message_file, sendmsg_url):
    message_file_content = message_file.read()
    subject_file_content = subject_file.read()
    username_list = usernames_file.readlines()
    username_count=len(username_list)
    msg_sended=0

    # remove duplicated usernames
    username_list=list(dict.fromkeys(username_list))

    for username in username_list:
        try:
            driver.get(sendmsg_url)
            print("messaging => " + username)
            username_field = driver.find_element(By.NAME, "username")
            username_field.send_keys(username.strip())

            subject_field = driver.find_element(By.NAME, "subject")
            subject_field.send_keys(subject_file_content)

            message_field = driver.find_element(By.NAME, "message")
            message_text = "Hello " + username + "\n"
            message_text += message_file_content
            message_field.send_keys(message_text)

            input_btns = driver.find_elements(By.TAG_NAME, "input")
            for input_btn in input_btns:
                if input_btn.get_attribute("type").__contains__("submit"):
                    input_btn.click()
                    break

            # check if message is sent
            if(checkAlert(driver)==True):
                #print("message sent => " + username)
                msg_sended+=1
            else:
                #print("error messaging => " + username)
                msg_sended += 0

        except:
            checkAlert(driver)
            pass

        print("Message sended: " + str(msg_sended) + " / " + str(username_count))




def checkAlert(driver):
    try:
        time.sleep(2)
        alert = driver.switch_to.alert
        alert.accept()
        return True
    except:
        return False
        pass