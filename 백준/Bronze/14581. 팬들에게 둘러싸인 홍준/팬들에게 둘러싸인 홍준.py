one_layer = ""
main_layer = ""
A = input()
for i in range(3):
    one_layer += ":fan:"
    if i == 1:
        main_layer += f":{A}:"
    else:
        main_layer += ":fan:"
print(one_layer)
print(main_layer)
print(one_layer)