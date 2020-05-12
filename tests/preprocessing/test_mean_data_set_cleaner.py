from unittest import TestCase

from data_sets import SECTION_2_DATA_PREPROCESSING
from data_sets.data_set_reader import read_data_set
from preprocessing.feature_cleaners import fill_in_missing_values_using_mean


class TestDataSetCleaner(TestCase):
    def test_when_features_are_missing_numeric_values_then_mean_is_used_to_fill_in_missing_feature_values(self):
        data_set = read_data_set(SECTION_2_DATA_PREPROCESSING)

        clean_data_set = fill_in_missing_values_using_mean(data_set, clean_start_index=1, clean_end_index=3)
        self.assertEqual(54000, clean_data_set.features[2][2])
        self.assertAlmostEqual(38.77, clean_data_set.features[6][1], 1)
