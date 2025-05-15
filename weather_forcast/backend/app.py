"""
Source Code for Backend APIs using FASTAPI
"""
import os
import uvicorn
from fastapi import FastAPI , HTTPException , Query
from fastapi.middleware.cors import CORSMiddleware
from cachetools import TTLCache
from dotenv import load_dotenv
import httpx

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

weather_cache = TTLCache(maxsize=100 , ttl=6000)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get('/')
def home():
    """
        Default Root API call
    """
    return {
        "message" : "Hello World From FastAPI"
    }

@app.get('/weather')
async def get_weather(city : str = Query(...,description="Enter City Name")):
    """
        Weather Forcast by City
    """
    city = city.lower().strip()

    if city in weather_cache:
        return {
                    "source" : "cache",
                    "data" : weather_cache[city]
                }

    params = {
                "q" : city,
                "appid" : API_KEY,
                "units" : "metric"
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                                        BASE_URL,
                                        params = params,
                                        timeout = 5.0
                                    )
            response.raise_for_status()
            data = response.json()
    except httpx.HTTPError as e:
        raise HTTPException(status_code=502,detail=f"Error Contacting OpenWeatherMap :: {str(e)}")
    
    final_data = {}
    final_data["city"] = data.get("name").capitalize()
    final_data["condition"] = data.get("weather")[0].get("main")
    final_data["temperature"] = data.get("main").get("temp")
    final_data["humidity"] = data.get("main").get("humidity")
    final_data["wind_speed"] = data.get("wind").get("speed")

    weather_cache[city] = final_data
    
    return {
                "source" : "live",
                "data" : final_data
            }



if __name__ == '__main__':
    uvicorn.run("app:app", host="127.0.0.1", port = 8000, reload= True)
  