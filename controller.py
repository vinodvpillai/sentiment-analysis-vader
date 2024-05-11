from models import SessionLocal, Rating
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def update_review_scores():

    db = SessionLocal()
    try:
        # Fetch reviews with missing scores
        reviews = db.query(Rating).filter(Rating.score.is_(None)).all()
        if not reviews:
            return False, "No reviews with missing scores found"
        
        # Initialize sentiment analyzer
        analyzer = SentimentIntensityAnalyzer()
        # Update scores for each review
        for r in reviews:
            # Calculate sentiment score for review text
            sentiment_score = analyzer.polarity_scores(r.review)["compound"]
            # Update review score in database
            r.score = sentiment_score
        
        db.commit()
        return True, "Scores updated successfully"
    except Exception as e:
        db.rollback()
        return False, str(e)
    finally:
        db.close()
