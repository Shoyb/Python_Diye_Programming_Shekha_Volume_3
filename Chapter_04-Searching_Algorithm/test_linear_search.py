from linear_search import linear_search

def test_element_found():
    """Test case for when the element is in the list."""
    L = [10, 20, 30, 40, 50]
    assert linear_search(L, 30) == 2

def test_element_not_found():
    """Test case for when the element is not in the list."""
    L = [10, 20, 30, 40, 50]
    assert linear_search(L, 60) == -1

def test_empty_list():
    """Test case for an empty list."""
    L = []
    assert linear_search(L, 10) == -1

def test_element_at_beginning():
    """Test case for when the element is at the beginning of the list."""
    L = [10, 20, 30, 40, 50]
    assert linear_search(L, 10) == 0

def test_element_at_end():
    """Test case for when the element is at the end of the list."""
    L = [10, 20, 30, 40, 50]
    assert linear_search(L, 50) == 4

def test_list_with_duplicates():
    """Test case for a list with duplicate elements, should return the first index."""
    L = [10, 20, 30, 20, 40]
    assert linear_search(L, 20) == 1
