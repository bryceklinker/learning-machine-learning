from data_sets.data_set import DataSet
from numpy import nan
from sklearn.impute import SimpleImputer

from preprocessing.clean_data_set import CleanDataSet


def fill_in_missing_values_using_mean(data_set: DataSet, clean_start_index, clean_end_index) -> CleanDataSet:
    cleaned_features = data_set.features.copy()
    features_to_clean = cleaned_features[:, clean_start_index: clean_end_index]
    cleaner = SimpleImputer(missing_values=nan, strategy='mean')
    cleaner.fit(features_to_clean)
    cleaned_features[:, clean_start_index: clean_end_index] = cleaner.transform(features_to_clean)
    return CleanDataSet(dependent_variable_vector=data_set.dependent_variable_vector,
                        features=cleaned_features,
                        source_data_set=data_set)
