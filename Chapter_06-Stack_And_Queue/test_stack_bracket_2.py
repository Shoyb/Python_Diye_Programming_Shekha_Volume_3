import pytest
from stack_bracket_2 import is_balanced

def test_balanced_simple():
    """Test simple balanced pairs."""
    assert is_balanced("()") is True
    assert is_balanced("[]") is True
    assert is_balanced("{}") is True

def test_balanced_nested():
    """Test nested balanced brackets."""
    assert is_balanced("({})") is True
    assert is_balanced("{[()]}") is True
    assert is_balanced("{{[[(())]]}}") is True

def test_balanced_sequential():
    """Test sequential balanced brackets."""
    assert is_balanced("()[]{}") is True
    # Note: The original code does not strip spaces, so " " might fail if treated as non-bracket
    # Assuming input is just brackets for sequential test without spaces unless logic handles it.
    assert is_balanced("()[]{}") is True

def test_unbalanced_single_char():
    """Test single characters which are inherently unbalanced."""
    assert is_balanced("(") is False
    assert is_balanced(")") is False
    assert is_balanced("[") is False
    assert is_balanced("]") is False
    assert is_balanced("{") is False
    assert is_balanced("}") is False

def test_unbalanced_mismatched_type():
    """Test brackets that are closed by the wrong type."""
    assert is_balanced("(]") is False
    assert is_balanced("{)") is False
    assert is_balanced("[}") is False

def test_unbalanced_wrong_nesting():
    """Test correctly typed but incorrectly nested brackets."""
    assert is_balanced("([)]") is False
    assert is_balanced("{[}]") is False

def test_starts_with_closing():
    """Test strings starting with a closing bracket."""
    assert is_balanced(")(") is False
    assert is_balanced("][") is False
    assert is_balanced("}{") is False

def test_missing_closing():
    """Test strings with missing closing brackets."""
    assert is_balanced("(()") is False
    assert is_balanced("{[}") is False

def test_excess_closing():
    """Test strings with extra closing brackets."""
    assert is_balanced("())") is False
    assert is_balanced("[]]") is False

def test_empty_string():
    """Test an empty string, which is technically balanced (no unbalanced brackets)."""
    assert is_balanced("") is True
