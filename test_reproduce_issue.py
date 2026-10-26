import pytest
from insertLL import LinkedList


def test_insert_at_index_negative():
    ll = LinkedList()
    with pytest.raises(IndexError):
        ll.insert_at_index(-1, 10)


def test_insert_at_index_out_of_bounds():
    ll = LinkedList()
    ll.insert_at_index(0, 1)
    ll.insert_at_index(1, 2)
    # Length is 2; valid insertion indices are 0, 1, 2. Index 3 is out of bounds.
    with pytest.raises(IndexError):
        ll.insert_at_index(3, 3)


def test_insert_at_index_valid():
    ll = LinkedList()
    ll.insert_at_index(0, 10)  # insert at head of empty list
    ll.insert_at_index(1, 30)  # insert at tail
    ll.insert_at_index(1, 20)  # insert in middle

    assert ll.head.data == 10
    assert ll.head.next.data == 20
    assert ll.head.next.next.data == 30
    assert ll.head.next.next.next is None


def test_delete_at_index_empty_list():
    ll = LinkedList()
    with pytest.raises(IndexError):
        ll.delete_at_index(0)


def test_delete_at_index_out_of_bounds():
    ll = LinkedList()
    ll.insert_at_index(0, 10)
    ll.insert_at_index(1, 20)

    with pytest.raises(IndexError):
        ll.delete_at_index(-1)

    with pytest.raises(IndexError):
        ll.delete_at_index(2)


def test_delete_at_index_valid():
    ll = LinkedList()
    ll.insert_at_index(0, 10)
    ll.insert_at_index(1, 20)
    ll.insert_at_index(2, 30)

    # Delete index 0 (head)
    ll.delete_at_index(0)
    assert ll.head.data == 20
    assert ll.head.next.data == 30

    # Delete index 1 (tail)
    ll.delete_at_index(1)
    assert ll.head.data == 20
    assert ll.head.next is None

    # Delete remaining element
    ll.delete_at_index(0)
    assert ll.head is None


def test_delete_by_value():
    ll = LinkedList()
    ll.insert_at_index(0, 10)
    ll.insert_at_index(1, 20)
    ll.insert_at_index(2, 30)

    # Delete non-existent value
    assert ll.delete(99) is False

    # Delete middle value
    assert ll.delete(20) is True
    assert ll.head.data == 10
    assert ll.head.next.data == 30
    assert ll.head.next.next is None

    # Delete head value
    assert ll.delete(10) is True
    assert ll.head.data == 30

    # Delete tail/only value
    assert ll.delete(30) is True
    assert ll.head is None