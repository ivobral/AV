import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s = Service(executable_path="E:\\Ivo faks\\geckodriver-v0.30.0-win64\\geckodriver.exe")

driver = webdriver.Firefox(service= s)                                  #otvara Firefox
driver.get("https://spribe.co/games/aviator")                           #dohvaća stranicu

play_demo_button = driver.find_element(By.CLASS_NAME, "btn-demo")        #dohvaća play demo botun
play_demo_button.click()                                                #klika play demo botun
age_button = driver.find_element(By.CLASS_NAME, "btn-age")               #dohvaća Yes I'm over 18 botun
age_button.click()                                                      #klika age button

driver.switch_to.window(driver.window_handles[1])

time.sleep(6)
auto_button = driver.find_element(By.XPATH, "/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[3]/app-bet-controls/div/app-bet-control/div/app-navigation-switcher/div/button[2]")
auto_button.click()

time.sleep(1)
slider_button = driver.find_element(By.XPATH, "/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[3]/app-bet-controls/div/app-bet-control[1]/div/div[2]/div[2]/div[1]/app-ui-switcher")
slider_button.click()

time.sleep(1)

auto_cashout_input = driver.find_element(By.XPATH, "/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[3]/app-bet-controls/div/app-bet-control[1]/div/div[2]/div[2]/div[2]/div/app-spinner/div/div[1]/input")
bet_input = driver.find_element(By.XPATH, "/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[3]/app-bet-controls/div/app-bet-control[1]/div/div[1]/div[1]/app-spinner/div/div[1]/input")

def Input_function(target_input, value):
    target_input.send_keys(Keys.CONTROL + "a")
    target_input.send_keys(Keys.DELETE)
    target_input.send_keys(value)

Input_function(auto_cashout_input, "1.20")
Input_function(bet_input, "0.29")



while True:
    bet_button = driver.find_element(By.XPATH, "/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[3]/app-bet-controls/div/app-bet-control[1]/div/div[1]/div[2]/button")
    payouts_block = driver.find_element(By.CLASS_NAME, "payouts-block")
    history = payouts_block.find_elements(By.TAG_NAME, "div")

    if float(history[0].text.replace("x", "")) >= 1.20 and bet_button.get_attribute("class") == "btn btn-success bet upper-font-r ng-star-inserted":
        bet_button.click()
    else:
        time.sleep(3)