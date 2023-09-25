from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return render_template('home.html')


@app.route('/sent', methods=['POST'])
def Sentiment():
    if request.method == 'POST':
        text = request.form.to_dict()
        text = str(list(text.values()))
        sent_score = TextBlob(text).sentiment.polarity
        if sent_score > 0:
            predict = 'Positive'
        elif sent_score == 0:
            predict = "Neutral"
        else:
            predict = "Negative"
        return render_template('predict.html', predict=predict)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
