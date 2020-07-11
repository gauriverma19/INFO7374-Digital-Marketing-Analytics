# Implementing Visual Search

## Team Information
| Name | NEU ID |
| --- | --- |
| Shubham Mahajan | 001314273 |
| Gauri Verma | 001306996 |
| Anurag Rachcha | 001375637 |


## Claat Link: 
https://codelabs-preview.appspot.com/?file_id=1s2TD3Hrc1xRaptC6GOS7QoZSNMhPvtcofi07SycDlJE#0

## Streamlit app - Hosted on Heroku platform


![streamlitapp-herokuhost](https://user-images.githubusercontent.com/59700753/87215750-99c17000-c307-11ea-965d-67a4aa6c868d.png)


## About the dataset: 

We will be using the Cdiscount dataset for our image similarity search. Cdiscount.com is France's largest non-food e-commerce company. While the company already sells everything from TVs to trampolines, the list of products is still rapidly growing. Cdiscount.com has over 30 million products up for sale. Below is a brief overview of the data used in our analysis-

train.bson - (Size: 58.2 GB) Contains a list of 7,069,896 dictionaries, one per product. Each dictionary contains a product id (key: _id), the category id of the product (key: category_id), and between 1-4 images, stored in a list (key: imgs). Each image list contains a single dictionary per image, which uses the format: {'picture': b'...binary string...'}. The binary string corresponds to a binary representation of the image in JPEG format.
Data Source :- https://www.kaggle.com/c/cdiscount-image-classification-challenge

Here is a brief description of the folder contains :- 

Cosine Similarity and FAISS: Contains python files and images used for the respective search algorithms

Spotify: Contains python files, images, and the json files created using Spotify Annoy method

Streamlit: Contains the images, .py code for the application, files for heroku deployment, and the csv files used for the application.



