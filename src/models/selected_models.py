from catboost import CatBoostClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.ensemble import (
    GradientBoostingClassifier,
    RandomForestClassifier,
    AdaBoostClassifier,
    VotingClassifier,
    StackingClassifier,
    BaggingClassifier,
)
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.neural_network import MLPClassifier


selected_models = [
    # Linear Models
    ("LDA", LinearDiscriminantAnalysis()),
    ("LOG", LogisticRegression(max_iter=1000, random_state=42)),
    ("SGD", SGDClassifier(loss="log_loss", max_iter=1000, random_state=42)),
    ("SVM", SVC(kernel="linear", probability=True, random_state=42, cache_size=500)),
    # Tree-based Models
    ("TREE", DecisionTreeClassifier(random_state=42)),
    ("RF", RandomForestClassifier(n_estimators=25, random_state=42)),
    (
        "BAG",
        BaggingClassifier(
            base_estimator=DecisionTreeClassifier(random_state=42),
            n_estimators=10,
            random_state=42,
        ),
    ),
    # Boosting Models
    ("ADA", AdaBoostClassifier(random_state=42)),
    ("GBM", GradientBoostingClassifier(n_estimators=25, random_state=42)),
    ("XGB", XGBClassifier(n_estimators=25, eval_metric="logloss", random_state=42)),
    ("CAT", CatBoostClassifier(silent=True, n_estimators=25, random_state=42)),
    # Distance-based and Probability Models
    ("NB", GaussianNB()),
    ("KNN", KNeighborsClassifier(n_neighbors=5)),
    # Neural Network Models
    ("MLP", MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=500, random_state=42)),
    # Ensemble Methods
    (
        "VOTING",
        VotingClassifier(
            estimators=[
                ("rf", RandomForestClassifier(n_estimators=25, random_state=42)),
                (
                    "xgb",
                    XGBClassifier(
                        n_estimators=25, eval_metric="logloss", random_state=42
                    ),
                ),
                (
                    "cat",
                    CatBoostClassifier(silent=True, n_estimators=25, random_state=42),
                ),
            ],
            voting="soft",
        ),
    ),
    (
        "STACKING",
        StackingClassifier(
            estimators=[
                ("rf", RandomForestClassifier(n_estimators=15, random_state=42)),
                (
                    "xgb",
                    XGBClassifier(
                        n_estimators=15, eval_metric="logloss", random_state=42
                    ),
                ),
                ("gbm", GradientBoostingClassifier(n_estimators=15, random_state=42)),
            ],
            final_estimator=LogisticRegression(random_state=42),
            cv=3,
        ),
    ),
]
