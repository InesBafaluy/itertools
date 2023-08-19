def reduce(predicate, iterable, initial=None):
  acc = iterable[0] if initial == None else initial 
  for x in iterable[1:] if initial == None else iterable :  
    acc = predicate(acc,x)
  return acc
