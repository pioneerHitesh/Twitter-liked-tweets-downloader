USERNAME =  "<your windows username here>"
user_data_path = rf"--user-data-dir=C:\Users\{USERNAME}\AppData\Local\Google\Chrome\User Data"

PROFILE = "<your chrome profile name here>" # It can be found by visiting chrome://version/
profile_directory = rf"--profile-directory={PROFILE}"

TWITTER_HANDLE =  "elonmusk"#"<your twitter handle here w/o @>"
likes_url = f"https://twitter.com/{TWITTER_HANDLE}/likes" 

# retweets_url = f"https://twitter.com/{twitter_handle}"

# Relative xpath of container inside which all tweets are displayed
TWEETS_CONTAINER_REL_XPATH = "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div/div"

# Relative xpath of anchor tag having original tweet's url 
TWEET_REL_XPATH = "//div/div/article/div/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/div/div[2]/div/div[3]/a"

# No of tweets to be extracted 
TWEET_LIMIT = 10

