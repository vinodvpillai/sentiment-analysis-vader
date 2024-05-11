from fastapi import FastAPI, HTTPException
from controller import update_review_scores
import uvicorn
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Endpoint to health check
@app.get("/api/v1/greet")
def greet():
    return {"message": "Hello World"}

# Endpoint to update scores for reviews with missing scores
@app.post("/api/v1/update_scores")
async def update_review_score():
    success, message = update_review_scores()
    if success:
        return {"message": message}
    else:
        raise HTTPException(status_code=500, detail=message)

# Main function
if __name__ == "__main__":
    SERVER_PORT = int(os.getenv('PORT'))
    uvicorn.run(app, host="127.0.0.1", port=SERVER_PORT)



