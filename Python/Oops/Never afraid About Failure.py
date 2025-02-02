from SAS import Car


class Electric_car(Car):
    def __init__(self, brand, model, battery_size, fuel_type):
        super().__init__(brand, model, fuel_type)

        self.battery_size = battery_size


car1 = Electric_car("Tesla", "Model X", "900 Kwm", "Electric_Charge")
print(car1.full_name)

print(car1.fuel_type)

from SAS import a1

print(a1)

from SAS import count

print(count)

car1.model = "AAA"
print(car1.model)


class Battery():
    def battery_info(self):
        return "This is Latest Generation Battery 7898kmb"


class Engine():
    def Engine_info(self):
        return f"This is Latest Engine of Redox 9000 Horsepower Engine With 78Km Milage"


class Electric_Car_2(Engine, Battery, Car):
    pass


My_New_Tesla = Electric_Car_2("Tesla", "Model S", "")
print(My_New_Tesla.Engine_info())
print(My_New_Tesla.battery_info())


class Processor:
    def __init__(self, name, speed, cores, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.speed = speed
        self.cores = cores


class Graphic_Card:
    def __init__(self, Model, memory, **kwargs):
        super().__init__(**kwargs)
        self.Graphic_Model = Model
        self.memory = memory


class Laptop:
    def __init__(self, name, model, manufacturer, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.model = model
        self.manufacturer = manufacturer


class Gaming_Laptop(Laptop, Processor, Graphic_Card):
    def __init__(self, model, manufacturer, brand, speed, cores, memory, name,Graphic_Model):
        super().__init__(model=model, manufacturer=manufacturer,  brand=brand, speed=speed,
                         cores=cores, memory=memory,Graphic_of_model = Graphic_Model)

    def show_specifications(self):
        return {"Model":{self.model},"brand":{self.}}