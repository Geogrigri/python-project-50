import json
import os

import pytest

from gendiff import generate_diff


def get_fixture_path(filename):
    return os.path.join("tests", "test_data", filename)


def read_fixture(filename):
    path = get_fixture_path(filename)
    with open(path) as file:
        return file.read()


@pytest.mark.parametrize(
    ("file1", "file2", "expected"),
    [
        ("file1.json", "file2.json", "expected_stylish.txt"),
        ("file1.yml", "file2.yml", "expected_stylish.txt"),
        (
            "nested_file1.json",
            "nested_file2.json",
            "nested_expected_stylish.txt",
        ),
        (
            "nested_file1.yml",
            "nested_file2.yml",
            "nested_expected_stylish.txt",
        ),
    ],
)
def test_generate_diff_stylish(file1, file2, expected):
    file_path1 = get_fixture_path(file1)
    file_path2 = get_fixture_path(file2)
    expected_result = read_fixture(expected)

    assert generate_diff(file_path1, file_path2) == expected_result.strip()


@pytest.mark.parametrize(
    ("file1", "file2"),
    [
        ("nested_file1.json", "nested_file2.json"),
        ("nested_file1.yml", "nested_file2.yml"),
    ],
)
def test_generate_diff_plain(file1, file2):
    file_path1 = get_fixture_path(file1)
    file_path2 = get_fixture_path(file2)
    expected_result = read_fixture("nested_expected_plain.txt").strip()

    assert generate_diff(file_path1, file_path2, "plain") == expected_result


def test_generate_diff_json_format():
    file_path1 = get_fixture_path("nested_file1.json")
    file_path2 = get_fixture_path("nested_file2.json")

    result = generate_diff(file_path1, file_path2, "json")

    assert isinstance(result, str)
    assert json.loads(result)
