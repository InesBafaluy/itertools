def map(predicate, iterable):  
  new_list = []
  for x in iterable :
    new_list.append(predicate(x))
  return new_list
