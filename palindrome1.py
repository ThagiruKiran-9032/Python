arr = [26,74,32,28,15,99]
n= int(input())
res =0
if n<=6:
    for i in range(n):
      for j in arr:
          res = res+ j
          j+=1
          print(res)
          break
      break
else:
    print("nv")