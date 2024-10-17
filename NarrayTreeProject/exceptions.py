
class TreeError(Exception):
    """
        Base class for exceptions related to a tree data structure.
    """
    def __init__(self, value):
        """
            Initialize a TreeError object with a specific value.

            Args:
                value: The value associated with the exception.
        """
        self.value = value

    def handel(self):
        """
            Handle the exception. This method should be overridden by subclasses.
        """
        pass


class TreeValueDoesNotExist(TreeError):
    """
       Exception raised when a value does not exist in the tree.
    """
    def handel(self):
        """
            Handle the exception by printing a message.
        """
        print(self.value, "does not valid, because it does not exist in the array tree!")


class TreeIllegalValue(TreeError):
    """
       Exception raised when a value is not a valid leaf in the tree.
    """
    def handel(self):
        """
            Handle the exception by printing a message.
        """
        print(self.value, "does not valid, because it does not a leaf!")
