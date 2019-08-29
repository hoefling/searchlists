import pyperclip
import pytest

from searchlists.lists import copy, create_string

TEST_LIST = [7, 809823, 102890, "string", 291]


def test_create_lists_separators():
    separators = [",", ";", " ", ", ", "; "]
    for sep in separators:
        string = create_string(TEST_LIST, sep=sep)
        expected = sep.join([str(k) for k in TEST_LIST])
        assert expected == string, "failed separation test"


def test_create_lists_prefix():

    prefixes = ["test-", "pre-", "p"]

    for pre in prefixes:
        string = create_string(TEST_LIST, prefix=pre, sep=", ")
        with_pre = [f"{pre}{k}" for k in TEST_LIST]
        expected = ", ".join(with_pre)
        assert expected == string, "failed prefix test"


def test_create_lists_suffix():
    suffixes = ["-post", "test", "-ending"]
    for suffix in suffixes:
        string = create_string(TEST_LIST, suffix=suffix, sep=", ")
        with_suffix = [f"{k}{suffix}" for k in TEST_LIST]
        expected = ", ".join(with_suffix)
        assert expected == string, "failed suffix test"


def test_quote():
    quoted = [f'"{i}"' for i in TEST_LIST]
    expected = ", ".join(quoted)
    string = create_string(TEST_LIST, quote=True, sep=", ")

    assert expected == string, "failed quote test"


def test_validate():

    kwargs = [
        {"items": "not a list"},
        {"items": TEST_LIST, "prefix": ["not", "a", "str"]},
        {"items": TEST_LIST, "suffix": ("not", "a", "str")},
        {"items": TEST_LIST, "sep": ("not", "a", "str")},
    ]
    for k in kwargs:
        with pytest.raises(TypeError):
            create_string(**k)


def test_copy():
    kwargs = [
        {"items": TEST_LIST},
        {"items": TEST_LIST, "quote": True},
        {"items": TEST_LIST, "prefix": "pre-"},
        {"items": TEST_LIST, "prefix": "pre-", "quote": True},
        {"items": TEST_LIST, "suffix": "-post"},
        {"items": TEST_LIST, "prefix": "pre-", "suffix": "-post"},
    ]

    for k in kwargs:
        copy(**k)  # copy items to clipboard
        string = create_string(**k)
        assert (
            string == pyperclip.paste(),
            "clipboard did not have expected value",
        )
