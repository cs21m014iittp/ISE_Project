from google_play_scraper import reviews
import csv
import time
import random


batch_size = 199
num_batches = 1000
app_list = ["org.mozilla.firefox","org.videolan.vlc"] # fill in app names


#function to extract the comment and star info from the raw json text
def process_and_combine(current_review_set,raw_reviews):
	for review in raw_reviews:
		temp=[]
		temp.append(review['content'])
		temp.append(review['score'])

		# check if this review was already seen before
		if temp not in current_review_set:
			current_review_set.append(temp)

	return current_review_set


# function to get as much reviews as we can
def get_reviews(app_name):
	result = []

	#get first batch of reviews and the nextPageToken
	temp_list , token = reviews(app_name,count=batch_size)
	
	#process and combine the current batch with overall result
	result = process_and_combine(result,temp_list)
	prev_review_count = len(result)
	
	# keep fetching reviews for the given number of batches
	for i in range(num_batches-1):
		temp_list,token = reviews(app_name,count=batch_size,continuation_token=token)

		result = process_and_combine(result,temp_list)

		#if no new reviews are fetched then stop
		if(prev_review_count == len(result)):
			break

		else:
			prev_review_count = len(result)
		
		if i%50==0:
			# print update on number of batches
			print(f'Batch {i/50} completed.')
			# print the number of reviews so far
			print(f'Successfully inserted {len(result)} {app_name} reviews into collection.\n')
	

	return result


if __name__ == "__main__":
	#open a csv file to write the output 	
	
	for app in app_list:
		output_file_name = "raw_data_"+app+".csv"
		with open(output_file_name,'w',newline='',encoding="utf-8") as output_file:
			output_writer = csv.writer(output_file)
			#write the header
			output_writer.writerow(['comment','star'])

			review_list = get_reviews(app)
			for review in review_list:
				try:
					output_writer.writerow(review)
				except csv.Error as error:
					print("error occured for review:",review)
					print(error)

		

