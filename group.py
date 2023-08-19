def group(predicate, iterable):
  dic={}
  for x in iterable :
    condition = predicate(x)
    if condition not in dic.keys():
      dic[condition] = []
    dic[condition].append(x)
  return dic
