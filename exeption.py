def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count +=1
    except:
        pass
    print("")
    return count
print(safe_print_list)