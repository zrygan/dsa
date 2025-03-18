import typing
import re

class Node:
    def __init__(self, number_of_fields: int, field_name_values: dict):
        self.fields = {} 
        self.version = 0
        self.back_pointers = [None] * number_of_fields
        self.mods = [None] * 2 *  number_of_fields
        self.number_of_fields = number_of_fields
        
        self.populate(field_name_values)

    def populate(self, field_name_values: dict):
        for key, value in field_name_values.items():
            self.fields[key] = value

    def check_if_full(self):
        if len(self.mods) == 2 * self.number_of_fields:
            return True
        
        return False
    
    def read_field(self, key: str):
        if key in self.fields.keys():
            return self.fields[key]
        else:
            return None
    
    def update_field(self, key: str, value):
        self.fields[key] = value


class Partially_Persistent:
    def __init__(self, number_of_fields: int, root_field_values: list):
        self.number_of_fields = number_of_fields
        self.check_number_of_fields(root_field_values)
        self.nodes = {}
        self.root = None
        self.create_root_node(root_field_values)

    def create_root_node(self, root_field_values: dict) -> Node:
        self.root = Node(self.number_of_fields, root_field_values)
        self.nodes.update({"root": self.root})

    def create_node(self, node_name: str, field_name_values: dict) -> None:
        self.check_number_of_fields(field_name_values)
        self.nodes.update(
            {node_name: Node(self.number_of_fields, field_name_values)}
        )

        self.update_nodes()

    def check_number_of_fields(self, num: int) -> bool:
        if len(num) != self.number_of_fields:
            raise Exception("Number of fields is not equal to the "
                            "number of fields of the root node."
                            "<number_of_fields must be == len(root_field_values)>")
    
    def read_node(self, node_name: str) -> Node:
        if node_name not in self.nodes.keys():
            return False
        
        return self.nodes[node_name]
    
    def update_nodes(self) -> None:
        # iterate through every node in the DS
        for _, node in self.nodes.items():

            # iterate through every field of that node
            for key, value in node.fields.items():

                # if the value of that field is a temporary node pointer
                if isinstance(value, str) and value.startswith("@"):
                    # Remove '@' and any whitespace
                    node_name = value[1:].strip()  
                    if node_name in self.nodes:
                        node.fields[key] = self.nodes[node_name]  # Replace with actual node reference
                    
# x = Partially_Persistent(3, {
#                              "1" : 1, 
#                              "2" : "@ Node 2", # pointer to Node 2, but it does not exist yet
#                              "3" : 3
#                              })
# x.create_node("Node 2", {"1": 1, "2": 2, "3": 3})

# root = x.read_node("root")
# print(root.read_field("2"))
