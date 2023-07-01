
from selenium.webdriver.remote.webelement import WebElement
from config import user_data_path,profile_directory,likes_url,TWEETS_CONTAINER_REL_XPATH,TWEET_REL_XPATH,TWEET_LIMIT
from selenium.common.exceptions import NoSuchElementException ,StaleElementReferenceException ,InvalidArgumentException
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from json import dump
from datetime import date


def get_liked_tweet(browser:webdriver.Chrome) -> dict:
    "Retrieves and extracts the tweet's text and link"

    tweet_dict = {}
    
    tweet_count = 0

    while(tweet_count <= TWEET_LIMIT):
    
        try:
             # extracts the tweet's container or html tag
            elements = browser.find_elements(by=By.CSS_SELECTOR,value="div[data-testid='cellInnerDiv']")
        except (NoSuchElementException,StaleElementReferenceException):
            # if element is not loaded retry after 5 seconds
            sleep(5)

            elements = browser.find_elements(by=By.CSS_SELECTOR,value="div[data-testid='cellInnerDiv']")
        
        for element in elements:
            tweet = element.text

            # extracts the liked tweet's orignal url including tweet id
            tweet_link = element.find_element(by=By.XPATH,value=TWEET_REL_XPATH).get_attribute("href")

            # increment the tweet count if the tweet is unique
            tweet_count = tweet_count if tweet_link in tweet_dict else tweet_count+1

            # Store the tweet's link and tweet in a dict
            tweet_dict[tweet_link] = tweet
 
        browser.execute_script("window.scrollBy(0, 350);") # 55 should be default
        sleep(5)
    
    return tweet_dict


def dump_liked_tweet(tweet_dict:dict) -> None:
    "Saves the tweets and tweet link to a json file"
    json_file_path = f"tweets {date.today()}.json"

    with open(json_file_path,"w") as json_file:
     dump(tweet_dict,json_file,indent=4)


if __name__ == "__main__":
    options = Options()

    # for invisible broswer window
    options.add_argument("--headless")

    # provide location where chrome stores profiles
    options.add_argument(user_data_path)

    # provide name of the profile in which twitter is logged in. 
    options.add_argument(profile_directory)

    try:    
        browser = webdriver.Chrome(options=options)
    except InvalidArgumentException:
        print("Please close the chrome window associated with user profile and re-run the program")

    browser.get(likes_url)


    sleep(5)
 
    tweets_container = browser.find_element(by=By.XPATH,value=TWEETS_CONTAINER_REL_XPATH)

    tweet_dict = get_liked_tweet(browser=browser)

    dump_liked_tweet(tweet_dict=tweet_dict)




