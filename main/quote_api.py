import urequests as requests

def quote_pull():
    api_key='d1939ae5c27eba55753d8075f65e7d0d'
    response = requests.get('https://favqs.com/api/qotd')
    data=response.json()
    author=data['quote']['author']
    quote=data['quote']['body']
    q_list=[quote,author]
    return q_list
    


