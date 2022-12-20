from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("chromedriver")
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://web.whatsapp.com/")


def msg():
    name = input('\n enter group/user name: ')
    message = input("enter your message to group/user: ")
    Count = int(input("enter the message count: "))

    # Find whom to message
    user = driver.find_element(By.XPATH, '//span[@title="{}"]'.format(name)
                               )
    user.click()

    text_box = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]")

    # Send Button
    for i in range(Count):
        text_box.send_keys(message)
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span").click()


driver.implicitly_wait(20)
msg()


def reps():
    print("Do you want to send more messages to anyone?")
    askUser = input("Press Y for yes and N for no : ")
    if askUser == 'Y' or askUser == 'y':
        msg()
        reps()
    elif askUser == 'N' or askUser == 'n':
        print("Thank you see you soon")
    else:

        print("Please enter valid option: \n")
        reps()


reps()
