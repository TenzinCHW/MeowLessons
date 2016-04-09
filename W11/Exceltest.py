from datetime import date,time,datetime
from decimal import Decimal
from xlwt import Workbook,Style

wb = Workbook()
ws = wb.add_sheet('Type examples')
ws.row(0).write(0,u'\xa3')
ws.row(0).write(1,'Text')
ws.row(1).write(0,3.1415)
ws.row(1).write(1,15)
ws.row(1).write(2,265L)
ws.row(1).write(3,Decimal('3.65'))
ws.row(2).set_cell_number(0,3.1415)
ws.row(2).set_cell_number(1,15)
ws.row(2).set_cell_number(2,265L)
ws.row(2).set_cell_number(3,Decimal('3.65'))
ws.row(3).write(0,date(2009,3,18))
ws.row(3).write(1,datetime(2009,3,18,17,0,1))
ws.row(3).write(2,time(17,1))
ws.row(4).set_cell_date(0,date(2009,3,18))
ws.row(4).set_cell_date(1,datetime(2009,3,18,17,0,1))
ws.row(4).set_cell_date(2,time(17,1))
ws.row(5).write(0,False)
ws.row(5).write(1,True)
ws.row(6).set_cell_boolean(0,False)
ws.row(6).set_cell_boolean(1,True)
ws.row(7).set_cell_error(0,0x17)
ws.row(7).set_cell_error(1,'#NULL!')
ws.row(8).write(0,'',Style.easyxf('pattern: pattern solid, fore_colour green;'))
ws.row(8).write(1,None,Style.easyxf('pattern: pattern solid, fore_colour blue;'))
ws.row(9).set_cell_blank(0,Style.easyxf('pattern: pattern solid, fore_colour yellow;'))
ws.row(10).set_cell_mulblanks(5,10,Style.easyxf('pattern: pattern solid, fore_colour red;'))



# book = Workbook()
# sheet1 = book.add_sheet('Sheet 1',cell_overwrite_ok=True)
# sheet1.write(0,0,'original')
# sheet = book.get_sheet(0)
# sheet.write(0,0,'new')
# sheet2 = book.add_sheet('Sheet 2')
# sheet2.write(0,0,'original')
# sheet2.write(0,0,'new')

# book = Workbook()
# sheet1 = book.add_sheet('meow')
# book.add_sheet('Sheet 2')
# sheet1.write(0,0,'A1')
# sheet1.write(0,1,'B1')
# row1 = sheet1.row(1)
# row1.write(0,'A2')
# row1.write(1,'B2')
# sheet1.col(0).width = 10000
# sheet2 = book.get_sheet(1)
# sheet2.row(0).write(0,'Sheet 2 A1')
# sheet2.row(0).write(1,'Sheet 2 B1')
# sheet2.flush_row_data()
# sheet2.write(1,0,'Sheet 2 A3')
# sheet2.col(0).width = 5000
# sheet2.col(0).hidden = True


wb.save('C:\Users\HanWei\Dropbox\SUTDNotes\SUTDTerm3\DigitalWorld\W11\meow.xls')