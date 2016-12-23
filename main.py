#------------------------
# Tutorial used:
#  - https://dev.groupme.com/tutorials/bots
#------------------------
import requests

# Test BotId (PokeBot)
test_bot_id = "e79eeed41464b0420d236832b5"
# Live BotId (Drummin)
bot_id = "8a55325d0dae7012663507383c"
# POST url
groupme_url = "https://api.groupme.com/v3/bots/post"

def send_poke_alert(nearby_pokemon):
    # Create message to send
    for pokemon in nearby_pokemon:
        message = "{poke} found!\nExpires in {exp}\n{link}"
        message = message.format(poke=pokemon.name,
                                 exp=pokemon.get_time_remaining(do_format=True),
                                 link=fastpokemap_url.format(lat=pokemon.location.lat, lon=pokemon.location.lon))
        # Send the Groupme message
        data = {"bot_id": bot_id, "text": message}
        r = requests.post(groupme_url, data=data)

if __name__ == "__main__":
    message = "Brobot in da hizhouuuuussseeeee"
    data = {"bot_id": test_bot_id, "text": message}
    r = requests.post(groupme_url, data=data)
