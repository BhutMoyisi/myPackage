# Return top n items from an array in descending order
def top_n_items(items, n):
    """_summary_

    Args:
        items (array): list or array-like object containing items
        n (int): number of top items to return
    Return:
        array: top n items in descending order
        
    Egs:
        >>> top_n_items([5, 1, 3, 7, 2], 3)
        [7, 5, 3]
        >>> top_n_items([10, 20, 15], 2)
        [20, 15]
    """
    
    for i in range(n):   # keep iterating until we have top n items
        for j in range(0, len(items)-i-1): 
            
            if items[j] > items[j+1] :    # if this item is bigger than next item...
                items[j], items[j+1] = items[j+1], items[j]   # swap them
                
    # get last two items from sorted array
    top_n_items = items[-n:]
    
    # reverse the array to get descending order
    return top_n_items[::-1]