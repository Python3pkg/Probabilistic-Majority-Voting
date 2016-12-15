# Probabilistic Majority Voting
Generic Majority Judgement Voting procedure for probabilities of categories in machine learning

<br>

## Usage
To install through PyPI

    pip install majorityvoting

And to use majority judgement voting in your code

    from majorityvoting import MajorityVoting

    voter = MajorityVoting.Voter(probabilities, categories)
    indices, names = voter.vote(windows=5)

The initializer takes in 2 arguments
* probabilities - a `numpy.ndarray` of lists (2d array) with equal length, each embedded list contains the probability of categories predicted by some machine learning algorithm, exactly the same you will get from [sklearn](http://scikit-learn.org/stable/)'s `predict_proba()` function
* categories - a list of names of categories, each category must match the index of it's probability in each and every embedded list in `probabilities`

## TODOs
1. It's a pain to manually check the size of the lists and embedded ones, will require input argument to be `pandas.DataFrame` type in the next version
