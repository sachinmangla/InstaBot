from selenium import webdriver
from time import sleep

class InstaBot:
    
    def __init__(self, username, password):
        self.driver = webdriver.Firefox(executable_path='geckodriver.exe')
        self.driver.get('https://www.instagram.com/') # open instagram login page
        sleep(5)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys(username) # Enter username in username field
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(password) # Enter password in password fiels
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button').click() # click login button
        sleep(5)
        

    def get_following(self):
        self.driver.get('https://www.instagram.com/sachinmangla843/') # open user profile page
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a').click() # click on following
        sleep(3)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]") # scroll box
        last_ht, ht = 0, 1
        while last_ht != ht: # scroll following list till end
            last_ht = ht
            sleep(5)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != ''] # name of user following
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button").click()
        return names

    def get_follows(self):
        self.driver.get('https://www.instagram.com/sachinmangla843/') # open user profile page again
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a').click() # click on follows
        sleep(3)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]") # scroll box
        last_ht, ht = 0, 1
        while last_ht != ht:  # scroll follows list till end
            last_ht = ht
            sleep(5)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != ''] # name of user follows
        # close button
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button").click()
        return names

    def close(self):
        self.driver.close() # Close instapage

username = 'Enter your username'
password = 'Enter you password'

bot = InstaBot(username, password)
list1 = bot.get_following()
list2 = bot.get_follows()
bot.close()

print('No of Following :- ', len(list1))
print('No of Follows :- ',len(list2))

for name in list1:
    if not name in list2:
       print(name) 
