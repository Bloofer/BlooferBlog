from flask import Flask, render_template
import reviewparser
import os
app = Flask(__name__)

@app.route("/")
def home():
    path, dirs, files = next(os.walk("/home/ubuntu/BlooferBlog/static/reviews"))
    file_count = len(files)

    rStringList = []
    rTitleList = []
    aTitleList = []
    rContentList = []
    for i in range(1, file_count+1):
        rStringList.append(reviewparser.getReview(i))
        rTitleList.append(reviewparser.getReviewTitle(rStringList[i-1]))
        aTitleList.append(reviewparser.getArticleTitle(rStringList[i-1], i))
        rContentList.append(reviewparser.getReviewContent(rStringList[i-1]))


    rTitle = reviewparser.getReviewTitle(rStringList[0])
    aTitle = reviewparser.getArticleTitle(rStringList[0], 1)
    rContent = reviewparser.getReviewContent(rStringList[0])


    return render_template('index.html', atitleList=aTitleList, titleList=rTitleList, contentsList=rContentList, iter=file_count)

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()
