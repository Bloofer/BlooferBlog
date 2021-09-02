import os
import blooferblog


num2kor = {1:'하나', 2:'둘', 3:'셋', 4:'넷', 5:'다섯', 6:'여섯', 7:'일곱', 8:'여덟', 9:'아홉',
           10:'열', 20:'스물', 30:'서른', 40:'마흔', 50:'쉰', 60:'예순', 70:'일흔', 80:'여든', 90:'아흔',
           100:'백'}


def getReview(rNum):
    rFile = blooferblog.app.open_resource('static/reviews/review'+str(rNum)+'.txt')
    rString = rFile.read().decode('utf-8')

    return rString


def getReviewContent(rString):
    lines = rString.splitlines()
    cnt = 0
    rContent = ''
    for line in lines:
        if cnt > 0:
            rContent += line + '\r\n'
        cnt += 1

    return rContent


def getReviewTitle(rString):
    rTitle = rString.splitlines()

    return rTitle[0]


def getNumToKorean(num):
    if num < 10:
        return num2kor[num]
    elif num < 100:
        return num2kor[num/10]+num2kor[num%10]
    else:
        return num2kor[num/100]+num2kor[(num%100)/10]+num2kor[num%10]


def getArticleTitle(rString, rNum):
    rTitle = rString.splitlines()
    rNumKor = '하나'
    bName = rTitle[0].split('-')

    return '책 리뷰 '+getNumToKorean(rNum)+'. '+bName[0]

def getReviewCount():
    return 0
