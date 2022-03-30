from google_play_scraper import app, reviews

review_list = []

list,continuation = reviews(
					'com.cricbuzz.android.vernacular',
					)
review_list.append(list)
while len(review_list) < 30000:
	list,continuation = reviews(
						'com.cricbuzz.android.vernacular',
						continuation_token=continuation
						)
	review_list.append(list)

print(len(review_list))

