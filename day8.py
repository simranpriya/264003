def my_function():
  print("Hello from a function")

my_function()

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")


def my_function(country = "Norway"):
  print("I am from " + country)


my_function("India")
my_function()
my_function("Brazil")


def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)