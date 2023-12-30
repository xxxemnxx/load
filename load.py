from pyrogram import Client
from bs4 import BeautifulSoup
import requests

API_ID = "16723398"
API_HASH = "9e07dd89d2f39bfadfd59798705e4662"
BOT_TOKEN = "6272490425:AAGdl_pVg3W57HzvwsNkU1OU5odyk9vRSRI"


app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

def scrape_website():
    url = "https://footballpredictions.net/correct-score-predictions-betting-tips"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        teams_elements = soup.select('.team-label')
        predictions_elements = soup.select('.prediction')

        result = []
        for teams, prediction in zip(teams_elements, predictions_elements):
            teams_text = teams.get_text(strip=True)
            prediction_text = prediction.get_text(strip=True)
            result.append(f"{teams_text} - {prediction_text}")

        return result

    else:
        return f"Error: {response.status_code}"

@app.on_message()
def handle_message(client, message):
    if message.text.lower() == "/get_predictions":
        predictions = scrape_website()
        if isinstance(predictions, list):
            formatted_predictions = "\n".join(predictions)
            message.reply_text(formatted_predictions)
        else:
            message.reply_text(predictions)

if __name__ == "__main__":
    app.run()
