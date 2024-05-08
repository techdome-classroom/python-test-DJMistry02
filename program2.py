# maybe check the indexes in both strings and check for values.. even if one possible true, return true. use dp to keep track of upto which indexes it has been calculated




def decode_message( s: str, p: str) -> bool:
    sLength = len(s)
    pLength = len(p)

    dp = [[[-1] * sLength] for _ in range(pLength)]
    

    return False