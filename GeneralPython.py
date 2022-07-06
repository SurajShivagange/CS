def histrogramCharacters():
    #open file in read mode
    file = open("E:\Documents\ME\Course\Sem 2\Cloud Security\Submissions\Lab Submission 2\Read File.txt", "r")

    #read the content of file
    data = file.read()

    data=data.lower()
    Dict=dict()
    for word in data:
        if word not in Dict:
            Dict[word]=1
        else:
            Dict[word]=Dict[word]+1
    print(Dict)
    for key, val in Dict.items():
        print(key, '\t', '*' *val)

def sortedHistogram():
     #open file in read mode
    file = open("E:\Documents\ME\Course\Sem 2\Cloud Security\Submissions\Lab Submission 2\Read File.txt", "r")

    #read the content of file
    data = file.read()
    #Converting the string to lowercase to avoid any ruleovers
    data=data.lower()
    Dict=dict()
    for word in data:
        if word not in Dict:
            Dict[word]=1
        else:
            Dict[word]=Dict[word]+1
    #print(Dict)

    sorted_values = sorted(Dict.values()) # Sort the values
    sorted_dict = {}

    for i in sorted_values:
        for k in Dict.keys():
            if Dict[k] == i:
                sorted_dict[k] = Dict[k]
                break

    #print(sorted_dict)

    outL = dict(list(sorted_dict.items())[0: 5]) 
    print("\n\nThe lowest frequency characters are:" + str(outL))

        
    outH = dict(list(sorted_dict.items())[-5: ])  
    print ("The highest frequency characters are:" + str(outH))  




def isPrime(number):
    num = number

    # define a flag variable
    flag = False

    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break

    # check if flag is True
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")    
