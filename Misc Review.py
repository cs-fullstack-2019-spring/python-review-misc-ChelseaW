# KEY: In future please remove any code that is not of your solution submission as hard to tell what to grade
# KEY: Missing Comments :-(

def main():
     # problem1()
     problem2()
    # challenge1()
    # challenge2()


# def problem1():
#code will continue to run until q gets it to quit

# user = ""
#
# while(user != 'q'):
#     user = input("Something")
#

# while():
#     if(user != 'q'):
#         print("It has Been Entered!!!")
#     elif(user != 'Q'):
#         user = int(input('Enter another code'))





def problem2():

    exercise2_helper(num1 =2, num2 =4, num3 =6, operation ="SUM")


    print(exercise2_helper(2,4,6,"SUM"))
    print(exercise2_helper(2,4,6,"PROD"))
    print(exercise2_helper(2,4,6,"AVG"))


def exercise2_helper(num1, num2, num3, operation):
    if (operation== "SUM"):
        return(num1 + num2 + num3)
    if (operation== "PROD"):
        return(num1 * num2 * num3)
    if (operation== "AVG"):
        return(num1 + num2 + num3 // 3)

    print(exercise2_helper(2,4,6,"SUM"))
    print(exercise2_helper(2,4,6,"PROD"))
    print(exercise2_helper(2,4,6,"AVG"))

if __name__ == '__main__':
    main()


    # exercise2_helper(num1 =2, num2 = 4, num3 = 6.operation("sum, prod, avg")):
    #
    # case 'sum':
    #     return('The Sum' + str(num1 + num2, num3),
    # case 'prod':
    #     return('The Prod' + str(num1 + num2, num3),
    # case 'avg':
    #     return('The Avg' + str(num1 + num2, num3),
    #



#     SUM - Return the sum of the 3 numbers
#     PROD - Return the product of the 3 numbers
#     AVG - Return the average of the 3 numbers
#

