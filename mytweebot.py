import time
import tweepy            #Twitter API
import pyowm             #Open-Weather API
import requests          #To Generate HTTP requests
from lxml import html    #Web-scraping


#Twitter API Credentials
print("Hello welcome to twitter bot")
CONSUMER_KEY = 'LF8lpNwDfaMsBM7aWwMQKNQpW'                              #Identification of the user 
CONSUMER_SECRET = '69H8jkcXiZjL2v9bGaQlmMNyliyrfjHI3eeQs4fx1Zlv46YNN0'
ACCESS_KEY = '1269971489219940353xxxxxxxxxxxxxxxzzAIYnCjWe'
ACCESS_SECRET = 'IboPZWtMqoXMCYpNxxxxxxxxxxxxxxxdGaNSxLkjXMc7Oe'


#Open-Weather API credential s& functions
owm = pyowm.OWM('ee95ce0f85bb812ced4795e9705fc954')  
observation = owm.weather_at_place('New Delhi,IN')
weather = observation.get_weather()
w=weather.get_status()
windspeed=weather.get_wind()  
humidlevel=weather.get_humidity()
temp=weather.get_temperature('celsius')
pressure=weather.get_pressure()


# Weather Emoji
Clouds = u'\U00002601'        #☁️️
Clear = u'\U00002600'         #☀️️
Rain =  u'\U00002614'         #☔
Extreme =  u'\U0001F300'      #🌀
Snow = u'\U00002744'          #❄️️
Thunderstorm = u'\U000026A1'  #⚡
Mist = u'\U0001F32B'          #⛅
Haze = u'\U0001F324'          #🌫️
Dust = u'\U0001F4A8'          #💨
Notsure = u'\U0001F648'       #🙈

#Twitter authentication details and verification
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)          #OAUTH Handler object 
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)                   #access keys to access the TW API
api = tweepy.API(auth, wait_on_rate_limit=True,                    #wait for rate limit to replenish
    wait_on_rate_limit_notify=True)                                #notify
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


#Storing the last seen id (user id)
FILE_NAME = 'last_seen_id.txt'              

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())       #strips newlines & whitespaces
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):    #writing the last seen id to the file
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


#News update function using NewsAPI.org   
def News_from_Google():
        url = ('http://newsapi.org/v2/top-headlines?country=in&apiKey=bfd4b49c3932432c88ffd48019a41ecd')
        response = requests.get(url).json()                       #retrieving & accessing the json data 
        article = response["articles"]                            
        results = []
    
        for ar in article: 
            results.append(ar["description"])                     #Adds item to the end of the list
         
        for i in range(len(results)): 
            x=0
            y=1
            for k in range(x,y):
                try: 
                    api.update_status(results[i])               
                    time.sleep(1)     
                    print('News Updated!')
                    x=x+2
                    y=y+2
                except tweepy.TweepError as error:
                 if error.api_code == 187:
                   print('duplicate status')
                 else:
                       raise error
                

                   
#Coronavirus Updates using worldometers.com and web-scraping              
def Covid_Update():
       cresponse=requests.get('https://www.worldometers.info/coronavirus/country/india/')              #response object -> cresponse
       doc = html.fromstring(cresponse.content)                                                        #reading the content from cresponse
       total, deaths, recovered = doc.xpath('//div[@class="maincounter-number"]/span/text()')          #elements of the webpage for info
       try: 
           api.update_status('COVID-19 Updates INDIA \n' + 'Total Cases: ' + total + '\nRecovered: ' + recovered 
                             + '\nDeaths: ' + deaths)
           print(total,deaths,recovered)
           print('Updated!')
       except tweepy.TweepError as e:
           if e.api_code == 187:
               print('duplicate status')
           else:
               raise e
               
#Function will reply to tweets based on the hashtag 
def Reply_to_Tweets():
       print('retrieving and replying to tweets...', flush=True)
       last_seen_id = retrieve_last_seen_id(FILE_NAME)                  #retrieve the last seen tweet id
       mentions = api.mentions_timeline(                                #returns the recent mentions 
                       last_seen_id,
                       tweet_mode='extended')
       for mention in reversed(mentions):
           print(str(mention.id) + ' - ' + mention.full_text, flush=True)   #.id & .full_text retrieve from the list
           last_seen_id = mention.id
           store_last_seen_id(last_seen_id, FILE_NAME)
        
           if '#helloworld' in mention.full_text.lower():       #convert to lower case, handling all cases and check 
                print('found #helloworld!', flush=True)
                print('responding back...', flush=True)
                api.update_status('@' + mention.user.screen_name +
                                  '#HelloWorld back to you!', mention.id)
                mention.favorite()
                mention.retweet()
                mention.user.follow() 
                
                                                
                                                
           elif '#weatherupdate' in mention.full_text.lower(): 
              if w == 'Rain' : 
                  api.update_status('@'+ mention.user.screen_name + ' Weather update | New Delhi, IN \n' +
                                    weather.get_status() + Rain + '\n' +                           
                                    'Current temperature = ' + str(int(temp['temp']))+'℃. \n' +
                                    'Wind speed = ' + str(int(windspeed['speed']))+' m/s \n' + 
                                    'Humidity = ' + str(int(humidlevel))+'% \n'
                                    'Pressure = ' + str(int(pressure['press'])) + 'hPa', mention.id) 
                                                        
                  print('found #weatherupdate', flush=True)
                  print('responding back...', flush=True) 
                  mention.favorite()
                  mention.retweet()
                  mention.user.follow()
                                                        
              if w == 'Clear' : 
                  api.update_status('@'+ mention.user.screen_name + ' Weather update | New Delhi, IN \n' +
                                    weather.get_status() + Clear + '\n' +                           
                                    'Current temperature = ' + str(int(temp['temp']))+'℃. \n' +
                                    'Wind speed = ' + str(int(windspeed['speed']))+' m/s \n' + 
                                    'Humidity = ' + str(int(humidlevel))+'% \n'
                                    'Pressure = ' + str(int(pressure['press'])) + 'hPa', mention.id) 
                  
                  print('found #weatherupdate', flush=True)
                  print('responding back...', flush=True) 
                  mention.favorite()
                  mention.retweet()
                  mention.user.follow()
                                                            
              if w == 'Extreme' : 
                  api.update_status('@'+ mention.user.screen_name + ' Weather update | New Delhi, IN \n' +
                                    weather.get_status() + Extreme + '\n' +                           
                                    'Current temperature = ' + str(int(temp['temp']))+'℃. \n' +
                                    'Wind speed = ' + str(int(windspeed['speed']))+' m/s \n' + 
                                    'Humidity = ' + str(int(humidlevel))+'% \n'
                                    'Pressure = ' + str(int(pressure['press'])) + 'hPa', mention.id)
                
                  print('found #weatherupdate', flush=True)
                  print('responding back...', flush=True) 
                  mention.favorite()
                  mention.retweet()
                  mention.user.follow()
                                                                
              if weather == 'Snow' : 
                 api.update_status('@'+ mention.user.screen_name + ' Weather update | New Delhi, IN \n' +
                                  weather.get_status() + Snow + '\n' +                           
                                 'Current temperature = ' + str(int(temp['temp']))+'℃. \n' +
                                 'Wind speed = ' + str(int(windspeed['speed']))+' m/s \n' + 
                                 'Humidity = ' + str(int(humidlevel))+'% \n'
                                 'Pressure = ' + str(int(pressure['press'])) + 'hPa', mention.id)
                 
                 print('found #weatherupdate', flush=True)
                 print('responding back...', flush=True) 
                 mention.favorite()
                 mention.retweet()
                 mention.user.follow()
                                                                    
              if w == 'Thunderstorm' : 
                     api.update_status('@'+ mention.user.screen_name + ' Weather update | New Delhi, IN \n ' +
                                       weather.get_status() + Thunderstorm + '\n' +                            
                                       'Current temperature = ' + str(int(temp['temp']))+'℃. \n' + 
                                       'Wind speed = ' + str(int(windspeed['speed']))+' m/s \n' + 
                                       'Humidity = ' + str(int(humidlevel))+'% \n'
                                       'Pressure = ' + str(int(pressure['press'])) + 'hPa', mention.id)
                     
                     print('found #weatherupdate', flush=True)
                     print('responding back...', flush=True) 
                     mention.favorite()
                     mention.retweet()
                     mention.user.follow()
                                                                            
              if w == 'Mist' : 
                   api.update_status('@'+ mention.user.screen_name + ' Weather update | New Delhi, IN \n' +
                                     weather.get_status() + Mist + '\n ' +                            
                                     'Current temperature = ' + str(int(temp['temp']))+'℃. \n' +
                                     'Wind speed = ' + str(int(windspeed['speed']))+' m/s \n' + 
                                     'Humidity = ' + str(int(humidlevel))+'% \n '
                                     'Pressure = ' + str(int(pressure['press'])) + 'hPa', mention.id)
                                                                                
                   print('found #weatherupdate', flush=True)
                   print('responding back...', flush=True) 
                   mention.favorite()
                   mention.retweet()
                   mention.user.follow()
                                                                             
              if w == 'Haze' : 
                      api.update_status('@'+ mention.user.screen_name + ' Weather update | New Delhi, IN \n' +
                                        weather.get_status() + Haze + '\n' +                           
                                        'Current temperature = ' + str(int(temp['temp']))+'℃. \n' +
                                        'Wind speed = ' + str(int(windspeed['speed']))+' m/s \n' + 
                                        'Humidity = ' + str(int(humidlevel))+'% \n'
                                        'Pressure = ' + str(int(pressure['press'])) + 'hPa', mention.id)
                      
                      print('found #weatherupdate', flush=True)
                      print('responding back...', flush=True) 
                      mention.favorite()
                      mention.retweet()
                      mention.user.follow()
                                                                                    
              if w == 'Dust' : 
                     api.update_status('@'+ mention.user.screen_name + ' Weather update | New Delhi, IN \n' +
                                       weather.get_status() + Dust + '\n' +                            
                                       'Current temperature = ' + str(int(temp['temp']))+'℃. \n' +
                                       'Wind speed = ' + str(int(windspeed['speed']))+' m/s \n' + 
                                       'Humidity = ' + str(int(humidlevel))+'% \n'
                                       'Pressure = ' + str(int(pressure['press'])) + 'hPa', mention.id)    
                     
                     print('found #weatherupdate', flush=True)
                     print('responding back...', flush=True) 
                     mention.favorite()
                     mention.retweet()
                     mention.user.follow()
                                                                                     
              if w == 'Notsure' : 
                    api.update_status('@'+ mention.user.screen_name + ' Weather update | New Delhi, IN \n' +
                                      weather.get_status() + Notsure + '\n ' +                            
                                      'Current temperature = ' + str(int(temp['temp']))+'℃. \n' +
                                      'Wind speed = ' + str(int(windspeed['speed']))+' m/s \n' + 
                                      'Humidity = ' + str(int(humidlevel))+'% \n'
                                      'Pressure = ' + str(int(pressure['press'])) + 'hPa', mention.id)  
                    
                    print('found #weatherupdate', flush=True)
                    print('responding back...', flush=True) 
                    mention.favorite()
                    mention.retweet()
                    mention.user.follow()
    
           elif '#newsupdate' in mention.full_text.lower(): 
              try: 
                  api.update_status('@' + mention.user.screen_name)
                  News_from_Google()
                  print('found #newsupdate', flush=True)
                  print('responding back...', flush=True)
                  mention.favorite()
                  mention.retweet()
                  mention.user.follow()   
              except tweepy.TweepError as f: 
                      if f.api_code == 187: 
                          print('duplicate status')
                      else: 
                          raise f
             
           elif '#covidupdate' in mention.full_text.lower(): 
                   api.update_status('@' + mention.user.screen_name)
                   Covid_Update() 
                   print('found #covidupdate', flush=True)
                   print('responding back...', flush=True)
                   mention.favorite()
                   mention.retweet()
                   mention.user.follow()                  
       
               
                                                                                                          
print(weather)
print('Temprature =',temp)   
print('Wind Speed =',windspeed)   
print('Pressure = ', pressure)       
print('Humidity =',humidlevel)          


while True:
    Reply_to_Tweets()
    time.sleep(5)
    
    