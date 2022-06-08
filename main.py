import message_sender
import username_scrapper

option=0
scrap_num=1

while True:
    while option < 1 or option > 4:
        print("==================================")
        print("==================================")
        print("1) scrap usernames")
        print("2) send messages")
        print("3) both")
        print("4) Exit")
        option = int(input("Select Option: "))

    if option == 4:
        exit()

    if option == 1 or option == 3:
        scrap_num = int(input(("How much usernames ? 10x: ")))

    print("starting ...")

    if option == 1:
        username_scrapper.username_scrapper(scrap_num)
    elif option == 2:
        message_sender.message_sender()
    else:
        username_scrapper.username_scrapper(scrap_num)
        message_sender.message_sender()

    # reset option
    option=0