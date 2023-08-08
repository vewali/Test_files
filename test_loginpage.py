import xlrd
import pytest
path = r"C:\Users\veere\PycharmProjects\pythonProject\my_sheet1.xlsx"

work_book = xlrd.open_workbook(path)
work_sheet = work_book.sheet_by_name("Cred1")
rows = work_sheet.get_rows()
header = next(rows)

data = [(row[0].value, row[1].value) for row in rows]
#data1 = [('user1', 'pwd1'), ('user1', 'pwd2'), ('user2', 'pwd1'), ('user2', 'pwd2')]
print(data)
@pytest.mark.parametrize("username, password", data)
def test_credentials(username,password):
     assert username == "user1", "invalid user"
     assert password == "pwd1", "invalid password"
