from mako.template import Template
import pdfkit


def test_render():
    mytemplate = Template(filename='/home/kevin/PycharmProjects/BingoCardCreator/src/testing/test.html')
    str = mytemplate.render()
    return str


def test_pdf_create():
    str = test_render()
    pdfkit.from_string(str, 'testing/test.pdf')