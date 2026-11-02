
k,n,w = map(int, input().split())

final_price = k * (w*(w+1)//2)
print(final_price - n if final_price>n else 0)
