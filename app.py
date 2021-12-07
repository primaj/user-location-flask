from flask import Flask, render_template, request, session
app = Flask(__name__)
app.secret_key = b'_5#y2L"54df3Q8z\n\xec]/'


# render the index page with current session coords
@app.route("/")
def index():
    return render_template('index.html', lat=session['user_coords']['lat'], lng=session['user_coords']['lng'])


# gets the user location and stores in the session dictionary
@app.route('/get_user_location', methods=['POST'])
def get_user_location():
    data = request.get_json()
    session['user_coords'] = data
    return data


if __name__ == "__main__":
    app.run()
