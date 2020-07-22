import math
import first_class
#from operators import ...

from package1.shipping import calc_shipping
calc_shipping()

#import package1.shipping
#package1.shipping.calc_shipping()

#from package1 import shipping
#shipping.calc_shipping()

def kgs_to_lbs(number):
    return math.ceil(number / 0.45)

def lbs_to_kgs(number):
    return math.floor(number * 0.45)

print(lbs_to_kgs(10))

val = first_class.Student("Juan", 34567)

val.print_object()

