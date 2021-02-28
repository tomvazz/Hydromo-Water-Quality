from selenium import webdriver
import time

def selenium_webdriver(quality_score, quality_result, name, city, isHelp, zip):

    if (isHelp == 0):
        driver = webdriver.Chrome("/Users/tomvazhekatt/Documents/Drivers/chromedriver")
        driver.get("https://waterqualityforum.vercel.app")

        create_post = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div/div/div')
        create_post.click()

        time.sleep(3)  # program sleeps for 3 seconds

        name_input = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div/div/div[1]/input')
        name_input.send_keys(name)

        score_input = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/input')
        score_input.send_keys(quality_score)

        city_input = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div/div/div[3]/input')
        city_input.send_keys(city)

        comment = f"I recieved a score of {quality_score} which is considered to be {quality_result}"
        comment_input = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div/div/div[4]/input')
        comment_input.send_keys(comment)

        save_button = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div/div/div[7]/div/div')
        save_button.click()
    else:
        driver = webdriver.Chrome("/Users/tomvazhekatt/Documents/Drivers/chromedriver")
        driver.get("https://www.statefarm.com")

        find_agent = driver.find_element_by_xpath('//*[@id="oneX-header"]/nav/section[3]/div[1]/div[1]/ul/li[7]/div/button')
        find_agent.click()

        time.sleep(2)

        zip_enter = driver.find_element_by_xpath('//*[@id="oneX-findAnAgentZipCode"]')
        zip_enter.send_keys(zip)

        agent_button = driver.find_element_by_xpath('//*[@id="findAnAgentButton"]')
        agent_button.click()