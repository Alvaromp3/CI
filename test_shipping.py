import unittest
from shipping import calculate_shipping


class TestShipping(unittest.TestCase):

    # validamos minimo 4 casos
    def test_weight_zero_invalid(self):
        with self.assertRaises(ValueError):
            calculate_shipping(0, False, "US")

    def test_weight_negative_invalid(self):
        with self.assertRaises(ValueError):
            calculate_shipping(-0.5, False, "US")

    def test_weight_over_50_invalid(self):
        with self.assertRaises(ValueError):
            calculate_shipping(50.0001, False, "US")

    def test_destination_invalid(self):
        with self.assertRaises(ValueError):
            calculate_shipping(2.0, False, "FR")

    def test_weight_50_valid(self):
        # limite superior
        self.assertEqual(calculate_shipping(50, False, "US"), 17.00)

    # minimo 5 casos por recargo de peso
    def test_weight_exact_1_0(self):
        self.assertEqual(calculate_shipping(1.0, False, "US"), 5.00)

    def test_weight_just_above_1_0(self):
        self.assertEqual(calculate_shipping(1.01, False, "US"), 8.00)

    def test_weight_exact_5_0(self):
        self.assertEqual(calculate_shipping(5.0, False, "CA"), 11.00)

    def test_weight_exact_20_0(self):
        self.assertEqual(calculate_shipping(20.0, False, "MX"), 17.00)

    def test_weight_just_above_20_0(self):
        self.assertEqual(calculate_shipping(20.01, False, "MX"), 22.00)

    # minimo 2 casos por express vs standard
    def test_express_vs_standard_us(self):
        self.assertEqual(calculate_shipping(2.0, False, "US"), 8.00)
        self.assertEqual(calculate_shipping(2.0, True, "US"), 12.80)

    def test_express_vs_standard_ca(self):
        self.assertEqual(calculate_shipping(6.0, False, "CA"), 15.00)
        self.assertEqual(calculate_shipping(6.0, True, "CA"), 24.00)

    def test_rounding_format(self):
        result = calculate_shipping(2.0, True, "US")
        self.assertEqual(result, 12.80)
        self.assertEqual(f"{result:.2f}", "12.80")


if __name__ == "__main__":
    unittest.main()
