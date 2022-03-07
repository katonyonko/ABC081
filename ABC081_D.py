from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="081"
#問題
problem="d"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/arc086_b".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''
'''
y = '''
'''
additional_case = []
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  N=int(input())
  A=list(map(int,input().split()))
  idx=0
  for i in range(N):
    if abs(A[i])>abs(A[idx]):
      idx=i
  print(2*N)
  if A[idx]>=0:
    print(idx+1, 1)
    print(idx+1, 1)
    for i in range(N-1):
      print(i+1,i+2)
      print(i+1,i+2)
  else:
    print(idx+1, N)
    print(idx+1, N)
    for i in reversed(range(N-1)):
      print(i+2,i+1)
      print(i+2,i+1)
  """ここから上にコードを記述"""

  print(test_case[__+1])