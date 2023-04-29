# Skipping Tests

import sys
import pytest

# skip, xfail, xpass, skipif

test_boolean_1_dont_run = "don't run"


@pytest.mark.skipif(condition=test_boolean_1_dont_run == "don't run", reason="Waiting definition")
def test_boolean_1():
    status = 100
    assert status == 100


@pytest.mark.skipif(condition=sys.version_info > (3, 10), reason="Python 3.10 not found")
def test_boolean_2():
    status = 100
    assert status == 100


@pytest.mark.skip
def test_boolean_3():
    status = 100
    assert status == 10


@pytest.mark.xfail
def test_boolean_4():
    status = 100
    assert status == 10
