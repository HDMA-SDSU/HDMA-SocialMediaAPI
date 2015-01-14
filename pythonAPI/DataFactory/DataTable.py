'''
THIS IS A WORK IN PROGRESS!!!

Example:

from excelUtils import DataTableFactory
table = DataTableFactory.getDataTable("c:\\Locations.xlsx")

table.getRowsAsList()

#or
table = DataTableFactory.getDataTable(open("c:\\Locations.csv"))

table.getRowsAsList()
'''



class DataTable(object):

	def __init__(self, colNames, rows):
		
		if not colNames:
			raise Exception("Error: Must pass column names to constructor.")
		
		if not rows:
			raise Exception("Error: Must rows to constructor.")
		
		self._colNames = colNames
		self._rows = rows
		
		
	def getColumnNames(self):
		return self._colNames
		

	def getRowsAsList(self):
		return self._rows
	
	
	def getRowsAsJSON(self):		
		results = []
		
		for rowIndx in xrange(len(self._rows)):
			doc = {}
		
			for colIndx, colName in enumerate(self._colNames):
				formattedName = colName.strip().replace(" ", "_")
				doc[formattedName] = self._rows[rowIndx][colIndx]
				
			results.append(doc)
			
		return results	


class DataTableFactory:
	EXCEL_EXTENSIONS = ('XLSX', 'XLS')
	CSV_EXTENSIONS = ('TXT', 'CSV')
	VALID_EXTENSIONS = EXCEL_EXTENSIONS + CSV_EXTENSIONS

	
	@staticmethod
	def getDataTable(fileName=None, fileStream=None, opts={}):
		'''
			Parses CSV or Excel data and returns a DataTable object.
			Note that a file name must be passed.  If no fileStream is passed,
			it will open a file using the fileName parameter.
		'''
		
		if not fileName:
			raise Exception("Error: Must pass a file name.")
		
		if fileName and not fileStream:
			try: 
				fileStream = open(fileName, "rb")
			except Exception, e:
				raise e
		
		ext = fileName.split('.')[-1].upper()
				
		if ext not in DataTableFactory.VALID_EXTENSIONS:
			raise Exception("Error: File must be one of the following types: %s" % ', '.join(DataTableFactory.VALID_EXTENSIONS))
		
		colNames = []
		rows = []
			
		if ext in DataTableFactory.EXCEL_EXTENSIONS:
			from xlrd import open_workbook
			
			output = fileStream.read()
			workbook = open_workbook(file_contents=output)
			sheet = workbook.sheet_by_index(0)
	
			colNames = [ sheet.cell_value(0, col).lower() for col in xrange(sheet.ncols) ]
			
			for rowIndx in xrange(1, sheet.nrows):
				rows.append([ sheet.cell_value(rowIndx, colIndx) for colIndx in xrange(len(colNames)) ])
					
		else:
			import csv
	
			delimiter = opts.get('delimiter', ',')
			quotechar = opts.get('quotechar', '"')
	
			reader = csv.reader(fileStream, delimiter=delimiter, quotechar=quotechar)

			data = [ row for row in reader ]

			colNames = [col.lower().strip() for col in data[0]]
			rows = [ row for row in data[1:] ]			
		
		return DataTable(colNames, rows)
		