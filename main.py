from flask import Flask, render_template, jsonify
import requests
import datetime as dt

app = Flask(__name__)

MY_NAME = 'Gavin "Siris" Martin'  # defined globally for reuse in routes and/or functions

@app.route('/')
def home():
    this_year = dt.datetime.now().year
    current_year = f'Copyright {this_year} {MY_NAME}. All Rights Reserved.'
    # render the template with necessary variables
    return render_template('index.html', CURRENT_YEAR=current_year)

@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    try:
        blog_response = requests.get(blog_url)
        blog_response.raise_for_status()  # Ensures we proceed only if the response was successful
        all_posts = blog_response.json()
    except requests.RequestException as e:
        print(f"Failed to retrieve blog data: {e}")
        # if an error occurs, return a JSON response with the error and a 500 status code
        return jsonify({"error": "Unable to fetch blog posts", "details": str(e)}), 500
    # if successful, render the index.html with the posts data
    return render_template("index.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
