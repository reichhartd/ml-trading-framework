from catboost import CatBoostClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier


models = [
    ("LDA", LinearDiscriminantAnalysis()),
    ("KNN", KNeighborsClassifier()),
    ("TREE", DecisionTreeClassifier()),
    ("NB", GaussianNB()),
    ("GBM", GradientBoostingClassifier(n_estimators=25)),
    ("XGB", XGBClassifier(n_estimators=25, eval_metric="logloss")),
    ("CAT", CatBoostClassifier(silent=True, n_estimators=25)),
    ("RF", RandomForestClassifier(n_estimators=25)),
]
