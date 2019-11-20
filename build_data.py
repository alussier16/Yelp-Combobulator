import json

#ex: trim_file("business.json", 1000)
def trim_businesses(file_businesses, num_businesses):
	file = open(file_businesses, "r")
	filedata = file.readlines()
	dataset = []
	business_id_list = []

	for line in filedata[:num_businesses]:
		data = json.loads(line)
		dataset.append(data)
		business_id_list.append(data['business_id'])
		#returns the first num_businesses businesses in the given file
	return dataset, business_id_list

def get_reviews(file_reviews, id_list):
	file = open(file_reviews, "r")
	filedata = file.readlines()
	dataset = []

	for line in filedata:
		data = json.loads(line)
		if data['business_id'] in id_list:
			dataset.append(data)
		#returns the reviews for the given business ID
	return dataset

def build_data(file_businesses, file_reviews, num_businesses):
	businesses, id_list = trim_businesses(file_businesses, num_businesses)
	reviews = get_reviews(file_reviews, id_list)

	b = open(str(num_businesses)+"businesses.json", "w+")
	r = open(str(num_businesses)+"reviews.json", "w+")

	b.write(businesses)
	r.write(reviews)


build_data("yelp_dataset/business.json", "yelp_dataset/review.json", 1000)
