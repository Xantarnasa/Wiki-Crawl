import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from time import sleep
liste_title=[]
liste_url=[]
# Function to fetch the HTML content of a given URL
def get_page(url):
    # Open the connection to the specified URL
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)

    # Read and return the content of the response
    return response.read()

# Function to extract all the links from a given HTML
def parse_links(html, base_url):
    # Use Beautiful Soup to parse the HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Create an empty list to store the extracted links
    links = []

    # Find all anchor tags in the parsed HTML
    for link in soup.findAll('a'):
        # Get the value of the 'href' attribute
        href = link.attrs.get('href')

        # If the 'href' attribute doesn't exist or has no value, skip this link
        if href == '' or href is None:
            continue

        # Join the base URL and the relative link to form an absolute URL
        full_url = urljoin(base_url, href)

        # Add the absolute URL to the list of links
        links.append(full_url)
        liste_url.append(full_url)
    # Return the list of links
    return links

# Function to print the title tag of a given HTML
def print_title(html):
    # Parse the HTML using Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the <head> element
    head = soup.head
    if head is None:
        # If the <head> element isn't present, return without doing anything
        return

    # Find the <title> element within the <head> element
    title = head.title
    if title is not None:
        # Print the text inside the <title> element
        liste_title.append(title.string)
        print(title.string)
# The entry point of our script
def main():
    # Ask the user for the initial URL
    url = input("Enter the starting URL: ")

    # Fetch the HTML content of the initial URL
    html = get_page(url)

    # Print the title tag of the fetched HTML
    print_title(html)

    # Extract all the links from the fetched HTML
    links = parse_links(html, url)

    # Iterate over every extracted link
    for link in links:
        try:
            # Fetch the HTML content of the current link
            html = get_page(link)

            # Print the title tag of the newly fetched HTML
            print_title(html)
        except Exception as e:
            # In case something goes wrong while trying to fetch the new link,
            # catch the exception and print an error message along with its type
            print(f"Error accessing {link}: {e}")

# Run the main function only when this script is run directly (not imported)
if __name__ == "__main__":
    main()