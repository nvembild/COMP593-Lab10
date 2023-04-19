'''
Library for interacting with the PokeAPI
https://pokeapi.co/
'''
import requests
import image_lib
import os
 
POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'
 
def main():
    # Test out the get_pokemon_into() function
    # Use breakpoints to view returned dictionary
    #poke_info = get_pokemon_info("Rockruff")
    #poke_info = get_pokemon_info(123)
    download_poke_img('ditto', r'D:\clg')
    return

def get_pokemon_info(pokey_name):
    """Gets information about a specified Pokemon from the PokeAPI.

    Args:
        pokemon_name (str): Pokemon name (or Pokedex number)

  Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
# Clean the Pokemon name parameter by:
    # - Converting to a string object, 
    # - Removing leading and trailing whitespace, and
    # - Converting to all lowercase letters
    pokey_name = str(pokey_name).strip().lower()

# Build the clean URL for the GET request
    url = POKE_API_URL + pokey_name
 
    # Send GET request for Pokemon info
    print(f'Getting information for {pokey_name}...', end='')
    resp_msg = requests.get(url)

# Check if request was successful
    if resp_msg.status_code == requests.codes.ok:
        print('success')
        # Return dictionary of Pokemon info
        return resp_msg.json()

    else:
        print('failure')
        print(f'Response code: {resp_msg.status_code} ({resp_msg.reason})')         
        return
    
def get_pokemon_names(offset=0, limit=100000):
    query_str_params = {
        'offset' :offset,
        'limit' :limit
    }

    resp_msg = requests.get(POKE_API_URL, params=query_str_params)

    if resp_msg.status_code == requests.codes.ok:
        poke_dict = resp_msg.json()
        poke_names_list = [p['name'] for p in poke_dict['results']]
        return poke_names_list
    
    else:
        print('failure')
        print(f'Response code: {resp_msg.status_code} ({resp_msg.reason})')
        return
    
def download_poke_img(pokey_name, save_dir):
    pokey_info = get_pokemon_info(pokey_name)
    if pokey_info is None:
        return
    
img_url = pokey_info['sprites']['other']['official-artwork']['front_default']

image_bytes = image_lib.download_picture(img_url)
if image_bytes is None:
    return

    
file_extn =  img_url.split('.')[-1]
image_path = os.path.join(save_dir, pokey_name)
    
if image_lib.save_picture_file(image_bytes, image_path):
    return image_path

     

    return

if _name_ == '_main_':  
    main()





