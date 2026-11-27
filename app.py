from flask import Flask, request, send_from_directory, Response
import json


# http://localhost:3000/etusivu/ - etusivu
# http://localhost:3000/static/style.css/ etc

app = Flask(__name__)


@app.route("/etusivu/") #etusivu
def etusivu():
    return send_from_directory("static", "menu.html")

@app.route("/etusivu/aloita") # jotenkin saadaan Aloita nappulalla peli käyntiin? -> viedään tieto JS koodille joka tekee lisää juttuja
def start_game():
    response = {"status": "online"}
    return response


@app.route("/static/<path:filename>") # voidaan kulkea static kansiota pitkin, hakea esimerkiksi Javascript tiedosto kun tämä luodaan.
def serve_static(filename):
    return send_from_directory('static', filename)

@app.route("/hello") # ihan vaan testailua varten.
def hello_world():
    return "Hello, World!"


@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint",
        "status": 404
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=404, mimetype="application/json")
    return http_response


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, use_reloader=True)