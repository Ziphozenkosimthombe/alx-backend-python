#!/usr/bin/env python3

from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Return the first element of a list """
    if lst:
        return lst[0]
    else:
        return None
