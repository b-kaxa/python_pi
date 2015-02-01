# coding:utf-8

from bottle import route, request, template, run
import re

# localhost:8080にアクセスしたときに最初に開くページ
@route('/')
def index():
  return template('index.tpl')

@route('/first_result/', method="POST")
def index():
  search_result = str(match(request.POST.get("first_number")))
  return template('first_result.tpl', search_result = search_result)

@route('/second_result/', method="POST")
def index():
  search_result = str(match(request.POST.get("second_number")))
  return template('first_result.tpl', search_result = search_result)

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


run(host = 'localhost', port = 8080, debug = True, reloader = True)