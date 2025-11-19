from myPackage import myModule

def test_myModule_function():
    """
    Test the 'top_n_items' function from myModule.
    """
    
    assert myModule.top_n_items([5, 1, 3, 7, 2], 3) == [7, 5, 3], "Test Case 1 Failed"
    assert myModule.top_n_items([10, 20, 15], 2) == [20, 15], "Test Case 2 Failed"  
    assert myModule.top_n_items([1, 2, 3, 4, 5], 5) == [5, 4, 3, 2, 1], "Test Case 3 Failed"