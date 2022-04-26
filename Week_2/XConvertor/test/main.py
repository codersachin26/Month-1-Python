import logging

import unittest
from Week_2.XConvertor.test.test_xconvertor import TestResults, TestXConvertor




# logger configuration
LOG_FILE_NAME = "test_xconvertor.log"
LEVEL = logging.DEBUG
FORMAT = '[%(asctime)s] : %(levelname)s -> %(message)s'
logging.basicConfig(filename=LOG_FILE_NAME,
                    level=LEVEL,
                    format=FORMAT,
                    filemode='w'
                    )

suite = unittest.TestSuite(
    unittest.TestLoader().loadTestsFromTestCase(TestXConvertor)

)
results = TestResults()

self = suite.run(results)



