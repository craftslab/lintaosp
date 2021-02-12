# -*- coding: utf-8 -*-

from lintaosp.aosp.abstract import AospAbstract
from lintaosp.config.config import Config


def test_aospabstract():
    class AospTest(AospAbstract):
        def __init__(self, config):
            super().__init__(config)

        def _execution(self, _):
            return "_execution"

    config = Config()
    aosp = AospTest(config)

    data = ["PHN0cmluZyBuYW1lPSJsaW50X2Fvc3AiPkxpbnQgQU9TUDwvc3RyaW5nPg=="]

    result = aosp.run(data)
    assert len(result) != 0
