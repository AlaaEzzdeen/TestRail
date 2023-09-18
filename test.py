def add_numbers(a, b):
    return a + b

def test_add_numbers():
    assert add_numbers(2, 2) == 4  # This test case will succeed
    assert add_numbers(3, 3) == 7  # This test case will fail

if __name__ == "__main__":
    test_add_numbers()