def type_detect_verify(bibjson_identifier):
    """
    determine if the provided bibjson identifier has a type of "PMID", by
    inspecting first the "type" parameter, and then by looking at the form
    of the id.  If it is a PMID, then verify that it is a valid one.
    
    Add "type" : "pmid" to the bibjson_identifier object if so
    """
    pass

def canonicalise(record):
    """
    create a canonical form of the identifier in the record['identifier'] field
    and insert it into the record['identifier']['canonical'].  This is of the form pmid:12345678
    """
    pass
    
def provider_resolver(record):
    """
    Take a pubmed id (if that is the type) and obtain a reference to the base
    URL of the resource that it links to.
    """
    pass
