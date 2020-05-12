from typing import Any, List

from pandas import DataFrame


class DataSet:
    @property
    def data_frame(self) -> DataFrame:
        return self.__data_frame

    @property
    def features(self):
        return self.__features

    @property
    def dependent_variable_vector(self):
        return self.__dependent_variable_vector

    def __init__(self,
                 data_frame: DataFrame,
                 features: List[List[Any]],
                 dependent_variable_vector: List[Any]):
        self.__dependent_variable_vector = dependent_variable_vector
        self.__features = features
        self.__data_frame = data_frame
