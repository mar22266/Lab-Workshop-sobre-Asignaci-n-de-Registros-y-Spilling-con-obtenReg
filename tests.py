from alloc_simple import RegisterAllocator

A = RegisterAllocator()
print(A.get_register("a"))  # R1
print(A.get_register("b"))  # R2
print(A.get_register("c"))  # R3
print(A.get_register("d"))  # fuerza spill
print(A)
