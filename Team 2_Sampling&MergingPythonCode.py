import pandas as pd

#sampling data
# try:
#     from StringIO import StringIO
# except ImportError:
#     from io import StringIO
# review_file = 'yelp_tip.csv'    # replace this with your data file
# df = pd.read_csv(review_file)
# df_sample = df.sample(frac=0.05)
# df_sample.to_csv("yelp_tip_sample.csv", index=None)

#import files
review = pd.read_csv('yelp_review_sample.csv')
business = pd.read_csv('yelp_business_sample.csv')
print(review.columns)
print(business.columns)
review = review.rename(columns={'date':'review_date', 'stars':'review_stars'})
business = business.rename(columns={'name':'business_name','neighborhood':'bs_neighborhood', 'address': 'bs_address',
                                    'city':'bs_city', 'state':'bs_state', 'postal_code': 'bs_postal_code',
                                    'latitude':'bs_latitude', 'longitude': 'bs_longitude', 'stars':'bs_stars',
                                    'review_count': 'bs_review_count', 'is_open':'bs_is_open',
                                    'categories':'bs_categories'})

#merge files
review_business_merged = pd.merge(review, business, how='inner', on = 'business_id')

#change columns order


review_business_merged= review_business_merged[['review_id', 'user_id', 'business_id','business_name','bs_stars',
                                               'review_stars','text', 'review_date', 'useful', 'funny', 'cool',
                                               'bs_neighborhood','bs_address', 'bs_city','bs_state','bs_postal_code',
                                               'bs_latitude', 'bs_longitude', 'bs_review_count', 'bs_is_open',
                                               'bs_categories']]

review_business_merged.to_csv('business_review_sample.csv', index=False)