"""
Code for Naive Bayes
"""
import math
import re


class NaiveBayesClassifier:
    def __init__(self) -> None:
        """
        Initialize a Bayes Classifier with dictionaries to store class
        probabilities and token probabilities.

        Attributes:
            prior_probs: log of overall class (ratings) probabilities.
            likelihood_probs: token <> rating likelihood probabilities.
        """
        self.prior_probs: dict[str, float] = {}
        self.likelihood_probs: dict[str, dict[str, float]] = {}

    def train(self, lines: list) -> None:
        """
        Train the Bayes Classifier on the provided list of lines.

        Args:
            lines (list): A list of training data in the format
            "rating|ID|text".
        """
        for line in lines:
            rating, _, text = self._split_data(line)
            tokens = self._preprocess_data(text)
            self._initialize_frequencies(rating, tokens)
        self._calculate_probs()

    def classify(self, lines: list) -> list:
        """
        Classify a list of lines using the trained Bayes Classifier.

        Args:
            lines (list): A list of data to be classified in the format
            "rating|ID|text".

        Returns:
            list: A list of predicted ratings.
        """
        results = []
        for line in lines:
            rating, _, text = self._split_data(line)
            tokens = self._preprocess_data(text)

            posterior_probs = self._initialize_posterior_probs()

            # Calculate overall posterior probabilities
            for rating in posterior_probs:
                for token in tokens:
                    # if token is missing, give it 0 probability
                    posterior_probs[rating] += math.log(
                        self.likelihood_probs.get(token, {}).get(rating, 1)
                    )

            # Determine the predicted classes based on max posterior
            # probability of classes/ratings
            predicted_class = max(
                posterior_probs,
                key=lambda rating: posterior_probs[rating],
            )
            results.append(f"{predicted_class}")

        return results

    def _initialize_frequencies(self, rating: str, tokens: list) -> None:
        """
        Create a frequency table of rating and token <> rating frequencies.

        Args:
            rating (str): The rating of the current data.
            tokens (list): The preprocessed tokens from the data's text.
        """
        # if class/rating doesn't exist, initialize it; else, sum accross
        if rating not in self.prior_probs:
            self.prior_probs[rating] = 1
        else:
            self.prior_probs[rating] += 1

        # Calculate the likelihood probabilities for each token in the
        # movie title given the class
        for token in tokens:
            if token not in self.likelihood_probs:
                self.likelihood_probs[token] = {}
            if rating not in self.likelihood_probs[token]:
                self.likelihood_probs[token][rating] = 1
            else:
                self.likelihood_probs[token][rating] += 1

    def _calculate_probs(self) -> None:
        """
        Calculate the prior probabilities and the likelihood
        probabilities.
        """
        # Calculate prior/rating probabilities or prior probabilities
        total_reviews = sum(self.prior_probs.values())
        for rating, frequency in self.prior_probs.items():
            self.prior_probs[rating] = frequency / total_reviews

        # Calculate likelihoods for each token ~ P(token|rating)
        for _, ratings in self.likelihood_probs.items():
            for rating, frequency in ratings.items():
                ratings[rating] = frequency / self.prior_probs[rating]

    @staticmethod
    def _split_data(line: str) -> list:
        """
        Extract labels and line from a given input line.

        Args:
            line (str): A line in the format "rating|ID|text".

        Returns:
            list: A list containing the rating and text.
        """
        return line.split("|")

    def _preprocess_data(self, text: str) -> list:
        """
        Preprocess the given text by removing punctuation, converting to
        lowercase, and removing stop tokens.

        Args:
            text (str): The input text to be preprocessed.

        Returns:
            list: A list of preprocessed tokens.
        """
        # Remove punctuation, commas, apostrophes
        text = re.sub(r"[^\w\s]", "", text)

        # Remove capitalization and split tokens
        tokens = text.lower().split()

        # Stoptoken removal
        stoptokens = set(
            ["the", "and", "is", "in", "it", "of", "a", "an", "as", "at", "be", "for"]
        )
        tokens = [token for token in tokens if token not in stoptokens]

        return tokens

    def _initialize_posterior_probs(self) -> dict:
        """
        Initialize by taking a log of all the rating/prior probabilities and
        converting them into log space. (This way we can add probabilities).

        Returns:
            dict: A dictionary with log probabilities for each rating.
        """
        return {
            rating: math.log(self.prior_probs[rating]) for rating in self.prior_probs
        }
