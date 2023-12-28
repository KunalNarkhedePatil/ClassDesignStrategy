"""
    @Author:Kunal Narkhede
    @Date:28/12/2023
    @Goal:To implement class HairDryer
    Capture Real Life Product on Amazon
    @link:http://surl.li/orswu
"""
import sys
class ProductDimension:
    """
        This class implement the Dimension of HairDryer
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
         

class HairDryer:
    def __init__(self,
                hd_brand:str,
                hd_colour:str,
                hd_material:str,
                hd_wattage_in_watts:int,
                hd_power_source:str,
                hd_is_discounted:bool,
                hd_prod_dimensions:ProductDimension,
                hd_date_of_first_available:str,
                hd_ASIN:str,
                hd_model_nr:str,
                hd_country_of_origin:str,
                hd_manufacturer:str,
                hd_imported_by:str,
                hd_net_quantity:int,
                hd_included_components:[str],
                hd_generic_name:str,
                hd_best_seller_rank:str
        ):
        
        if type(hd_brand)!=str:
            raise TypeError("hd_brand must be str")
        if type(hd_colour)!=str:
            raise TypeError("hd_colour must be in str")
        if type(hd_material)!=str:
            raise TypeError("hd_material must be in str")
        if type(hd_wattage_in_watts)!=int:
            raise TypeError("hd_wattage_in_watts must be in int")
        if hd_wattage_in_watts<=0:
            raise ValueError("hd_wattage_in_watts must be positive")
        if type(hd_power_source)!=str:
            raise TypeError("hd_power_source must be in str")
        if type(hd_is_discounted)!=bool:
            raise TypeError("hd_is_discounted must be in bool")
        if type(hd_prod_dimensions)!=ProductDimension:
            raise TypeError("hd_prod_dimensions must be in ProductDimension")
        if type(hd_date_of_first_available)!=str:
            raise TypeError("hd_date_of_first_available must be in str")
        if type(hd_ASIN)!=str:
            raise TypeError("hd_ASIN must be in str")
        if type(hd_model_nr)!=str:
            raise TypeError("hd_model_nr must be in str")
        if type(hd_country_of_origin)!=str:
            raise TypeError("hd_country_of_origin must be in str")
        if type(hd_manufacturer)!=str:
            raise TypeError("hd_manufacturer must be in str")
        if type(hd_imported_by)!=str:
            raise TypeError("hd_imported_by must be in str")
        if type(hd_net_quantity)!=int:
            raise TypeError("hd_net_quantity must be in int")
        if hd_net_quantity<=0:
            raise ValueError("hd_net_quantity must be positive")
        if '__iter__' not in dir(type(hd_included_components)):
            raise TypeError("hd_included_components must be iterable")
        for components in hd_included_components:
            if type(components)!=str:
                raise TypeError("components must be in str")
        if type(hd_generic_name)!=str:
            raise TypeError("hd_generic_name must be in str")
        if type(hd_best_seller_rank)!=str:
            raise TypeError("hd_best_seller_rank must be in str")
        
        self.hd_brand=hd_brand
        self.hd_colour=hd_colour
        self.hd_material=hd_material
        self.hd_wattage_in_watts=hd_wattage_in_watts
        self.hd_power_source=hd_power_source
        self.hd_is_discounted=hd_is_discounted
        self.hd_prod_dimensions=hd_prod_dimensions
        self.hd_date_of_first_available=hd_date_of_first_available
        self.hd_ASIN=hd_ASIN
        self.hd_model_nr=hd_model_nr
        self.hd_country_of_origin=hd_country_of_origin
        self.hd_manufacturer=hd_manufacturer
        self.hd_imported_by=hd_imported_by
        self.hd_net_quantity=hd_net_quantity
        self.hd_included_components=hd_included_components
        self.hd_generic_name=hd_generic_name
        self.hd_best_seller_rank=hd_best_seller_rank
    
    #getter method
    
    def get_hd_brand(self)->str:
        """ 
            Returns the hd_brand attribute of the calling object 
        """
        return self.hd_brand
    
    def get_hd_colour(self)->str:
        """ 
            Returns the hd_colour attribute of the calling object 
        """
        return self.hd_colour
    
    def get_hd_material(self)->str:
        """ 
            Returns the hd_material attribute of the calling object 
        """
        return self.hd_material
    
    def get_hd_wattage_in_watts(self)->int:
        """ 
            Returns the hd_wattage_in_watts attribute of the calling object 
        """
        return self.hd_wattage_in_watts
    
    def get_hd_power_source(self)->str:
        """ 
            Returns the hd_power_source attribute of the calling object 
        """
        return self.hd_power_source
    
    def get_hd_is_discounted(self)->bool:
        """ 
            Returns the hd_is_discounted attribute of the calling object 
        """
        return self.hd_is_discounted
    
    def get_hd_prod_dimensions(self)->ProductDimension:
        """ 
            Returns the hd_prod_dimensions attribute of the calling object 
        """
        return self.hd_prod_dimensions
    
    def get_hd_date_of_first_available(self)->str:
        """ 
            Returns the hd_date_of_first_available attribute of the calling object 
        """
        return self.hd_date_of_first_available
    
    def get_hd_ASIN(self)->str:
        """ 
            Returns the hd_ASIN attribute of the calling object 
        """
        return self.hd_ASIN
    
    def get_hd_model_nr(self)->str:
        """ 
            Returns the hd_model_nr attribute of the calling object 
        """
        return self.hd_model_nr
    
    def get_hd_country_of_origin(self)->str:
        """ 
            Returns the hd_country_of_origin attribute of the calling object 
        """
        return self.hd_country_of_origin
    
    def get_hd_manufacturer(self)->str:
        """ 
            Returns the hd_manufacturer attribute of the calling object 
        """
        return self.hd_manufacturer
    
    def get_hd_imported_by(self)->str:
        """ 
            Returns the hd_imported_by attribute of the calling object 
        """
        return self.hd_imported_by
    
    def get_hd_net_quantity(self)->int:
        """ 
            Returns the hd_net_quantity attribute of the calling object 
        """
        return self.hd_net_quantity
    
    def get_hd_included_components(self)->[str]:
        """ 
            Returns the hd_included_components attribute of the calling object 
        """
        return self.hd_included_components
    
    def get_hd_generic_name(self)->str:
        """ 
            Returns the hd_generic_name attribute of the calling object 
        """
        return self.hd_generic_name
    
    def get_hd_best_seller_rank(self)->str:
        """ 
            Returns the hd_best_seller_rank attribute of the calling object 
        """
        return self.hd_best_seller_rank
    
    #Setter Method
    
    def set_hd_brand(self,new_hd_brand)->None:
        """
            Sets the hd_brand attribute of the calling object to @new_hd_brand
            Before setting, TypeCheck is performed and this function returns nothing
        """
        if type(new_hd_brand)!=str:
            raise TypeError("new_hd_brand must be in str")
        self.hd_brand=new_hd_brand
    
    def set_hd_colour(self,new_hd_colour)->None:
        """
            Sets the hd_colour attribute of the calling object to @new_hd_colour
            Before setting, TypeCheck is performed and this function returns nothing
        """
        if type(new_hd_colour)!=str:
            raise TypeError("new_hd_colour nust be  in str")
        self.hd_colour=new_hd_colour
    
    def set_hd_material(self,new_hd_material)->None:
        """
            Sets the hd_material attribute of the calling object to @new_hd_material
            Before setting, TypeCheck is performed and this function returns nothing
        """
        if type(new_hd_material)!=str:
            raise TypeError("new_hd_material must be str")
        self.hd_material=new_hd_material
    
    def set_hd_wattage_in_watts(self,new_hd_wattage_in_watts)->None:
        """
            Sets the hd_wattage_in_watts attribute of the calling object to @new_hd_wattage_in_watts
            Before setting, TypeCheck and ValueCheck is performed.
        """
        if type(new_hd_wattage_in_watts)!=int:
            raise TypeError("new_hd_wattage_in_watts must be in int")
        if new_hd_wattage_in_watts<=0:
            raise ValueError("new_hd_wattage_in_watts must be positive")
        self.hd_wattage_in_watts=new_hd_wattage_in_watts
        
    def set_hd_power_source(self,new_hd_power_source)->None:
        """
            Sets the hd_power_source attribute of the calling object to @new_hd_power_source
            Before setting, TypeCheck is performed and this function returns nothing
        """
        if type(new_hd_power_source)!=str:
            raise TypeError("new_hd_power_source must be in str")
        self.hd_power_source=new_hd_power_source
    
    def set_hd_is_discounted(self,new_hd_is_discounted)->None:
        """
            Sets the hd_is_discounted attribute of the calling object to @new_hd_is_discounted
            Before setting, TypeCheck is performed and this function returns nothing
        """
        if type(new_hd_is_discounted)!=bool:
            raise TypeError("new_hd_is_discounted must be in bool")
        self.hd_is_discounted=new_hd_is_discounted
    
    def set_hd_prod_dimensions(self,new_hd_prod_dimensions)->None:
        """
            Sets the hd_prod_dimensions attribute of the calling object to @new_hd_prod_dimensions
            Before setting, TypeCheck is performed and this function returns nothing
        """
        if type(new_hd_prod_dimensions)!=ProductDimension:
            raise TypeError("new_hd_prod_dimensions must be in ProductDimension")
        self.hd_prod_dimensions=new_hd_prod_dimensions
    
    def set_hd_date_of_first_available(self,new_hd_date_of_first_available)->None:
        """
            Sets the hd_date_of_first_available attribute of the calling object to @new_hd_date_of_first_available
            Before setting, TypeCheck is performed and this function returns nothing
        """
        if type(new_hd_date_of_first_available)!=str:
            raise TypeError("new_hd_date_of_first_available must be in str")
        self.hd_date_of_first_available=new_hd_date_of_first_available
    
    def set_hd_ASIN(self,new_hd_ASIN)->None:
        """
            Sets the hd_ASIN attribute of the calling object to @new_hd_ASIN
            Before setting, TypeCheck is performed and this function returns nothing
        """
        if type(new_hd_ASIN)!=str:
            raise TypeError("new_hd_ASIN must be in str")
        self.hd_ASIN=new_hd_ASIN
        
    def set_hd_model_nr(self,new_hd_model_nr)->None:
        """
            Sets the hd_model_nr attribute of the calling object to @new_hd_model_nr
            Before setting, TypeCheck is performed and this function returns nothing
        """
        if type(new_hd_model_nr)!=str:
            raise TypeError("new_hd_model_nr must be in str")
        self.hd_model_nr=new_hd_model_nr
    
    def set_hd_country_of_origin(self,new_hd_country_of_origin)->None:
        """
            Sets the hd_country_of_origin attribute of the calling object to @new_hd_country_of_origin
            Before setting, TypeCheck is performed and this function returns nothing
        """
        if type(new_hd_country_of_origin)!=str:
            raise TypeError("new_hd_country_of_origin must be in str")
        self.hd_country_of_origin=new_hd_country_of_origin
    
    def set_hd_manufacturer(self,new_hd_manufacturer)->None:
        """
            Sets the hd_manufacturer attribute of the calling object to @new_hd_manufacturer
            Before setting, TypeCheck is performed and this function returns nothing
        """
        if type(new_hd_manufacturer)!=str:
            raise TypeError("new_hd_manufacturer must be in str")
        self.hd_manufacturer=new_hd_manufacturer
        
    def set_hd_imported_by(self,new_hd_imported_by)->None:
        """
            Sets the hd_imported_by attribute of the calling object to @new_hd_imported_by
            Before setting, TypeCheck is performed and this function returns nothing
        """
        if type(new_hd_imported_by)!=str:
            raise TypeError("new_hd_imported_by must be in str")
        self.hd_imported_by=new_hd_imported_by
    
    def set_hd_net_quantity(self,new_hd_net_quantity)->None:
        """
            Sets the hd_net_quantity attribute of the calling object to @new_hd_net_quantity
            Before setting, TypeCheck and ValueCheck is performed.
        """
        if type(new_hd_net_quantity)!=int:
            raise TypeError("new_hd_net_quantity must be in int")
        if new_hd_net_quantity<=0:
            raise ValueError("new_hd_net_quantity must be positive")
        self.hd_net_quantity=new_hd_net_quantity

    def set_hd_included_components(self,new_hd_included_components)->None:
        """
            Sets the hd_included_components attribute of the calling object to @new_hd_included_components
            Before setting, TypeCheck is performed and this function returns nothing
        """
        if '__iter__' not in dir(type(new_hd_included_components)):
            raise TypeError("new_hd_included_components must be iterable")
        for component in new_hd_included_components:
            if type(component)!=str:
                raise TypeError("component must be in str")
        self.hd_included_components=new_hd_included_components
    
    def set_hd_generic_name(self,new_hd_generic_name)->None:
        """
            Sets the hd_generic_name attribute of the calling object to @new_hd_generic_name
            Before setting, TypeCheck is performed and this function returns nothing
        """
        if type(new_hd_generic_name)!=str:
            raise TypeError("new_hd_generic_name must be in str")
        self.hd_generic_name=new_hd_generic_name
        
    def set_hd_best_seller_rank(self,new_hd_best_seller_rank)->None:
        """
            Sets the hd_best_seller_rank attribute of the calling object to @new_hd_best_seller_rank
            Before setting, TypeCheck is performed and this function returns nothing
        """
        if type(new_hd_best_seller_rank)!=str:
            raise TypeError("new_hd_best_seller_rank must be in str")
        self.hd_best_seller_rank=new_hd_best_seller_rank
    def show_details(self)->None:
        print("Brand:{}".format(self.hd_brand))
        print("Colour:{}".format(self.hd_colour))
        print("Material:{}".format(self.hd_material))
        print("Wattage:{}".format(self.hd_wattage_in_watts))
        print("Power Source:{}".format(self.hd_power_source))
        print("Is Discounted By Manufacturer:{}".format(self.hd_is_discounted))
        print("Product Dimensions:{}".format(self.hd_prod_dimensions.__dict__))
        print("Date of First Available:{}".format(self.hd_date_of_first_available))
        print("ASIN Number:{}".format(self.hd_ASIN))
        print("Model Number:{}".format(self.hd_model_nr))
        print("Country Of Origin:{}".format(self.hd_country_of_origin))
        print("Manufacturer:{}".format(self.hd_manufacturer))
        print("Imported By:{}".format(self.hd_imported_by))
        print("Net Quantity:{}".format(self.hd_net_quantity))
        print("Included Components:{}".format(self.hd_included_components))
        print("Generic Name:{}".format(self.hd_generic_name))
        print("Best Seller Rank:{}".format(self.hd_best_seller_rank))
        
def main()->None:
    hd_obj=HairDryer(
        "Havells",
        "Turquoise",
        "Plastic",
        1200,
        "Corded Electric",
        False,
        ProductDimension(18.3,7.7,25.2,335.0),
        "13 January 2017",
        "B01N33BLDT",
        "Havells HD3151 Hair Dryer",
        "China",
        "Havells",
        "Imported by Havells India Limited , QRG Tower Sector 126 Noida",
        1,
        ["Hair dryer", "Nozzle", "Instruction manual"],
        "Dryer",
        "31 in Beauty"        
    )
    print("HairDryer PRODUCT DETAILS:")
    #we can get the attribute using getter method and 
    # we can also set the specific attribute using setter method 
    hd_obj.show_details()
    sys.exit(0)
main() 

"""
Output:

HairDryer PRODUCT DETAILS:
Brand:Havells
Colour:Turquoise
Material:Plastic
Wattage:1200
Power Source:Corded Electric
Is Discounted By Manufacturer:False
Product Dimensions:{'length': 18.3, 'width': 7.7, 'height': 25.2, 'weight_in_gm': 335.0}
Date of First Available:13 January 2017
ASIN Number:B01N33BLDT
Model Number:Havells HD3151 Hair Dryer
Country Of Origin:China
Manufacturer:Havells
Imported By:Imported by Havells India Limited , QRG Tower Sector 126 Noida
Net Quantity:1
Included Components:['Hair dryer', 'Nozzle', 'Instruction manual']
Generic Name:Dryer
Best Seller Rank:31 in Beauty    
"""
        


