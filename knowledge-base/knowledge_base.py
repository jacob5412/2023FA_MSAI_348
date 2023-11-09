import copy

import read
from logical_classes import *
from util import *

verbose = 0


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules
        self.ie = InferenceEngine()

    def __repr__(self):
        return "KnowledgeBase({!r}, {!r})".format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def _get_fact(self, fact):
        """INTERNAL USE ONLY
        Get the fact in the KB that is the same as the fact argument

        Args:
            fact (Fact): Fact we're searching for

        Returns:
            Fact: matching fact
        """
        for kbfact in self.facts:
            if fact == kbfact:
                return kbfact

    def _get_rule(self, rule):
        """INTERNAL USE ONLY
        Get the rule in the KB that is the same as the rule argument

        Args:
            rule (Rule): Rule we're searching for

        Returns:
            Rule: matching rule
        """
        for kbrule in self.rules:
            if rule == kbrule:
                return kbrule

    def kb_add(self, fact_rule):
        """Add a fact or rule to the KB
        Args:
            fact_rule (Fact or Rule) - Fact or Rule to be added
        Returns:
            None
        """
        printv("Adding {!r}", 1, verbose, [fact_rule])
        if isinstance(fact_rule, Fact):
            if fact_rule not in self.facts:
                self.facts.append(fact_rule)
                for rule in self.rules:
                    self.ie.fc_infer(fact_rule, rule, self)
            else:
                if fact_rule.supported_by:
                    ind = self.facts.index(fact_rule)
                    for f in fact_rule.supported_by:
                        self.facts[ind].supported_by.append(f)
                else:
                    ind = self.facts.index(fact_rule)
                    self.facts[ind].asserted = True
        elif isinstance(fact_rule, Rule):
            if fact_rule not in self.rules:
                self.rules.append(fact_rule)
                for fact in self.facts:
                    self.ie.fc_infer(fact, fact_rule, self)
            else:
                if fact_rule.supported_by:
                    ind = self.rules.index(fact_rule)
                    for f in fact_rule.supported_by:
                        self.rules[ind].supported_by.append(f)
                else:
                    ind = self.rules.index(fact_rule)
                    self.rules[ind].asserted = True

    def kb_assert(self, fact_rule):
        """Assert a fact or rule into the KB

        Args:
            fact_rule (Fact or Rule): Fact or Rule we're asserting
        """
        printv("Asserting {!r}", 0, verbose, [fact_rule])
        self.kb_add(fact_rule)

    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Statement to be asked (will be converted into a Fact)

        Returns:
            listof Bindings|False - list of Bindings if result found, False otherwise
        """
        print("Asking {!r}".format(fact))
        if factq(fact):
            f = Fact(fact.statement)
            bindings_lst = ListOfBindings()
            # ask matched facts
            for fact in self.facts:
                binding = match(f.statement, fact.statement)
                if binding:
                    bindings_lst.add_bindings(binding, [fact])

            return bindings_lst if bindings_lst.list_of_bindings else []

        else:
            print("Invalid ask:", fact.statement)
            return []

    def kb_retract(self, fact_rule):
        """Retract a fact or a rule from the KB

        Args:
            fact_rule (Fact or Rule) - Fact or Rule to be retracted

        Returns:
            None
        """
        printv("Retracting {!r}", 0, verbose, [fact_rule])

        self._kb_retract_helper(fact_rule)

    def _kb_retract_helper(self, fact_rule, depth=0):
        # Fetch fact or rule from KB
        fact_rule = self._get_fact(fact_rule) or self._get_rule(fact_rule)

        # if the fact is asserted, don't remove it if it's a recursive removal
        if not fact_rule.asserted or depth == 0:
            if len(fact_rule.supported_by) != 0:
                fact_rule.asserted = False  # Inferred facts are unaffected
                return None
            if isinstance(fact_rule, Fact):
                self.facts.remove(fact_rule)
            elif isinstance(fact_rule, Rule):
                self.rules.remove(fact_rule)
        else:
            return None

        # Remove supported facts/rules
        for supports_fact_rule in fact_rule.supports_facts + fact_rule.supports_rules:
            for supported_by_fact_rule in supports_fact_rule.supported_by:
                supports_fact_rule = self._get_fact(
                    supports_fact_rule
                ) or self._get_rule(supports_fact_rule)
                if fact_rule in supported_by_fact_rule:
                    supports_fact_rule.supported_by.remove(supported_by_fact_rule)
                    self._kb_retract_helper(supports_fact_rule, depth + 1)


class InferenceEngine(object):
    def fc_infer(self, fact, rule, kb):
        """Forward-chaining to infer new facts and rules

        Args:
            fact (Fact) - A fact from the KnowledgeBase
            rule (Rule) - A rule from the KnowledgeBase
            kb (KnowledgeBase) - A KnowledgeBase

        Returns:
            Nothing
        """
        printv(
            "Attempting to infer from {!r} and {!r} => {!r}",
            1,
            verbose,
            [fact.statement, rule.lhs, rule.rhs],
        )

        lhs_statements = rule.lhs
        rhs_statement = rule.rhs
        associated_bindings = match(fact.statement, lhs_statements[0])

        # if no bindings, then exit
        if associated_bindings == False:
            return None

        # if LHS is only one statement
        elif len(lhs_statements) == 1:
            new_fact = Fact(
                statement=instantiate(rhs_statement, associated_bindings),
                supported_by=[[fact, rule]],
            )
            fact.supports_facts.append(new_fact)
            rule.supports_facts.append(new_fact)
            kb.kb_add(new_fact)

        # else go through LHS and RHS
        else:
            new_rule = Rule(
                rule=[
                    [
                        instantiate(lhs_statement, associated_bindings)
                        for lhs_statement in lhs_statements[1:]
                    ],
                    instantiate(rhs_statement, associated_bindings),
                ],
                supported_by=[[fact, rule]],
            )
            fact.supports_rules.append(new_rule)
            rule.supports_rules.append(new_rule)
            kb.kb_add(new_rule)
