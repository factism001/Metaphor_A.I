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

while True:
    try:
        # Perform the job search using the Metaphor API
        search_response = metaphor.search(
            query=query,
            num_results=num_results,
            start_published_date=start_published_date,
            type='neural'
        )
        contents_response = search_response.get_contents()

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

            # Extract the main content from the cleaned HTML
            main_content = soup.get_text()

            # Print numbered result
            print(f"Result {result_counter}:")
            print(f"Title: {content.title}\nURL: {content.url}\nSerial Number: {content.id}\n")
            print(f"Main Content:\n{main_content}\n")

        # Prompt the user for a new number to print
        input_indices = input("Enter the index of content to print (or 'exit' to quit): ")

        # Check if the user wants to exit
        if input_indices.lower() == 'exit':
            break

        # Convert the input to an integer
        selected_index = int(input_indices) - 1

        # Print the selected cleaned text content
        if 0 <= selected_index < len(contents_response.contents):
            print(f"Cleaned Text for Result {selected_index + 1}:\n{main_content_list[selected_index]}\n")

    except Exception as e:
        print("An error occurred:", str(e))

