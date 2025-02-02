class Car:
    all = []
    Car_count = 0
    def __init__(self,brand,model,fuel_type):
        self.brand = brand
        self.__model = model
        self.fuel_type = fuel_type

        Car.all.append(self)
        Car.Car_count += 1

    def __repr__(self):
        return f"{self.__class__.__name__},({self.brand}),({self.__model}),({self.fuel_type})"

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self,value):
            if len(value) > 10:
                print("Length of Value is Too Long!")
            else:
                self.__model = value

    def full_name(self):
        return f"{self.brand} {self.__model}"


Car1 = Car("Tesla","Model_X","Petrol")

my_new_car = Car("Tata","Safari","Diesel")

a1 = (Car.all)
print(a1)

count = Car.Car_count


for car in Car.all:
    if car.brand == "Tesla" and isinstance(car,Car):
        print(f"Tesla Found in Car")
        break
    else:
        print("No Car Found")
