from flask import Flask, render_template, request

app = Flask(__name__)

# Sample content data and user preferences
content_data = {
    1: "Article 1",
    2: "Article 2",
    3: "Article 3",
    4: "Article 4",
    5: "Article 5",
}

user_preferences = {
    "user1": [1, 2],
    "user2": [3, 4],
    "user3": [2, 5],
}

@app.route('/')
def home():
    return 'Welcome to the Content Recommendation System!'

@app.route('/recommend', methods=['POST', 'GET'])
def recommend():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        if user_id in user_preferences:
            user_likes = user_preferences[user_id]
            recommended_content = [content_data[content_id] for content_id in user_likes]
            return render_template('recommendations.html', user_id=user_id, recommended_content=recommended_content)
        else:
            return "User not found. Please enter a valid user ID."

    return render_template('recommendations.html', user_id="", recommended_content=[])

if __name__=="__main__":
    app.run(host="0.0.0.0")
