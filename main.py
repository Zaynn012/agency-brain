from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def read_root():
    return{"service":"agencybrain","status":"running"}

@app.get("/health")
def health_check():
    return{"stauts":"okayish"}
