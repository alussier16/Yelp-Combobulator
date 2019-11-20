import json

#ex: trim_file("business.json", 1000)
def trim_businesses(file_businesses, num_businesses):
	file = open(file_name, "r")
    filedata = file.readlines()
    dataset = []
    for i in range (0, num_businesses):
    	dataset.append(data['text'])
    #returns the first num_businesses businesses in the given file
    return dataset

def get_business_reviews(file_reviews, business_id):
    file = open(file_name, "r")
    filedata = file.readlines()
    dataset = []

    for line in filedata:
        data = json.loads(line)
        if data['business_id'] == business_id:
            dataset.append(data['text'])
    #returns the reviews for the given business ID
    return dataset

def build_data(file_businesses, file_reviews, num_businesses):
	businesses = trim_businesses(file_businesses, num_businesses)
	business_data=businesses.file.readlines()
	reviews = []
	b = open((str)num_businesses+businesses.json, "w+")
	r = open((str)num_businesses+reviews.json, "w+")

	for line in business_data:
		data = json.loads(line)
		b.write(data['text'])
		if data['business_id'] in business_data:
			temp_reviews = get_business_reviews(file_reviews, data['business_id'])
			reviews.append(temp_reviews)
			r.write(temp_reviews)

build_data("yelp_dataset/business.json", "yelp_dataset/review.json", 1000)
