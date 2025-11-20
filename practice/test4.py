l1 = "Hello333,,  %%%World! , dds".split(",")
l2 = [x.strip(" 3%!") for x in l1]
print(l1)
print(l2)

l3 = "aaa, bb, ccc, ddd".split(",", maxsplit=1)
print(l3)

