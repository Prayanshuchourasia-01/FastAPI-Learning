from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message":"my First API is working"}

@app.get("/about")
def about():
    return {"Project":"Loan Risk Model" , "Version":"1.0"}


@app.get("/customer")
def get_customer(customerId : int):
    return {
        "customerId":customerId,
        "Name": "Ashwin",
        "Status ":"Active"
    }