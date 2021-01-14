import salt.modules.win_disk as win_disk
from tests.support.mixins import LoaderModuleMockMixin
from tests.support.unit import TestCase


class MockKernel32:
    """
    Mock windll class
    """

    def __init__(self):
        pass

    @staticmethod
    def GetLogicalDrives():
        """
        Mock GetLogicalDrives method to return C, D, and F.
        """
        return int("101100", 2)


class MockWindll:
    """
    Mock windll class
    """

    def __init__(self):
        self.kernel32 = MockKernel32()


class MockCtypes:
    """
    Mock ctypes class
    """

    def __init__(self):
        self.windll = MockWindll()


class WinDiskTestCase(TestCase, LoaderModuleMockMixin):
    """
    Test cases for salt.modules.win_disk
    """

    def setup_loader_modules(self):
        return {win_disk: {"ctypes": MockCtypes()}}

    def test_letters(self):
        self.assertListEqual(win_disk.letters(), ["C", "D", "F"])

    def test_usage(self):
        """
        Test if it return usage information for volumes mounted on this minion.
        """
        self.assertDictEqual(
            win_disk.usage(),
            {
                "C:\\": {
                    "available": None,
                    "1K-blocks": None,
                    "used": None,
                    "capacity": None,
                    "filesystem": "C:\\",
                },
                "D:\\": {
                    "available": None,
                    "1K-blocks": None,
                    "used": None,
                    "capacity": None,
                    "filesystem": "D:\\",
                },
                "F:\\": {
                    "available": None,
                    "1K-blocks": None,
                    "used": None,
                    "capacity": None,
                    "filesystem": "F:\\",
                },
            },
        )
