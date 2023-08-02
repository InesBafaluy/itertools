def group(predicate, iterable):
  dic={}
  for x in iterable :
    if predicate(x) not in dic.keys():
      dic[predicate(x)] = []
    dic[predicate(x)].append(x)
  return dic
