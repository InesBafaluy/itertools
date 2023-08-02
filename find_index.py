def find_index(predicate, iterable):
  for i in range(len(iterable)) :
    if predicate(iterable[i]):
      return i
  return (-1)
