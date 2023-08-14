import unittest

class TestHelloWorldDAG(unittest.TestCase):
    
    def test_print_hello(self):
        from dags.hello_world_dag import print_hello
        result = print_hello()
        self.assertEqual(result, "Hello world!")

if __name__ == '__main__':
    unittest.main()