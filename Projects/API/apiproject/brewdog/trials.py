import requests 
from requests.exceptions import HTTPError
from getpass import getpass

def trial():
    url = 'https://api.punkapi.com/v2/beers?abv_gt=6'
    # response = requests.get(url, params={'brewed_before':'11-2010'})
    # response = requests.get(url, params=[('brewed_before','11-2010')], timeout = (2, 5))
    response = requests.get(url, params=b'brewed_before=11-2010')
    if response.status_code == 200:
        print('Whats up')
        # print(response.content)
        print(response.status_code)
        response.encoding = 'utf-8'
        beer_methods = response.json()
        print(type(response))
        # print(response.content)
        
        # print(beer_methods.index('value'))
        counter = 1
        beer_names = []
        images = []
        for items in beer_methods:
            # print(items)
            # print(f'items is a {type(items)}')
            # list(items)
            # print(type(items))
            first_brew = items['name']
            image_location = items['image_url']
            beer_names.append(first_brew)
            images.append(image_location)
            print(f" Beer {counter} Name : {first_brew} \n Beer {counter}\'s photo can be found via this link{image_location}")
            counter +=1
        print(beer_names)
        print(images)
        # list(beer_methods)
        # print(type(beer_methods))
        # for items in beer_methods:
        #     print(items)
        # print(response.headers)
        # print(response.request.body)
        # print(response.request.url)
        # print(response.headers['Content-Type'])
        
    else:
        print("Nein")
    # for url in 'https://api.punkapi.com/v2/beers?brewed_before=11-2012&abv_gt=6':
    #     try:
    #         response = requests.get(url)

    #         response.raise_for_status()

    #     except HTTPError as http_err:
    #         print(f'http error occurred: {http_err}')
    #     except Exception as err:
    #         print(f'Other error occurred: {err}')
    #     else:
    #         print('Success')
    
    


trial()