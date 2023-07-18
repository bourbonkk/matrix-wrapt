from __future__ import print_function

import unittest

import pickle

import matrix_wrapt

class CustomObjectProxy(matrix_wrapt.ObjectProxy):

    def __reduce_ex__(self, proto):
        return (list, (self.__wrapped__,))

class TestObjectPickle(unittest.TestCase):

    def test_pickle(self):
        proxy = matrix_wrapt.ObjectProxy([1])

        with self.assertRaises(NotImplementedError) as context:
            data = pickle.dumps(proxy)

        self.assertTrue(str(context.exception) ==
                'object proxy must define __reduce_ex__()')

    def test_pickle_proxy(self):
        proxy1 = CustomObjectProxy([1])
        pickled = pickle.dumps(proxy1)
        restored = pickle.loads(pickled)

        self.assertEqual(proxy1.__wrapped__, restored)

if __name__ == '__main__':
    unittest.main()
