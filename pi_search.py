# coding:utf-8

import os
from bottle import route, request, template, run, re, static_file, url

@route('/')
def index():
  return template('./views/index.tpl', get_url = url)

@route('/first_result/', method="POST")
def index():
  # search
  search_result = str(match(request.POST.get("first_number")))

  # calc
  score_result = str(get_score(request.POST.get("first_number")))

  # view
  return template('./views/first_result.tpl', search_result = search_result, score_result = score_result, get_url = url)

@route('/second_result/', method="POST")
def index():
  # search
  search_result = str(match(request.POST.get("second_number")))

  # calc
  score_result = get_score(request.POST.get("second_number"))
  score_result = int(score_result) + int(request.POST.get("total_score"))

  # view
  return template('./views/second_result.tpl', search_result = search_result, score_result = score_result, get_url = url)

@route('/final_result/', method="POST")
def index():
  # search
  search_result = str(match(request.POST.get("third_number")))

  # calc
  score_result = get_score(request.POST.get("third_number"))
  score_result = int(score_result) + int(request.POST.get("total_score"))

  # view
  return template('./views/final_result.tpl', search_result = search_result, score_result = score_result, get_url = url)

# define about reading static files
@route('/bower_components/:path#.+#', name='static')
def static(path):
    return static_file(path, root='bower_components')

@route('/static/:path#.+#', name='original')
def static(path):
    return static_file(path, root='static')

# from http://codepad.org/N9hPp78j
# calc pi
def pi(n=10000):
  a,b,i = 10**n, 10**n, n*8+1
  while i>=3: a,i = (a+b+b)*(i/2)/i, i-2
  return a-b

# return search result
def match(number = 10):
  pattern = str(pi())
  match_number = number

  matchOB = re.search(str(match_number),str(pattern))

  if matchOB:
    return_text = (str(matchOB.group()) + "は小数点第" + str(matchOB.start()+1) + "位から第" + str(matchOB.end()) + "位に最初に出現します！")
    return return_text
  else:
    return_text = (str(match_number) + 'は円周率10000桁の中に存在しません！残念！')
    return return_text

# return score result
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

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True, reloader=True)