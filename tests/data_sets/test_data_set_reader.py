from unittest import TestCase

from data_sets import SECTION_2_DATA_PREPROCESSING
from data_sets.data_set_reader import read_data_set


class TestDataSetReader(TestCase):
    def test_when_csv_data_set_is_read_then_features_include_non_dependent_data(self):
        data_set = read_data_set(SECTION_2_DATA_PREPROCESSING)

        self.assertEqual(10, len(data_set.features))
        self.assertEqual(3, len(data_set.features[0]))

    def test_when_csv_data_set_is_read_then_dependent_variable_vector_is_the_last_column_of_data(self):
        data_set = read_data_set(SECTION_2_DATA_PREPROCESSING)

        self.assertEqual(10, len(data_set.dependent_variable_vector))
        self.assertEqual('No', data_set.dependent_variable_vector[0])
