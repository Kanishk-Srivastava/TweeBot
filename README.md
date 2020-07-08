# TweeBot <a href="https://twitter.com/TweeBot22" target="_blank">`@TweeBot22`</a>
#### A Twitter Bot that responds to tweets, updates weather, news and COVID-19 stats. ![Build Status](http://img.shields.io/travis/badges/badgerbadgerbadger.svg?style=flat-square)
***Built in Python***
## Setting up 
- First of all create a *Twitter Developer account* <a href="https://developer.twitter.com/en" target="_blank">`https://developer.twitter.com/en`</a> .
- Then create an app which will provide you with **Consumer API keys** and **Access keys** in the keys and token section.
- For Weather API, go to <a href="https://openweathermap.org/" target="_blank">`https://openweathermap.org/`</a> and obtain the API keys. 
- Check your Python version in terminal/command line using `python --version` or `python3 --version`. 
- You can also use pythonanywhere.com and host the python script so that it works even if you shut down your computer. *Needs to be refreshed every 7-8 hours if using the free account.* 

## Libraries used
- **Tweepy** *Used to access the Twitter API* 
`pip install tweepy`.
- **Pyowm** *Used to access the Weather API* 
`pip install pyowm`. 
- **Requests** *Used for HTTP requests (web scraping*) 
`pip install requests`. 
*Use `pip3` if `pip` does not work.* 
> Create a `last_seen_id.txt` file in the same directory where the code is which will store the last seen tweet's id.

## Features 
- When a user mentions the bot and uses the #helloworld hashtag, the bot likes the tweet, retweets and follows the user. 
    - This is done using the functions available in Tweepy. 
- When a user mentions and uses the #weatherupdate hashtag, the bot will like, retweet and follow the user if not followed already and tweet a weather update. Each weather status has an emoticon assigned to it. 
- When a user mentions and uses the #newsupdate hashtag, the bot will like, retweet and follow the user if not followed already and tweet the 8-12 top live news each in a separate tweet.
    - This is done using the `newsapi.org` API and HTTP requests. The website has various sources from which user can scrape the top live news. 
- When a user mentions and uses the #covidupdate hashtag, the bot tweets the COVID-19 stats of India. 
    - This is done by scraping the information from `https://www.worldometers.info/coronavirus/country/india/`. 
## Contributing

> To get started... 👨🏻‍💻 

### Step 1

- **Option 1**
    - 🍴 Fork this repo!

- **Option 2**
    - 👯 Clone this repo to your local machine using `https://github.com/Kanishk-Srivastava/TweeBot.git`

### Step 2

- **HACK AWAY!** 🔨🔨🔨

### Step 3

- 🔃 Create a new pull request using <a href="https://github.com/Kanishk-Srivastava/TweeBot/compare/" target="_blank">`https://github.com/Kanishk-Srivastava/TweeBot/compare/`</a>.



## Support

Reach out to me at one of the following places! ✌🏼

- Twitter at <a href="https://twitter.com/Kanishk2209" target="_blank">`@Kanishk2209`</a>
- Connect with me on LinkedIn <a href="https://www.linkedin.com/in/kanishks22/"  target="_blank">`Kanishk Srivastava`</a>



## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](https://github.com/Kanishk-Srivastava/TweeBot/blob/master/LICENSE)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**