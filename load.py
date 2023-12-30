from pyrogram import Client, filters
from bs4 import BeautifulSoup
import requests

api_id = '16723398'
api_hash = '9e07dd89d2f39bfadfd59798705e4662'
bot_token = '6785681031:AAHjd_DZWFnwIjSEtT2kTNESikaycsk37Ks'

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("correct"))
def get_correct_predictions(_, message):
    url = "https://footballpredictions.net/correct-score-predictions-betting-tips"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    predictions = []

    match_elements = soup.select('.match-card')

    for index, match_element in enumerate(match_elements, start=1):
        teams_element = match_element.select('.team-label')
        prediction_text = match_element.select_one('.prediction').get_text(strip=True)

        teams_text = ' / '.join(team.get_text(strip=True) for team in teams_element)

        if teams_text and prediction_text:
            prediction_with_teams = f"{index}) {teams_text} - Dəqiq hesab {prediction_text}"
            predictions.append(prediction_with_teams)

    if predictions:
        message.reply_text('\n'.join(predictions))
    else:
        message.reply_text('Xəta.')

app.run()
