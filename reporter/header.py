

import datetime
import warnings
import json

def _validate2(author):
    print(author)
    has_first = "first" in author.keys() # checks that the key 'first' 
                                  # belongs to the author dictionnary
    has_last = "last" in author # equivalent
    return has_first and has_last

    



def create_header(authors, city="Paris"):
    """Returns the header string
    
    This function creates a header string with today's date
    and the names of the authors.
    
    Parameters
    ----------
    authors : list of dictionnaries
        Each dict should have at least the keys 
        'first' and 'last'
    city : str, optional, default 'Paris'
        The city from which the report is emitted
        
    Returns
    -------
    header_string : str
        the header string ...
        
    Example
    -------
    >>> authors = [{}, {}]
    >>> res = cre...
    
    """
    
    today = datetime.date.today().strftime('%d/%m/%Y')
    lines = [f"{city}, le {today}", "\n", "### Authors:"]
    for author in authors:
        try:
            first = author["first"]
            #1 / 0  ### This interupts the prorgamm
        except KeyError:
            warnings.warn('Key first not found, please fix input')
            first = 'XX'
        try:
            last = author["last"]
        except KeyError:
            warnings.warn('Key last not found, please fix input')
            last = 'XX'
            
        lines.append(f"- {first} {last}")
    return "\n".join(lines)


def _validate(author):
    #if {"first", "last"}.issubset(author):
    #    return True
    #else:
    
    missing = {"first", "last"}.difference(author)
    if not missing:
        return True
    for miss in missing:
        warnings.warn(f"Key {miss} is missing")
    return False

