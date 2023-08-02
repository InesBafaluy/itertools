def find(predicate, iterable):
  for x in iterable :
    if predicate(x):
      return x
  return None
