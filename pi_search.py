# coding:utf-8
# 正規表現を用いたプログラム

import re

# from http://codepad.org/N9hPp78j
def pi(n=10000):
  a,b,i = 10**n, 10**n, n*8+1
  while i>=3: a,i = (a+b+b)*(i/2)/i, i-2
  return a-b

def match(text):
  pattern = pi()
  match_text = text

  # print pattern
  # print match_text

  matchOB = re.search(str(match_text),str(pattern))

  if matchOB:
    print (str(matchOB.group()) + "は小数点第" + str(matchOB.start()+1) + "位から第" + str(matchOB.end()) + "位に最初に出現します")
  else:
    print(str(text) + 'は円周率10000桁の中に存在しません')


# p = re.compile('[0-9]')
#print p

# m = re.findall('[0-9]',"9098")
# m = p.match("9098")
# print m
# print m.end()
# print m.start()
# print m.span()

# m = p.search("76238947569098")
# print m.group()
# print m.end()
# print m.start()
# print m.span()
