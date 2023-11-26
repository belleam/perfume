## Fragrance Matchmaker

The Fragrance Matchmaker contains three different recommendation systems for fragrances:
* Scent Matcher - a content-based recommendation model based on scent notes
* Sensation Matcher - a content-based recommendation model based on sentiment scores of each perfume’s description
* Shape Matcher - a recommendation system based on visual similarity using the CNN model VGG-16 to match perfumes by shape

Details of the data processing and model creation are in the [perfume.ipynb notebook](https://github.com/belleam/perfume/blob/main/perfume.ipynb).

The models have also been implemented in a [Streamlit app](https://fragrancematchmaker.streamlit.app/). The code for these are in Hompeage.py and in the pages folder.

The dataset is from [Kaggle](https://www.kaggle.com/datasets/nandini1999/perfume-recommendation-dataset) and was scraped from the fragrance retailer Luckyscent's e-commerce website.