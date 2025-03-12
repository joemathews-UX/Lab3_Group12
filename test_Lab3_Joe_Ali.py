import unittest
from app.Lab3_Joe_Ali import circle_area, trapezium_area, ellipse_area, rhombus_area

class TestShapes(unittest.TestCase):

    def setUp(self):
        print("Setup: Preparing tests...")

    def tearDown(self):
        print("Teardown: Cleaning up after tests...")

    # Circle Tests
    def test_circle_area_valid(self):
        self.assertAlmostEqual(circle_area(5), 78.53981633974483)

    def test_circle_area_zero(self):
        self.assertEqual(circle_area(0), 0.0)

    def test_circle_area_negative(self):
        with self.assertRaises(ValueError):
            circle_area(-3)

    # Trapezium Tests
    def test_trapezium_area_valid(self):
        self.assertEqual(trapezium_area(4, 6, 5), 25.0)

    def test_trapezium_area_zero_height(self):
        self.assertEqual(trapezium_area(4, 6, 0), 0.0)

    # Ellipse Tests
    def test_ellipse_area_valid(self):
        self.assertAlmostEqual(ellipse_area(3, 4), 37.69911184307752)

    def test_ellipse_area_zero_semi_axis(self):
        self.assertEqual(ellipse_area(0, 4), 0.0)

    # Rhombus Tests
    def test_rhombus_area_valid(self):
        self.assertEqual(rhombus_area(6, 8), 24.0)

    def test_rhombus_area_zero_diagonals(self):
        self.assertEqual(rhombus_area(0, 0), 0.0)

    def test_rhombus_area_negative_diagonals(self):
        with self.assertRaises(ValueError):
            rhombus_area(-5, 12)

if __name__ == "__main__":
    unittest.main()