from ._base import DirSyncTestCase
from . import trees

from dirsync import sync


class ErrorsTests(DirSyncTestCase):

    init_trees = (('src', trees.simple), ('dst', trees.simple))

    def test_nonexistent_src(self):
        with self.assertRaises(ValueError):
            sync('srcc', 'dst', 'sync', create=True)

    def test_nonexistent_dest(self):
        with self.assertRaises(ValueError):
            sync('src', 'dstt', 'sync', create=False)
