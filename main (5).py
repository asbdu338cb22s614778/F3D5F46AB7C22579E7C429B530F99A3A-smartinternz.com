def linearsearchproduct(productlist, targetproduct):
  indices=[]
  for index, product in enumerate(productlist):
     if product==targetproduct:
       indices. append(index)
  return indices
product= ["bangles","chains","earings","ring","bangles"]
target="bangles"
target2="saree"
result=linearsearchproduct(product,  target)
print(result)
      