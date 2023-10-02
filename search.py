from metaphor_python import Metaphor
from bs4 import BeautifulSoup


# Replace 'YOUR_API_KEY' with your actual Metaphor API key
api_key = '98c8e544-1e55-4fa4-b103-f8ecef2d4394'

# Initialize the Metaphor client
metaphor = Metaphor(api_key)

# Define your search query and location (you can modify these values)
query = 'job vacancies'
location = 'lagos'  # Replace with your desired location

try:
    # Perform the job search using the Metaphor API
    search_response = metaphor.search(
            query=query, 
            num_results=5,
            start_published_date='2022-01-01',
            type='neural'
            )
    contents_response = search_response.get_contents()

    # Print content for each result
    for content in contents_response.contents:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(content.extract, 'html.parser')

        # Extract text content
        clean_text = soup.get_text()

        print(f"Title: {content.title}\nURL: {content.url}\nSerial Number: {content.id}\n")

except Exception as e:
    print("An error occurred:", str(e))

