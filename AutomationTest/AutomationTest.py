import glob
import os
from log import Log
from web import Web

URL = "https://www.cathaybk.com.tw/cathaybk"

# Create output directory and clear files if exists.
outputDir = os.path.join(os.getcwd(), "output")
if not os.path.exists(outputDir):
    os.makedirs(outputDir)
for file in os.listdir(outputDir):
    os.remove(os.path.join(outputDir, file))

# Start logging module
log = Log()

# Record the error message of current stage.
stageFailedMessage = ""
completed = False
# Retry for no more than 5 times.
retryCounter = 5

while retryCounter > 0:
    try:
        web = Web(URL)
    except:
        # Record the error message of current stage.
        stageFailedMessage = "Failed to connect to " + URL + "\n"
        retryCounter -= 1
        log.warning(stageFailedMessage)
        continue

    '''
    Step 1
    Screenshot all the webpage.
    '''
    web.screenshot(os.path.join(outputDir, "AutomationTest 1st Screenshot.png"))

    try:
        # Get the element, with class 'cubre-o-menu__btn', which child contains text "產品介紹"
        # This element is interactable while its child isn't.
        introduction = web.find_element("xpath", \
                              ".//*[text()='產品介紹']/ancestor::*[contains(@class, 'cubre-o-menu__btn')]")
    except:
        stageFailedMessage = "Cannot find \"產品介紹\" on the webpage\n"
        retryCounter -= 1
        log.warning(stageFailedMessage)
        web.close()
        continue
    try:
        # If this element is interactable, click and enter.
        # If not, print message into log and continue the program.
        web.click(introduction)
    except:
        log.info("產品介紹 is not interactable.")

    try:
        # Get the element, with class 'cubre-o-menuLinkList__btn', which child contains text "信用卡"
        # This element is interactable while its child isn't.
        creditCard = web.find_element("xpath", \
                                  ".//*[text()='信用卡']/ancestor::*[contains(@class, 'cubre-o-menuLinkList__btn')]")
    except:
        stageFailedMessage = "Cannot find \"信用卡\" on the webpage\n"
        retryCounter -= 1
        log.warning(stageFailedMessage)
        web.close()
        continue
    try:
        # If this element is interactable, click and enter.
        # If not, print message into log and continue the program.
        web.click(creditCard)
    except:
        log.info("產品介紹 is not interactable.")

    try:
        # Get the element, with class 'cubre-o-menuLinkList__content', which child contains text "信用卡"
        listOfCreditCard = web.find_element("xpath", \
                                      ".//*[text()='信用卡']/ancestor::*[contains(@class, 'cubre-o-menuLinkList__content')]")
    except:
        stageFailedMessage = "Cannot find child elements under \"信用卡\".\n"
        retryCounter -= 1
        log.warning(stageFailedMessage)
        web.close()
        continue
    
    '''
    Step 2
    Screenshot all the elements under menu "信用卡".
    Count the number of child elements under menu "信用卡" and print the result into output file.
    '''
    web.screenshot(os.path.join(outputDir, "AutomationTest 2nd Screenshot.png"))
    f = open(os.path.join(outputDir, "AutomationTest 2nd Result.txt"), "w")
    f.write("There're " + str(len(listOfCreditCard.find_elements("xpath", ".//a"))) + \
            " items under \"個人金融 > 產品介紹 > 信用卡\"")
    f.close()


    try:
        # Get the element with text "信用卡"
        # This element is interactable.
        creditCardIntro = web.find_element("xpath", \
                                        "//*[text()='卡片介紹']")
        web.click(creditCardIntro)
    except:
        stageFailedMessage = "Cannot find \"卡片介紹\" on the webpage\n"
        retryCounter -= 1
        log.warning(stageFailedMessage)
        web.close()
        continue
    try:
        # Get the element, with class 'cubre-m-anchor__btn', which child contains text "停發卡"
        # This element is interactable while its child isn't.
        cancelledCard = web.find_element("xpath", \
                                      ".//*[text()='停發卡']/ancestor::*[contains(@class, 'cubre-m-anchor__btn')]")
        web.click(cancelledCard)
    except:
        stageFailedMessage = "Cannot find \"停發卡\" on the webpage\n"
        retryCounter -= 1
        log.warning(stageFailedMessage)
        web.close()
        continue
    try:
        # Get the element, with class 'cubre-o-block__wrap', which child contains text "停發卡"
        # This element is interactable while its child isn't.
        divCancelledCard = web.find_element("xpath", \
                                      ".//*[text()='停發卡']/ancestor::*[contains(@class, 'cubre-o-block__wrap')]")
        print()
    except:
        stageFailedMessage = "Cannot find \"停發卡\" on the webpage\n"
        retryCounter -= 1
        log.warning(stageFailedMessage)
        web.close()
        continue

    '''
    Step 3
    Screenshot all the elements under menu "信用卡".
    Count the number of child elements under menu "信用卡" and print the result into output file.
    '''
    slidesCancelledCard = divCancelledCard.find_elements("xpath", \
                                ".//*[contains(@aria-label, 'Go to slide')]")
    for index in range(len(slidesCancelledCard)):
        web.click(slidesCancelledCard[index])
        web.screenshot(os.path.join(outputDir, "AutomationTest 3rd slide" + str(index) + " Screenshot.png"))
    
    numberOfCancelledCard = divCancelledCard.get_attribute("outerHTML").count("本卡已停止申辦")
    f = open(os.path.join(outputDir, "AutomationTest 3rd Result.txt"), "w")
    f.write("There're " + str(numberOfCancelledCard) + \
            " cards under \"個人金融 > 產品介紹 > 信用卡 > 卡片介紹 > 停發卡\"")
    f.close()

    completed = True
    break

'''
Finish function:
Print out the result into log.
Then close the webDriver.
'''
if retryCounter > 0:
    log.info("\n##################\n##### PASSED #####\n##################\n")
else:
    failedMeassage = "\n##################\n##### FAILED #####\n" + \
                     "##################\n" + \
                     "AutomationTest failed: " + stageFailedMessage
                     
    log.error(failedMeassage)
