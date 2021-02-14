# -*- coding: utf-8 -*-

import os

from lintaosp.printer.printer import Printer, PrinterException
from lintaosp.proto.proto import Format, Type


def test_exception():
    exception = PrinterException("exception")
    assert str(exception) == "exception"


def test_printer():
    buf = {
        "aosp": {
            Format.FILENAME: "/path/to/file",
            Format.LINENUM: 1,
            Format.COLNUM: 1,
            Format.ERRORNUM: "strings",
            Format.ERRORDETAILS: "details",
            Format.ERRORTYPE: Type.ERROR,
        }
    }

    printer = Printer()

    name = "printer.json"
    printer.run(data=buf, name=name, append=False)
    assert os.path.isfile(name)
    os.remove(name)

    name = "printer.txt"
    printer.run(data=buf, name=name, append=False)
    assert os.path.isfile(name)
    os.remove(name)

    name = "printer.xlsx"
    printer.run(data=buf, name=name, append=False)
    assert os.path.isfile(name)
    os.remove(name)
