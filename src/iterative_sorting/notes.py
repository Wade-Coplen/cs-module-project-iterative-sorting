#We will write our function to expect a sorted list of integers. If the item we are searching 
# for is in the list, then we will return the position that it holds in the list.

def binary_search(my_list, search_item):
    low = 0
    high = len(my_list) -1
    while low <= high:
    #we want the loop to continue so long as the low pointer is less than or equal to the high
        middle = (low + high) //2
        guess = my_list[middle]
        #find the middle index, the use it to retrieve the index of the middle
        #our guess could be to high, low or correct. The (if) statements act as a filter.
        if guess == search_item:
            return middle
            #if our (guess) is equal to our(search_item) it means the (middle) is correct. Return (middle)
        if guess > search_item:
            high = midde -1
            #if our (guess) is too high we change our pointer to the index before the previous (middle) value
        else:
            low = middle + 1
            #if our (guess) is too low then we change our pointer to the index just after the previous (middle) value
    return None
    # do this if our (search_item) is not found in our (my_list)

    #Key points:
    #1. we set pointers to (low) and (high). Generally (low) is 0. (high) is len(list) -1
    #2. find the middle index. By doing this we can essentially split the list in half versus having to iterate over the list mulitple times. If we can determine if our (search_item) is lower or higher than the middle value, it is much faster.
    #3. Assign the (middle) value to a (guess) variable
    #4. create an (if) block to filter whether or not our (search_item) is greater, equal or correct
    #5. if too high change the pointer to the index just before the (middle) value
    #6. if  (search_item) is equal to (middle), return the (middle) value    
    #7. if our (guess) is lower than the (search_item), change the pointer to the index just after the (middle value)
    test_list = [2,4,7,8,9,10,12,34,45]
    binary_search(test_list, 7)