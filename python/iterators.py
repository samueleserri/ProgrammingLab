class My_Range:
    def __init__(self, start, end):
        self.current=start
        self.end=end
    def __iter__(self):
        return self
    def __next__(self):
        if self.current>=self.end:
            raise StopIteration
        current = self.current
        self.current=self.current + 1
        return current

def test_iter():
    myiter=My_Range(1,10)
    result = []
    for item in myiter:
        result.append(item)
    if result != [1,2,3,4,5,6,7,8,9]:
        raise Exception('Errore nella classe My_Range')

test_iter()