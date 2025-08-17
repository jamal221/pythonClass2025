#KMM
def KMM(a, b):
  if a > b:
    k = a
  else:
    k = b

  while(True):
    if((k % a == 0) and (k % b == 0)):
      n = k
      break
    k += 1

  return n
