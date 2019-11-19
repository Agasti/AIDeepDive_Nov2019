import helper_functions as hf

#help(hf.stringer)
#help(hf.duplicates)
#help(hf.pancaker)


print(hf.stringer(12345))
print(hf.duplicates([1,2,3], [4,5]))

choices = {'the_string' : "1234", 'the_list' : [1,2,3,4], 'the_tuple' : (1,2,3,4)}

choice = input("choose what you want to pancake: (type 'the_string', 'the_list' or 'the_tuple')")

print(hf.pancaker(choices[choice]))