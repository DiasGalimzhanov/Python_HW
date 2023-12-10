# 1 задание не понятное. Последнее задание такое же как второе


def dictionary():
    dic = {"car":"машина","ice":"лед","fire":"огонь"}
    while True:
        print("1 from add in dictionary")
        print("2 from delete in dictionary")
        print("3 from search in dictionary")
        print("4 from replace in dictionary")
        print("5 from exit")
        
        inp = int(input("Enter: "))
        if inp == 1:
            print("Enter wort (en-ru) for add")
            word = input()
            word = word.split("-")
            print(word)
            dic[word[0]]=word[1]
            print(dic)
            continue
        elif inp == 2:
            print("Enter word (en) for delete")
            word = input()
            del dic[word]
            print(dic)
            continue
        elif inp == 3:
            print("Enter word (en) for search")
            word = input()
            print(dic.get(word))
        elif inp == 4:
            print("Enter word (en-(new)en-ru) for replace")
            word = input()
            word = word.split("-")
            dic[word[1]]= dic[word[0]]
            del dic[word[0]]
            dic[word[1]]=word[2]
            print(dic)
        elif inp == 5:
            break
#dictionary()

def set_gen(nums):
    res = set()

    for num in nums:
        count = nums.count(num)

        if count == 1:
            res.add(num)
        else:
            repeated_str = str(num) * count
            res.add(num)
            res.add(repeated_str)

    return res

nums = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 6, 6]
print(set_gen(nums))

def biggest_dict(**kwargs):
    my_dict = {'first_one': 'we can do it'}

    res = {**kwargs,**my_dict}
    print(res)

print(biggest_dict(dsd="udsh",last=5,seven=6,dog="pes"))

def last():
    my_dict = {'first': 1, 'second': 2, 'third': 3, 'fourth': 4, 'fifth': 5}

    first_key, last_key = next(iter(my_dict)), next(reversed(my_dict))
    my_dict[first_key], my_dict[last_key] = my_dict[last_key], my_dict[first_key]

    second_key = list(my_dict.keys())[1]
    del my_dict[second_key]

    my_dict['new_key'] = 'new_value'

    print(my_dict)