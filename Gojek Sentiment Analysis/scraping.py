from google_play_scraper import reviews, Sort
import pandas as pd

# Define app ID
app_id = "com.gojek.app"

# Initialize variables
all_reviews = []
token = None  # Start without a token
total_reviews = 30000  # Target number of reviews

while len(all_reviews) < total_reviews:
    print(f"Scraping... Collected {len(all_reviews)} reviews so far.")

    # Fetch reviews with continuation token
    review_data, token = reviews(
        app_id,
        lang="id",
        country="id",
        sort=Sort.MOST_RELEVANT,
        count=1000,  # Fetch in batches of 1000
        continuation_token=token  # Use token for pagination
    )

    all_reviews.extend(review_data)

    # Stop if there are no more reviews
    if token is None:
        break

# Convert to DataFrame
df = pd.DataFrame(all_reviews)

# Save to CSV
df.to_csv("gojek_reviews.csv", index=False)

print(f"Scraping complete! {len(df)} reviews saved to 'gojek_reviews.csv'.")
