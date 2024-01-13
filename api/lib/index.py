def getIxSafe(obj, ix):
    try:
        return str(obj[ix])
    except KeyError:
        return None
