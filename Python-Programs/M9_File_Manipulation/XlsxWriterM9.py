# win install
# pip install --user XlsxWriter

import xlsxwriter
# create workbook
outWorkbook = xlsxwriter.Workbook("grades.xlsx")
outSheet = outWorkbook.add_worksheet()

# column titles
outSheet.write("A1", "Names")
outSheet.write("B1", "Asgn 1")
outSheet.write("C1", "Asgn 2")
outSheet.write("D1", "Asgn 3")
outSheet.write("E1", "Avg")

# function returning names from ids
def IdToName(ID):
    if (ID == 1):
        return "Matt"
    elif (ID == 2):
        return "Mark"
    elif (ID == 3):
        return "Luke"
        
# content
grades = {1:[67,56,75],
          2:[70,67,52],
          3:[82,98,87]}

# content to cells
for i in range(1, 4):
    outSheet.write(i, 0, IdToName(i))
    outSheet.write(1, i, grades[1][i-1])
    outSheet.write(2, i, grades[2][i-1])
    outSheet.write(3, i, grades[3][i-1])

# calculate first students average
for j in range (0, 3):
    outSheet.write(j+1, 4, sum(grades[j+1])/float(3))

# close workbook
outWorkbook.close()
