class Kilometer:
    def __init__(self, kilometers=0):
        self.kilometers=kilometers
    def to_meters(self):
        return (kilometers*1000)
    def get_kilometers(self):
        print('Getting Value')
        return self._kilometers
    def set_kilometers(self,value):
        if value>20:
            raise ValueError("Kilometers greater than 20km")
    print("setting value")
    self._kilometers=value
kilometers=property(get_kilometers,set_kilometers)
k=Kilometer(10)
