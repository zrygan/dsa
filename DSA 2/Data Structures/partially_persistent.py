import copy


class Partially_Persistent_Node:
    def __init__(self, number_of_fields: int, field_name_values: dict):
        self.fields = {}
        self.version_counter = 0
        self.versions = {}
        self.back_pointers = [None] * number_of_fields
        self.mods = [None] * 2 * number_of_fields
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

    def read_field_at_version(self, key: str, version: int):
        if self.version_counter < version or key not in self.fields.keys():
            return None

        return self.versions[version].fields[key]

    def update_field(self, key: str, value):
        old_Partially_Persistent_Node = copy.deepcopy(self)
        self.version_counter += 1
        self.versions.update({self.version_counter: old_Partially_Persistent_Node})
        self.fields[key] = value


class Partially_Persistent:
    def __init__(self, number_of_fields: int, root_field_values: list):
        self.number_of_fields = number_of_fields
        self.check_number_of_fields(root_field_values)
        self.Partially_Persistent_Nodes = {}
        self.root = None
        self.create_root_Partially_Persistent_Node(root_field_values)

    def create_root_Partially_Persistent_Node(
        self, root_field_values: dict
    ) -> Partially_Persistent_Node:
        self.root = Partially_Persistent_Node(self.number_of_fields, root_field_values)
        self.Partially_Persistent_Nodes.update({"root": self.root})

    def create_Partially_Persistent_Node(
        self, Partially_Persistent_Node_name: str, field_name_values: dict
    ) -> None:
        self.check_number_of_fields(field_name_values)
        self.Partially_Persistent_Nodes.update(
            {
                Partially_Persistent_Node_name: Partially_Persistent_Node(
                    self.number_of_fields, field_name_values
                )
            }
        )

        self.update_Partially_Persistent_Nodes()

    def check_number_of_fields(self, num: int) -> bool:
        if len(num) != self.number_of_fields:
            raise Exception(
                "PARTIALLY PERSISTENT [Error 1]. "
                "Number of fields is not equal to the "
                "number of fields of the root Partially_Persistent_Node. "
                "<number_of_fields must be == len(root_field_values)>"
            )

    def read_Partially_Persistent_Node(
        self, Partially_Persistent_Node_name: str, version: int = None
    ) -> Partially_Persistent_Node:
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

    def update_Partially_Persistent_Nodes(self) -> None:
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
