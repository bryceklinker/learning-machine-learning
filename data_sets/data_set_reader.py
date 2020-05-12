from os.path import join, dirname

from pandas import read_csv

from data_sets.data_set import DataSet

ROOT_PATH = join(dirname(__file__), 'files')


def read_data_set(name: str, dependent_variable_vector_index=-1) -> DataSet:
    data_frame = read_csv(join(ROOT_PATH, "{}.csv".format(name)))
    features = data_frame.iloc[:, 0:dependent_variable_vector_index].values
    dependent_variable_vector = data_frame.iloc[:, dependent_variable_vector_index].values
    return DataSet(data_frame=data_frame, features=features, dependent_variable_vector=dependent_variable_vector)
