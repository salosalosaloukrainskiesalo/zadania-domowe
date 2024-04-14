import string
def reverse(text: str) -> str:
    """
    Return the 'text' backwards.

    Parameters
    ----------
    text: str
        The input string

    Returns
    -------
    str
        The text written backwards.
    """
    pass
    return(text[::-1])

def first_to_upper(text: str) -> str:
    """
    Changes each first character of the word to uppercase.

    Parameters
    ----------
    text: str
        The input string

    Returns
    -------
    str
        The modified text
    """
    a = ""

    b = True
    for c in text:
        if c in string.whitespace or c in string.punctuation:
            a+=c
            b = True
            continue
        if c in string.digits:
            a+=c
            b = False
            continue
        if c.islower() and b:
            a+=c.upper()
            b = False
            continue

        a+=c
        b=False

    return a

def count_vowels(text: str) -> int:
    """
    Counts number of vovels in the text.

    Parameters
    ----------
    text: str
        The input string

    Returns
    -------
    inp
        Number of vowels.
    """
    l = list(text)
    r=0
    for i in l:
        if(i=='A' or i=='a' or i=='o' or i=='O' or i=='E' or i=='e' or i=='Y' or i=='y' or i=='I' or i=='i' or i=='U' or i=='u' or i=='ó' or i=='Ó' or i=='ą' or i=='Ą' or i=='ę' or i=='Ę'):
             r = r + 1
    return (r)


def sum_digits(text: str) -> int:
    """
    Finds all digitts in the text and returns its sum.

    Parameters
    ----------
    text: str
        The input string

    Returns
    -------
    int
        Sum of all digits in the text.
    """
    a=list(text)
    sum = 0
    for i in a:
        if i == '1' or i =='2' or i =='3' or i =='4' or i =='5' or i =='6' or i =='7' or i =='8' or i =='9' or i =='0':
            sum+=int(i)
    return sum


def search_substr(text: str, sub: str) -> int:
    """
    Search for sub(string) in the text. Returns the position or None.

    Parameters
    ----------
    text: str
        The input string

    Returns
    -------
    int or None
        Position of the sub(string) or None.
    """
    a = len(text)
    b = len(sub)
    for i in range(a - b + 1):
        if text[i: i + b] == sub:
            return(i)
