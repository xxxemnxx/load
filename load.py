from pyrogram import Client, filters
from bs4 import BeautifulSoup
import requests


API_ID = "16723398"
API_HASH = "9e07dd89d2f39bfadfd59798705e4662"
BOT_TOKEN = "6815920860:AAF6M1HA3ubMB1kTMjUjTlbzE-UNX5zVQ0E"

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
def start(_, message):
    message.reply_text('Salam, günlük mərc təxminləri botuna xoş gəlmisiniz ! Istifadə üçün əmrləri bilirsinizsə yazaraq davam edin əgər bilmirsinizsə adminlə əlaqə saxlayın. Unutmayın mərcdə 100/100 deyə birşey yoxdur. Bu bot sizin üçün ideal seçimləri analiz edərək istifadəniz üçün verir. Tovsiyyəmiz odur ki, ortalaması 3-0/3-1 olan oyunlara 1.5 ataraq 3-4əmsal yığasınız. Və etdiyiniz mərclərdən, uduzduğunuz oyunlardan biz məsuliyyət daşımırıq.')


@app.on_message(filters.command("hacidayi1213"))
def help_command(client, message):
    help_text = (
       "Salam! Premium üçün olan əmrlərə xoş gəlmisiniz 🫴\n"
       "/send25 - 2.5 alt/üst təxminləri 🗺️\n"
       "/sendqq - Qolqol təxminləri 🗺️\n"
       "/sendscore - Dəqiq hesab 🗺️\n"
       "/12 - Kim qazanacaq 🗺️"
                )
    message.reply_text(help_text)
            
            
    



@app.on_message(filters.command("send25"))
def get_predictions(_, message):
    url = "https://footballpredictions.net/under-over-2-5-goals-betting-tips-predictions"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    predictions = []

    
    match_elements = soup.select('.match-card')
    
    for index, match_element in enumerate(match_elements, start=1):
        teams_element = match_element.select('.team-label')
        prediction_text = match_element.select_one('.prediction').get_text(strip=True)

        teams_text = ' / '.join(team.get_text(strip=True) for team in teams_element)

        if teams_text and prediction_text:
            prediction_with_teams = f"{index}) {teams_text} netice‘‘ {prediction_text}"
            predictions.append(prediction_with_teams)

    
    if predictions:
        message.reply_text('\n'.join(predictions))
    else:
        message.reply_text('Xeta.')
        
@app.on_message(filters.command("12"))
def get_predictions(_, message):
    url = "https://footballpredictions.net/win-draw-win-predictions-full-time-result-betting-tips"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    predictions = []

    
    match_elements = soup.select('.match-card')
    
    for index, match_element in enumerate(match_elements, start=1):
        teams_element = match_element.select('.team-label')
        prediction_text = match_element.select_one('.prediction').get_text(strip=True)

        teams_text = ' / '.join(team.get_text(strip=True) for team in teams_element)

        if teams_text and prediction_text:
            prediction_with_teams = f"{index}) {teams_text} netice˜ {prediction_text}"
            predictions.append(prediction_with_teams)

    
    if predictions:
        message.reply_text('\n'.join(predictions))
    else:
        message.reply_text('xeta.')
        
        
@app.on_message(filters.command("sendqq"))
def get_predictions(_, message):
    url = "https://footballpredictions.net/btts-tips-both-teams-to-score-predictions"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    predictions = []

    
    match_elements = soup.select('.match-card')
    
    for index, match_element in enumerate(match_elements, start=1):
        teams_element = match_element.select('.team-label')
        prediction_text = match_element.select_one('.prediction').get_text(strip=True)

        teams_text = ' / '.join(team.get_text(strip=True) for team in teams_element)

        if teams_text and prediction_text:
            prediction_with_teams = f"{index}) {teams_text} netice˜ {prediction_text}"
            predictions.append(prediction_with_teams)

    
    if predictions:
        message.reply_text('\n'.join(predictions))
    else:
        message.reply_text('xeta.')        
        
@app.on_message(filters.command("sendscore"))
def get_predictions(_, message):
    try:
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
                prediction_with_teams = f"{index}) {teams_text} ðŸ‘‘ {prediction_text}"
                predictions.append(prediction_with_teams)

        
        if predictions:
            message.reply_text('\n'.join(predictions))
        else:
            message.reply_text('XÉ™ta.')
      
    except Exception as e:
        print(f"xeta: {e}")

app.run()
