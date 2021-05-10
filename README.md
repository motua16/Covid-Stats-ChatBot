# Covid-Stats-ChatBot

ChatBot that gives real time statistics for any location in India. It currently accepts any post-office/district/state name. 

__Bot utilises the following API's:__

Covid19india API: 
* https://api.covid19india.org/data.json
* https://api.covid19india.org/state_district_wise.json

Postal PIN Code API:
* http://www.postalpincode.in/Api-Details

## About

### Project Overview

A bot that gives real time covid-19 data can be very handy. It also handles general chitchat and maintains an interactive conversation.

The main tasks involved in this project are as follows:
* Defining various intents that we want the bot to identify
* Defining the domain, general stories and rules that it needs to follow
* Defining actions that it needs to perform in various circumstances
* Training the model on this data


## Demo

![](gif/gif.gif)

## How to use

* Clone the repo and change your directory:
  
  `git clone https://github.com/motua16/Covid-Stats-ChatBot `
  
  `cd Covid-Stats-ChatBot`

* Create a virtual Environment and activate it

  `python3 -m venv env`
  
  `source env/bin/activate`

* Install rasa-x

  `pip install pip rasa-x -i https://pypi.rasa.com/simple`
  
* Open rasa shell and interact

  `rasa shell -m models/final.tar.gz`
  
## Features and Limitations

The bot currently has these features:

* It remembers your name from earlier in the conversation
* It gives the data for district corresponding to the pincode/city/post-office name you enter. For eg: if you type 110016, which is the pincode for Hauz Khas, New Delhi then it gives you the data for the District under which it comes i.e., South West Delhi
* It asks if you want previously calculated results, if prompt is yes: then the previous result is shown, otherwise Nationwide data is shown
* It can handle basic greetings and conversations

These are the limitations:

* Since there can be multile places in India with the same name, sometimes we get results that are not what we expect. So it is better to go with pincodes
* There can be minor spelling difference for the same place in the 2 API's that are being called, in which case we dont get desired results. for  eg `Visakhapatnam and Vishakhapatnam`
* Sometimes the bot can interpret name of a person as a place or vice versa. So it is better to use complete sentences like `My name is John` when asked


## Repository Structure

```
- bot
| - actions # package containing actions
| |- __pycache__  #bytecode-compiles version of program files
| |- __init__ # defines a package
| |- actions_1.py # handles calls to api's
| |- actions_2.py # handles name of user
| |- actions_3.py # handles if the user wants previously fetched results

| - data
| |- nlu.yml # intents definition
|-|- rules.yml  # defines rules
|-|- stories.yml # defines stories

- demo
|- gif.gif # animation 

- models
|- final.tar.gz # final trained model

- README.md

- tests
|- test_stories #  test stories

- config.yml # configuration
- credentials.yml # adding REST endpoints
- domain.yml # define domain of the bot
- endpoints.yml # defining action endpoint



```

## Further Steps


* Deploy this bot on WhatsApp or Telegram 
* Deploy as an online application
* Giving more training examples and defining strategies so that the bot can effectively distinguish between name of a person and name of a place.
