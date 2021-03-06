import inspect
import re
from unittest import TestCase
from thread_job import ThreadJob

INHERITANCE_JOB_PATT = re.compile('<class thread_job.ThreadJob.*'
                                  'class job.Job.*>')


class TestJobRefactoring(TestCase):

    def testJobRefactoring_inheritance(self):
        self.assertNotEqual(
            re.search(
                INHERITANCE_JOB_PATT, unicode(
                    inspect.getmro(ThreadJob))), None)
