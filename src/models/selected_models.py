from catboost import CatBoostClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.ensemble import (
    GradientBoostingClassifier,
    RandomForestClassifier,
    AdaBoostClassifier,
    BaggingClassifier,
)
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.neural_network import MLPClassifier


RANDOM_STATE = 42

selected_models = [
    # Linear Models
    ("LDA", LinearDiscriminantAnalysis()),
    ("LOG", LogisticRegression(max_iter=1000, random_state=RANDOM_STATE)),
    ("SGD", SGDClassifier(loss="log_loss", max_iter=1000, random_state=RANDOM_STATE)),
    (
        "SVM",
        SVC(kernel="rbf", probability=True, random_state=RANDOM_STATE, cache_size=500),
    ),
    # Tree-based Models
    ("TREE", DecisionTreeClassifier(max_depth=6, random_state=RANDOM_STATE)),
    ("RF", RandomForestClassifier(n_estimators=100, max_depth=10, random_state=RANDOM_STATE)),
    (
        "BAG",
        BaggingClassifier(
            estimator=DecisionTreeClassifier(max_depth=6, random_state=RANDOM_STATE),
            n_estimators=50,
            random_state=RANDOM_STATE,
        ),
    ),
    # Boosting Models
    ("ADA", AdaBoostClassifier(n_estimators=50, random_state=RANDOM_STATE)),
    (
        "GBM",
        GradientBoostingClassifier(n_estimators=100, max_depth=5, random_state=RANDOM_STATE),
    ),
    (
        "XGB",
        XGBClassifier(
            n_estimators=100,
            max_depth=6,
            eval_metric="logloss",
            random_state=RANDOM_STATE,
        ),
    ),
    (
        "CAT",
        CatBoostClassifier(silent=True, n_estimators=100, depth=6, random_state=RANDOM_STATE),
    ),
    # Distance-based and Probability Models
    ("NB", GaussianNB()),
    ("KNN", KNeighborsClassifier(n_neighbors=15, weights="distance")),
    # Neural Network Models
    (
        "MLP",
        MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=1000, random_state=RANDOM_STATE),
    ),
]
