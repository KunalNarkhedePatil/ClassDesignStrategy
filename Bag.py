import sys
class ProductDimension:
    """
        This class implement the Dimension of Bag
        @__init__(self, length: float, width: float, height: float, weight_in_gm: float):
        Constructor
        @get_length(self) 
            getter of attribute length
        @get_width(self)
            getter of attribute width
        @get_height(self)
            getter of attribute height
        @get_weight_in_gm(self)
            getter of attribute weight_in_gm
        ------------------------------------- 
        @set_length(self):
            setter of attribute length
        @set_width(self):
            setter of attribute width
        @set_height(self):
            setter of attribute height
        @set_weight_in_gm(self):
            setter of attribute weight_in_gm  
    """
    
    def __init__(
             self,
             length:float,
             width:float,
             height:float,
             weight_in_gm:float
        ):
        
        """
            Constructor of ProductDimension class:
            @__init__(self, length: float, width: float, height: float, weight_in_gm: float):
            
            @self:newly created class object of ProductDimension
            @length:Client specified value for attribute length
            @width:Client specified value for attribute width
            @height:Client specified value for attribute height
            @weight_in_gm:Client specified value for attribute weight_in_gm
        
        """
        if type(length)!=float:
            raise TypeError("Bad type:length")
        if type(width)!=float:
            raise TypeError("Bad type:width")
        if type(height)!=float:
            raise TypeError("Bad type:height")
        if type(weight_in_gm)!=float:
            raise TypeError("Bad type:weight_in_gm")
        if length<=0.0:
            raise ValueError("Length must be positive")
        if width<=0.0:
            raise ValueError("Width must be positive")
        if height<=0.0:
            raise ValueError("Height must be positive")
        if weight_in_gm<=0.0:
            raise ValueError("weight_in_gm must be positive")
        
        self.length=length
        self.width=width
        self.height=height
        self.weight_in_gm=weight_in_gm
        
    #getter method   
        
    def get_length(self) -> float:
        """ 
            Returns the length attribute of the calling object 
        """
        return self.length
    
    def get_width(self) -> float:
        """ 
            Returns the width attribute of the calling object 
        """
        return self.width
    
    def get_height(self) -> float:
        """ 
            Returns the height attribute of the calling object 
        """
        return self.height
    
    def get_weight_in_gm(self) -> float:
        """ 
            Returns the weight_in_gm attribute of the calling object 
        """
        return self.weight_in_gm
   
    #setter method
    
    def set_length(self,new_length:float):
        """
            Sets the length attribute of the calling object to @new_length
            Before setting, TypeCheck and ValueCheck is performed.
        """
        if type(new_length)!=float:
            raise TypeError("new_length must be an float")
        if new_length <= 0.0:
            raise TypeError("new_length must be positive")
        self.length=new_length
        
    def set_width(self,new_width:float):
        """
            Sets the width attribute of the calling object to @new_width
            Before setting, TypeCheck and ValueCheck is performed.
        """
        if type(new_width)!=float:
            raise TypeError("new_width must be an float")
        if new_width <= 0.0:
            raise ValueError("new_width must be positive")
        self.width=new_width
        
    def set_height(self,new_height:float):
        """
            Sets the height attribute of the calling object to @new_height
            Before setting, TypeCheck and ValueCheck is performed.
        """
        if type(new_height)!=float:
            raise TypeError("new_height must be an float")
        if new_height <= 0.0 :
            raise ValueError("new_height must be positive")
        self.height=new_height 
        
    def set_weight_in_gm(self,new_weight_in_gm:float):
        """
            Sets the weight_in_gm attribute of the calling object to @new_weight_in_gm
            Before setting, TypeCheck and ValueCheck is performed.
        """
        if type(new_weight_in_gm)!=float:
            raise TypeError("new_weight_in_gm must be an float")
        if new_weight_in_gm <= 0.0:
            raise ValueError("new_weight_in_gm must be positive")
        self.weight_in_gm=new_weight_in_gm
         
class Bag:
    def __init__(self,
                bag_colour:str,
                bag_model_number:str,
                bag_prod_dimensions:ProductDimension,
                bag_primary_material:str,
                bag_capacity:str,
                bag_volume_capacity_in_lt:int,
                bag_warranty_desc:str,
                bag_shape:str,
                bag_manufacturer:str,
                bag_ASIN:str,
                bag_country_of_origin:str,
                bag_cust_reviews:float,
                bag_best_seller_rank:str,
                bag_date_first_available:str,
                bag_generic_name:str
                ):
            
            if type(bag_colour)!=str:
                raise TypeError("bag_colour must be in str")
            if type(bag_model_number)!=str:
                raise TypeError("bag_model_number must be in str")
            if type(bag_prod_dimensions)!=ProductDimension:
                raise TypeError("bag_prod_dimensions must be in str")
            if type(bag_primary_material)!=str:
                raise TypeError("bag_primary_material must be in str")
            if type(bag_capacity)!=str:
                raise TypeError("bag_capacity must be in str")
            if type(bag_volume_capacity_in_lt)!=int:
                raise TypeError("bag_volume_capacity_in_lt must be in str")
            if bag_volume_capacity_in_lt<=0:
                raise ValueError("bag_volume_capacity_in_lt must be positive")
            if type(bag_warranty_desc)!=str:
                raise TypeError("bag_warranty_desc must be in str")
            if type(bag_shape)!=str:
                raise TypeError("bag_shape must be in str")
            if type(bag_manufacturer)!=str:
                raise TypeError("bag_manufacturer must be in str")
            if type(bag_ASIN)!=str:
                raise TypeError("bag_ASIN must be in str")
            if type(bag_country_of_origin)!=str:
                raise TypeError("bag_country_of_origin must be in str")
            if type(bag_cust_reviews)!=float:
                raise TypeError("bag_cust_reviews must be in float")
            if bag_cust_reviews<=0.0:
                raise ValueError("bag_cust_reviews must be in positve")
            if type(bag_best_seller_rank)!=str:
                raise TypeError("bag_best_seller_rank must be in str")
            if type(bag_date_first_available)!=str:
                raise TypeError("bag_date_first_available must be in str")
            if type(bag_generic_name)!=str:
                raise TypeError("bag_generic_name must be inn str")
            
            
            self.bag_colour=bag_colour
            self.bag_model_number=bag_model_number
            self.bag_prod_dimensions=bag_prod_dimensions
            self.bag_primary_material=bag_primary_material
            self.bag_capacity=bag_capacity
            self.bag_volume_capacity_in_lt=bag_volume_capacity_in_lt
            self.bag_warranty_desc=bag_warranty_desc
            self.bag_shape=bag_shape
            self.bag_manufacturer=bag_manufacturer
            self.bag_ASIN=bag_ASIN
            self.bag_country_of_origin=bag_country_of_origin
            self.bag_cust_reviews=bag_cust_reviews
            self.bag_best_seller_rank=bag_best_seller_rank
            self.bag_date_first_available=bag_date_first_available
            self.bag_generic_name=bag_generic_name
            
    #Getter
          
    def get_bag_colour(self)->str:
        """ 
            Returns the bag_colour attribute of the calling object 
        """
        return self.bag_colour
    
    def get_bag_model_number(self)->str:
        """ 
            Returns the bag_model_number attribute of the calling object 
        """
        return self.bag_model_number
    
    def get_bag_prod_dimensions(self)->ProductDimension:
        """ 
            Returns the bag_prod_dimensions attribute of the calling object 
        """
        return self.bag_prod_dimensions
    
    def get_bag_primary_material(self)->str:
        """ 
            Returns the bag_primary_material attribute of the calling object 
        """
        return self.bag_primary_material
    
    def get_bag_capacity(self)->str:
        """ 
            Returns the bag_capacity attribute of the calling object 
        """
        return self.bag_capacity
    
    def get_bag_volume_capacity_in_lt(self)->int:
        """ 
            Returns the bag_volume_capacity_in_lt attribute of the calling object 
        """
        return self.bag_volume_capacity_in_lt
    
    def get_bag_warranty_desc(self)->str:
        """ 
            Returns the bag_warranty_desc attribute of the calling object 
        """
        return self.bag_warranty_desc
    
    def get_bag_shape(self)->str:
        """ 
            Returns the bag_shape attribute of the calling object 
        """
        return self.bag_shape
    
    def get_bag_manufacturer(self)->str:
        """ 
            Returns the bag_manufacturer attribute of the calling object 
        """
        return self.bag_manufacturer
    
    def get_bag_ASIN(self)->str:
        """ 
            Returns the bag_ASIN attribute of the calling object 
        """
        return self.bag_ASIN
    
    def get_bag_country_of_origin(self)->str:
        """ 
            Returns the bag_country_of_origin attribute of the calling object 
        """
        return self.bag_country_of_origin
    
    def get_bag_cust_reviews(self)->float:
        """ 
            Returns the bag_cust_reviews attribute of the calling object 
        """
        return self.bag_cust_reviews
    
    def get_bag_best_seller_rank(self)->str:
        """ 
            Returns the bag_best_seller_rank attribute of the calling object 
        """
        return self.bag_best_seller_rank
    
    def get_bag_date_first_available(self)->str:
        """ 
            Returns the bag_date_first_available attribute of the calling object 
        """
        return self.bag_date_first_available
    
    def get_bag_generic_name(self)->str:
        """ 
            Returns the bag_generic_name attribute of the calling object 
        """
        return self.bag_generic_name
    
    
    #Setter Method
    
    def set_bag_colour(self,new_bag_colour)->None:
        """
            Sets the bag_colour attribute of the calling object to @new_bag_colour
            Before setting, TypeCheck is performed and this function returns nothing
        """
        if type(new_bag_colour)!=str:
            raise TypeError("new_bag_colour must be in str")
        self.bag_colour=new_bag_colour
        
    def set_bag_model_number(self,new_bag_model_number)->str:
        """
            Sets the bag_model_number attribute of the calling object to @new_bag_model_number
            Before setting, TypeCheck is performed and this function returns nothing
        """
        if type(new_bag_model_number)!=str:
            raise TypeError("new_bag_model_number must be in str")
        self.bag_model_number=new_bag_model_number
        
    def set_bag_prod_dimensions(self,new_bag_prod_dimensions)->None:
        """
            Sets the bag_prod_dimensions attribute of the calling object to @new_bag_prod_dimensions
            Before setting, TypeCheck is performed and this function returns nothing
        """
        if type(new_bag_prod_dimensions)!=ProductDimension:
            raise TypeError("new_bag_prod_dimensions must be in ProductDimension")
        self.bag_prod_dimensions=new_bag_prod_dimensions
        
    def set_bag_primary_material(self,new_bag_primary_material)->None:
        """
            Sets the bag_primary_material attribute of the calling object to @new_bag_primary_material
            Before setting, TypeCheck is performed and this function returns nothing
        """
        if type(new_bag_primary_material)!=str:
            raise TypeError("new_bag_primary_material must be in str")
        self.bag_primary_material=new_bag_primary_material
        
    def set_bag_capacity(self,new_bag_capacity):
        """
            Sets the bag_capacity attribute of the calling object to @new_bag_capacity
            Before setting, TypeCheck is performed and this function returns nothing
        """
        if type(new_bag_capacity)!=str:
            raise TypeError("new_bag_capacity must be in str")
        self.bag_capacity=new_bag_capacity
        
    def set_bag_volume_capacity_in_lt(self,new_bag_volume_capacity_in_lt)->None:
        """
            Sets the bag_volume_capacity_in_lt attribute of the calling object to @new_bag_volume_capacity_in_lt
            Before setting, TypeCheck and ValueCheck is performed.and this 
            function returns nothing
        """
        if type(new_bag_volume_capacity_in_lt)!=int:
            raise TypeError("new_bag_volume_capacity_in_lt must be in int")
        if new_bag_volume_capacity_in_lt<=0:
            raise  ValueError("new_bag_volume_capacity_in_lt must be positive")
        self.bag_volume_capacity_in_lt=new_bag_volume_capacity_in_lt
        
    def set_bag_warranty_desc(self,new_bag_warranty_desc)->str:
        """
            Sets the bag_warranty_desc attribute of the calling object to @new_bag_warranty_desc
            Before setting, TypeCheck is performed and this function returns nothing
        """
        if type(new_bag_warranty_desc)!=str:
            raise TypeError("new_bag_warranty_desc must be in str")
        self.bag_warranty_desc=new_bag_warranty_desc
        
    def set_bag_shape(self,new_bag_shape)->None:
        """
            Sets the bag_shape attribute of the calling object to @new_bag_shape
            Before setting, TypeCheck is performed and this function returns nothing
        """
        if type(new_bag_shape)!=str:
            raise TypeError("new_bag_shape must be in str")
        self.bag_shape=new_bag_shape
        
    def set_bag_manufacturer(self,new_bag_manufacturer)->None:
        """
            Sets the bag_manufacturer attribute of the calling object to @new_bag_manufacturer
            Before setting, TypeCheck is performed and this function returns nothing
        """
        if type(new_bag_manufacturer)!=str:
            raise TypeError("new_bag_manufacturer must be in str")
        self.bag_manufacturer=new_bag_manufacturer
        
    def set_bag_ASIN(self,new_bag_ASIN)->None:
        """
            Sets the bag_ASIN attribute of the calling object to @new_bag_ASIN
            Before setting, TypeCheck is performed and this function returns nothing
        """
        if type(new_bag_ASIN)!=str:
            raise TypeError("new_bag_ASIN must be in str")
        self.bag_ASIN=new_bag_ASIN
        
    def set_bag_country_of_origin(self,new_bag_country_of_origin)->None:
        """
            Sets the bag_country_of_origin attribute of the calling object to @new_bag_country_of_origin
            Before setting, TypeCheck is performed and this function returns nothing
        """
        if type(new_bag_country_of_origin)!=str:
            raise TypeError("new_bag_country_of_origin must be in str")
        self.bag_country_of_origin=new_bag_country_of_origin
        
    def set_bag_cust_reviews(self,new_bag_cust_reviews)->None:
        """
            Sets the bag_cust_reviews attribute of the calling object to @new_bag_cust_reviews
            Before setting, TypeCheck and ValueCheck is performed.and this 
            function returns nothing
        """
        if type(new_bag_cust_reviews)!=float:
            raise TypeError("new_bag_cust_reviews must be in float")
        if new_bag_cust_reviews<=0.0:
            raise ValueError("new_bag_cust_reviews must be positive")
        self.bag_cust_reviews=new_bag_cust_reviews
        
    def set_bag_best_seller_rank(self,new_bag_best_seller_rank)->None:
        """
            Sets the bag_best_seller_rank attribute of the calling object to @new_bag_best_seller_rank
            Before setting, TypeCheck is performed and this function returns nothing
        """
        if type(new_bag_best_seller_rank)!=str:
            raise TypeError("new_bag_best_seller_rank must be in str")
        self.bag_best_seller_rank=new_bag_best_seller_rank
        
    def set_bag_date_first_available(self,new_bag_date_first_available)->None:
        """
            Sets the bag_date_first_available attribute of the calling object to @new_bag_date_first_available
            Before setting, TypeCheck is performed and this function returns nothing
        """
        if type(new_bag_date_first_available)!=str:
            raise TypeError("new_bag_date_first_available must be in str")
        self.bag_date_first_available=new_bag_date_first_available
        
    def set_bag_generic_name(self,new_bag_generic_name)->None:    
        """
            Sets the bag_generic_name attribute of the calling object to @new_bag_generic_name
            Before setting, TypeCheck is performed and this function returns nothing
        """
        if type(new_bag_generic_name)!=str:
            raise TypeError("new_bag_generic_name must be in str")
        self.bag_generic_name=new_bag_generic_name
        
    def show_bag_details(self)->None:
        print("Bag Colour:{}".format(self.bag_colour))
        print("Bag Model Number:{}".format(self.bag_model_number))
        print("Bag Dimensions:{}".format(self.bag_prod_dimensions.__dict__))
        print("Bag Primary Material:{}".format(self.bag_primary_material))
        print("Bag Capacity:{}".format(self.bag_capacity))
        print("Bag Volume Capacity in Liter:{}".format(self.bag_volume_capacity_in_lt))
        print("Bag Warrenty Description:{}".format(self.bag_warranty_desc))
        print("Bag Shape:{}".format(self.bag_shape))
        print("Bag Manufacturer:{}".format(self.bag_manufacturer))
        print("Bag ASIN:{}".format(self.bag_ASIN))
        print("Bag Country of Origin:{}".format(self.bag_country_of_origin))
        print("Bag Customer Reviews:{}".format(self.bag_cust_reviews))
        print("Bag Best Seller Rank:{}".format(self.bag_best_seller_rank))
        print("Bag Date Of First Available:{}".format(self.bag_date_first_available))
        print("Bag Generic Name:{}".format(self.bag_generic_name))
       
    
def main():
    
    bag_obj=Bag(
            "Blue",
            "AMT FIZZ SCH BAG 02 - BLUE",
            ProductDimension(22.0,31.5,49.5,400.0),
            "Polyester",
            "L",
            32,
            "1 year",
            "Rectangular",
            "Samsonite",
            "B07CG8BFPP",
            "India",
            4.0,
            "21 in Bags",
            "18-April-2018",
            "Backpack"
        )
    print("BAG PRODUCT DETAILS:")
    bag_obj.show_bag_details()
    #we can also get the attribute using getter method and 
    #set the specific attribute using setter method 
    sys.exit(0) 
main()

"""
Output:-

BAG PRODUCT DETAILS:
Bag Colour:Blue
Bag Model Number:AMT FIZZ SCH BAG 02 - BLUE
Bag Dimensions:{'length': 22.0, 'width': 31.5, 'height': 49.5, 'weight_in_gm': 400.0}
Bag Primary Material:Polyester
Bag Capacity:L
Bag Volume Capacity in Liter:32
Bag Warrenty Description:1 year
Bag Shape:Rectangular
Bag Manufacturer:Samsonite
Bag ASIN:B07CG8BFPP
Bag Country of Origin:India
Bag Customer Reviews:4.0
Bag Best Seller Rank:21 in Bags
Bag Date Of First Available:18-April-2018
Bag Generic Name:Backpack
"""