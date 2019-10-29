
##Problem 1
#import random
#def rng():
#    return([random.randint(1,20) for i in range(10)])
#    
#def find_second(nums):
#    set_nums = set(nums)
#    temp = sorted(set_nums)
#    second_highest = temp[-2]
#    second_highest_index = nums.index(second_highest)
#    
#    return(second_highest, second_highest_index)
#
#if __name__ == "__main__":
#    nums = rng()
#    second_high, index = find_second(nums)
#    print("List of Integers: ", nums)
#    print("Second largest: ", second_high)
#    print("Its Index: ",index)
#    
    


##Problem 2
#def isAnagram(s1, s2):
#    return(sorted(s1) == sorted(s2))
#    
#if __name__ == "__main__":
#    s1 = input("Enter Word 1")
#    s2 = input("Enter Word 2")
#    
#    
#    if isAnagram(s1,s2):
#        print("The Words ", s1, " and ", s2, "are Anagrams")
#    else:
#        print("The Words ", s1, " and ", s2, "are not Anagrams")
        


##Program 3
#import sys
#def read_data():
#    try:
#        file = open("timings.txt")
#        dictionary = {}
#        for line in file:
#            line = line.replace("\n", "")
#            info = line.split(",")
#            name = info[0]
#            timings = info[1:]
#            dictionary[name] = timings
#            
#        return dictionary
#    
#    except:
#        e = sys.exc_info()
#        print(e)
#
#def get_avg(times):
#    sum_ = 0
#    for time in times:
#        minute = time.split(":")[0]
#        seconds = time.split(":")[1]
#        
#       
#        total_seconds = int(minute)*60 + int(seconds)
#        sum_ += total_seconds
#        
#    avg = sum_/len(times)
#    minute = int(avg/60)
#    seconds = int(avg%60)
#    
#    if int(seconds/10) == 0:
#        return(str(minute) + ":0" + str(seconds))
#        
#    return (str(minute) + ":" + str(seconds))
#        
#    
#
#if __name__ == "__main__":
#    dictionary = read_data()
#    data = []
#    if dictionary:
#        for key in dictionary.keys():
#            name = key
#            min_ = min(dictionary[key])
#            max_ = max(dictionary[key])
#            average = get_avg(dictionary[key])
#            data.append([name, min_, max_, average])
#            
#        print(["Athlete", "Min", "Max", "Average"])
#        for item in data:
#            print(item)
    
#Problem 4
#bloodtypes = "AB AB B O A A AB O AB A O O A A A O O O AB O A A A A A AB AB A AB O AB O A O O O AB O AB AB AB A A O"
#filename = "bloodtype.txt"
#with open(filename, 'a+') as file:
#    file.write(bloodtypes)
#file.close()

#Problem 5
#import sys
#
#def bldcount(filename):
#    try:
#        file = open(filename, "r")
#        all_data = file.readlines()    
#    except:
#        e = sys.exc_info()
#        print(e)
#    
#    count = {}
#    for data in all_data:
#        data = data.replace("\n", "")
#        temp = data.split(" ")
#        for bloodtype in temp:
#            if bloodtype not in count:
#                count[bloodtype] = 1
#            else:
#                count[bloodtype] += 1
#        
#    for bld in count.keys():
#        if count[bld] != 1:
#            print("There are", count[bld], "patients of blood type", bld)
#        else:
#            print("There is one patient of blood type ", bld)
#        
#
#if __name__ == "__main__":
#    filename = input("Enter Filename: ")
##    filename = "bloodtype.txt"
#    bldcount(filename)
    
    
    
    
        
        
        
    
    

