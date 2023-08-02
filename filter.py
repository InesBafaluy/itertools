def filter(predicate, iterable):
  for x in iterable :
    if not predicate(x):
      iterable.remove(x)
  return iterable
