from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# class ParkingSlot(BaseModel):
#     "Avilable_Slot":int
#     "Occupied":int

ParkingSlot = {
     "Avilable_Slot":50,
     "Occupied":0
}

@app.get("/AvilableSlot")
def Avl_slot():
    return {
        "Avilable Slot":ParkingSlot["Avilable_Slot"]
    }

@app.get("/OccupiedSlot")
def Occ_slot():
    return {
        "Occupied": ParkingSlot["Occupied"]
    }


@app.post("/getSlot")
def getSlot(numberOfSlot:int):
    if ParkingSlot["Avilable_Slot"] >= numberOfSlot:
        ParkingSlot["Avilable_Slot"] = ParkingSlot["Avilable_Slot"]-numberOfSlot
        ParkingSlot["Occupied"] = ParkingSlot["Occupied"]+numberOfSlot
    else:
        return{
            "Booking Status" : "Failed",
            "Reason" : "Insuffient Slot"
        }
    return {
        "Slot Booked Status" : "Success",
        "Now Avilable Slot " : ParkingSlot["Avilable_Slot"]
    }

@app.post("/relieveSlot")

def RelieveSlot(numberOfSlot:int):
    if ParkingSlot["Avilable_Slot"] < 50:
        ParkingSlot["Avilable_Slot"] = ParkingSlot["Avilable_Slot"]+numberOfSlot
        ParkingSlot["Occupied"] = ParkingSlot["Occupied"] - numberOfSlot
    else:
        return{
            "Status":"Invalid"
        }
    return {
        "RelieveSlot Status" : "Success",
        "Current Avilable Slot" : ParkingSlot["Avilable_Slot"]
    }