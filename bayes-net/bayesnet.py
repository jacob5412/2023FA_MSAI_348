"""
Bayesian Network Module

This module contains classes to create and manipulate Bayesian Networks, a probabilistic graphical model representing
uncertain relationships between variables. It includes classes:
    - BayesNet: Represents the Bayesian Network structure and operations to add nodes.
    - BayesNode: Represents nodes in the Bayesian Network, storing probabilities and relationships.

Usage:
1. Create a BayesNet object: net = BayesNet()
2. Create BayesNode objects: node = BayesNode(name, parents, values)
3. Add nodes to the network: net.add(node)
4. Perform operations like retrieving variables: net.get_var(name)

Example:
net = BayesNet()
node_A = BayesNode('A', None, {'': 0.7, 'T': 0.3})
node_B = BayesNode('B', ['A'], {'T': 0.9, 'F': 0.1})
net.add(node_A)
net.add(node_B)
variable_A = net.get_var('A')

This module provides tools to construct and work with Bayesian Networks for probabilistic reasoning and decision-making.
"""

class BayesNet:
    """
    Represents a Bayesian Network.

    Attributes:
        variables (list): List of BayesNode objects representing variables in the network.
        variable_names (list): List of names of variables in the network.
    """
    def __init__(self):
        """
        Initializes an empty Bayesian Network.
        """
        self.variables = []
        self.variable_names = []

    def add(self, node):
        """
        Adds Bayes Node to Bayes Net.

        Parameters:
            node (BayesNode): Node to be added to the Bayes Net.

        Returns:
            None
        """
        if node.parents is None:
            self.variables.append(node)
            self.variable_names.append(node.name)
        else:
            for p in node.parents:
                if p not in self.variable_names:
                    print("Parent must be added to Net first")
                    return
            self.variables.append(node)
            self.variable_names.append(node.name)

    def get_var(self, name):
        """
        Gets a Bayes Net variable.

        Parameters:
            name (String): Name of the variable.

        Returns:
            Object
        """
        print("getting", name)
        for v in self.variables:
            if v.name == name:
                return v
        print("None found")


class BayesNode:
    """
    Represents a node in a Bayesian Network.

    Attributes:
        name (str): Name of the node.
        parents (list): List of parent nodes' names.
        values (dict): Probabilities associated with different states of the node.
    """
    def __init__(self, name, parents, values):
        """
        Initializes a Bayes Node.

        Parameters:
            name (str): Name of the node.
            parents (list): List of parent nodes' names.
            values (dict): Probabilities associated with different states of the node.
        """
        self.name = name
        self.parents = parents
        self.values = values

    def __str__(self):
        """
        Returns a string representation of the BayesNode.

        Returns:
            str
        """
        return "({}, {}, {})".format(self.name, self.parents, self.values)

    def repr(self):
        """
        Returns a string representation of the BayesNode.

        Returns:
            str
        """
        return "({}, {}, {})".format(self.name, self.parents, self.values)

    def probability(self, hypothesis, evidence):
        """
        Calculates the associated joint probability

        Parameters:
            hypothesis (Boolean): is the hypothesis True or False?
            evidence (Array): facts about the world state

        Returns:
            Float
        """
        if self.parents is None:
            v = self.values[""]
        elif len(self.parents) == 1:
            v = self.values[evidence[self.parents[0]]]
        else:
            key = []
            for p in self.parents:
                if p in evidence:
                    key.append(evidence[p])
            v = self.values[tuple(key)]
        if hypothesis:
            return v
        else:
            return 1 - v
