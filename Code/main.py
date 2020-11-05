from gui.guimaker import *
from synthnet import *


class user_graph:
    def __init__(self):
        self.user_num_vertices = 0
        self.user_num_communities = 0
        self.user_cross_community_edges = 0
        self.user_vertices = []
        self.user_edges = []
        self.user_communities = {}
        self.graph = nx.Graph()
        
        self.feature_list = []




g = user_graph()

"""

    Functions to initialize num_vertices, num_communities, cross_community_edges and
    build the clauset network

"""

def initialize_num_vertices(value):
    g.user_num_vertices = int(value)
    #print(g.user_num_vertices)
    
def initialize_num_communities(value):
    g.user_num_communities = int(value)
    #print(g.user_num_communities)
    
def initialize_cross_community_edges(value):
    g.user_cross_community_edges = int(value)
    #print(g.user_cross_community_edges)
    
"""

    Functions to build the clauset network

"""
def build_clauset_network():
    g.user_vertices, g.user_edges, g.user_communities = Clauset_Network(g.user_num_vertices, g.user_num_communities, g.user_cross_community_edges)
    
    """
    print("user_vertices: ")
    print(len(g.user_vertices))
    print("user_edges: ")
    print(len(g.user_edges))
    print("user_communities: ")
    print(len(g.user_communities))
    print("built")
    """





#################################### Distribution feature 1 widgets ##################################

"""

    Functions to initialize the first feature.
    

"""

distribution_1 = ''

uniform_lower_1_value = 0
uniform_upper_1_value = 0

power_lower_1_value = 0
power_upper_1_value = 0
power_a_1_value = 0

normal_mean_1_value = 0
normal_deviation_1_value = 0

def initialize_uniform_lower_1(value):
    global uniform_lower_1_value
    uniform_lower_1_value = value 

def initialize_uniform_upper_1(value):
    global uniform_upper_1_value
    uniform_upper_1_value = value



def initialize_power_lower_1(value):
    global power_lower_1_value
    power_lower_1_value = value
    
def initialize_power_upper_1(value):
    global power_upper_1_value
    power_upper_1_value = value
    
def initialize_power_a_1(value):
    global power_a_1_value
    power_a_1_value = value
    


def initialize_normal_mean_1(value):
    global normal_mean_1_value
    normal_mean_1_value = value 

def initialize_normal_deviation_1(value):
    global normal_deviation_1_value
    normal_deviation_1_value = value
   
    

    

uniform_lower_1 = Slider(1, 1000, 0, callback = initialize_uniform_lower_1)
uniform_upper_1 = Slider(1, 1000, 0, callback = initialize_uniform_upper_1)
uniform_lower_1_text = Text('lower')
uniform_upper_1_text = Text('upper')


power_lower_1 = Slider(1, 1000, 0, callback = initialize_power_lower_1)
power_upper_1 = Slider(1, 1000, 0, callback = initialize_power_upper_1)
power_a_1 = Slider(1, 1000, 0, callback = initialize_power_a_1)
power_lower_1_text = Text('lower')
power_upper_1_text = Text('upper')
power_a_1_text = Text('a')


normal_mean_1 = Slider(1, 1000, 0, callback = initialize_normal_mean_1)
normal_deviation_1 = Slider(1, 1000, 0, callback = initialize_normal_deviation_1)
normal_mean_1_text = Text('mean')
normal_deviation_1_text = Text('deviation')


uniform_lower_1.hide()
uniform_upper_1.hide()
power_lower_1.hide()
power_upper_1.hide()
power_a_1.hide()
normal_mean_1.hide()
normal_deviation_1.hide()



def hide_unhide_1(index, value):
    #print(value)
    global distribution_1
    distribution_1 = value
    if value == 'uniform':
        if uniform_lower_1.is_hidden():
            uniform_lower_1.show()
        if uniform_upper_1.is_hidden():
            uniform_upper_1.show()
        if uniform_lower_1_text.is_hidden():
            uniform_lower_1_text.show()
        if uniform_upper_1_text.is_hidden():
            uniform_upper_1_text.show()
            
            
        if not(power_lower_1.is_hidden()):
            power_lower_1.hide()
        if not(power_upper_1.is_hidden()):
            power_upper_1.hide()
        if not(power_a_1.is_hidden()):
            power_a_1.hide()
        if not(power_lower_1_text.is_hidden()):
            power_lower_1_text.hide()
        if not(power_upper_1_text.is_hidden()):
            power_upper_1_text.hide()
        if not(power_a_1_text.is_hidden()):
            power_a_1_text.hide()    
        
            
        if not(normal_mean_1.is_hidden()):
            normal_mean_1.hide()
        if not(normal_deviation_1.is_hidden()):
            normal_deviation_1.hide()
        if not(normal_mean_1_text.is_hidden()):
            normal_mean_1_text.hide()
        if not(normal_deviation_1_text.is_hidden()):
            normal_deviation_1_text.hide()
        
    elif value == 'power':
        if not(uniform_lower_1.is_hidden()):
            uniform_lower_1.hide()
        if not(uniform_upper_1.is_hidden()):
            uniform_upper_1.hide()
        if not(uniform_lower_1_text.is_hidden()):
            uniform_lower_1_text.hide()
        if not(uniform_upper_1_text.is_hidden()):
            uniform_upper_1_text.hide()
            
        if power_lower_1.is_hidden():
            power_lower_1.show()
        if power_upper_1.is_hidden():
            power_upper_1.show()
        if power_a_1.is_hidden():
            power_a_1.show()
        if power_lower_1_text.is_hidden():
            power_lower_1_text.show()
        if power_upper_1_text.is_hidden():
            power_upper_1_text.show()
        if power_a_1_text.is_hidden():
            power_a_1_text.show()
            
        if not(normal_mean_1.is_hidden()):
            normal_mean_1.hide()
        if not(normal_deviation_1.is_hidden()):
            normal_deviation_1.hide()
        if not(normal_mean_1_text.is_hidden()):
            normal_mean_1_text.hide()
        if not(normal_deviation_1_text.is_hidden()):
            normal_deviation_1_text.hide()
        
    elif value == 'normal':
        if not(uniform_lower_1.is_hidden()):
            uniform_lower_1.hide()
        if not(uniform_upper_1.is_hidden()):
            uniform_upper_1.hide()
        if not(uniform_lower_1_text.is_hidden()):
            uniform_lower_1_text.hide()
        if not(uniform_upper_1_text.is_hidden()):
            uniform_upper_1_text.hide()
        
            
        if not(power_lower_1.is_hidden()):
            power_lower_1.hide()
        if not(power_upper_1.is_hidden()):
            power_upper_1.hide()
        if not(power_a_1.is_hidden()):
            power_a_1.hide()
        if not(power_lower_1_text.is_hidden()):
            power_lower_1_text.hide()
        if not(power_upper_1_text.is_hidden()):
            power_upper_1_text.hide()
        if not(power_a_1_text.is_hidden()):
            power_a_1_text.hide()
            
            
        if normal_mean_1.is_hidden():
            normal_mean_1.show()
        if normal_deviation_1.is_hidden():
            normal_deviation_1.show()
        if normal_mean_1_text.is_hidden():
            normal_mean_1_text.show()
        if normal_deviation_1_text.is_hidden():
            normal_deviation_1_text.show()

########################################################################################################################

########################################### Distribution feature 2 widgets ###########################################

"""

    Functions to initialize the second feature.
    

"""

distribution_2 = ''

uniform_lower_2_value = 0
uniform_upper_2_value = 0

power_lower_2_value = 0
power_upper_2_value = 0
power_a_2_value = 0

normal_mean_2_value = 0
normal_deviation_2_value = 0

def initialize_uniform_lower_2(value):
    global uniform_lower_2_value
    uniform_lower_2_value = value 

def initialize_uniform_upper_2(value):
    global uniform_upper_2_value
    uniform_upper_2_value = value



def initialize_power_lower_2(value):
    global power_lower_2_value
    power_lower_2_value = value
    
def initialize_power_upper_2(value):
    global power_upper_2_value
    power_upper_2_value = value
    
def initialize_power_a_2(value):
    global power_a_2_value
    power_a_2_value = value
    


def initialize_normal_mean_2(value):
    global normal_mean_2_value
    normal_mean_2_value = value 

def initialize_normal_deviation_2(value):
    global normal_deviation_2_value
    normal_deviation_2_value = value
   
    

    

uniform_lower_2 = Slider(1, 1000, 0, callback = initialize_uniform_lower_2)
uniform_upper_2 = Slider(1, 1000, 0, callback = initialize_uniform_upper_2)
uniform_lower_2_text = Text('lower')
uniform_upper_2_text = Text('upper')


power_lower_2 = Slider(1, 1000, 0, callback = initialize_power_lower_2)
power_upper_2 = Slider(1, 1000, 0, callback = initialize_power_upper_2)
power_a_2 = Slider(1, 1000, 0, callback = initialize_power_a_2)
power_lower_2_text = Text('lower')
power_upper_2_text = Text('upper')
power_a_2_text = Text('a')


normal_mean_2 = Slider(1, 1000, 0, callback = initialize_normal_mean_2)
normal_deviation_2 = Slider(1, 1000, 0, callback = initialize_normal_deviation_2)
normal_mean_2_text = Text('mean')
normal_deviation_2_text = Text('deviation')


uniform_lower_2.hide()
uniform_upper_2.hide()
power_lower_2.hide()
power_upper_2.hide()
power_a_2.hide()
normal_mean_2.hide()
normal_deviation_2.hide()



def hide_unhide_2(index, value):
    global distribution_2
    distribution_2 = value
    if value == 'uniform':
        if uniform_lower_2.is_hidden():
            uniform_lower_2.show()
        if uniform_upper_2.is_hidden():
            uniform_upper_2.show()
        if uniform_lower_2_text.is_hidden():
            uniform_lower_2_text.show()
        if uniform_upper_2_text.is_hidden():
            uniform_upper_2_text.show()
            
            
        if not(power_lower_2.is_hidden()):
            power_lower_2.hide()
        if not(power_upper_2.is_hidden()):
            power_upper_2.hide()
        if not(power_a_2.is_hidden()):
            power_a_2.hide()
        if not(power_lower_2_text.is_hidden()):
            power_lower_2_text.hide()
        if not(power_upper_2_text.is_hidden()):
            power_upper_2_text.hide()
        if not(power_a_2_text.is_hidden()):
            power_a_2_text.hide()    
        
            
        if not(normal_mean_2.is_hidden()):
            normal_mean_2.hide()
        if not(normal_deviation_2.is_hidden()):
            normal_deviation_2.hide()
        if not(normal_mean_2_text.is_hidden()):
            normal_mean_2_text.hide()
        if not(normal_deviation_2_text.is_hidden()):
            normal_deviation_2_text.hide()
        
    elif value == 'power':
        if not(uniform_lower_2.is_hidden()):
            uniform_lower_2.hide()
        if not(uniform_upper_2.is_hidden()):
            uniform_upper_2.hide()
        if not(uniform_lower_2_text.is_hidden()):
            uniform_lower_2_text.hide()
        if not(uniform_upper_2_text.is_hidden()):
            uniform_upper_2_text.hide()
            
        if power_lower_2.is_hidden():
            power_lower_2.show()
        if power_upper_2.is_hidden():
            power_upper_2.show()
        if power_a_2.is_hidden():
            power_a_2.show()
        if power_lower_2_text.is_hidden():
            power_lower_2_text.show()
        if power_upper_2_text.is_hidden():
            power_upper_2_text.show()
        if power_a_2_text.is_hidden():
            power_a_2_text.show()
            
        if not(normal_mean_2.is_hidden()):
            normal_mean_2.hide()
        if not(normal_deviation_2.is_hidden()):
            normal_deviation_2.hide()
        if not(normal_mean_2_text.is_hidden()):
            normal_mean_2_text.hide()
        if not(normal_deviation_2_text.is_hidden()):
            normal_deviation_2_text.hide()
        
    elif value == 'normal':
        if not(uniform_lower_2.is_hidden()):
            uniform_lower_2.hide()
        if not(uniform_upper_2.is_hidden()):
            uniform_upper_2.hide()
        if not(uniform_lower_2_text.is_hidden()):
            uniform_lower_2_text.hide()
        if not(uniform_upper_2_text.is_hidden()):
            uniform_upper_2_text.hide()
        
            
        if not(power_lower_2.is_hidden()):
            power_lower_2.hide()
        if not(power_upper_2.is_hidden()):
            power_upper_2.hide()
        if not(power_a_2.is_hidden()):
            power_a_2.hide()
        if not(power_lower_2_text.is_hidden()):
            power_lower_2_text.hide()
        if not(power_upper_2_text.is_hidden()):
            power_upper_2_text.hide()
        if not(power_a_2_text.is_hidden()):
            power_a_2_text.hide()
            
            
        if normal_mean_2.is_hidden():
            normal_mean_2.show()
        if normal_deviation_2.is_hidden():
            normal_deviation_2.show()
        if normal_mean_2_text.is_hidden():
            normal_mean_2_text.show()
        if normal_deviation_2_text.is_hidden():
            normal_deviation_2_text.show()




####################################################################################






####################################### Distribution feature 3 widgets ###########################################

"""

    Functions to initialize the third feature.
    

"""

distribution_3 = ''

uniform_lower_3_value = 0
uniform_upper_3_value = 0

power_lower_3_value = 0
power_upper_3_value = 0
power_a_3_value = 0

normal_mean_3_value = 0
normal_deviation_3_value = 0

def initialize_uniform_lower_3(value):
    global uniform_lower_3_value
    uniform_lower_3_value = value 

def initialize_uniform_upper_3(value):
    global uniform_upper_3_value
    uniform_upper_3_value = value



def initialize_power_lower_3(value):
    global power_lower_3_value
    power_lower_3_value = value
    
def initialize_power_upper_3(value):
    global power_upper_3_value
    power_upper_3_value = value
    
def initialize_power_a_3(value):
    global power_a_3_value
    power_a_3_value = value
    


def initialize_normal_mean_3(value):
    global normal_mean_3_value
    normal_mean_3_value = value 

def initialize_normal_deviation_3(value):
    global normal_deviation_3_value
    normal_deviation_3_value = value
   
    

    

uniform_lower_3 = Slider(1, 1000, 0, callback = initialize_uniform_lower_3)
uniform_upper_3 = Slider(1, 1000, 0, callback = initialize_uniform_upper_3)
uniform_lower_3_text = Text('lower')
uniform_upper_3_text = Text('upper')


power_lower_3 = Slider(1, 1000, 0, callback = initialize_power_lower_3)
power_upper_3 = Slider(1, 1000, 0, callback = initialize_power_upper_3)
power_a_3 = Slider(1, 1000, 0, callback = initialize_power_a_3)
power_lower_3_text = Text('lower')
power_upper_3_text = Text('upper')
power_a_3_text = Text('a')


normal_mean_3 = Slider(1, 1000, 0, callback = initialize_normal_mean_3)
normal_deviation_3 = Slider(1, 1000, 0, callback = initialize_normal_deviation_3)
normal_mean_3_text = Text('mean')
normal_deviation_3_text = Text('deviation')


uniform_lower_3.hide()
uniform_upper_3.hide()
power_lower_3.hide()
power_upper_3.hide()
power_a_3.hide()
normal_mean_3.hide()
normal_deviation_3.hide()



def hide_unhide_3(index, value):
    global distribution_3
    distribution_3 = value
    if value == 'uniform':
        if uniform_lower_3.is_hidden():
            uniform_lower_3.show()
        if uniform_upper_3.is_hidden():
            uniform_upper_3.show()
        if uniform_lower_3_text.is_hidden():
            uniform_lower_3_text.show()
        if uniform_upper_3_text.is_hidden():
            uniform_upper_3_text.show()
            
            
        if not(power_lower_3.is_hidden()):
            power_lower_3.hide()
        if not(power_upper_3.is_hidden()):
            power_upper_3.hide()
        if not(power_a_3.is_hidden()):
            power_a_3.hide()
        if not(power_lower_3_text.is_hidden()):
            power_lower_3_text.hide()
        if not(power_upper_3_text.is_hidden()):
            power_upper_3_text.hide()
        if not(power_a_3_text.is_hidden()):
            power_a_3_text.hide()    
        
            
        if not(normal_mean_3.is_hidden()):
            normal_mean_3.hide()
        if not(normal_deviation_3.is_hidden()):
            normal_deviation_3.hide()
        if not(normal_mean_3_text.is_hidden()):
            normal_mean_3_text.hide()
        if not(normal_deviation_3_text.is_hidden()):
            normal_deviation_3_text.hide()
        
    elif value == 'power':
        if not(uniform_lower_3.is_hidden()):
            uniform_lower_3.hide()
        if not(uniform_upper_3.is_hidden()):
            uniform_upper_3.hide()
        if not(uniform_lower_3_text.is_hidden()):
            uniform_lower_3_text.hide()
        if not(uniform_upper_3_text.is_hidden()):
            uniform_upper_3_text.hide()
            
        if power_lower_3.is_hidden():
            power_lower_3.show()
        if power_upper_3.is_hidden():
            power_upper_3.show()
        if power_a_3.is_hidden():
            power_a_3.show()
        if power_lower_3_text.is_hidden():
            power_lower_3_text.show()
        if power_upper_3_text.is_hidden():
            power_upper_3_text.show()
        if power_a_3_text.is_hidden():
            power_a_3_text.show()
            
        if not(normal_mean_3.is_hidden()):
            normal_mean_3.hide()
        if not(normal_deviation_3.is_hidden()):
            normal_deviation_3.hide()
        if not(normal_mean_3_text.is_hidden()):
            normal_mean_3_text.hide()
        if not(normal_deviation_3_text.is_hidden()):
            normal_deviation_3_text.hide()
        
    elif value == 'normal':
        if not(uniform_lower_3.is_hidden()):
            uniform_lower_3.hide()
        if not(uniform_upper_3.is_hidden()):
            uniform_upper_3.hide()
        if not(uniform_lower_3_text.is_hidden()):
            uniform_lower_3_text.hide()
        if not(uniform_upper_3_text.is_hidden()):
            uniform_upper_3_text.hide()
        
            
        if not(power_lower_3.is_hidden()):
            power_lower_3.hide()
        if not(power_upper_3.is_hidden()):
            power_upper_3.hide()
        if not(power_a_3.is_hidden()):
            power_a_3.hide()
        if not(power_lower_3_text.is_hidden()):
            power_lower_3_text.hide()
        if not(power_upper_3_text.is_hidden()):
            power_upper_3_text.hide()
        if not(power_a_3_text.is_hidden()):
            power_a_3_text.hide()
            
            
        if normal_mean_3.is_hidden():
            normal_mean_3.show()
        if normal_deviation_3.is_hidden():
            normal_deviation_3.show()
        if normal_mean_3_text.is_hidden():
            normal_mean_3_text.show()
        if normal_deviation_3_text.is_hidden():
            normal_deviation_3_text.show()




####################################################################################
            
            
####################################### Distribution feature 4 widgets ###########################################

"""

    Functions to initialize the fourth feature.
    

"""

distribution_4 = ''

uniform_lower_4_value = 0
uniform_upper_4_value = 0

power_lower_4_value = 0
power_upper_4_value = 0
power_a_4_value = 0

normal_mean_4_value = 0
normal_deviation_4_value = 0

def initialize_uniform_lower_4(value):
    global uniform_lower_4_value
    uniform_lower_4_value = value 

def initialize_uniform_upper_4(value):
    global uniform_upper_4_value
    uniform_upper_4_value = value



def initialize_power_lower_4(value):
    global power_lower_4_value
    power_lower_4_value = value
    
def initialize_power_upper_4(value):
    global power_upper_4_value
    power_upper_4_value = value
    
def initialize_power_a_4(value):
    global power_a_4_value
    power_a_4_value = value
    


def initialize_normal_mean_4(value):
    global normal_mean_4_value
    normal_mean_4_value = value 

def initialize_normal_deviation_4(value):
    global normal_deviation_4_value
    normal_deviation_4_value = value
   
    

    

uniform_lower_4 = Slider(1, 1000, 0, callback = initialize_uniform_lower_4)
uniform_upper_4 = Slider(1, 1000, 0, callback = initialize_uniform_upper_4)
uniform_lower_4_text = Text('lower')
uniform_upper_4_text = Text('upper')


power_lower_4 = Slider(1, 1000, 0, callback = initialize_power_lower_4)
power_upper_4 = Slider(1, 1000, 0, callback = initialize_power_upper_4)
power_a_4 = Slider(1, 1000, 0, callback = initialize_power_a_4)
power_lower_4_text = Text('lower')
power_upper_4_text = Text('upper')
power_a_4_text = Text('a')


normal_mean_4 = Slider(1, 1000, 0, callback = initialize_normal_mean_4)
normal_deviation_4 = Slider(1, 1000, 0, callback = initialize_normal_deviation_4)
normal_mean_4_text = Text('mean')
normal_deviation_4_text = Text('deviation')


uniform_lower_4.hide()
uniform_upper_4.hide()
power_lower_4.hide()
power_upper_4.hide()
power_a_4.hide()
normal_mean_4.hide()
normal_deviation_4.hide()



def hide_unhide_4(index, value):
    global distribution_4
    distribution_4 = value
    if value == 'uniform':
        if uniform_lower_4.is_hidden():
            uniform_lower_4.show()
        if uniform_upper_4.is_hidden():
            uniform_upper_4.show()
        if uniform_lower_4_text.is_hidden():
            uniform_lower_4_text.show()
        if uniform_upper_4_text.is_hidden():
            uniform_upper_4_text.show()
            
            
        if not(power_lower_4.is_hidden()):
            power_lower_4.hide()
        if not(power_upper_4.is_hidden()):
            power_upper_4.hide()
        if not(power_a_4.is_hidden()):
            power_a_4.hide()
        if not(power_lower_4_text.is_hidden()):
            power_lower_4_text.hide()
        if not(power_upper_4_text.is_hidden()):
            power_upper_4_text.hide()
        if not(power_a_4_text.is_hidden()):
            power_a_4_text.hide()    
        
            
        if not(normal_mean_4.is_hidden()):
            normal_mean_4.hide()
        if not(normal_deviation_4.is_hidden()):
            normal_deviation_4.hide()
        if not(normal_mean_4_text.is_hidden()):
            normal_mean_4_text.hide()
        if not(normal_deviation_4_text.is_hidden()):
            normal_deviation_4_text.hide()
        
    elif value == 'power':
        if not(uniform_lower_4.is_hidden()):
            uniform_lower_4.hide()
        if not(uniform_upper_4.is_hidden()):
            uniform_upper_4.hide()
        if not(uniform_lower_4_text.is_hidden()):
            uniform_lower_4_text.hide()
        if not(uniform_upper_4_text.is_hidden()):
            uniform_upper_4_text.hide()
            
        if power_lower_4.is_hidden():
            power_lower_4.show()
        if power_upper_4.is_hidden():
            power_upper_4.show()
        if power_a_4.is_hidden():
            power_a_4.show()
        if power_lower_4_text.is_hidden():
            power_lower_4_text.show()
        if power_upper_4_text.is_hidden():
            power_upper_4_text.show()
        if power_a_4_text.is_hidden():
            power_a_4_text.show()
            
        if not(normal_mean_4.is_hidden()):
            normal_mean_4.hide()
        if not(normal_deviation_4.is_hidden()):
            normal_deviation_4.hide()
        if not(normal_mean_4_text.is_hidden()):
            normal_mean_4_text.hide()
        if not(normal_deviation_4_text.is_hidden()):
            normal_deviation_4_text.hide()
        
    elif value == 'normal':
        if not(uniform_lower_4.is_hidden()):
            uniform_lower_4.hide()
        if not(uniform_upper_4.is_hidden()):
            uniform_upper_4.hide()
        if not(uniform_lower_4_text.is_hidden()):
            uniform_lower_4_text.hide()
        if not(uniform_upper_4_text.is_hidden()):
            uniform_upper_4_text.hide()
        
            
        if not(power_lower_4.is_hidden()):
            power_lower_4.hide()
        if not(power_upper_4.is_hidden()):
            power_upper_4.hide()
        if not(power_a_4.is_hidden()):
            power_a_4.hide()
        if not(power_lower_4_text.is_hidden()):
            power_lower_4_text.hide()
        if not(power_upper_4_text.is_hidden()):
            power_upper_4_text.hide()
        if not(power_a_4_text.is_hidden()):
            power_a_4_text.hide()
            
            
        if normal_mean_4.is_hidden():
            normal_mean_4.show()
        if normal_deviation_4.is_hidden():
            normal_deviation_4.show()
        if normal_mean_4_text.is_hidden():
            normal_mean_4_text.show()
        if normal_deviation_4_text.is_hidden():
            normal_deviation_4_text.show()




####################################################################################
            
            
####################################### Distribution feature 5 widgets ###########################################

"""

    Functions to initialize the fifth feature.
    

"""

distribution_5 = ''

uniform_lower_5_value = 0
uniform_upper_5_value = 0

power_lower_5_value = 0
power_upper_5_value = 0
power_a_5_value = 0

normal_mean_5_value = 0
normal_deviation_5_value = 0

def initialize_uniform_lower_5(value):
    global uniform_lower_5_value
    uniform_lower_5_value = value 

def initialize_uniform_upper_5(value):
    global uniform_upper_5_value
    uniform_upper_5_value = value



def initialize_power_lower_5(value):
    global power_lower_5_value
    power_lower_5_value = value
    
def initialize_power_upper_5(value):
    global power_upper_5_value
    power_upper_5_value = value
    
def initialize_power_a_5(value):
    global power_a_5_value
    power_a_5_value = value
    


def initialize_normal_mean_5(value):
    global normal_mean_5_value
    normal_mean_5_value = value 

def initialize_normal_deviation_5(value):
    global normal_deviation_5_value
    normal_deviation_5_value = value
   
    

    

uniform_lower_5 = Slider(1, 1000, 0, callback = initialize_uniform_lower_5)
uniform_upper_5 = Slider(1, 1000, 0, callback = initialize_uniform_upper_5)
uniform_lower_5_text = Text('lower')
uniform_upper_5_text = Text('upper')


power_lower_5 = Slider(1, 1000, 0, callback = initialize_power_lower_5)
power_upper_5 = Slider(1, 1000, 0, callback = initialize_power_upper_5)
power_a_5 = Slider(1, 1000, 0, callback = initialize_power_a_5)
power_lower_5_text = Text('lower')
power_upper_5_text = Text('upper')
power_a_5_text = Text('a')


normal_mean_5 = Slider(1, 1000, 0, callback = initialize_normal_mean_5)
normal_deviation_5 = Slider(1, 1000, 0, callback = initialize_normal_deviation_5)
normal_mean_5_text = Text('mean')
normal_deviation_5_text = Text('deviation')


uniform_lower_5.hide()
uniform_upper_5.hide()
power_lower_5.hide()
power_upper_5.hide()
power_a_5.hide()
normal_mean_5.hide()
normal_deviation_5.hide()



def hide_unhide_5(index, value):
    global distribution_5
    distribution_5 = value
    if value == 'uniform':
        if uniform_lower_5.is_hidden():
            uniform_lower_5.show()
        if uniform_upper_5.is_hidden():
            uniform_upper_5.show()
        if uniform_lower_5_text.is_hidden():
            uniform_lower_5_text.show()
        if uniform_upper_5_text.is_hidden():
            uniform_upper_5_text.show()
            
            
        if not(power_lower_5.is_hidden()):
            power_lower_5.hide()
        if not(power_upper_5.is_hidden()):
            power_upper_5.hide()
        if not(power_a_5.is_hidden()):
            power_a_5.hide()
        if not(power_lower_5_text.is_hidden()):
            power_lower_5_text.hide()
        if not(power_upper_5_text.is_hidden()):
            power_upper_5_text.hide()
        if not(power_a_5_text.is_hidden()):
            power_a_5_text.hide()    
        
            
        if not(normal_mean_5.is_hidden()):
            normal_mean_5.hide()
        if not(normal_deviation_5.is_hidden()):
            normal_deviation_5.hide()
        if not(normal_mean_5_text.is_hidden()):
            normal_mean_5_text.hide()
        if not(normal_deviation_5_text.is_hidden()):
            normal_deviation_5_text.hide()
        
    elif value == 'power':
        if not(uniform_lower_5.is_hidden()):
            uniform_lower_5.hide()
        if not(uniform_upper_5.is_hidden()):
            uniform_upper_5.hide()
        if not(uniform_lower_5_text.is_hidden()):
            uniform_lower_5_text.hide()
        if not(uniform_upper_5_text.is_hidden()):
            uniform_upper_5_text.hide()
            
        if power_lower_5.is_hidden():
            power_lower_5.show()
        if power_upper_5.is_hidden():
            power_upper_5.show()
        if power_a_5.is_hidden():
            power_a_5.show()
        if power_lower_5_text.is_hidden():
            power_lower_5_text.show()
        if power_upper_5_text.is_hidden():
            power_upper_5_text.show()
        if power_a_5_text.is_hidden():
            power_a_5_text.show()
            
        if not(normal_mean_5.is_hidden()):
            normal_mean_5.hide()
        if not(normal_deviation_5.is_hidden()):
            normal_deviation_5.hide()
        if not(normal_mean_5_text.is_hidden()):
            normal_mean_5_text.hide()
        if not(normal_deviation_5_text.is_hidden()):
            normal_deviation_5_text.hide()
        
    elif value == 'normal':
        if not(uniform_lower_5.is_hidden()):
            uniform_lower_5.hide()
        if not(uniform_upper_5.is_hidden()):
            uniform_upper_5.hide()
        if not(uniform_lower_5_text.is_hidden()):
            uniform_lower_5_text.hide()
        if not(uniform_upper_5_text.is_hidden()):
            uniform_upper_5_text.hide()
        
            
        if not(power_lower_5.is_hidden()):
            power_lower_5.hide()
        if not(power_upper_5.is_hidden()):
            power_upper_5.hide()
        if not(power_a_5.is_hidden()):
            power_a_5.hide()
        if not(power_lower_5_text.is_hidden()):
            power_lower_5_text.hide()
        if not(power_upper_5_text.is_hidden()):
            power_upper_5_text.hide()
        if not(power_a_5_text.is_hidden()):
            power_a_5_text.hide()
            
            
        if normal_mean_5.is_hidden():
            normal_mean_5.show()
        if normal_deviation_5.is_hidden():
            normal_deviation_5.show()
        if normal_mean_5_text.is_hidden():
            normal_mean_5_text.show()
        if normal_deviation_5_text.is_hidden():
            normal_deviation_5_text.show()




####################################################################################



"""
    a function that constructs the feature list required by "add_feature_vector" function in synthnet
    
    returns: a list containing the 5 feature attributes chosen by the user. 

"""
def build_feature_dict():
    g.feature_list = []
    if(distribution_1 == 'uniform'):
        g.feature_list.append(('uniform', (uniform_lower_1_value, uniform_upper_1_value)))
    elif(distribution_1 == 'power'):
        g.feature_list.append(('power', (power_a_1_value, power_lower_1_value, power_upper_1_value)))
    elif(distribution_1 == 'normal'):
        g.feature_list.append(('normal', (normal_mean_1_value , normal_deviation_1_value )))
    
    if(distribution_2 == 'uniform'):
        g.feature_list.append(('uniform', (uniform_lower_2_value, uniform_upper_2_value)))
    elif(distribution_2 == 'power'):
        g.feature_list.append(('power', (power_a_2_value, power_lower_2_value, power_upper_2_value)))
    elif(distribution_2 == 'normal'):
        g.feature_list.append(('normal', (normal_mean_2_value, normal_deviation_2_value)))
      
    if(distribution_3 == 'uniform'):
        g.feature_list.append(('uniform', (uniform_lower_3_value, uniform_upper_3_value)))
    elif(distribution_3 == 'power'):
        g.feature_list.append(('power', (power_a_3_value, power_lower_3_value, power_upper_3_value)))
    elif(distribution_3 == 'normal'):
        g.feature_list.append(('normal', (normal_mean_3_value, normal_deviation_3_value)))
        
        
    if(distribution_4 == 'uniform'):
        g.feature_list.append(('uniform', (uniform_lower_4_value, uniform_upper_4_value)))
    elif(distribution_4 == 'power'):
        g.feature_list.append(('power', (power_a_4_value, power_lower_4_value, power_upper_4_value)))
    elif(distribution_4 == 'normal'):
        g.feature_list.append(('normal', (normal_mean_4_value, normal_deviation_4_value)))
        
    if(distribution_5 == 'uniform'):
        g.feature_list.append(('uniform', (uniform_lower_5_value, uniform_upper_5_value)))
    elif(distribution_5 == 'power'):
        g.feature_list.append(('power', (power_a_5_value, power_lower_5_value, power_upper_5_value)))
    elif(distribution_5 == 'normal'):
        g.feature_list.append(('normal', (normal_mean_5_value, normal_deviation_5_value)))
        
    
    #print(g.feature_list)
    return g.feature_list
    
    
"""

    array to build the gui

"""

array = [
	[Spacing(5, 5)                      ],
	[Text('\t\tEnter the fields below to simulate your own Clauset Network! '), None            ],
	[Text('Number of vertices'), Slider(1, 1000, 500, callback = initialize_num_vertices),
      Text('Number of communities'), Slider(1, 1000, 500, callback = initialize_num_communities),
      Text('Number of cross community edges'), Slider(1, 1000, 500, callback = initialize_cross_community_edges)],
  
    [Button("Build the Clause Network", callback=build_clauset_network)],
    
    
    [OptionMenu(['uniform', 'normal', 'power'], callback = hide_unhide_1)],    
    [uniform_lower_1_text, uniform_lower_1, uniform_upper_1_text, uniform_upper_1],
    [power_lower_1_text, power_lower_1, power_upper_1_text, power_upper_1,power_a_1_text, power_a_1],
    [normal_mean_1_text, normal_mean_1, normal_deviation_1_text, normal_deviation_1],
    
    [OptionMenu(['uniform', 'normal', 'power'], callback = hide_unhide_2)],    
    [uniform_lower_2_text, uniform_lower_2, uniform_upper_2_text, uniform_upper_2],
    [power_lower_2_text, power_lower_2, power_upper_2_text, power_upper_2,power_a_2_text, power_a_2],
    [normal_mean_2_text, normal_mean_2, normal_deviation_2_text, normal_deviation_2],
    
    [OptionMenu(['uniform', 'normal', 'power'], callback = hide_unhide_3)],    
    [uniform_lower_3_text, uniform_lower_3, uniform_upper_3_text, uniform_upper_3],
    [power_lower_3_text, power_lower_3, power_upper_3_text, power_upper_3,power_a_3_text, power_a_3],
    [normal_mean_3_text, normal_mean_3, normal_deviation_3_text, normal_deviation_3],
    
    [OptionMenu(['uniform', 'normal', 'power'], callback = hide_unhide_4)],    
    [uniform_lower_4_text, uniform_lower_4, uniform_upper_4_text, uniform_upper_4],
    [power_lower_4_text, power_lower_4, power_upper_4_text, power_upper_4,power_a_4_text, power_a_4],
    [normal_mean_4_text, normal_mean_4, normal_deviation_4_text, normal_deviation_4],
    
    
    [OptionMenu(['uniform', 'normal', 'power'], callback = hide_unhide_5)],    
    [uniform_lower_5_text, uniform_lower_5, uniform_upper_5_text, uniform_upper_5],
    [power_lower_5_text, power_lower_5, power_upper_5_text, power_upper_5,power_a_5_text, power_a_5],
    [normal_mean_5_text, normal_mean_5, normal_deviation_5_text, normal_deviation_5],
    
    [Button("Build the Feature Dictionary", callback=build_feature_dict)],
	[Spacing(5, 5)                      ],
]

create_gui(array, title = 'Evolution of Clusters')

