test = ('I', 'am', 'a', 'test', 'tuple')
arrTest = 'I am a test tuple'.split()

def oddTuples(aTup):
    return aTup[::2]

print(oddTuples(test))
