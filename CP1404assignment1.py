"""
Name: Reuben Bogogolelo
Date:  27 December 2016 - 11 January 2017
Brief program details:
This program loads everything on the books.csv and will show the quantity of items in the main(). It consists of 8 functions,
with one function being main() controlling all other seven functions. The program display the list of required/completed books
based on user input. The program has been designed to add the new books to the list as in the csv file and make the book from
required to completed, which change the value in the list file_list. After the user quits the program, it then reads the file
and then overwrite the list of book in the file books.csv. Its been made (program) to handle the error-checking.

Repository: https://github.com/reubenbogogolelo.......

"""

from operator import itemgetter
FILENAME = "books.csv"
INPUT_LIST = ['R','C','A','M','Q']
global index_of_Required_Books
index_of_Required_Books =[]
UserInputToMark = ''
file_list = []# pls explain wat ths array is supposed to do
#selectedIndex = 0 #for debugging remove later

def read_file():
    global file_list
    file_pointer = open(FILENAME)
    for index, data in enumerate (file_pointer.readlines()):
        data = data.strip()
        datum = data.split(",")
        file_list.append(datum)
    file_list.sort(key=itemgetter(1,2))
    file_pointer.close()
    return file_list


def print_header(): #this function is designed to list the books as read by read_file() and brings the menu for the user to chose based on their option.
    print("""
Reading list 1.0 - by Reuben
{} books loaded from books.csv
    """.format(len(file_list)))
    print("Menu: \n R - List required books \n C - List completed books \n A - Add new book \n M - Mark a book as completed \n Q - Quit")


def display_books(selected_input):#this function is designed to display the books marked as completed or required ones as per the users input choice.
    counter_one =0
    total_pages = 0
    global index_of_Required_Books
    index_of_Required_Books = []

    if selected_input.upper()=='C': # to take care of the completed books only.
        variable_text = "Completed books:"
    elif selected_input.upper()=='R':# to take care of the required books only.
        variable_text = "Required books:"
    print(variable_text)

    for i in range(0, (len(file_list))):
        if file_list[i][3].upper() == selected_input.upper(): #this will Sort the books as they appear on the csv file.
            print("{}. {:50} by {:20} {} pages" .format(i, file_list[i][0],file_list[i][1],file_list[i][2]))
            index_of_Required_Books.append(int(i))
            counter_one +=1
            total_pages += int(file_list[i][2])#this will add all the pages of books marked as completed


    print("Total pages for {} book: {} ".format(counter_one, total_pages))

    print("Menu: \n R - List required books \n C - List completed books \n A - Add new book \n M - Mark a book as completed \n Q - Quit")


def marking_a_book(selected_input):# has been designed to list the number of a book to mark as completed.
    global selectedIndex
    if (selected_input == "M") or (selected_input == "m"):
        display_books('r')
        print("Enter the number of a book to mark as completed")
        while True:
            try:
                UserInputToMark = int(input(">>>"))
                break
            except ValueError:
                print('Invalid input; enter a valid number')
                #input choice should be 'm/M' otherwise any other unput will be handled.
        print(
            "Menu: \n R - List required books \n C - List completed books \n A - Add new book \n M - Mark a book as completed \n Q - Quit")

        Flag = False
        for i in range(0, (len(index_of_Required_Books))):

            if (index_of_Required_Books[i]) == UserInputToMark:
                Flag = True
                break

        if Flag == False:
            print("That book is already completed")# it will print the text when the flag is False.
            print("Menu: \n R - List required books \n C - List completed books \n A - Add new book \n M - Mark a book as completed \n Q - Quit")
            UserInputToMark = input(">>>")

            if UserInputToMark.upper() == "M":
                display_books('r')

                while True:
                    try:
                        global finalMarkingInupt
                        finalMarkingInupt = int(input(">>>"))

                        break
                    except ValueError:
                        print('Invalid input; enter a valid number')

                for j in range(0, (len(index_of_Required_Books))):

                    if index_of_Required_Books[j] == finalMarkingInupt:
                        file_list[j][3] = "c"# will only display the marked as 'c' in the csv file
                        print("{} by {} marked as completed".format(file_list[j][0], file_list[j][1]))
                        print("Menu: \n R - List required books \n C - List completed books \n A - Add new book \n M - Mark a book as completed \n Q - Quit")
                        UserInputToMark = input(">>>")
                        if (UserInputToMark.upper() != "A") or (UserInputToMark.upper() != "Q"):
                            print("Invalid input menu choice")


def adding_a_book(UserInputToMark):# designed to add a new book.
    flag=True
    if UserInputToMark.upper() == "A": #input should be 'a' only when the user wants to add the new book.
        while True:
            print("Input can not be blank")
            UserInputToMarkTitle = input("Title: ")#promts the user to input tittle of the book to be added.
            if (UserInputToMarkTitle != ""):# input should not be blank
                break

        while True:
            print("Input can not be blank")
            UserInputToMarkAuthor = input("Author: ")#promts the user to input the author of the book to be added.
            if (UserInputToMarkAuthor != ""):#input should not be blank.
                break

        while flag:
            try:
                UserInputToMarkPages = int(input("Pages: "))#promts the user to input the number of pages of a book to be added.

                while UserInputToMarkPages <0:
                    print("Number must be >= 0")# number of pages should not be less than 0.
                    UserInputToMarkPages = int(input("Pages: "))
                flag=False
            except ValueError:
                        print('Invalid input; enter a valid number')

        AddedBookDetail = []
        AddedBookDetail.append(UserInputToMarkTitle)# title will be appended to the list.
        AddedBookDetail.append(UserInputToMarkAuthor)# author will be appended to the list.
        AddedBookDetail.append(str(UserInputToMarkPages))#pages will be appended to the list.
        AddedBookDetail.append('r')
        file_list.append(AddedBookDetail)#the book will be appended accordigly.
        print('{} by {}, ({}) added to reading list'.format(UserInputToMarkTitle, UserInputToMarkAuthor, UserInputToMarkPages))
        print(
            "Menu: \n R - List required books \n C - List completed books \n A - Add new book \n M - Mark a book as completed \n Q - Quit")


def main():#the main function as the master controller will let the user enter the option.
    read_file()# this function will be called
    print_header()# this function will be called
    highLevelInput = input(">>>")# input prompt

    while True:
        if (highLevelInput.upper() == 'R') or highLevelInput.upper() == 'C' or highLevelInput.upper() == 'A' or highLevelInput.upper() == 'M' or highLevelInput.upper() == 'Q':
            Dummy =1 #Dummy code
        else:
            print((highLevelInput.upper() != 'R') or highLevelInput.upper() != 'C' or highLevelInput.upper() != 'A' or highLevelInput.upper() != 'M' or highLevelInput.upper() != 'Q')
            #print(highLevelInput.upper()!='Q')
            while True:
                print("Invalid Menu Choice")
                print("Menu: \n R - List required books \n C - List completed books \n A - Add new book \n M - Mark a book as completed \n Q - Quit")
                highLevelInput = input(">>>")
                if highLevelInput.upper() != 'R' or highLevelInput.upper() != 'C' or highLevelInput.upper() != 'A' or highLevelInput.upper() != 'M' or highLevelInput.upper() != 'Q':
                    break

        if highLevelInput.upper()=='R':
            display_books('r')#if the option is true, then the display() will be called
        elif highLevelInput.upper() == 'C':
            display_books('c')#if the option is true, then the display() will be called
        elif highLevelInput.upper() == 'A':
            adding_a_book('a')#if the option is true, then the adding_a_book() function will be called
        elif highLevelInput.upper() == 'M':
            marking_a_book('m')#if the option is true, then the marking() will be called
        highLevelInput = input(">>>")#input prompt for the user for all the above functions.

        if (highLevelInput.upper() == "Q"): #the choice is restricted to 'Q/q' and will exit the program.
            print("{} books saved to {}".format(len(file_list), FILENAME))# this will list all the books in the csv file.
            print("Have a nice day :)")

    return

main()


