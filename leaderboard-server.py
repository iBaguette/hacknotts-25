import flask, waitress, json

app = flask.Flask(__name__)

try:
    with open("leaderboard.json", "r") as f:
        leaderboard_data = json.load(f)
except FileNotFoundError:
    leaderboard_data = []

@app.route("/leaderboard", methods=["GET"])
def get_leaderboard():
    return flask.jsonify(leaderboard_data)

@app.route("/leaderboard", methods=["POST"])
def update_leaderboard():
    new_entry = flask.request.json
    leaderboard_data.append(new_entry)
    with open("leaderboard.json", "w") as f:
        json.dump(leaderboard_data, f)
    return flask.jsonify(new_entry), 201

if __name__ == "__main__":
    waitress.serve(app, host="0.0.0.0", port=25252)
