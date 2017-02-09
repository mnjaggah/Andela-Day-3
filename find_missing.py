def find_missing(a, b):
  lst1 = a + b
  lst2 = []
  
  if len(lst1) == 0 or a == b:
    return 0
  else:
    for x in lst1: #iterate through the new loop
      if lst1.count(x) == 1:
        lst2.append(x)
    return lst2
print (find_missing([1,3,4],[1,3]))