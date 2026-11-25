import pytest
from insertLL import LinkedList


def ll_to_list(ll):
    result = []
    curr = ll.head
    while curr:
        result.append(curr.data)
        curr = curr.next
    return result


def test_delete_at_end_multi_node():
    ll = LinkedList()
    ll.insert_at_index(0, 10)
    ll.insert_at_index(1, 20)
    ll.insert_at_index(2, 30)

    assert hasattr(ll, "delete_at_end"), "LinkedList has no method 'delete_at_end'"
    ll.delete_at_end()

    assert ll_to_list(ll) == [10, 20]


def test_delete_at_end_single_node():
    ll = LinkedList()
    ll.insert_at_index(0, 10)

    assert hasattr(ll, "delete_at_end"), "LinkedList has no method 'delete_at_end'"
    ll.delete_at_end()

    assert ll.head is None
    assert ll_to_list(ll) == []


def test_delete_at_end_empty_list():
    ll = LinkedList()

    assert hasattr(ll, "delete_at_end"), "LinkedList has no method 'delete_at_end'"
    with pytest.raises(IndexError, match="Index out of bounds"):
        ll.delete_at_end()