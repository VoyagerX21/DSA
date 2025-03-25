class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = [[0 for _ in range(26)] for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        self.sheet[ord(cell[0])-65][int(cell[1:])-1] = value

    def resetCell(self, cell: str) -> None:
        self.sheet[ord(cell[0])-65][int(cell[1:])-1] = 0

    def getValue(self, formula: str) -> int:
        first, second = formula.split('+')
        first = first[1:]
        print(first, second)
        if first.isdigit():
            if second.isdigit():
                return int(first)+int(second)
            else:
                return int(first)+self.sheet[ord(second[0])-65][int(second[1:])-1]
        elif second.isdigit():
            return self.sheet[ord(first[0])-65][int(first[1:])-1]+int(second)
        else:
            return self.sheet[ord(first[0])-65][int(first[1:])-1]+self.sheet[ord(second[0])-65][int(second[1:])-1]



# Your Spreadsheet object will be instantiated and called as such:
obj = Spreadsheet(458)
# obj.setCell(cell,value)
# obj.resetCell(cell)
param_3 = obj.getValue("=O126+10272")