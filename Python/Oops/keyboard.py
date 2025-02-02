from item import Item

class keyboard(Item):
    def __init__(self,name,price:int,quantity = 0,broken_phone = 0): # The Action Will Done On Every Instances
        # Call To Super Method to Have Access of all Attributes / Methods
        super().__init__(
            name,price,quantity
        )
