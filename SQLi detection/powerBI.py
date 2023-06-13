import requests
import json
from bs4 import BeautifulSoup

# Make a request to the website with the data
url = 'https://www.boxofficemojo.com/chart/top_lifetime_gross/?ref_=bo_cso_ac_tab_toplifetimegross'
response = requests.get(url)

# Parse the HTML with Beautiful Soup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table with the movie data
table = soup.find('table')

# Find all rows in the table
rows = table.find_all('tr')

# Create a list to hold the movie data
movies = []

# Loop through each row and extract the movie data
for row in rows:
    cells = row.find_all('td')
    if len(cells) != 5:
        continue
    rank = cells[0].text.strip()
    title = cells[1].text.strip()
    studio = cells[2].text.strip()
    gross = cells[3].text.strip()
    year = cells[4].text.strip()
    movie = {
        'rank': rank,
        'title': title,
        'studio': studio,
        'gross': gross,
        'year': year
    }
    movies.append(movie)
    print(movie)

# Write the movie data to a JSON file
if movies:
    with open('top_grossing_movies.json', 'w') as f:
        json.dump(movies, f, indent=4)
        print("JSON file written successfully")
else:
    print("No data found")
