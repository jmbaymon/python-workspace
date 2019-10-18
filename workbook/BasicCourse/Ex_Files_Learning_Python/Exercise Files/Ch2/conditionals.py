#
# Example file for working with conditional statements
#

def main():
  x, y = 200, 200
  
  # conditional flow uses if, elif, else  
  if (x < y):
        st ="x is less than y"
  elif(x == y):
        st = "x is equal to y"
  else:
        st = "x is greater than y"
  print(st)
  # conditional statements let you use "a if C else b"
  st = "x < y " if(x<y) else "x is greater than or the same as y"
  

if __name__ == "__main__":
  main()
