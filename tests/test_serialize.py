import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
# This line is now corrected to import from 'serialize'
from serialize import Node, serialize, deserialize

# normal (4)
def test_roundtrip_small():
    r = Node(1, Node(2), Node(3))
    s = serialize(r)
    rr = deserialize(s)
    assert serialize(rr) == s

def test_roundtrip_unbalanced():
    r = Node(1, Node(2, Node(3)), None)
    s = serialize(r)
    assert serialize(deserialize(s)) == s

def test_roundtrip_strings():
    r = Node("root", Node("L"), Node("R"))
    s = serialize(r)
    assert serialize(deserialize(s)) == s

def test_none_tree():
    s = serialize(None)
    assert s == '#'
    assert serialize(deserialize(s)) == '#'

# edge (3)
def test_only_left_chain():
    r = Node(1, Node(2, Node(3)))
    assert serialize(deserialize(serialize(r))) == serialize(r)

def test_only_right_chain():
    r = Node(1, None, Node(2, None, Node(3)))
    assert serialize(deserialize(serialize(r))) == serialize(r)

def test_mixed_values_types():
    r = Node("1", Node("two"), Node(3))
    s = serialize(r)
    rr = deserialize(s)
    assert serialize(rr) == s

# harder (3)
def test_big_shape():
    r = Node(4,
             Node(2, Node(1), Node(3)),
             Node(6, Node(5), Node(7)))
    s = serialize(r)
    assert serialize(deserialize(s)) == s

def test_random_tokens_stability():
    r = Node(0, Node(-1), Node(10))
    s = serialize(r)
    assert isinstance(deserialize(s), Node)

def test_multiple_hashes():
    assert serialize(deserialize('# # #')) == '#'

