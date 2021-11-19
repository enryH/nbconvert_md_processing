"""
Unit and regression test for the nbconvert_md_processing package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import nbconvert_md_processing

with open('simple_notebook.md') as f:
    input_str = f.read()
    
def test_nbconvert_md_processing_parse():
    """Test removing of pandas headers"""
    transformed = nbconvert_md_processing.parse(input_str, verbose=True)
    
    with open('simple_notebook_wo_headers.md') as f:
        expected_str = f.read()
    assert transformed == expected_str
    
def test_nbconvert_md_processing_parse_urls():
    """Test removing of pandas headers and url replacement."""
    transformed = nbconvert_md_processing.parse(input_str, verbose=True,
                                                urls_fpath='urls_to_replace.txt')
    
    with open('simple_notebook_wo_headers_urls_replaced.md') as f:
        expected_str = f.read()
        
    assert transformed == expected_str