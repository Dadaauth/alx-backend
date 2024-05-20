#!/usr/bin/env python3
"""A module documentation"""


def index_range(page: int, page_size: int) -> tuple:
    """A function documentation is always necessary!"""
    start_idx = 0
    end_idx = 0
    for _ in range(1, page):
        start_idx += page_size
    end_idx += start_idx + page_size
    return (start_idx, end_idx)
