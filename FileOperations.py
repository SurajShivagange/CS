#1. a. Read the content from the file, and write into another file
def readWrite():
    # Creating an output file in writing mode
    output_file = open("E:\Documents\ME\Course\Sem 2\Cloud Security\Submissions\Lab Submission 2\Write File.txt", "w")
    
    # Opening input file and scanning each line from input file and writing in output file
    with open("E:\Documents\ME\Course\Sem 2\Cloud Security\Submissions\Lab Submission 2\Read File.txt", "r") as scan:
        output_file.write(scan.read())
    
    # Closing the output file
    output_file.close()

    print("Read and Write complete. Written to file successfully\n\n")



#1. b. Count the total number of characters in the file
def countCharacters():
    #open file in read mode
    file = open("E:\Documents\ME\Course\Sem 2\Cloud Security\Submissions\Lab Submission 2\Read File.txt", "r")

    #read the content of file
    data = file.read()

    #get the length of the data
    number_of_characters = len(data)

    print('Number of characters in text file :', number_of_characters)




#1. c. Reverse the content from the file.
def reverseFile():
    # Open the file in write mode
    f1 = open("E:\Documents\ME\Course\Sem 2\Cloud Security\Submissions\Lab Submission 2\Reverse File.txt", "w")

    # Open the input file and get
    # the content into a variable data
    with open("E:\Documents\ME\Course\Sem 2\Cloud Security\Submissions\Lab Submission 2\Read File.txt", "r") as myfile:
        data = myfile.read()

    # For Full Reversing we will store the value of data into new variable data_1
    # in a reverse order using [start: end: step], where step when passed -1 will reverse the string
    data_1 = data[::-1]

    # Now we will write the fully reverse data in the output1 file using following command
    f1.write(data_1)

    f1.close()
    print("\n\nReverse of file content complete. Written to file successfully\n\n")