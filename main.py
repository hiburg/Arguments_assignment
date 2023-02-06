# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

#Part 1: Greet Template
def greet(name,greeting="Hello, <name>!"):
    index = greeting.find("<")
    text1 = greeting[:index]
    text2 = greeting[index+6:]              # <name> has a length of 6 !
    text  = text1 + str(name) + text2
    return text



#Part 2: Force
def force(mass, body='earth'):
    gravity_surf = {"sun": 274, "jupiter": 24.92, "neptune": 11.15, "saturn": 10.44,
                    "earth": 9.798, "uranus": 8.87, "venus": 8.87, "mars": 3.71,
                    "mercury": 3.7, "moon": 1.62, "pluto": 0.58}

    body    = body.lower()                 #just to be sure, search dictionary with body in lowercase
    force   = 0

    if gravity_surf.get(body, -1) != -1:   #if not found, get will return -1 
        gravity = round(gravity_surf[body],1)
        force = mass * gravity

    return force



#Part 3: Gravity
def pull(m1, m2, d):
    G       = 6.674 * 10 **-11          # gravitational attraction
    pull    = 0

    if d != 0:                          # no division by zero                         
        pull = G * ((m1*m2)/d**2)
    
    return pull




#print(pull(800, 1500, 3))
