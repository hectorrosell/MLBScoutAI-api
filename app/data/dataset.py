# @title Import Python Libraries
# General data science libraries
import pandas as pd
import numpy as np

# Pulling data from APIs, parsing JSON
import requests
import json

# Interfacing w/ Cloud Storage from Python
# from google.cloud import storage

# Plotting
# import matplotlib.pyplot as plt
# import seaborn as sns

# from IPython.display import HTML, Image

# @title Function to Load Newline Delimited JSON into Pandas DF
def load_newline_delimited_json(url):
    """Loads a newline-delimited JSON file from a URL into a pandas DataFrame.

    Args:
        url: The URL of the newline-delimited JSON file.

    Returns:
        A pandas DataFrame containing the data, or None if an error occurs.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        data = []
        for line in response.text.strip().split("\n"):
            try:
                data.append(json.loads(line))
            except json.JSONDecodeError as e:
                print(f"Skipping invalid JSON line: {line} due to error: {e}")

        return pd.DataFrame(data)
    except requests.exceptions.RequestException as e:
        print(f"Error downloading data: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


# @title Function to Process Results from Various MLB Stats API Endpoints
def process_endpoint_url(endpoint_url, pop_key=None):
    """
    Fetches data from a URL, parses JSON, and optionally pops a key.

    Args:
      endpoint_url: The URL to fetch data from.
      pop_key: The key to pop from the JSON data (optional, defaults to None).

    Returns:
      A pandas DataFrame containing the processed data
    """
    json_result = requests.get(endpoint_url).content

    data = json.loads(json_result)

    # if pop_key is provided, pop key and normalize nested fields
    if pop_key:
        df_result = pd.json_normalize(data.pop(pop_key), sep="_")
    # if pop_key is not provided, normalize entire json
    else:
        df_result = pd.json_normalize(data)

    return df_result


def get_sports ():
    #@title Sports (Different Baseball Leagues/Levels/Competitions)
    sports_endpoint_url = 'https://statsapi.mlb.com/api/v1/sports'

    sports = process_endpoint_url(sports_endpoint_url, 'sports')

    print(sports)


def get_players(season, sport):
    """
    Obtiene todos los jugadores de una temporada específica para un deporte determinado.

    Args:
        season (int): Temporada para la cual obtener los jugadores.
        sport (int): ID del deporte (1 para MLB, etc.).

    Returns:
        list: Lista de jugadores.
    """

    # Construir la URL correcta usando el ID del deporte
    single_season_players_url = f'https://statsapi.mlb.com/api/v1/sports/{sport}/players?season={season}'

    players = process_endpoint_url(single_season_players_url, 'people')

    # Filtrar las columnas 'id' y 'fullName'
    players_filtered = players[['id', 'fullName']]

    return players_filtered


#print ( get_players(2024, 1) )