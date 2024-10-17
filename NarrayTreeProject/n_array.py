from exceptions import TreeValueDoesNotExist, TreeIllegalValue


class NArray:
    """
       A class representing an N-ary tree.
    """
    def __init__(self, entry):
        """
            Initialize an NArray object with an entry value and children.

            Args:
                entry: The entry value for the node.
        """
        self.entry = entry  # Set the entry value for the node
        self.children = [None] * 4  # Initialize an array to hold child nodes

    def __str__(self):
        """
           Return a string representation of the NArray object.
        """
        args = ""
        if self.children[0]:
            args += f"{self.children[0]}"  # Add the string representation of the first child
        if self.children[1]:
            if self.children[0] is None:
                args += f"{self.children[1]}"  # Add the string representation of the second child
            else:
                args += f";{self.children[1]}"  # Add the string representation of the second child
        if self.children[2]:
            if self.children[0] is None and self.children[1] is None:
                args += f"{self.children[2]}"  # Add the string representation of the third child
            else:
                args += f";{self.children[2]}"  # Add the string representation of the third child
        if self.children[3]:
            if self.children[0] is None and self.children[1] is None and self.children[2] is None:
                args += f"{self.children[3]}"  # Add the string representation of the fourth child
            else:
                args += f";{self.children[3]}"  # Add the string representation of the fourth child
        return f"<{self.entry}>[{args}]"  # Return the formatted string representation

    def __repr__(self):
        """
            Return a string representation of the NArray object for debugging purposes.
        """
        args = ""
        if self.children[0]:
            args += f",{repr(self.children[0])}"  # Add the representation of the first child
        if self.children[1]:
            args += f",{repr(self.children[1])}"  # Add the representation of the second child
        if self.children[2]:
            args += f",{repr(self.children[2])}"  # Add the representation of the third child
        if self.children[3]:
            args += f",{repr(self.children[3])}"  # Add the representation of the fourth child
        return f'NArry({self.entry}{args})'  # Return the formatted string representation

    def insert(self, value):
        """
            Insert a value into the N-ary tree.

            Args:
                value: The value to be inserted.
        """
        # Insert a value into the N-ary tree.
        # If the current node is None, create a new node with the given value.
        if self is None:
            return NArray(value)

        # If the value is less than the current entry, handle cases based on the children's states.
        if value < self.entry:
            # If the first child is None, insert the value as the first child.
            if self.children[0] is None:
                self.children[0] = NArray(value)
            # If the second child is None, insert the value as the second child.
            elif self.children[1] is None:
                # If the value is less than the first child's entry, rearrange the nodes accordingly.
                if self.children[0].entry < value:
                    self.children[1] = NArray(value)
                elif value < self.children[0].entry:
                    self.children[1] = NArray(self.children[0].entry)
                    self.children[0] = NArray(value)
            # Recursively insert the value into the first child.
            else:
                if value < self.children[1].entry:
                    self.children[0].insert(value)
                elif self.children[1].entry < value:
                    self.children[1].insert(value)

        # If the value is greater than the current entry, handle cases based on the children's states.
        elif self.entry < value:
            # If the third child is None, insert the value as the third child.
            if self.children[2] is None:
                self.children[2] = NArray(value)
            # If the fourth child is None, insert the value as the fourth child.
            elif self.children[3] is None:
                # If the value is greater than the third child's entry, rearrange the nodes accordingly.
                if self.children[2].entry < value:
                    self.children[3] = NArray(value)
                elif value < self.children[2].entry:
                    self.children[3] = NArray(self.children[2].entry)
                    self.children[2] = NArray(value)
            # Recursively insert the value into the third child.
            else:
                if value < self.children[3].entry:
                    self.children[2].insert(value)
                elif self.children[3].entry < value:
                    self.children[3].insert(value)
        return self

    def delete(self, value):
        """
            Delete a value from the N-ary tree.

            Args:
                value: The value to be deleted.
        """
        # Check if the current node is None
        if self is None:
            return

        # If the value is less than the current entry, handle cases based on the children's states.
        if value < self.entry:
            # If the first child is None, raise an exception as the value doesn't exist in the tree.
            if self.children[0] is None:
                raise TreeValueDoesNotExist(value)
            # If the second child is None, perform deletion based on the first child.
            elif self.children[1] is None:
                # If the value is not present or already deleted in the first child, raise an exception.
                if value < self.children[0].entry or self.children[0].entry < value:
                    self.children[0].delete(value)
                # If the value is present and not deleted in the first child, handle deletion or raise an exception.
                else:
                    # If all children of the first child are None, delete the first child.
                    if all(child is None for child in self.children[0].children):
                        self.children[0] = None
                    else:
                        raise TreeIllegalValue(value)
            # If both children are present, recursively search and delete the value.
            else:
                # Perform deletion based on the first and second children.
                if value < self.children[0].entry:
                    self.children[0].delete(value)
                elif self.children[0].entry < value:
                    # If the value is present in the second child, delete it or raise an exception.
                    if value < self.children[1].entry:
                        self.children[0].delete(value)
                    elif self.children[1].entry < value:
                        self.children[1].delete(value)
                    else:
                        # If all children of the second child are None, delete the second child.
                        if all(child is None for child in self.children[1].children):
                            self.children[1] = None
                        else:
                            raise TreeIllegalValue(value)
                else:
                    # If all children of the first child are None, delete the first child.
                    if all(child is None for child in self.children[0].children):
                        self.children[0] = None
                    else:
                        raise TreeIllegalValue(value)
        # If the value is greater than the current entry, handle cases based on the children's states.
        elif self.entry < value:
            # Handle cases where the third and fourth children are None.
            if self.children[2] is None:
                raise TreeValueDoesNotExist(value)
            elif self.children[3] is None:
                # If the value is not present or already deleted in the third child, raise an exception.
                if value < self.children[2].entry or self.children[2].entry < value:
                    self.children[2].delete(value)
                # If the value is present and not deleted in the third child, handle deletion or raise an exception.
                else:
                    # If all children of the third child are None, delete the third child.
                    if all(child is None for child in self.children[2].children):
                        self.children[2] = None
                    else:
                        raise TreeIllegalValue(value)
            else:
                # Perform deletion based on the third and fourth children.
                if value < self.children[2].entry:
                    self.children[2].delete(value)
                elif self.children[2].entry < value:
                    # If the value is present in the fourth child, delete it or raise an exception.
                    if value < self.children[3].entry:
                        self.children[2].delete(value)
                    elif self.children[3].entry < value:
                        self.children[3].delete(value)
                    else:
                        # If all children of the fourth child are None, delete the fourth child.
                        if all(child is None for child in self.children[3].children):
                            self.children[3] = None
                        else:
                            raise TreeIllegalValue(value)
                else:
                    # If all children of the third child are None, delete the third child.
                    if all(child is None for child in self.children[2].children):
                        self.children[2] = None
                    else:
                        raise TreeIllegalValue(value)
        # If the value matches the current entry, handle deletion or raise an exception.
        else:
            # If all children are None, set the current node to None.
            if all(child is None for child in self.children):
                self = None
            else:
                raise TreeIllegalValue(value)
