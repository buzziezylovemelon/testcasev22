def alternatingCharacters(s):
    d=0
    sl=list(s)
    for i in range(0, len(sl)-1):
        if sl[i]==sl[i+1]:
            d+=1
    return d

def test_alternatingCharacters():
    assert alternatingCharacters("AAAA") == 3   
    assert alternatingCharacters("BBBBB") == 4
    assert alternatingCharacters("CCDD") == 2
    assert alternatingCharacters("XYXYXXY") == 1
    assert alternatingCharacters("Z") == 0
    assert alternatingCharacters("") == 0
    assert alternatingCharacters("XY" * 500) == 0
    assert alternatingCharacters("M" * 1000) == 999

test_alternatingCharacters()
print("All passed")