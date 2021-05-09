# Covid-Stats-ChatBot
Get live Covid-19 stats for any Pincode/Town/State in India with this Rasa ChatBot

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

## Demo

![](demo/gif.gif)

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




