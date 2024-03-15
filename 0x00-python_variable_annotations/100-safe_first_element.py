#!/usr/bin/env python3

from typing import Sequence, Union, Any, NonType


def safe_first_element(lst: Sequence[Any]) -> Union[Any, NonType]:
    """ Return the first element of a list """
    if lst:
        return lst[0]
    else:
        return None
