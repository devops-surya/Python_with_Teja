import library

print(library.Max)


import library_other 
print(library_other.Min)

from library_other import other
print(other)



from library_other import other as ot, Min as M
print(ot)
print(M)