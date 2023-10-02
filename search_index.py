from metaphor_python import Metaphor
from bs4 import BeautifulSoup

# Replace 'YOUR_API_KEY' with your actual Metaphor API key
api_key = '98c8e544-1e55-4fa4-b103-f8ecef2d4394'

# Initialize the Metaphor client
metaphor = Metaphor(api_key)

# Prompt the user for search query, num_results, and start_published_date
query = input("Enter the search query: ")
num_results = int(input("Enter the number of results to retrieve: "))
start_published_date = input("Enter the start published date (YYYY-MM-DD): ")

try:
    # Perform the job search using the Metaphor API
    search_response = metaphor.search(
        query=query,
        use_autoprompt=True,
        num_results=num_results,
        start_published_date=start_published_date,
        type='neural'
    )
    contents_response = search_response.get_contents()

    # Initialize a list to store cleaned text content
    cleaned_text_list = []

    # Initialize a counter for result numbering
    result_counter = 0

    # Extract and store cleaned text content for each result
    for content in contents_response.contents:
        # Increment the result counter
        result_counter += 1

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(content.extract, 'html.parser')

        # Define a function to remove unwanted elements (e.g., headers, footers)
        def remove_unwanted_elements(soup):
            # Identify and remove unwanted elements based on HTML structure
            for element in soup(["header", "footer", "nav", "aside"]):
                element.decompose()

        # Remove unwanted elements from the parsed HTML
        remove_unwanted_elements(soup)

        # Extract text content and add it to the list
        clean_text = soup.get_text()
        cleaned_text_list.append(clean_text)

        # Print numbered result
        print(f"Result {result_counter}:")
        print(f"Title: {content.title}\nURL: {content.url}\nSerial Number: {content.id}\n")

    # Prompt the user for indices of content to print
    input_indices = input("Enter the indices of content to print (comma-separated): ")
    selected_indices = [int(index) - 1 for index in input_indices.split(',')]

    # Print the selected cleaned text content
    for index in selected_indices:
        if 0 <= index < len(cleaned_text_list):
            print(f"Cleaned Text for Result {index + 1}:\n{cleaned_text_list[index]}\n")

except Exception as e:
    print("An error occurred:", str(e))

