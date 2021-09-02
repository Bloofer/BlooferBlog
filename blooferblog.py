from flask import Flask, render_template
import reviewparser
app = Flask(__name__)

@app.route("/")
def home():
    rString = reviewparser.getReview(1)
    rTitle = reviewparser.getReviewTitle(rString)
    aTitle = reviewparser.getArticleTitle(rString, 1)
    rContent = reviewparser.getReviewContent(rString)
    return render_template('index.html', atitle=aTitle, title=rTitle, content=rContent)

if __name__ == '__main__':
    app.run()
