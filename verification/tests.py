"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[("+a", 7), ("-b", 8), ("*a", 10)]],
            "answer": {"a": 70, "b": -8}
        },
        {
            "input": [[]],
            "answer": {}
        },
        {
            "input": [[('+a', 5), ('+a', -5), ('-a', 5), ('-a', -5)]],
            "answer": {}
        },
        {
            "input": [[('*a', 0), ('=a', 0), ('/a', 0), ('-a', -5)]],
            "answer": {"a": 5}
        }
    ],
    "Extra": [
        {
            "input": [[("+a", 0), ("*b", 0), ("+", 35)]],
            "answer": {}
        },
        {
            "input": [[("+a", -5), ("-aa", -20), ("*aa", 5)]],
            "answer": {"a": -5, "aa": 100}
        },
        {
            "input": [[("+a", 5), ("*a", 6), ("/a", 3), ("=a", 3)]],
            "answer": {"a": 3}
        },
        {
            "input": [[("+a", 5), ("*a", 0)]],
            "answer": {}
        }
    ]
}
