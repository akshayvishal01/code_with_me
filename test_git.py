class Rectangle:
    def __init__(self,length,breadth,unit_cost = 0):
        self.length = length
        self.breadth = breadth
        self.unit_cost = unit_cost

    #Calculate the area of the rectangle
        
    def cal_area(self):
        return self.length*self.breadth
    
    #Calculate the cost

    def unit_per_cost(self):
        area = self.cal_area()
        return area*self.unit_cost
    
#putting the figures in rectangle and cost of each sq meter of the rectangle = 4000
    
r = Rectangle(10,20,18)
print("Area of Rectangle: %s sq units" % (r.cal_area()))
