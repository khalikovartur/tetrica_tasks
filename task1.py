def task(array):   
    list_nums = [int(i) for i in array]
    return f"OUT: {list_nums.index(0)}"
    
print(task("111111111110000000000000000"))


