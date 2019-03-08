import re


def normalize(st):
    """

    :param st:
    :return:
    """
    # SEPARATOR_RE = re.compile(r'^([\d\s*[\d\.,/]*)\s*(.+)')
    return re.sub(r'\s+', ' ', re.compile(r'^([\d\s*[\d\.,/]*)\s*(.+)').sub('\g<1> \g<2>', st)).strip()


def escape_re_string(text):
    """

    :param text:
    :return:
    """
    text = text.replace('.', '\.')
    return re.sub(r'\s+', ' ', text)
