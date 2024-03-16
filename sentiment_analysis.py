"""


"""
import os
import sys
import spacy
import pandas as pd
from spacytextblob.spacytextblob import SpacyTextBlob   


nlp = spacy.load("en_core_web_sm")
nlp_lg = spacy.load('en_core_web_lg')
nlp.add_pipe('spacytextblob')

# Create dataframe reading from CSV

df = pd.read_csv(os.path.join(sys.path[0],'amazon_product_reviews.csv'))

# Selects reviews.text column

reviews_data = df['reviews.text']

# Clean data

clean_data = reviews_data.dropna()

# Function for predicting the sentiment of a review

def sentiment_prediction():
    
    text = nlp(review)

    # Sentiment polarity and subjectivity

    polarity = text._.blob.polarity
    sentiment = text._.blob.sentiment

    # Returns a rating based on polarity

    if (polarity >= 0.5):
    
        return sentiment, "Very Positive"

    elif (polarity >= 0.25):
        
     return sentiment, "Positive"

    elif (polarity > 0):

        return sentiment, "Slightly Positive"

    elif (polarity <= -0.5):
        
        return sentiment, "Very Negative"
    
    elif (polarity <= -0.25):
        
        return sentiment, "Negative"
    
    elif (polarity < 0):

        return sentiment, "Slightly Negative"

    else:

        return sentiment, "Neutral"

# Function for similarity

def similarity():
    
    text1 = nlp_lg(compare1)
    text2 = nlp_lg(compare2)

    # Produces and returns score on how similar the texts are

    similarity_score = text1.similarity(text2)

    return similarity_score

# Testing sentitment_prediction function

key = 176
review = str(clean_data[key])
print(f"REVIEW: {review}\nSENTIMENT: {sentiment_prediction()}")

key = 2482
review = str(clean_data[key])
print(f"REVIEW: {review}\nSENTIMENT: {sentiment_prediction()}")

key = 0
review = str(clean_data[key])
print(f"REVIEW: {review}\nSENTIMENT: {sentiment_prediction()}")

# Testing Similarity function

compare1 = str(clean_data[23])
compare2 = str(clean_data[124])
print (f"SIMILARITY SCORE: {similarity()}")

compare1 = str(clean_data[25])
compare2 = str(clean_data[25])
print (f"SIMILARITY SCORE: {similarity()}")

compare1 = str(clean_data[240])
compare2 = str(clean_data[1240])
print (f"SIMILARITY SCORE: {similarity()}")