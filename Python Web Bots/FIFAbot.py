from selenium.common.exceptions import NoSuchElementException  
from selenium import webdriver
import time

#IMPORTANT: close all instances of google chrome before running

class WebBot:
    #function to start chrome and go to desired website
    def __init__(self):
        options = webdriver.ChromeOptions() 
        options.add_argument("--user-data-dir=/Users/macbookpro/Library/Application Support/Google/Chrome/") #Path to your chrome profile
        options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        chrome_driver_binary = "/usr/local/bin/chromedriver"
        self.driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
        
        self.driver.get("https://www.ea.com/en-gb/fifa/ultimate-team/web-app/")
        
        time.sleep(10)
        print("Get Ready!")
        time.sleep(8)
        print("5")
        time.sleep(1)
        print("4")
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(2)
        print("Here we gooo!")
        time.sleep(1)

        self.getToMarket()
        self.fillFilter()

    def botSpeed(self):
        time.sleep(.1) #.3 works great

    def check_exists_by_xpath(self,xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    def getToMarket(self):
    
        #1.click on transfers
        self.driver.find_element_by_xpath('/html/body/main/section/nav/button[3]').click() #copy full xpath
        self.botSpeed()

        #2.Go to market
        self.driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/div[2]').click()
        self.botSpeed()
    
    def fillFilter(self):

        #Filter Information all lower case except for playerName
        playerName = "Lionel Messi"
        quality = "none"
        position = "none"
        rarity = "none"
        chemistryStyle = "none"
        upToWhatMinPrice = 250 #must be greater than 200
        maxPrice = 300 #must be greater than upToWhatMinPrice
        buyHowMany = 20 #how many times do you want the code to run/try buying cards?

        minPriceCounter = 200 #DO NOT CHANGE THIS VALUE EVER
        totalRunCounter = 1 #DO NOT CHANGE THIS VALUE EVER
        xpath = ''

        #3.type in player name
        if playerName != "none":
            self.driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/input').send_keys(playerName)
            time.sleep(.5)
            self.driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[2]/ul/button[1]').click() #copy full xpath
            self.botSpeed()

        #4.Quality (none)
        if quality == "gold":
            self.driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div/div').click() #copy full xpath
            self.botSpeed()
            self.driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div/ul/li[4]').click() #copy full xpath
            self.botSpeed()
        elif quality == "special":
            self.driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div/div').click() #copy full xpath
            self.botSpeed()
            self.driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div/ul/li[5]').click() #copy full xpath
            self.botSpeed()
        elif quality == "bronze":
            self.driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div/div').click() #copy full xpath
            self.botSpeed()
            self.driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div/ul/li[2]').click() #copy full xpath
            self.botSpeed()

        #5.Position(none) 20 change
        if position == "option1":
            self.driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[4]/div/div').click() #copy full xpath
            self.botSpeed()
            self.driver.find_element_by_xpath('').click() #copy full xpath
            self.botSpeed()
        elif position == "option2":
            self.driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[4]/div/div').click() #copy full xpath
            self.botSpeed()
            self.driver.find_element_by_xpath('').click() #copy full xpath
            self.botSpeed()
        elif position == "option3":
            self.driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[4]/div/div').click() #copy full xpath
            self.botSpeed()
            self.driver.find_element_by_xpath('').click() #copy full xpath
            self.botSpeed()
        elif position == "option4":
            self.driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[4]/div/div').click() #copy full xpath
            self.botSpeed()
            self.driver.find_element_by_xpath('').click() #copy full xpath
            self.botSpeed()
        

        #6.Rarity(none)
        if rarity == "rare":
            self.driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[3]/div/div').click() #copy full xpath
            self.botSpeed()
            self.driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[3]/div/ul/li[3]').click() #copy full xpath
            self.botSpeed()
        elif rarity == "common":
            self.driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[3]/div/div').click() #copy full xpath
            self.botSpeed()
            self.driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[3]/div/ul/li[2]').click() #copy full xpath
            self.botSpeed()

        #7.Chemistry Style (Hunter)
        if chemistryStyle == "shadow":
            self.driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[5]/div/div').click() #copy full xpath
            self.botSpeed()
            self.driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[5]/div/ul/li[20]').click() #copy full xpath
            self.botSpeed()
        elif chemistryStyle == "hunter":
            self.driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[5]/div/div').click() #copy full xpath
            self.botSpeed()
            self.driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[5]/div/ul/li[18]').click() #copy full xpath
            self.botSpeed()


        #8.min price starts at 0
        self.driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[5]/div[2]/input').send_keys(minPriceCounter) #starts at 0 (will enter 0)
        self.botSpeed()

        #9.Max
        self.driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/input').send_keys(maxPrice)
        self.botSpeed()
        
        #10.click search
        self.driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[2]').click()
        print("searching...")
        self.botSpeed()

        #if the click buy now for x amount element exist
        
        xpath = '/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/button[2]'
        elementExists = self.check_exists_by_xpath(xpath)

        if elementExists == True:

            #11.click buy now for x amount
            self.driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/button[2]').click()
            self.botSpeed()

            #12.click “ok” accept
            self.driver.find_element_by_xpath('/html/body/div[6]/section/div/div/button[1]').click()
            self.botSpeed()

            print("WE BOUGHT A CARD!")
        else:
            #13.then go back to filter area
            self.driver.find_element_by_xpath('/html/body/main/section/section/div[1]/button[1]').click()
            self.botSpeed()

            #looping steps to keep running the bot

        setter = 0

        while minPriceCounter <= upToWhatMinPrice and buyHowMany > 1:

            buyHowMany = buyHowMany - 1

            print("Bot run: " , totalRunCounter)

            if totalRunCounter == 1:
                print("Entering finite loop!") #just a message to let us know where its at
                
            totalRunCounter = totalRunCounter + 1 #will count and print the number of runs of our bot

            #if minPriceCounter is equal to upToWhatMinPrice then reset to 200 (which is the minimum)
            if minPriceCounter >= upToWhatMinPrice:
                self.driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[5]/div[2]/input').clear() 
                self.driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[5]/div[2]/input').send_keys(200) #enter 200 which is the minimum
                setter = 1
                self.botSpeed()

            #change min price + 50 (add counter) )
            if setter == 0:
                minPriceCounter = minPriceCounter + 50 #check if you need to move this after the code below or leave before, it might casue array overflow
                self.driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[5]/div[2]/button[2]').click() #click will add 50
                self.botSpeed()
            

            setter = 0

            #10.click search
            self.driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[2]').click()
            print("searching...")
            self.botSpeed()

            #if the click buy now for x amount element exist
            xpath = '/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/button[2]'
            elementExists = self.check_exists_by_xpath(xpath)

            if elementExists == True:

                #11.click buy now for x amount
                self.driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/button[2]').click()
                self.botSpeed()

                #12.click “ok” accept
                self.driver.find_element_by_xpath('/html/body/div[6]/section/div/div/button[1]').click()
                self.botSpeed()

                print("WE BOUGHT A CARD!")
            else:
                #13.then go back to filter area
                self.driver.find_element_by_xpath('/html/body/main/section/section/div[1]/button[1]').click()
                self.botSpeed()

        print("Bot run: " , totalRunCounter)
        print("Total Bot run: " , totalRunCounter)
        #System.out.print(“number of iterations: “counter), out it in the while loop so it prints each line to terminal
      
WebBot() #calls the WebBot class.
