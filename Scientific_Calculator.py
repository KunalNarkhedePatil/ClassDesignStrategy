"""
    @Author:Kunal Narkhede
    @Date:30/12/2023
    @Goal:To implement class Scientific_Calculator
    Capture Real Life Product on Amazon
    @link:http://surl.li/ostaf
"""
import sys
class ProductDimension:
    """
        This class implement the Dimension of Scientific_Calculator
        @__init__(self, length: float, width: float, height: float, weight: float):
        Constructor
        @get_length(self) 
            getter of attribute length
        @get_width(self)
            getter of attribute width
        @get_height(self)
            getter of attribute height
        @get_weight(self)
            getter of attribute weight
        ------------------------------------- 
        @set_length(self):
            setter of attribute length
        @set_width(self):
            setter of attribute width
        @set_height(self):
            setter of attribute height
        @set_weight(self):
            setter of attribute weight  
    """
    
    def __init__(
                self,
                length:float,
                width:float,
                height:float,
                weight:float
        ):
        """
            Constructor of ProductDimension class:
            @__init__(self, length: float, width: float, height: float, weight: float):
            
            @self:newly created class object of ProductDimension
            @length:Client specified value for attribute length
            @width:Client specified value for attribute width
            @height:Client specified value for attribute height
            @weight:Client specified value for attribute weight
        
        """
        
        if type(length)!=float:
            raise TypeError("length must be in float")
        if length<=0.0:
            raise ValueError("length must be positive")
        if type(width)!=float:
            raise TypeError("width must be in float")
        if width<=0.0:
            raise ValueError("width must be positive")
        if type(height)!=float:
            raise TypeError("height must be in float")
        if height<=0.0:
            raise ValueError("height must be positive")
        if type(weight)!=float:
            raise TypeError("weight must be in float")
        if weight<=0.0:
            raise ValueError("weight must be positive")
        
        self.length=length
        self.width=width
        self.height=height
        self.weight=weight
        
    def get_length(self)->float:
        """ 
            Returns the length attribute of the calling object 
        """
        return self.length
    
    def get_width(self)->float:
        """ 
            Returns the width attribute of the calling object 
        """
        return self.width
    
    def get_height(self)->float:
        """ 
            Returns the height attribute of the calling object 
        """
        return self.height
    
    def get_weight(self)->float:
        """ 
            Returns the weight attribute of the calling object 
        """
        return self.weight
    
    #Setter method
    
    def set_length(self,new_length)->None:
        """
            Sets the length attribute of the calling object to @new_length
            Before setting, TypeCheck and ValueCheck is performed.
        """
        if type(new_length)!=float:
            raise TypeError("new_length must be in float")
        if new_length<=0.0:
            raise TypeError("new_length must be positive")
        self.length=new_length
     
    def set_width(self,new_width)->None:
        """
            Sets the width attribute of the calling object to @new_width
            Before setting, TypeCheck and ValueCheck is performed.
        """
        if type(new_width)!=float:
            raise TypeError("new_width must be in float")
        if new_width<=0.0:
            raise ValueError("new_width must be positive")
        self.width=new_width
        
    def set_height(self,new_height)->None:
        """
            Sets the height attribute of the calling object to @new_height
            Before setting, TypeCheck and ValueCheck is performed.
        """
        if type(new_height)!=float:
            raise TypeError("new_height must be in float")
        if new_height<=0.0:
            raise ValueError("new_height must be positive")
        self.height=new_height
        
    def set_weight(self,new_weight)->None:
        """
            Sets the weight attribute of the calling object to @new_weight
            Before setting, TypeCheck and ValueCheck is performed.
        """
        if type(new_weight)!=float:
            raise TypeError("new_weight must be in float")
        if new_weight<=0.0:
            raise ValueError("new_weight must be positive")
        self.weight=new_weight
        
class Scientific_Calculator:
    def __init__(
            self,
            cal_brand:str,
            cal_model_number:str,
            cal_colour:str,
            cal_material:str,
            cal_generic_name:str,
            cal_prod_dimensions:ProductDimension,
            cal_manufacture_part_nr:str,
            cal_manufacturer:str,
            cal_country_of_origin:str,
            cal_ASIN_nr:str,
            cal_cust_reviews:float,
            cal_best_seller_rank:str,
            cal_date_of_first_available:str,
            cal_imported_by:str,
            cal_included_component:str
        ):
            if type(cal_brand)!=str:
                raise TypeError("cal_brand must be in str")
            if type(cal_model_number)!=str:
                raise TypeError("cal_model_number must be str")
            if type(cal_colour)!=str:
                raise TypeError("cal_colour must be in str")
            if type(cal_material)!=str:
                raise TypeError("cal_material must be in str")
            if type(cal_generic_name)!=str:
                raise TypeError("cal_generic_name must be in str")
            if type(cal_prod_dimensions)!=ProductDimension:
                raise TypeError("cal_prod_dimensions must be in ProductDimension")
            if type(cal_manufacture_part_nr)!=str:
                raise TypeError("cal_manufacture_part_nr must be in str")
            if type(cal_manufacturer)!=str:
                raise TypeError("cal_manufacturer must be in str")
            if type(cal_country_of_origin)!=str:
                raise TypeError("cal_country_of_origin must be in str")
            if type(cal_ASIN_nr)!=str:
                raise TypeError("cal_ASIN_nr must be in str")
            if type(cal_cust_reviews)!=float:
                raise TypeError("cal_cust_reviews must be in float")
            if cal_cust_reviews<=0.0:
                raise ValueError("cal_cust_reviews must be positive")
            if type(cal_best_seller_rank)!=str:
                raise TypeError("cal_best_seller_rank must be in str")
            if type(cal_date_of_first_available)!=str:
                raise TypeError("cal_date_of_first_available must be in str")
            if type(cal_imported_by)!=str:
                raise TypeError("cal_imported_by must be in str")
            if type(cal_included_component)!=str:
                raise TypeError("cal_included_component must be in str")
            
            self.cal_brand=cal_brand
            self.cal_model_number=cal_model_number
            self.cal_colour=cal_colour
            self.cal_material=cal_material
            self.cal_generic_name=cal_generic_name
            self.cal_prod_dimensions=cal_prod_dimensions
            self.cal_manufacture_part_nr=cal_manufacture_part_nr
            self.cal_manufacturer=cal_manufacturer
            self.cal_country_of_origin=cal_country_of_origin
            self.cal_ASIN_nr=cal_ASIN_nr
            self.cal_cust_reviews=cal_cust_reviews
            self.cal_best_seller_rank=cal_best_seller_rank
            self.cal_date_of_first_available=cal_date_of_first_available
            self.cal_imported_by=cal_imported_by
            self.cal_included_component=cal_included_component
            
            
            
    def get_cal_brand(self)->str:
        """ 
            Returns the cal_brand attribute of the calling object 
        """
        return self.cal_brand
    
    def get_cal_model_number(self)->str:
        """ 
            Returns the cal_model_number attribute of the calling object 
        """
        return self.cal_model_number
    
    def get_cal_colour(self)->str:
        """ 
            Returns the cal_colour attribute of the calling object 
        """
        return self.cal_colour
    
    def get_cal_material(self)->str:
        """ 
            Returns the cal_material attribute of the calling object 
        """
        return self.cal_material
    
    def get_cal_generic_name(self)->str:
        """ 
            Returns the cal_generic_name attribute of the calling object 
        """
        return self.cal_generic_name
    
    def get_cal_prod_dimensions(self)->ProductDimension:
        """ 
            Returns the cal_prod_dimensions attribute of the calling object 
        """
        return self.cal_prod_dimensions
    
    def get_cal_manufacture_part_nr(self)->str:
        """ 
            Returns the cal_manufacture_part_nr attribute of the calling object 
        """
        return self.cal_manufacture_part_nr
    
    def get_cal_manufacturer(self)->str:
        """ 
            Returns the cal_manufacturer attribute of the calling object 
        """
        return self.cal_manufacturer
    
    def get_cal_country_of_origin(self)->str:
        """ 
            Returns the cal_country_of_origin attribute of the calling object 
        """
        return self.cal_country_of_origin
    
    def get_cal_ASIN_nr(self)->str:
        """ 
            Returns the cal_ASIN_nr attribute of the calling object 
        """
        return self.cal_ASIN_nr
    
    def get_cal_cust_reviews(self)->float:
        """ 
            Returns the cal_cust_reviews attribute of the calling object 
        """
        return self.cal_cust_reviews
    
    def get_cal_best_seller_rank(self)->str:
        """ 
            Returns the cal_best_seller_rank attribute of the calling object 
        """
        return self.cal_best_seller_rank
    
    def get_cal_date_of_first_available(self)->str:
        """ 
            Returns the cal_date_of_first_available attribute of the calling object 
        """
        return self.cal_date_of_first_available
    
    def get_cal_imported_by(self)->str:
        """ 
            Returns the cal_imported_by attribute of the calling object 
        """
        return self.cal_imported_by
    
    def get_cal_included_component(self)->str:
        """ 
            Returns the cal_included_component attribute of the calling object 
        """
        return self.cal_included_component
    
    
    #Setter Method
    
    def set_cal_brand(self,new_cal_brand)->None:
        """
            Sets the cal_brand attribute of the calling object to @new_cal_brand
            Before setting, TypeCheck is performed and this function returns nothing
        """
        if type(new_cal_brand)!=str:
            raise TypeError("new_cal_brand must be in str")
        self.cal_brand=new_cal_brand
    
    def set_cal_model_number(self,new_cal_model_number)->None:
        """
            Sets the cal_model_number attribute of the calling object to @new_cal_model_number
            Before setting, TypeCheck is performed and this function returns nothing
        """
        if type(new_cal_model_number)!=str:
            raise TypeError("new_cal_model_number must be in str")
        self.cal_model_number=new_cal_model_number
    
    def set_cal_colour(self,new_cal_colour)->None:
        """
            Sets the cal_colour attribute of the calling object to @new_cal_colour
            Before setting, TypeCheck is performed and this function returns nothing
        """
        if type(new_cal_colour)!=str:
            raise TypeError("new_cal_colour msut be in str")
        self.cal_colour=new_cal_colour
    
    def set_cal_material(self,new_cal_material)->None:
        """
            Sets the cal_material attribute of the calling object to @new_cal_material
            Before setting, TypeCheck is performed and this function returns nothing
        """
        if type(new_cal_material)!=str:
            raise TypeError("new_cal_material must be in str")
        self.cal_material=new_cal_material
    
    def set_cal_generic_name(self,new_cal_generic_name)->None:
        """
            Sets the cal_generic_name attribute of the calling object to @new_cal_generic_name
            Before setting, TypeCheck is performed and this function returns nothing
        """
        if type(new_cal_generic_name)!=str:
            raise TypeError("new_cal_generic_name must be in str")
        self.cal_generic_name=new_cal_generic_name
    
    def set_cal_prod_dimensions(self,new_cal_prod_dimensions)->None:
        """
            Sets the cal_prod_dimensions attribute of the calling object to @new_cal_prod_dimensions
            Before setting, TypeCheck is performed and this function returns nothing
        """
        if type(new_cal_prod_dimensions)!=ProductDimension:
            raise TypeError("new_cal_prod_dimensions must be in ProductDimension")
        self.cal_prod_dimensions=new_cal_prod_dimensions
        
    def set_cal_manufacture_part_nr(self,new_cal_manufacture_part_nr)->None:
        """
            Sets the cal_manufacture_part_nr attribute of the calling object to @new_cal_manufacture_part_nr
            Before setting, TypeCheck is performed and this function returns nothing
        """
        if type(new_cal_manufacture_part_nr)!=str:
            raise TypeError("new_cal_manufacture_part_nr must be in str")
        self.cal_manufacture_part_nr=new_cal_manufacture_part_nr
    
    def set_cal_manufacturer(self,new_cal_manufacturer)->None:
        """
            Sets the cal_manufacturer attribute of the calling object to @new_cal_manufacturer
            Before setting, TypeCheck is performed and this function returns nothing
        """
        if type(new_cal_manufacturer)!=str:
            raise TypeError("new_cal_manufacturer must be in str")
        self.cal_manufacturer=new_cal_manufacturer
    
    def set_cal_country_of_origin(self,new_cal_country_of_origin)->None:
        """
            Sets the cal_country_of_origin attribute of the calling object to @new_cal_country_of_origin
            Before setting, TypeCheck is performed and this function returns nothing
        """
        if type(new_cal_country_of_origin)!=str:
            raise TypeError("new_cal_country_of_origin must be in str")
        self.cal_country_of_origin=new_cal_country_of_origin
        
    def set_cal_ASIN_nr(self,new_cal_ASIN_nr)->None:
        """
            Sets the cal_ASIN_nr attribute of the calling object to @new_cal_ASIN_nr
            Before setting, TypeCheck is performed and this function returns nothing
        """
        if type(new_cal_ASIN_nr)!=str:
            raise TypeError("new_cal_ASIN_nr must in str")
        self.cal_ASIN_nr=new_cal_ASIN_nr
    
    def set_cal_cust_reviews(self,new_cal_cust_reviews)->None:
        """
            Sets the cal_cust_reviews attribute of the calling object to @new_cal_cust_reviews
            Before setting, TypeCheck and ValueCheck is performed.and this 
            function returns nothing
        """
        if type(new_cal_cust_reviews)!=float:
            raise TypeError("new_cal_cust_reviews must be in float")
        if new_cal_cust_reviews<=0.0:
            raise ValueError("new_cal_cust_reviews must be positive")
        self.cal_cust_reviews=new_cal_cust_reviews
        
    def set_cal_best_seller_rank(self,new_cal_best_seller_rank)->None:
        """
            Sets the cal_best_seller_rank attribute of the calling object to @new_cal_best_seller_rank
            Before setting, TypeCheck is performed and this function returns nothing
        """
        if type(new_cal_best_seller_rank)!=str:
            raise TypeError("new_cal_best_seller_rank must be in str")
        self.cal_best_seller_rank=new_cal_best_seller_rank
        
    def set_cal_date_of_first_available(self,new_cal_date_of_first_available)->None:
        """
            Sets the cal_date_of_first_available attribute of the calling object to @new_cal_date_of_first_available
            Before setting, TypeCheck is performed and this function returns nothing
        """
        if type(new_cal_date_of_first_available)!=str:
            raise TypeError("new_cal_date_of_first_available must be in str")
        self.cal_date_of_first_available=new_cal_date_of_first_available
        
    def set_cal_imported_by(self,new_cal_imported_by)->None:
        """
            Sets the cal_imported_by attribute of the calling object to @new_cal_imported_by
            Before setting, TypeCheck is performed and this function returns nothing
        """
        if type(new_cal_imported_by)!=str:
            raise TypeError("new_cal_imported_by must be in str")
        self.cal_imported_by=new_cal_imported_by
    
    def set_cal_included_component(self,new_cal_included_component)->None:
        """
            Sets the cal_included_component attribute of the calling object to @new_cal_included_component
            Before setting, TypeCheck is performed and this function returns nothing
        """
        if type(new_cal_included_component)!=str:
            raise TypeError("new_cal_included_component must be in str")
        self.cal_included_component=new_cal_included_component
    def show_details(self)->None:
        """
            This function display all the characteristics of Scientific_Calculator class
        """
        print("Brand:{}".format(self.cal_brand))
        print("Model Number:{}".format(self.cal_model_number))
        print("Colour:{}".format(self.cal_colour))
        print("Material:{}".format(self.cal_material))
        print("Generic Name:{}".format(self.cal_generic_name))
        print("Product Dimensions:{}".format(self.cal_prod_dimensions.__dict__))
        print("Manufacturer Part Number:{}".format(self.cal_manufacture_part_nr))
        print("Manufacturer:{}".format(self.cal_manufacturer))
        print("Country Of Origin:{}".format(self.cal_country_of_origin))
        print("ASIN Number:{}".format(self.cal_ASIN_nr))
        print("Customer Reviews:{}".format(self.cal_cust_reviews))
        print("Best Seller Rank:{}".format(self.cal_best_seller_rank))
        print("Date Of First Available:{}".format(self.cal_date_of_first_available))
        print("Imported By:{}".format(self.cal_imported_by))
        print("Included Components:{}".format(self.cal_included_component))
def main()->None:
    cal_obj=Scientific_Calculator(
                            "Casio",
                            "FX-991ES Plus-2nd Edition",
                            "Black",
                            "Plastic",
                            "Scientific",
                            ProductDimension(16.2,7.7,1.1,95.0),
                            "C79",
                            "Casio",
                            "Thailand",
                            "B0846D5CBP",
                            4.5,
                            "#24 in Office Products",
                            "17 February 2020",
                            "Casio India Co Pvt Ltd, A-41, 1st Floor, MCIE, Mathura Road, New Delhi-110044",
                            "1 Scientific Calculator")
    print("Scientific Calculator PRODUCT DETAILS:")
    cal_obj.show_details()
    #we can also get the attribute using getter method and 
    #set the specific attribute using setter method 
    
    sys.exit(0)                    
                          
main()    

"""
Output:

Scientific Calculator PRODUCT DETAILS:
Brand:Casio
Model Number:FX-991ES Plus-2nd Edition
Colour:Black
Material:Plastic
Generic Name:Scientific
Product Dimensions:{'length': 16.2, 'width': 7.7, 'height': 1.1, 'weight': 95.0}
Manufacturer Part Number:C79
Manufacturer:Casio
Country Of Origin:Thailand
ASIN Number:B0846D5CBP
Customer Reviews:4.5
Best Seller Rank:#24 in Office Products
Date Of First Available:17 February 2020
Imported By:Casio India Co Pvt Ltd, A-41, 1st Floor, MCIE, Mathura Road, New Delhi-110044
Included Components:1 Scientific Calculator    
"""