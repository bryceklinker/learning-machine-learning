from typing import Any, List

from data_sets.data_set import DataSet


class CleanDataSet(DataSet):
    @property
    def source_data_set(self) -> DataSet:
        return self.__source_data_set

    def __init__(self,
                 dependent_variable_vector: List[Any] = None,
                 features: List[List[Any]] = None,
                 source_data_set: DataSet = None):
        super().__init__(data_frame=source_data_set.data_frame,
                         features=features,
                         dependent_variable_vector=dependent_variable_vector)
        self.__source_data_set = source_data_set
