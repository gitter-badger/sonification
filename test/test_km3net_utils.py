from unittest import TestCase
from hypothesis import given
from hypothesis.strategies import integers
import sonification.km3net_utils


class TestPmt_id_to_storey(TestCase):
    @given(k=integers(min_value=0))
    def test_pmt_id_to_storey(self, k):
        self.assertTrue(type(sonification.km3net_utils.pmt_id_to_storey(k)) is int)
