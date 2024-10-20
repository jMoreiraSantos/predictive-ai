import requests
import utils


import requests
import json

secrets = utils.load_secrets('secrets.json')

class Data_Extraction:
    
    def fetch_soccer_odds(api_key):
        url = "https://api.oddsapi.io/v1/odds"
        """
        key: soccer_portugal_primeira_liga
        
        """
        headers = {
            "Authorization": api_key
        }

        # Example parameters: adjust as needed
        params = {
            "sport": "soccer",
            "region": "Europe",  # Specify region if needed
            "mkt": "h2h"  # Market type (e.g., head-to-head)
        }

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()  # Raise an error for bad responses

            odds_data = response.json()
            return odds_data

        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
        except Exception as err:
            print(f"An error occurred: {err}")


    def save_odds_to_file(odds_data, file_path):
        try:
            with open(file_path, 'w') as file:
                json.dump(odds_data, file, indent=4)
            print(f"Odds data saved to {file_path}")
        except Exception as err:
            print(f"An error occurred while saving to file: {err}")


    def load_odds(self):
        secrets = self.load_secrets('secrets.json')
        if secrets:
            api_key = secrets.get("ODDS_API")
            odds = self.fetch_soccer_odds(api_key)
            if odds:
                self.save_odds_to_file(odds, 'soccer_odds.json')