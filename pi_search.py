# coding:utf-8

from bottle import route, request, template, run, re

# localhost:8080にアクセスしたときに最初に開くページ
@route('/')
def index():
  return template('index.tpl')

@route('/first_result/', method="POST")
def index():
  # 入力された数字がどこに出現するか
  search_result = str(match(request.POST.get("first_number")))

  # スコアの計算
  score_result = str(get_score(request.POST.get("first_number")))

  # .tplの読み込み
  return template('first_result.tpl', search_result = search_result, score_result = score_result)

@route('/second_result/', method="POST")
def index():
  # 入力された数字がどこに出現するか
  search_result = str(match(request.POST.get("second_number")))

  # スコアの計算
  score_result = get_score(request.POST.get("second_number"))
  score_result = int(score_result) + int(request.POST.get("total_score"))

  # .tplの読み込み
  return template('second_result.tpl', search_result = search_result, score_result = score_result)

@route('/final_result/', method="POST")
def index():
  # 入力された数字がどこに出現するか
  search_result = str(match(request.POST.get("third_number")))

  # スコアの計算
  score_result = get_score(request.POST.get("third_number"))
  score_result = int(score_result) + int(request.POST.get("total_score"))

  # .tplの読み込み
  return template('final_result.tpl', search_result = search_result, score_result = score_result)

# from http://codepad.org/N9hPp78j
# 円周率を一万桁まで返す関数
def pi(n=10000):
  a,b,i = 10**n, 10**n, n*8+1
  while i>=3: a,i = (a+b+b)*(i/2)/i, i-2
  return a-b

# 任意の検索結果を返す関数
def match(number = 10):
  pattern = str(pi())
  match_number = number

  matchOB = re.search(str(match_number),str(pattern))

  if matchOB:
    return_text = (str(matchOB.group()) + "は小数点第" + str(matchOB.start()+1) + "位から第" + str(matchOB.end()) + "位に最初に出現します")
    return return_text
  else:
    return_text = (str(match_number) + 'は円周率10000桁の中に存在しません')
    return return_text

# スコアを返す関数
def get_score(number = 10):
  pattern = str(pi())
  match_number = number

  matchOB = re.search(str(match_number),str(pattern))

  if matchOB:
    return_score = matchOB.end()
    return return_score
  else:
    return_score = 0
    return return_score


run(host = 'localhost', port = 8080, debug = True, reloader = True)