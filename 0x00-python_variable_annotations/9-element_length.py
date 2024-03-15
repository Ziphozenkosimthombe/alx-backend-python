#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence], return_type: List[Tuple[Sequence, int]]) -> List[Tuple[Sequence, int]]:
    """ Return a list of tuples, each containing a sequence and its length"""
    return [(i, len(i)) for i in lst]