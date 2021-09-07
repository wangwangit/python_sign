import json
import requests

corpid = 'xxx'  # 上面提到的你的企业ID
corpsecret = 'xxxx'  # 上图的Secret
agentid = xxxx  # 填写你的企业ID，不加引号，是个整型常数,就是上图的AgentId


# 企业微信推送
def wxPush(message, url):
    token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?' + 'corpid=' + corpid + '&corpsecret=' + corpsecret
    req_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token='
    resp = requests.get(token_url).json()
    access_token = resp['access_token']
    data = {
        "touser": "@all",
        "toparty": "@all",
        "totag": "@all",
        "toall": 0,
        "msgtype": "textcard",
        "agentid": agentid,
        "textcard": {
            "title": "每日一题",
            "description": message,
            "url": url,
            "btntxt": "更多"
        }
    }
    data = json.dumps(data)
    req_urls = req_url + access_token
    res = requests.post(url=req_urls, data=data)
    print(res.text)


# 获取leetcode题目
def get_leetcode():
    base_url = 'https://leetcode-cn.com'
    # 获取今日每日一题的题名(英文)
    response = requests.post(base_url + "/graphql", json={
        "operationName": "questionOfToday",
        "variables": {},
        "query": "query questionOfToday { todayRecord {   question {     questionFrontendId     questionTitleSlug     "
                 "__typename   }   lastSubmission {     id     __typename   }   date   userStatus   __typename }} "
    })
    leetcodeTitle = json.loads(response.text).get('data').get('todayRecord')[0].get("question").get('questionTitleSlug')

    # 获取今日每日一题的所有信息
    url = base_url + "/problems/" + leetcodeTitle
    response = requests.post(base_url + "/graphql",
                             json={"operationName": "questionData", "variables": {"titleSlug": leetcodeTitle},
                                   "query": "query questionData($titleSlug: String!) {  question(titleSlug: $titleSlug) { "
                                            "   questionId    questionFrontendId    boundTopicId    title    titleSlug    "
                                            "content    translatedTitle    translatedContent    isPaidOnly    difficulty  "
                                            "  likes    dislikes    isLiked    similarQuestions    contributors {      "
                                            "username      profileUrl      avatarUrl      __typename    }    "
                                            "langToValidPlayground    topicTags {      name      slug      translatedName "
                                            "     __typename    }    companyTagStats    codeSnippets {      lang      "
                                            "langSlug      code      __typename    }    stats    hints    solution {      "
                                            "id      canSeeDetail      __typename    }    status    sampleTestCase    "
                                            "metaData    judgerAvailable    judgeType    mysqlSchemas    enableRunCode    "
                                            "envInfo    book {      id      bookName      pressName      source      "
                                            "shortDescription      fullDescription      bookImgUrl      pressImgUrl      "
                                            "productUrl      __typename    }    isSubscribed    isDailyQuestion    "
                                            "dailyRecordStatus    editorType    ugcQuestionId    style    __typename  }}"})
    # 转化成json格式
    jsonText = json.loads(response.text).get('data').get("question")
    # 题目题号
    no = jsonText.get('questionFrontendId')
    # 题名（中文）
    leetcodeTitle = jsonText.get('translatedTitle')
    htmlText = "<div>" + no + '.' + leetcodeTitle + "</div>"
    print(htmlText)
    wxPush(htmlText, url)


if __name__ == '__main__':
    get_leetcode()
