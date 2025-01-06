"""
Source Code : REST API Endpoints creation using Fast API
"""
from typing import Dict, List , Optional
from fastapi import FastAPI, Query , Path , HTTPException , status , Body
from model import car_model
from test import cars_data

app = FastAPI() #create a FASTAPI application

"""
Now create a decorator and function for the Endpoints accordingly
"""

#endpoint
@app.get("/")
def root():
    """ 
        Function what it should return for the endpoint 
            by default FAST API will return json formats
    """
    return {"User" : "Hello world using FASTAPI by chandu!!!"}

#Create an endpoin which will return all the cars
@app.get("/cars" , response_model = List[Dict[int,car_model.CarModel]])
def get_cars(number : Optional[int] = Query(10)):
    """
        End point which will return the no of cars requested
    """
    result = []
    for id,car in list(cars_data.cars.items())[:int(number)]:
        response = {}
        response[id] = car
        result.append(response)
    return result

#create an Endpoint which will return car details based on id
@app.get("/cars/{id}", response_model=car_model.CarModel)
def get_car_by_id(id : int = Path(...,ge=0,le=999)):
    """
        End point which will return the car details for the given id
    """
    response = cars_data.cars.get(id)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Card ID not found , Please enter a valid one!")
    else:
        return response

#Create endpoint to Post car details
@app.post("/cars",status_code=status.HTTP_201_CREATED)
def post_car_details(body_car = List[car_model.CarModel] , min_id : Optional[int] = Body(0)):
    """
     Function to Create the Car Details in the Database
    """
    if len(body_car)<1:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Please Enter Car Details to add!!!")
    min_id = len(cars_data.cars.values()) + min_id
    for car in body_car:
        while cars_data.cars.get(min_id):
            min_id+=1
        cars_data.cars[min_id] = car
        min_id+=1
    #return {"status" : status.HTTP_201_CREATED}