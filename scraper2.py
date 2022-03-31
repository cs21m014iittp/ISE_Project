from google_play_scraper import app, reviews_all

review_list = reviews_all('com.cricbuzz.android.vernacular')

#continuation = _ContinuationToken(len(review_list))
print(len(review_list))
print(review_list[0])
