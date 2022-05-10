
import requests

def get_books():


    booksAPI = "https://api.nytimes.com/svc/books/v3/lists/full-overview.json"

    API_KEY = "LQ8st1GtDxGKCPpsDLYMoLqdq3HAWsEe"
    query = f'{booksAPI}?api-key={API_KEY}'
    response = requests.get(query)

    return response.json()