#'map' 함수
# map(fun, args,...)

f = lambda x, y : x*y
args1 = [1,2,3,4,5,6,7]
args2 = [5,2,4,56,1,2,3]

ret = map(f, args1, args2)

print(list(ret))
