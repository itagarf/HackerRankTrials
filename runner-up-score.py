#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
#You are given  scores. Store them in a list and find the score of the runner-up.
#Input Format:
#The first line contains n. 
#The second line contains an array of integers each separated by a space.

n = int(input())
arr = map(int, input().split())
arr1 = list(arr)
arr2 = max(arr1)
while arr2 == max(arr1):
  arr1.remove(max(arr1))
    
print(max(arr1))