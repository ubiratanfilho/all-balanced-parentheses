def balanced_parens(n):
  
  if n == 0:
    return ['']

  ans = []
  for c in range(2**(2*n)):
    s = "%0" + str(2*n) + "i"
    s = str(s %int(bin(c)[2::])).replace('1', "(").replace('0', ")")

    if s.count("(") == s.count(")"):
          soma = 0 
          for a in s:
            if a == "(":
              soma += 1
            else:
              soma -= 1
            if soma < 0 or soma > n:
              break
          if soma == 0:
            ans.append(s)

  return ans

balanced_parens(8)
