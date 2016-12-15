# Probabilistic Majority Voting
Generic Majority Judgement Voting procedure for probabilities of categories in machine learning

<br>

## Usage
This is not important enough to go in `pip`, at least I don't think it is, so you'll have to put the source files/folder in correct directory and import the module to use it

    from majorityvoting import MajorityVoting

    voter = MajorityVoting.Voter(probabilities, categories)
    indices, names = voter.vote(windows=5)

The initializer takes in 2 arguments
* probabilities - a `numpy.ndarray` of lists (2d array) with equal length, each embedded list contains the probability of categories predicted by some machine learning algorithm, exactly the same you will get from [sklearn](http://scikit-learn.org/stable/)'s `predict_proba()` function
* categories - a list of names of categories, each category must match the index of it's probability in each and every embedded list in `probabilities`

## TODOs
1. It's a pain to manually check the size of the lists and embedded ones, will require input argument to be `pandas.DataFrame` type in the next version 
2. Window size only supports odd numbers, maybe I actually will not support even numbers, who knows, I need to learn more
3. When there is multiple majority, the algorithm automatically abandons everything and start from scratch to look for a popular candidate, I might, in future versions, extract the tied candidates and only compare the popular votes of those ones, although most of the cases this is not going to make a difference
