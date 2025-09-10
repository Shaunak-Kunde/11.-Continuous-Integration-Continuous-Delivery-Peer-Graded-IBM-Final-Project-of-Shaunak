import app

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(app.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(app.subtract(5, 3), 2)

if __name__ == "__main__":
    unittest.main()
