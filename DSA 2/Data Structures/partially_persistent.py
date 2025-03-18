import copy

"""
The TT : Zhean Ganituen (2025)

Partially Persistent Data Structure Implementation

A partially persistent data structure allows access to all previous versions while
only permitting modifications to the most recent version. This implementation follows
the fat node method where each node stores a limited number of modifications directly.

This module provides classes for creating and managing partially persistent nodes and structures.
"""


class Partially_Persistent_Node:
    """
    A node in a partially persistent data structure.

    This class implements the 'fat node' technique for partial persistence, where each node
    maintains its own version history. It can store a limited number of modifications and
    allows field access across different versions.

    Attributes:
        fields (dict): Current field values of the node
        version_counter (int): Current version number of the node
        versions (dict): Dictionary mapping version numbers to node states
        back_pointers (list): References to previous node versions
        mods (list): List to track modifications (limited to 2 * number_of_fields)
        number_of_fields (int): Maximum number of fields this node can have
    """

    def __init__(self, number_of_fields: int, field_name_values: dict):
        """
        Initialize a new partially persistent node.

        Args:
            number_of_fields (int): Maximum number of fields this node can have
            field_name_values (dict): Initial values for each field, mapping field names to values
        """
        self.fields = {}
        self.version_counter = 0
        self.back_pointers = [None] * number_of_fields
        self.mods = [None] * 2 * number_of_fields
        self.number_of_fields = number_of_fields

        self.populate(field_name_values)

    def populate(self, field_name_values: dict):
        """
        Populate the node's fields with initial values.

        Args:
            field_name_values (dict): Dictionary mapping field names to their values
        """
        for key, value in field_name_values.items():
            self.fields[key] = value

    def check_if_full(self):
        """s
        Check if the node has reached its modification capacity.

        In the fat node method, we limit the number of modifications to 2 * number_of_fields
        to maintain amortized performance characteristics.

        Returns:
            bool: True if the node is full (can't store more modifications), False otherwise
        """
        for mod in self.mods:
            if mod is None:
                return False

        return True

    def read_field(self, key: str):
        """
        Read the value of a field from the current version of the node.

        Args:
            key (str): The field name to read

        Returns:
            The value of the field, or None if the field doesn't exist
        """
        if key in self.fields.keys():
            return self.fields[key]
        else:
            return None

    def read_field_at_most_version(self, key: str, version: int):
        """
        Read the value of a field at a specific version of the node; if it does
        not find a version with that version number, it will look for the first 
        one before it.

        Args:
            key (str): The field name to read
            version (int): The version number to read from

        Returns:
            The value of the field at the given version, or None if the field
            or version doesn't exist
        """
        # decrement the version, since mods is 0 indexed
        version -= version
        if (self.number_of_fields * 2 < version
            or key not in self.fields.keys()
        ):
            return None

        for i in range(version - 1, -1, -1):
            if (self.mods[i] != None):
                return self.mods[i][key]

    def read_field_at_version(self, key: str, version: int):
        """
        Read the value of a field at a specific version of the node.

        Args:
            key (str): The field name to read
            version (int): The version number to read from

        Returns:
            The value of the field at the given version, or None if the field
            or version doesn't exist
        """
        # decrement the version, since mods is 0 indexed
        version -= version

        if (self.number_of_fields * 2 < version
            or key not in self.fields.keys()
        ):
            return None

        return self.mods[version][key] if not None else None


    def update_field(self, key: str, value):
        """
        Update the value of a field in the node, creating a new version.

        This method creates a deep copy of the current node state before applying
        the update, allowing access to previous versions.

        Args:
            key (str): The field name to update
            value: The new value for the field
        """
        if self.check_if_full() is False:
            self.mods[self.version_counter] = {key: self.fields[key]}
            self.version_counter += 1
            self.fields[key] = value
        else:
            # TODO case for when mods is full
            pass

class Partially_Persistent:
    """
    A container class for managing a collection of partially persistent nodes.

    This class provides methods for creating, reading, and updating partially
    persistent nodes, as well as managing relationships between them.

    Attributes:
        number_of_fields (int): The number of fields each node should have
        Partially_Persistent_Nodes (dict): Dictionary mapping node names to node objects
        root (Partially_Persistent_Node): The root node of the structure
    """

    def __init__(self, number_of_fields: int, root_field_values: list):
        """
        Initialize a new partially persistent data structure.

        Args:
            number_of_fields (int): The number of fields each node should have
            root_field_values (list): The initial field values for the root node
        """
        self.number_of_fields = number_of_fields
        self.check_number_of_fields(root_field_values)
        self.Partially_Persistent_Nodes = {}
        self.root = None
        self.make_root(root_field_values)

    def make_root(self, root_field_values: dict) -> Partially_Persistent_Node:
        """
        Create and initialize the root node of the data structure.

        Args:
            root_field_values (dict): The initial field values for the root node

        Returns:
            Partially_Persistent_Node: The newly created root node
        """
        self.root = Partially_Persistent_Node(self.number_of_fields, root_field_values)
        self.Partially_Persistent_Nodes.update({"root": self.root})

    def make_node(
        self, Partially_Persistent_Node_name: str, field_name_values: dict
    ) -> None:
        """
        Create a new node in the data structure.

        Args:
            Partially_Persistent_Node_name (str): Name or identifier for the new node
            field_name_values (dict): Initial field values for the node
        """
        self.check_number_of_fields(field_name_values)
        self.Partially_Persistent_Nodes.update(
            {
                Partially_Persistent_Node_name: Partially_Persistent_Node(
                    self.number_of_fields, field_name_values
                )
            }
        )

        self.__update_node()

    def check_number_of_fields(self, num: int) -> bool:
        """
        Check if the number of fields matches the expected number.

        This ensures consistency in the number of fields across all nodes in the
        data structure.

        Args:
            num (int): The field values container to check

        Raises:
            Exception: If the number of fields doesn't match the expected number

        Returns:
            bool: True if validation passes (implicitly, as exceptions are raised otherwise)
        """
        if len(num) != self.number_of_fields:
            raise Exception(
                "PARTIALLY PERSISTENT [Error 1]. "
                "Number of fields is not equal to the "
                "number of fields of the root Partially_Persistent_Node. "
                "<number_of_fields must be == len(root_field_values)>"
            )

    def read_node(
        self, Partially_Persistent_Node_name: str, version: int = None
    ) -> Partially_Persistent_Node:
        """
        Read a node, optionally at a specific version.

        Args:
            Partially_Persistent_Node_name (str): The name of the node to read
            version (int, optional): The version to read. If None, returns the most recent version.

        Returns:
            Partially_Persistent_Node: The requested node, or False if not found
        """
        if version is None:
            # get the most recent
            if (
                Partially_Persistent_Node_name
                not in self.Partially_Persistent_Nodes.keys()
            ):
                return False

            return self.Partially_Persistent_Nodes[Partially_Persistent_Node_name]
        else:
            #   IF an nth version of that Partially_Persistent_Node exists DO
            #       RETURN that version of the Partially_Persistent_Node
            #   ELSE
            #       RETURN false
            if (
                Partially_Persistent_Node_name
                not in self.Partially_Persistent_Nodes.keys()
            ):
                return False

            Partially_Persistent_Node = self.Partially_Persistent_Node[
                Partially_Persistent_Node_name
            ].versions[version]
            return Partially_Persistent_Node if not None else False

    def __update_node(self) -> None:
        """
        NOT MEANT TO BE CALLED OUTSIDE THE CLASS (a helper function). 
        Maybe you want to use `update_field` instead.
        Resolve references between nodes in the data structure.

        This method processes string references that start with '@' and replaces them
        with actual node references, allowing nodes to reference each other.
        """
        # iterate through every Partially_Persistent_Node in the DS
        for _, Partially_Persistent_Node in self.Partially_Persistent_Nodes.items():

            # iterate through every field of that Partially_Persistent_Node
            for key, value in Partially_Persistent_Node.fields.items():

                # if the value of that field is a temporary Partially_Persistent_Node pointer
                if isinstance(value, str) and value.startswith("@"):
                    # Remove '@' and any whitespace
                    Partially_Persistent_Node_name = value[1:].strip()
                    if (
                        Partially_Persistent_Node_name
                        in self.Partially_Persistent_Nodes
                    ):
                        Partially_Persistent_Node.fields[key] = (
                            self.Partially_Persistent_Nodes[
                                Partially_Persistent_Node_name
                            ]
                        )  # Replace with actual Partially_Persistent_Node reference
