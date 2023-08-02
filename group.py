def group(predicate, iterable):
  dic = {'even':[],'odd':[]}
  for x in iterable :
    dic[predicate(x)].append(x)
  return dic
