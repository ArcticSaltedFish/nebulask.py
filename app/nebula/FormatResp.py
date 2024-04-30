#!/usr/bin/env python
# --coding:utf-8--

# Copyright (c) 2020 vesoft inc. All rights reserved.
#
# This source code is licensed under Apache 2.0 License.


from typing import Dict

import pandas as pd
import prettytable
from nebula3.data.ResultSet import ResultSet


################################
#     Method 1 (Recommended)   #
################################
import json


def result_to_dict(result: ResultSet) -> dict[str, list]:
    """
    build list for each column, and transform to dataframe
    """
    assert result.is_succeeded()
    columns = result.keys()
    d: Dict[str, list] = {}
    for col_num in range(result.col_size()):
        col_name = columns[col_num]
        col_list = result.column_values(col_name)
        d[col_name] = [x.cast() for x in col_list]
    # return pd.DataFrame.from_dict(d, columns=columns)
    return d
