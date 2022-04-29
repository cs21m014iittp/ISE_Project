import pandas as pd
import numpy as np

data = pd.read_csv("match_output.csv")
final_output = open("final_output.txt",'w')


total_reviews = data.shape[0]
reviews_with_one_match = 0
reviews_with_two_match = 0
reviews_with_three_match = 0

temp = 0
for index,row in data.iterrows():
	flag = [False,False,False]

	# find out if the current review has a match and if yes then mark how many matches it has
	try:
		if not pd.isna(row['report1']) :
			flag[0]=True
			reviews_with_one_match += 1
	except:
		temp += 1

	try:
		if not pd.isna(row['report2']) :
			flag[1]=True
			reviews_with_two_match += 1
			reviews_with_one_match -= 1
	except:
		temp += 1

	try:
		if not pd.isna(row['report3']) :
			flag[2]=True
			reviews_with_three_match += 1
			reviews_with_two_match -= 1
	except:
		temp += 1

	# store the review if it has a match and all the corresponding matching bug reports

	if flag[0]:
		final_output.write("-------------------------------------------------------------------------\n")
		final_output.write("review:-\n")
		final_output.write(f"{row['review']}\n\n")
		final_output.write(f"Match 1:\n")
		final_output.write(f"{row['report1']}\n")
		final_output.write(f"similarity score: {row['similarity_value'].lstrip('[').rstrip(']').split(',')[0]}\n\n")
	else:
		continue

	if flag[1]:
		final_output.write(f"Match 2:\n")
		final_output.write(f"{row['report2']}\n")
		final_output.write(f"similarity score: {row['similarity_value'].lstrip('[').rstrip(']').split(',')[1]}\n\n")
	else:
		#final_output.write("-------------------------------------------------------------------------\n")
		continue


	if flag[2]:
		final_output.write(f"Match 3:\n")
		final_output.write(f"{row['report3']}\n")
		final_output.write(f"similarity score: {row['similarity_value'].lstrip('[').rstrip(']').split(',')[2]}\n\n")
	else:
		#final_output.write("-------------------------------------------------------------------------\n")
		continue




final_output.write("total number of reviews = {}\n".format(total_reviews))
final_output.write("total number of reivews with one matching bug report = {}\n".format(reviews_with_one_match))
final_output.write("percentage = {}\n".format((reviews_with_one_match*100)/total_reviews))
final_output.write("total number of reivews with two matching bug reports = {}\n".format(reviews_with_two_match))
final_output.write("percentage = {}\n".format((reviews_with_two_match*100)/total_reviews))
final_output.write("total number of reivews with three matching bug reports = {}\n".format(reviews_with_three_match))
final_output.write("percentage = {}\n".format((reviews_with_three_match*100)/total_reviews))
