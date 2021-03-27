from fastapi import FastAPI, HTTPException
import requests
import math

from models.color import Color
from models.product import PaperProduct
from db import PRODUCTS

app = FastAPI()

# Specific functions for endpoint
def eucledian_distance(point1, point2):
    '''Returns the eucledian distance from 2 3-D points'''
    result = [(x2-x1)**2 for x1, x2 in zip(point1, point2)]
    return math.sqrt(sum(result))

def distances_from(color, color_list, size):
    '''Returns the eucledian distance from 2 3-D points'''
    results = []
    for elem in color_list:
        dist = eucledian_distance(color, elem.main_color.rgb())
        results.append((dist, elem))
    results.sort(key=lambda x: x[0])
    results = results[:size]
    return [x[1].get_dict() for x in results]



@app.get('/suggest_paper_product')
def get_suggest_paper_product(color: str, count: int):
    ''' This endpoint should return a list of paper products. This list will
        be in size as indicated by the "count" parameter.
        The function will attempt to obtain exact color matches and if that is
        not enough to get the values required by the "count" parameter a second
        attempt will be made by using a Eucledian distance criteria to find the
        remaining products
    '''

    # Getting "matching colors" from the external API using the requested color
    url = f'https://ryym3ua1el.execute-api.eu-central-1.amazonaws.com/prod/'
    req = requests.get(url, params={'color': color})
    try:
        match_colors = req.json()['matchingColors']
    except:
        raise HTTPException(status_code=404, detail='Item not found')

    # Appending the requested color hex value to a list, so it can be matched
    colors_to_match = [color.upper()]
    # Appending the hex values of the colors obtained from the external API
    colors_to_match += [col.upper() for col in match_colors]

    matched_products = [] # List where matched products will be placed
    temp_db = list(PRODUCTS) # Copy of Database for optimization purposes.
                             # The products found on the first iteration are
                             # removed from the list so they won't be verified
                             # again


    # First Iteration to find Exact matches
    for index, product in enumerate(PRODUCTS):
        if product.matches_color(colors_to_match, hexcheck=True):
            colors_to_match.remove(product.main_color.hexvalue)
            matched_products.append(temp_db.pop(index).get_dict())

        if not colors_to_match or len(matched_products) == count:
            break


    # Second Iteration to find closest matches using Eucledian distance.
    # This iteration will only be carried out if needed to optimize memory
    # usage
    result_length = len(matched_products)
    if result_length < count:
        # Creating a Color instance for the requested color
        req_color = Color(hexvalue=color)
        size_to_get = count-result_length
        matched_products += distances_from(req_color.rgb(),
                                           temp_db,
                                           size_to_get)

    return matched_products
