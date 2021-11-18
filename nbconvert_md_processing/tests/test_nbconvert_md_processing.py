"""
Unit and regression test for the nbconvert_md_processing package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import nbconvert_md_processing


def test_nbconvert_md_processing_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "nbconvert_md_processing" in sys.modules
