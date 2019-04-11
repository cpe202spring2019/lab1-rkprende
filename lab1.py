
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if int_list == []:
      return None
   max = int_list[0]
   for i in range(1, len(int_list)):
      if int_list[i] > max:
         max = int_list[i]
   return max


def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list ==[]:
      return None
   if len(int_list)== 1:
      return int_list
   else:
      temp = reverse_rec(int_list[1:])
      return temp + temp.append(int_list[0])


def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   mid = (high + low)//2   #index of midpoint
   if int_list ==[]:       #if list is empty
      return None
   if low > high :         #if target not in list
      return None
   if target == int_list[mid]:   #if target found
      return mid
   if target > int_list[mid]:    #if target is larger than midpoint value
      return bin_search(target, mid+1, high, int_list)
   else:                         #if target is less than midpoint value
      return bin_search(target, low, mid-1, int_list)
