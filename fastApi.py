from fastapi import FastAPI
import uvicorn


app=FastAPI()

@app.get("/users")
def hello():
    return "hello world"

@app.post("/hello")
def greetings(name:str):
    return (f"hello {name} . how are you ?")

if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=3000)