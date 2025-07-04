# Pre-Market-AI-Powered-Stock-Market-Insights-Bot


## Objective

To create a Telegram bot that delivers pre-market insights based on real-time data and AI-generated analysis. The bot fetches global market indicators at predefined times, analyzes them via an AI model using a custom prompt, and sends insights directly to subscribed Telegram users. The goal is to help retail and institutional investors get a clear, data-backed picture of the market before trading hours.


## Introduction

Build a Telegram bot that automates the following:
*	Fetches important market data at predefined times (05:00 AM and 08:30 AM IST).
*	Sends this data along with a prompt to a powerful AI model (deepseek/deepseek-r1-0528:free) to generate concise, actionable insights.
*	Sends the resulting analysis via Telegram to all subscribed users.

# Technical Architecture

## DATA SOURCES

### US Indices

*	Dow Jones
*	Nasdaq
*	S&P 500

###	Global Indicators 

* 	Brent Crude Oil
*	Dollar Index (DXY)
*	USD/INR Offshore NDF
*	India VIX 

### India Indices

*   Nifty 50
*   Sensex
*   Bank Nifty

## Work Flow

<img src="app/assets/Work Flow.png" alt="Project Work Flow" width ="100" height="100" border="10"/>


## Project Structure

Pre-Market-AI-Powered-Stock-Market-Insights-Bot/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── assets/                        # Contains bot_workflow.png and other visuals
│   ├── Work Flow.png
│
│   ├── api/                           # API routing & Telegram handlers
│   │   ├── api.py
│   │   ├── telegram_bot_handlers.py
│   │   ├── __init__.py
│   │   
│
│   ├── core/                          # Constants and persistent user data
│   │   ├── constaints.py
│   │   ├── user_ids.json
│   │   ├── __init__.py
│   │   
│
│   ├── services/                      # All data fetching and AI summarization logic
│   │   ├── fetch_data.py
│   │   ├── fetch_global_indices_data.py
│   │   ├── fetch_india_indices_data.py
│   │   ├── fetch_us_indices_data.py
│   │   ├── get_ai_stock_summary.py
│   │   ├── get_us_index_ticket.py
│   │   ├── __init__.py
│   │   
│
├── requirements.txt                  # Python dependencies
├── README.md                         # Project documentation
└── LICENSE                           # (If added)



##  Use Cases

*	Retail Traders: Quickly understand market mood.
*	Brokerage Firms: Share with clients as value-added service.
*	Institutional Investors: Supplement internal dashboards.
*	Finfluencers/Communities: Get daily talking points.


## How to install this project 

* clone this repo 
        git clone https://github.com/Pranith124/Pre-Market-AI-Powered-Stock-Market-Insights-Bot.git
        cd Pre-Market-AI-Powered-Stock-Market-Insights-Bot
* create a new virtual environment and activate it 
* install the requirements
        pip install -r requirements.txt
* Add your API keys
        Telegram bot token
        AI model API token
* place the tokens on core package on constraints.py file
* create a user_ids.json file at core package for storing ids of subscribers
* run the project by pass the command 




