import pytest
from linked_list import LinkedList

@pytest.fixture
def ll():
    """Returns an empty LinkedList instance."""
    return LinkedList()

@pytest.fixture
def populated_ll():
    """Returns a LinkedList with some data."""
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    return ll

def test_init(ll):
    """Test the constructor."""
    assert ll.head is not None
    assert ll.head.next is None
    assert str(ll) == ""

def test_repr_single_node(ll):
    """Test __repr__ with a single node."""
    ll.append(10)
    assert str(ll) == "10"

def test_repr_multiple_nodes(populated_ll):
    """Test __repr__ with multiple nodes."""
    assert str(populated_ll) == "10,20,30"

def test_append_to_empty_list(ll):
    """Test appending an element to an empty list."""
    ll.append(5)
    assert ll.head.next.data == 5
    assert ll.head.next.next is None
    assert str(ll) == "5"

def test_append_to_non_empty_list(populated_ll):
    """Test appending an element to a non-empty list."""
    populated_ll.append(40)
    assert str(populated_ll) == "10,20,30,40"

def test_prepend_to_empty_list(ll):
    """Test prepending an element to an empty list."""
    ll.prepend(5)
    assert ll.head.next.data == 5
    assert ll.head.next.next is None
    assert str(ll) == "5"

def test_prepend_to_non_empty_list(populated_ll):
    """Test prepending an element to a non-empty list."""
    populated_ll.prepend(5)
    assert str(populated_ll) == "5,10,20,30"
    assert populated_ll.head.next.data == 5

def test_search_empty_list(ll):
    """Test searching in an empty list."""
    assert ll.search(10) is None

def test_search_item_exists(populated_ll):
    """Test searching for an item that exists."""
    node = populated_ll.search(20)
    assert node is not None
    assert node.data == 20

def test_search_item_not_exists(populated_ll):
    """Test searching for an item that does not exist."""
    assert populated_ll.search(100) is None

def test_remove_from_empty_list(ll):
    """Test removing from an empty list."""
    result = ll.remove(10)
    assert result is None
    assert str(ll) == ""

def test_remove_non_existent_item(populated_ll):
    """Test removing an item that is not in the list."""
    populated_ll.remove(100)
    assert str(populated_ll) == "10,20,30"

def test_remove_first_item(populated_ll):
    """Test removing the first item."""
    populated_ll.remove(10)
    assert str(populated_ll) == "20,30"

def test_remove_middle_item(populated_ll):
    """Test removing a middle item."""
    populated_ll.remove(20)
    assert str(populated_ll) == "10,30"

def test_remove_last_item(populated_ll):
    """Test removing the last item."""
    populated_ll.remove(30)
    assert str(populated_ll) == "10,20"

def test_remove_only_item(ll):
    """Test removing the only item in the list."""
    ll.append(5)
    ll.remove(5)
    assert str(ll) == ""
    assert ll.head.next is None

def test_insert_after_item(populated_ll):
    """Test inserting an item after a specific item."""
    populated_ll.insert(20, 25)
    assert str(populated_ll) == "10,20,25,30"

def test_insert_after_last_item(populated_ll):
    """Test inserting after the last item."""
    populated_ll.insert(30, 35)
    assert str(populated_ll) == "10,20,30,35"

def test_insert_item_not_found(populated_ll):
    """Test inserting when the target item is not found."""
    populated_ll.insert(100, 150)
    assert str(populated_ll) == "10,20,30"

def test_insert_into_empty_list(ll):
    """Test inserting into an empty list."""
    ll.insert(10, 20)
    assert str(ll) == ""

def test_reverse_empty_list(ll):
    """Test reversing an empty list."""
    ll.reverse()
    assert str(ll) == ""

def test_reverse_single_element_list(ll):
    """Test reversing a list with a single element."""
    ll.append(10)
    ll.reverse()
    assert str(ll) == "10"

def test_reverse_multiple_elements(populated_ll):
    """Test reversing a list with multiple elements."""
    populated_ll.reverse()
    assert str(populated_ll) == "30,20,10"

def test_insertion_sort_empty_list(ll):
    """Test sorting an empty list."""
    ll.insertion_sort()
    assert str(ll) == ""

def test_insertion_sort_single_element(ll):
    """Test sorting a list with a single element."""
    ll.append(10)
    ll.insertion_sort()
    assert str(ll) == "10"

def test_insertion_sort_unsorted_list():
    """Test sorting an unsorted list."""
    ll = LinkedList()
    ll.append(30)
    ll.append(10)
    ll.append(20)
    ll.append(5)
    ll.insertion_sort()
    assert str(ll) == "5,10,20,30"

def test_insertion_sort_with_duplicates():
    """Test sorting a list with duplicate values."""
    ll = LinkedList()
    ll.append(10)
    ll.append(5)
    ll.append(10)
    ll.append(2)
    ll.insertion_sort()
    assert str(ll) == "2,5,10,10"