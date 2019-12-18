import json

#ex: trim_file("business.json", 1000)
def trim_businesses(file_businesses, num_businesses):
	file = open(file_businesses, encoding="utf8")
	filedata = file.readlines()
	dataset = []
	business_id_list = []
	total_reviews = 0
	for line in filedata[:num_businesses]:
		data = json.loads(line)
		dataset.append(data)
		business_id_list.append(data['business_id'])
		total_reviews += data['review_count']
		#returns the first num_businesses businesses in the given file
	return dataset, business_id_list, total_reviews

def get_reviews(file_reviews, id_list):
	dataset = []
	total_words, total_sentences = 0, 0
	with open(file_reviews, encoding="utf8") as filedata:
		for line in filedata:
			data = json.loads(line)
			if data['business_id'] in id_list:
				dataset.append(data)
				total_words += len(data['text'].split())
				total_sentences += data['text'].count('.')
		#returns the reviews for the given business ID
	return dataset, total_words, total_sentences

def build_data(file_businesses, file_reviews, num_businesses):
	businesses, id_list, total_reviews = trim_businesses(file_businesses, num_businesses)
	total_business = num_businesses
	reviews, total_words, total_sentences = get_reviews(file_reviews, id_list)
	wpr = total_words/total_reviews
	rpb = total_reviews/total_business
	spr = total_sentences/total_reviews
	stats = {'Total reviews':total_reviews, 'Total words':total_words, 'Total sentences':total_sentences, 'Average words per review':wpr, 'Average sentences per review':spr, 'Average reviews per business':rpb}
	with open("stats.json", "w+") as outfile:
		json.dump(stats, outfile)
	with open("short_businesses.json", "w+") as outfile:
		json.dump(businesses, outfile)
	with open("short_reviews.json", "w+") as outfile:
		json.dump(reviews, outfile)

build_data("yelp_dataset/business.json", "yelp_dataset/review.json", 1000)