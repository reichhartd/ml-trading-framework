from catboost import CatBoostClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.ensemble import (
    GradientBoostingClassifier,
    RandomForestClassifier,
    AdaBoostClassifier,
)
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression


selected_models = [
    ("LDA", LinearDiscriminantAnalysis()),
    ("LOG", LogisticRegression(max_iter=1000, random_state=42)),
    ("NB", GaussianNB()),
    ("KNN", KNeighborsClassifier(n_neighbors=5)),
    ("TREE", DecisionTreeClassifier(random_state=42)),
    ("RF", RandomForestClassifier(n_estimators=25, random_state=42)),
    ("ADA", AdaBoostClassifier(random_state=42)),
    ("GBM", GradientBoostingClassifier(n_estimators=25, random_state=42)),
    ("XGB", XGBClassifier(n_estimators=25, eval_metric="logloss", random_state=42)),
    ("CAT", CatBoostClassifier(silent=True, n_estimators=25, random_state=42)),
]
