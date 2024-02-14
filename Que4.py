class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def display_info(self):
        print(f"{self.make} {self.model} {self.year}")

    def calculate_depreciation(self,no_of_years):
        self.no_of_years=no_of_years
        if no_of_years >=5:
            print("10%"+" depreciated")
        elif no_of_years >=10 and no_of_years >=5:
            print("20%"+" depreciation")
        elif no_of_years>=20 and no_of_years<=10:
            print("30%"+" depreciation")
c1=Car("xyz",'BMW',2000)
c1.display_info()
c1.calculate_depreciation(5)

