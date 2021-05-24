
from tkinter import *    # importing everything in the tkinter module
from tkinter import messagebox   # import the messagebox from the tkinter module

root = Tk()    # create window
root.title("NextPage")    # name the window
root.geometry("600x600")     # setting the window size
root.config(bg="dark slate gray")     # changing the window background-color


# Python program for implementation of Insertion Sort

# Function to do insertion sort
def insertionSort(arr):
    # Loop from the second element of the array until
    # the last element
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):   # sets up the loop that determines the key_item that the function will position during each iteration

        # This is the element we want to position in its
        # correct place
        key = arr[i]     # initializes key_item with the item that the function is trying to place

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position

        # or

        # Initialize the variable that will be used to
        # find the correct position of the element referenced
        # by `key_item`
        j = i-1   # initializes a variable that will consecutively point to each element to the left of key item

        # Run through the list of items (the left
        # portion of the array) and find the correct position
        # of the element referenced by `key_item`. Do this only
        # if `key_item` is smaller than its adjacent values.
        while j >= 0 and key < arr[j]:     # compares key_item with each value to its left using a while loop, shifting the elements to make room to place key_item

                # Shift the value one position to the left
                # and reposition j to point to the next element
                # (from right to left)
                arr[j + 1] = arr[j]
                j -= 1

        # When you finish shifting the elements, you can position
        # `key_item` in its correct location
        arr[j + 1] = key    # positions key_item in its correct place after the algorithm shifts all the larger values to the right


# Driver code to test above
arr = [42, 12, 13, 89, 63, 11]
insertionSort(arr)


sorted_list = Label(root, text="11, 12, 13, 42, 63, 89")
sorted_list.place(x=200, y=100)

def exit():
    root.destroy()


exit_btn = Button(root, text="Exit Program", borderwidth="10", bg="Aqua", font=("Consolas 15 bold"), command=exit)
exit_btn.place(x=200, y=300)

# starting the app
root.mainloop()
