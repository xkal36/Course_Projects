#!/usr/bin/python

# Completed for Udacity CS101 Course.

example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures.\
Jimmy is connected to Olive, John, Debra.\
Jimmy likes to play ."

"""
1. Data Structure changed: it is now a dictionary where each name is mapped
to a dictionary containing the keys "Connections" and "Games", where the 
values for each are lists containing their connections and prefered games respectively.

2. The procedures following the create_data_structure procedure are now more modular:
instead of getting the connections of a user like before, we now simply call the 
procedure 'get_connections' on that user.

3.find_path procedure changed in order to pass the new autograder.

4. Different MYOP: it now computes the clustering coefficient of the network.
This is explained below.

5. More comments explaining the logic and functionality of the code.

6. Three relevant updates included.

7. get_secondary_connections changed to also include the user themselves as a secondary connection if they are one,
as it would not pass the updated autograder otherwise.

"""

# ----------------------------------------------------------------------------- 
# create_data_structure(string_input): 
#   Parses a block of text (such as examnple_input above) and stores relevant 
#   information into a data structure (a dictionary). If the input is an empty string,
#   we return an empty dictionary.
# 
# Arguments: 
#   string_input: block of text containing the network information
# 
# Returns: 
#   The new network data structure (a dictionary)

# Helper procedure: Extracts all the names in order from string_input, and puts each one into a list as a string
def extract_names(string_input): 
	names = []
	list_of_sentences = string_input.split(".") # splits the input string into individual sentences
	every_second_sentence = list_of_sentences[::2] # we loop through every second sentence to extract the names: quicker
	for sentence in every_second_sentence:
		name = sentence[0:sentence.find(" ")] # isolates the user's name
		if len(name) > 0 and name not in names:
			names.append(name) #adds the users's name to our list of names (only if it not an empty string and isn't already there)
	return names

# Helper procedure: all connections for each person are put into a single string (with commas etc); same for games
def extract_con_and_games(string_input): 
    con_initial = []
    games_initial = []
    list_of_sentences = string_input.split(".") # splits the input string into individual sentences
    for sentence in list_of_sentences:
        if list_of_sentences.index(sentence) % 2 == 0: # to get the sentences listing the user's connections
            start_word = sentence.find("to") + 1  # finds the point in the sentence where th user's connections are given
            con_initial.append(sentence[start_word + len("to"):]) # adds every user's connections to the list, as a list
        else: # gets the sentences listing the user's preferred games
        	start_word = sentence.find("play") + 1 # finds the point in the sentence where the user's preferred games are given
        	games_initial.append(sentence[start_word + len("play"):]) # adds every user's games to the list, as a list
    return con_initial, games_initial

# Helper procedure: makes a proper list of connections and games for each person: each connection and game now an individual string
def get_con_and_games(string_input):
	connections = []
	games = []
	con_initial = extract_con_and_games(string_input)[0] # first return result of said procedure
	games_initial = extract_con_and_games(string_input)[1] # second returned result of said procedure
	for element in con_initial:
		if len(element) > 0: #makes sure we don't add an empty string
			connections.append([e.strip() for e in element.split(',')]) # removes whitespace
        else:
            connections.append([]) # creates an empty list of connections for the user if they have none
	for element in games_initial:
		if len(element) > 0: # same as above
			games.append([e.strip() for e in element.split(',')]) # removes whitespace
        else:
            games.append([]) # same as above
	return connections, games    	


# Creates a dictionary of the form: {<user_name>: {"Connections": [con_1, con_2], "Games": [game_1, game_2]}
def create_data_structure(string_input):
    if len(string_input) == 0: # ie is an empty string
	    network = {} # we return a dict with no users
    else:
    	names = extract_names(string_input)
        cons = get_con_and_games(string_input)[0] # first returned result from said procedure
        games = get_con_and_games(string_input)[1] # second returned result from said procedure
        network = {name: {"Connections": con, "Games": game} for (name, con, game) in zip(names, cons, games)} # maps each user to their lists of connections and games
    return network
  

# ----------------------------------------------------------------------------- # 
# Note that the first argument to all the procedures below is 'network' This is the #
# data structure that was created with the create_data_structure procedure,    #
# though it may be modified as we add new users or new connections. Each       #
# procedure below will then modify or extract information from 'network'        # 
# ----------------------------------------------------------------------------- #


# ----------------------------------------------------------------------------- 
# get_connections(network, user): 
#   Returns a list of all the connections a user has.
#
# Arguments: 
#   network: The network created with create_data_structure. 
#   user:    String containing the name of the user.
# 
# Returns: 
#   A list of all connections the user has. If the user has no connections, 
#   returns an empty list. We do not need to explicitly state this in the procedure, 
#   as if the user has no connections, create_data_structure will create an empty list for that user.
#   If the user is not in network, it returns None.  

net = create_data_structure(example_input)


def get_connections(network, user):
    if user in network:
        return network[user]["Connections"]
    else:
        return None



# -------------------------------------------------------------
# get_games_liked(network, user): 
#   Returns a list of all the games a user likes
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all games the user likes.
#   - If the user likes no games, return an empty list:
#     we don't need to specify this: this is implicit 
#     in how the network data structure is built
#   - If the user is not in network, return None.

def get_games_liked(network,user):
	if get_connections(network, user) != None: # ie if user exists in network
		return network[user]["Games"] # returns their list of games
	else: # ie user doesn't exist in network
		return None


# ----------------------------------------------------------------------------- 
# add_connection(network, user_A, user_B): 
#   Adds a connection from user_A to user_B i.e. adds user_B as a connection of user_A (user_B is added to 
#   the list of User_A's connections). Makes sure to check that both users exist in network.
# 
# Arguments: 
#   network: The network created with create_data_structure. 
#   user_A:  String with the name of the user (e.g. "Gary")
#   user_B:  String with the name of the user that will be the new connection.
#
# Returns: 
#   The updated network with the new connection added (if necessary), or False 
#   if user_A or user_B do not exist in network.

def add_connection(network, user_A, user_B):
    if get_connections(network, user_A) != None and get_connections(network, user_B) != None: # ie if both users exist in the network
        if user_B == user_A: # user is trying to add themselves
            print "You cannot add yourself as a connection!"
            return
        else:
            if user_B not in get_connections(network, user_A): # if user_B is not already connected to user_A
                get_connections(network, user_A).append(user_B) # add user_B as a connection of user_A's; to their list of connections
                return network
    else:
        return False # if one of or both user_A and user_B don't exist in the network





# ----------------------------------------------------------------------------- 
# add_new_user(network, user, games): 
#   Creates a new user profile and adds that user to the network, along with
#   any game preferences specified in games. We assume that the user has no 
#   connections to begin with, so we create an empty list for connections, while
#   their prefered games are put in a list mapped to the key "Games".
# 
# Arguments:
#   network: The network you created with create_data_structure. 
#   user:    String containing the users name to be added (e.g. "Dave")
#   games:   List containing the user's favorite games, e.g.:
#            ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
#
# Returns: 
#   The updated network with the new user and game preferences added. 
#   If the user is already in the network, we return network unchanged.


def add_new_user(network, user, games):
    if get_connections(network, user) == None: # ie if the user does not yet exist in the network
        network[user] = {"Connections": [], "Games": games}
    return network
	
# ----------------------------------------------------------------------------- 
# get_secondary_connections(network, user): 
#   Finds all the secondary connections, i.e. connections of connections, of a 
#   given user.
# 
# Arguments: 
#   network: The network you created with create_data_structure. 
#   user:    String containing the name of a user.
#
# Returns: 
#   A list containing the secondary connections (connections of connections).
#   If the user is not in the network, return None. If a user has no primary 
#   connections to begin with, you should return an empty list.
# 
# NOTE: 
# The list will contain a user's primary connection that is a secondary connection as well.


def get_secondary_connections(network, user):
    sec_cons = []
    if get_connections(network, user) != None: # ie if the user exists in the network
        for prim_name in get_connections(network, user):
            for sec_name in get_connections(network, prim_name):
                # if the user has not alreday been included in the secondary connections list, 
                # is not the user themselves, and is not a primary connection, 
                # we add it to the list of secondary connections
                if sec_name not in sec_cons and sec_name not in get_connections(network, user):
                    sec_cons.append(sec_name) 
    else:
        return None
    return sec_cons


# -----------------------------------------------------------------------------     
# connections_in_common(network, user_A, user_B): 
#   Finds the number of people that user_A and user_B have in common.
#  
# Arguments: 
#   network: The network you created with create_data_structure. 
#   user_A:    String containing the name of user_A.
#   user_B:    String containing the name of user_B.
#
# Returns: 
#   The number of connections in common (integer). Returns False if 
#   user_A or user_B are not in network.

def connections_in_common(network, user_A, user_B):
    connections_in_common = 0 # we add to this number each time we find a connection in common, and return the final result
    if get_connections(network, user_A) != None and get_connections(network, user_B) != None: # ie if both users exist in the network
        for connection in get_connections(network, user_A): # goes through each connection of user_A
            if connection in get_connections(network, user_B): # checks if it is in user_B's list of connections ie if it is also connected to user_B
                connections_in_common += 1 # if it is, we add 1 to connections_in_common
    else:
        return False # if one of or both user_A and user_B don't exist in the network
    return connections_in_common

# ----------------------------------------------------------------------------- 
# path_to_friend(network, user_A, user_B): 
#   Finds the shortest connections path from user_A to user_B. It has to be an existing path.
#   
# Arguments:
#   network: The network you created with create_data_structure. 
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
# 
# Returns:
#   A List showing the path from user_A to user_B. If such a path does not 
#   exist, returns None
#
# Sample output:
#   >>> print path_to_friend(network, "Abe", "Zed")
#   >>> ['Abe', 'Gel', 'Sam', 'Zed']
#   This implies that Abe is connected with Gel, who is connected with Sam, 
#   who is connected with Zed.


"""
# Old version: returns a path of connections from user_A to user_B
def path_to_friend(network, user_A, user_B, path=[]):
    user_A_connections = get_connections(network, user_A)
    path = path + [user_A]
    if user_A not in network:
        return None
    if user_A == user_B:
        return path 
    for connection in user_A_connections: # loops through user A's connections
        if connection not in path:  # makes sure we haven't checked this connection before (avoids continous loop)
            newpath = path_to_friend(network, connection, user_B, path)
            if newpath: # if True; if we did not get None
                return newpath
    return None # if the first if statement in the for loop above is not executed; means there is no path
"""


# New version: returns a path of connections from user_A to user_B
def path_to_friend(network, user_A, user_B, path=None):
    if user_A == user_B:
        return path # returns None
    if path is None:
        path = []
    path = path + [user_A]
    if user_A not in network:
        return None
    for connection in get_connections(network, user_A): # loops through user A's connections
        if connection not in path:  # makes sure we haven't checked this connection before (avoids continous loop)
            newpath = path_to_friend(network, connection, user_B, path + [connection])
            if newpath: # if True; if we did not get None
                for name in newpath:
                    if newpath.count(name) > 1:
                        newpath.remove(name)
                return newpath
    return None # if the first if statement in the for loop above is not executed; means there is no path



# -----------------------------------------------------------------------------
# Make-Your-Own-Procedure (MYOP): computing the network clustering coefficient

"""
A clustering coefficient is a measure of the degree to which nodes in a graph tend to cluster together. 

The local clustering coefficient of a vertex (node) in a graph quantifies how close 
its neighbors (immediate connections) are to being a clique (complete graph).
This computes to 1 if every neighbour connected to the input node is also 
connected to every other vertex/node within the neighbourhood of the input node 
(its immediate connections), and 0 if no vertex that is connected to the 
input node connects to any other vertex that is connected to the input node.

The clustering coefficient for the whole network is the average of the 
local clustering coefficients of all the vertices in the network.

We define a procedure for creating the local clustering coefficient for a particular node,
and then use this in the procedure below it to calculate the overall/average clustering coefficient.

A graph is considered small-world if its average clustering coefficient
is significantly higher than a random graph constructed on the same vertex set.

In summary, the clustering coefficient is the ratio of the number of actual edges there are
between neighbors to the number of potential edges there are between neighbors
(all possible edges between the vertices). This is seen in the second last line of
the local_clustering_coefficient procedure below. The clustering coefficient is therefore a real number 
between zero and one that is zero when there is no clustering, and one for maximal clustering.

For more information see: http://en.wikipedia.org/wiki/Clustering_coefficient
"""
# -----------------------------------------------------------------------------

# Helper procedure: computes the clustering coefficient for each node/user
# (also useful as a stand-alone procedure)
def local_clustering_coefficient(network, user):
    if len(get_connections(network, user)) == 1: # ie if user has only one connection
        return 0.0
    links = 0
    for w in get_connections(network, user): # goes through all neighbors
        for u in get_connections(network, user): # goes through each pair of neighbors
            if u in get_connections(network, w): # checks for each user whether they are in every other user's connections list
                links += 0.5 # if so, we add 0.5 to links
    local_cc = 2.0*links/(len(neighbors)*(len(neighbors)-1)) # explained above in docstring
    return local_cc

# MYOP: computes the network average clustering coefficient
def average_clustering_coefficient(network):
    total = 0
    for user in network.keys(): # ie for every user/key in the network dictionary
        total += local_clustering_coefficient(network, user) # adds to total the clustering coefficient of each and every user
    total_cc = total/len(network) # gives us the average clustering coefficient
    return total_cc



