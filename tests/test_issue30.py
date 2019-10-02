import pickle
import sys

import six
import pytest
pytest.importorskip('twisted')
from twisted.python.failure import Failure  # noqa: F402

from tblib import pickling_support  # noqa: F402


def test_30():
    pickling_support.install()

    try:
        raise ValueError
    except ValueError:
        s = pickle.dumps(sys.exc_info())

    f = None
    try:
        six.reraise(*pickle.loads(s))
    except ValueError:
        f = Failure()

    assert f is not None
