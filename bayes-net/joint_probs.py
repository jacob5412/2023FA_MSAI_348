"""
Code for join probabilities
"""
import copy

from bayesnet import BayesNet


def ask(var: str, value: bool, evidence: dict, bn: BayesNet) -> float:
    """
    Calculate conditional probability P(var = value | evidence) using Bayesian
    Network.

    Args:
        var (str): The variable for which the conditional probability is
        calculated.
        value (bool): The desired value of the variable (True or False).
        evidence (dict): A dictionary of known evidence variables and their
        values.
        bn (BayesNet): The Bayesian Network.

    Returns:
        float: The conditional probability P(var = value | evidence).
    """
    probabilities = {}
    for val in [True, False]:
        evidence[var] = val
        probabilities[val] = calculate_joint_probability(
            bn.variable_names, evidence, bn
        )
    return probabilities[value] / sum(probabilities.values())


def calculate_joint_probability(variables: list, evidence: dict, bn: BayesNet) -> float:
    """
    Calculate the joint probability of a set of variables given evidence in a
    Bayesian Network.

    Args:
        variables (list): A list of variables for which to calculate the joint
        probability.
        evidence (dict): A dictionary of known evidence variables and their
        values.
        bn (BayesNet): The Bayesian Network.

    Returns:
        float: The joint probability of the specified variables given the
        evidence.
    """
    if len(variables) == 0:
        return 1.0

    # calculate current node's probability
    current_var = variables[0]
    current_node = bn.get_var(current_var)

    if current_var in evidence:
        return current_node.probability(
            evidence[current_var], evidence
        ) * calculate_joint_probability(variables[1:], evidence, bn)

    # if variable doesn't exist in evidence, enumerate all probs
    evidence_true = copy.deepcopy(evidence)
    evidence_true[current_var] = True
    evidence_false = copy.deepcopy(evidence)
    evidence_false[current_var] = False
    return (
        current_node.probability(True, evidence)
        * calculate_joint_probability(variables[1:], evidence_true, bn)
    ) + (
        current_node.probability(False, evidence)
        * calculate_joint_probability(variables[1:], evidence_false, bn)
    )
