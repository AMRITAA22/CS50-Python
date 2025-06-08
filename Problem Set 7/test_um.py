from um import count
def test_one_um():
    assert count("um") == 1
    assert count("hello, um, world") == 1
def test_multiple_ums():
    assert count("um um um") == 3
    assert count("Um, um... UM!") == 3
def test_no_um():
    assert count("yummy") == 0
    assert count("umbrella") == 0
    assert count("hummus") == 0
def test_edge_cases():
    assert count("Um?") == 1
    assert count("  um  ") == 1
    assert count("Well... um... maybe.") == 1
