import sys

n = int(input())
postFix = list(input()) #후위표기식
operator = [] #연산자
operand = {} #피연산자

def Calculate(x, y, z):
  if(z=='+'):
    return x+y
  if(z=='-'):
    return x-y
  if(z=='*'):
    return x*y
  if(z=='/'):
    return x/y
  
for i in range(len(postFix)):
  x = postFix[i]
  if(x=='*' or x=='-' or x=='+' or x=='/'):
    operator.append(x) #연산자는 연산자 리스트(operator)에 추가
  else:
    if(x not in operand.keys()):
      #*피연산자는 'AA+AB+' 와 같이 동일한 값(A)이 중복해서 나올 수 있으므로
      #*이미 넣은 값은 제외하고 dict에 추가함 예){'A': 1, 'B': 2}
      operand[x] = int(input())

for i in range(len(postFix)):
  x = postFix[i]
  if(ord(x) >= 65 and ord(x) <= 90): #A,B,C..인 피연산자를 operand 딕셔너리에 담아놓은 value로 바꿔줌
    postFix[i] = operand[x]
#*postFix=[1,1,'+',1,2,'+']

stack = [] #딤이넣을 스택
for i in postFix:
  if(i not in operator):  #피연산자라면(1,2,3 등) 스택에 넣어주기
    stack.append(i)
  
  else:   #연산자라면 (+, -, *, /)
    x = stack.pop()
    y = stack.pop() #스택의 마지막 두개 항목을 뽑아서 계산후 스택에 넣어주기
    stack.append(Calculate(y, x, i))

print('%0.2f' % stack[0])

# 후위표기식을 입력하고
# 피연산자의 개수만큼 수를 입력받는다
# 피연산자는 A,B,C로 주어진다
# 문제를 제대로 읽자...