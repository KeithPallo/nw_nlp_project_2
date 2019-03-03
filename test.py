class Ingredients(??????????):
	# ...
	Name = ""
	Qty = 0
	Measure = 0
	Details = ""
	PrepStyle = ""
	Methods = []
	Toolset = []
	PrefComb = []

	def __init__(self,
				 Name="",
				 Qty=0,
				 Measure=0,
				 Details="",
				 PrepStyle="",
				 Methods=[],
				 Toolset=[],
				 PrefComb=[],
				 ):
		self.Name = Name
		self.Qty = Qty,
		self.Measure = Measure
		self.Details = Details
		self.PrepStyle = PrepStyle
		self.Methods = Methods
		self.Toolset = Toolset
		self.PrefComb = PrefComb

	def printIngredient(self):
		# print()
		print("Name: ", self.Name)
		if self.Qty:
			print("Name: ", self.Qty)

# meat_options
meat_options = []
meat_options = []