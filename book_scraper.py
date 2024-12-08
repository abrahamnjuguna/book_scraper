import requests 
from bs4 import BeautifulSoup 
import pandas as pd 

books = []  
# Loop through the first 4 pages of the website
for i in range(1, 5):
    # Define the URL for each page (note the dynamic page number)
    url = f'https://books.toscrape.com/catalogue/page-{i}.html'
    
    # Send a GET request to the URL and get the response content
    response = requests.get(url)
    response = response.content  # Extract the content of the response
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response, 'html.parser')
    
    # Find the ordered list (<ol>) containing the book entries
    ol = soup.find('ol')
    
    # Find all book entries (<article> elements) within the <ol> list
    articles = ol.find_all('article', class_='product_pod')

    # Iterate over each book entry to extract details
    for article in articles:
        # Extract the book title from the <img> tag's 'alt' attribute
        image = article.find('img')
        title = image.attrs['alt']
        
        # Extract the star rating from the 'class' attribute of the <p> tag
        star = article.find('p')
        star = star['class'][1]  # The second class value represents the rating
        
        # Extract the price from the <p> tag with the class 'price_color'
        price = article.find('p', class_='price_color').text
        price = price[1:]  # Remove the currency symbol (£)
        
        # Append the extracted details as a list to the 'books' list
        books.append([title, star, price])

# Convert the list of books into a DataFrame for easier data manipulation
df = pd.DataFrame(books, columns=['Title', 'Star Rating', 'Price'])

# Save the DataFrame to a CSV file
df.to_csv('books.csv')

# The code scrapes book details (title, star rating, and price) from 4 pages 
# of the "Books to Scrape" website and saves the data into a CSV file.




