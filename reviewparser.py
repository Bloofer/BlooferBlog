import os
import blooferblog


num2kor = {0:'', 1:'하나', 2:'둘', 3:'셋', 4:'넷', 5:'다섯', 6:'여섯', 7:'일곱', 8:'여덟', 9:'아홉',
           10:'열', 20:'스물', 30:'서른', 40:'마흔', 50:'쉰', 60:'예순', 70:'일흔', 80:'여든', 90:'아흔',
           100:'백'}


def getReview(rNum):
    rFile = blooferblog.app.open_resource('static/reviews/review'+str(rNum)+'.txt')
    rString = rFile.read().decode('utf-8')

    return rString


def getReviewContent(rString):
    lines = rString.splitlines()
    cnt = 0
    rContent = []
    for line in lines:
        if cnt > 0:
            rContent.append(line)
        cnt += 1

    return rContent


def getReviewTitle(rString):
    rTitle = rString.splitlines()

    return rTitle[0]


def getNumToKorean(num):
    if num < 10:
        return num2kor[num]
    elif num >= 10 and num < 100:
        q, r = divmod(num, 10)
        return num2kor[q*10] + num2kor[r]
    else:
        return str(num2kor[num/100])+str(num2kor[(num%100)/10])+str(num2kor[num%10])


def getArticleTitle(rString, rNum):
    rTitle = rString.splitlines()
    bName = rTitle[0].split('-')

    return '책 리뷰 '+getNumToKorean(rNum)+'. '+bName[0]

class Review:

    def __init__(self):
        self.rNum = 0           # 리뷰 번호 (e.g. 책 리뷰 하나.)
        self.rating = 0         # 리뷰 별점 (별점 5개 기준 1~10)
        self.reviewTitle = ''   # 리뷰 제목 (e.g. 직업으로서의 소설가 - 무라카미 하루키 ★★★★)
        self.reviewContent = '' # 리뷰 내용
        self.articleTitle = ''  # 글 타이틀 (e.g. 책 리뷰 마흔다섯. 직업으로서의 소설가)

        
