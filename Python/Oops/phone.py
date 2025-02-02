from item import Item
class Phone(Item):
    def __init__(self,name,price:int,quantity = 0,broken_phone = 0): # The Action Will Done On Every Instances
        # Call To Super Method to Have Access of all Attributes / Methods
        super().__init__(
            name,price,quantity
        )
        self.broken_phone = broken_phone
        assert broken_phone >= 0,f" Broken_Phone quantity be greater Than Zero"


phone1 = Phone("TrialPhone1",500,5)
phone2 = Phone("TrialPhone2",700,9)
