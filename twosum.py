def twosum( nums, target):
  hm={}
  for i, n in enumerate(nums):
    c = target-n
    if c in hm:
      return [hm[c],i]
    hm[n] = i
  return []
