class User():

    def __init__(self, id, firstName, lastName, isAdmin, orderId, email = "", password = ""):
        self.id = id
        self.email = email 
        self.password = password
        self.firstName = firstName
        self.lastName = lastName
        self.isAdmin = isAdmin
        self.orderId = orderId