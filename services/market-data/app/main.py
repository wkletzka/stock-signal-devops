##  Market Data Microservice ##
from fastapi import FastAPI
import os
import requests

app = FastAPI()

API_KEY = os.getenv("ALPHA_VANTAGE_KEY") #used 'export ..." to set API key

print("API_KEY:", os.environ.get("API_KEY")) #debugging

@app.get("/health") #FastAPI route decorator used to handle GET requests to /health
def health(): ##function that handles that request - this is just to make sure service works
    return {"status": "ok"}

@app.get("/price")
def get_price(symbol: str): #FastAPI expects a query parameter, e.g. /price?symbol=AAPL
    if not API_KEY:
        return {"error": "API key not set"} #checks that the api key exists in the env
    
    url = "https://www.alphavantage.co/query" #setting up stock API url and parameters to get data
    params = {
        "function": "GLOBAL_QUOTE", #AlphaVantage endpoint used for current stock prices
        "symbol": symbol,           #Stock ticker passed in by user
        "apikey": API_KEY           #secret key injected from environment
    }

    response = requests.get(url, params=params) #sends GET request to AV with query paramters
    if not response.ok: #checks if response was NOT properly received (not codes 200-299)
        return {"error": f"request failed -> status code: {response.status_code}"} #return error code
        
    data = response.json() #store data from api call
    print(data)

    price = data["Global Quote"]["05. price"] 
    open = data["Global Quote"]["02. open"] 
    high = data["Global Quote"]["03. high"] 
    low = data["Global Quote"]["04. low"] 
    vol = data["Global Quote"]["06. volume"] 
    latestDay = data["Global Quote"]["07. latest trading day"]
    previousClose = data["Global Quote"]["08. previous close"]
    change = data["Global Quote"]["09. change"]
    changePercent = data["Global Quote"]["10. change percent"]

    return {
        "symbol": symbol,
        "price": price,
        "open": open,
        "high": high,
        "low": low,
        "volume": vol,
        "latest trading day": latestDay,
        "previous close": previousClose,
        "change ($)": change,
        "change percent": changePercent
    }

    #timeSeries = data["Time Series (5min)"] 
    #latestTime = sorted(timeSeries.keys())[-1]  if I had the premium version I could use this
    #price = timeSeries[latestTime]["4. close"]