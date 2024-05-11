# VADER Sentiment Analysis

This project demonstrates how to use sentiment analysis using the VADER library. The sentiment analysis is performed on reviews fetched from a database, and the sentiment scores are then updated back into the database.

## Project Structure

The project follows the following structure:

- **models.py**: Contains the SQLAlchemy model definition for the Review table and database-related operations.
- **controller.py**: Implements the business logic for updating sentiment scores based on reviews.
- **main.py**: Sets up the FastAPI application and defines routes for interacting with the controller.
- **.env**: Contains environment variables, such as the DATABASE_URL.
- **requirements.txt**: Lists the Python dependencies required to run the project.

## Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/sentiment-analysis-vader.git
cd sentiment-analysis-vader
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up your database and update the `DATABASE_URL` and `PORT` in the `.env` file accordingly.

4. Run the FastAPI server:

```bash
python main.py
```

## Usage

Once the server is running, you can access the API at `http://localhost:8000`. 

To update sentiment scores for reviews, make a POST request to `/api/v1/update_scores`. The API will fetch reviews with missing scores, perform sentiment analysis, and update the scores in the database.

