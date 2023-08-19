def filter(predicate, iterable):
  new_list = []
  for x in iterable :
    print(predicate(x))
    if predicate(x):
      new_list.append(x)
  return new_list
