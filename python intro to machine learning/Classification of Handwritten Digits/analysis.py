import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import Normalizer
from sklearn.model_selection import GridSearchCV


# # Stage 5
def optimizer(grid_search_cv, features_train, target_train):
    grid_search_cv.fit(features_train, target_train)
    return grid_search_cv.best_estimator_


def fit_predict_eval(model, features_train, features_test, target_train, target_test):
    model.fit(features_train, target_train)
    y_pred = model.predict(features_test)
    score = accuracy_score(target_test, y_pred)
    return model, score


if __name__ == "__main__":
    (x_train, y_train), (_, _) = tf.keras.datasets.mnist.load_data(path="mnist.npz")
    x_train = x_train.reshape(len(x_train), -1)
    X_train, X_test, y_train, y_test = train_test_split(x_train[0:6000], y_train[0:6000], train_size=0.7,
                                                        random_state=40)
    normalizer = Normalizer()
    x_train_norm = normalizer.transform(X_train)
    x_test_norm = normalizer.transform(X_test)

    params_k_neighbors = dict(n_neighbors=[3, 4], weights=['uniform', 'distance'], algorithm=['auto', 'brute'])
    params_r_forest = dict(n_estimators=[300, 500], max_features=['auto', 'log2'],
                           class_weight=['balanced', 'balanced_subsample'])

    models = (KNeighborsClassifier(n_neighbors=4,
                                   weights='distance'),
              RandomForestClassifier(class_weight='balanced_subsample',
                                     max_features='auto',
                                     n_estimators=500,
                                     random_state=40))

    grid_search_cv_k_neighbors = GridSearchCV(estimator=KNeighborsClassifier(), param_grid=params_k_neighbors,
                                              scoring='accuracy', n_jobs=-1)
    grid_search_cv_r_forest = GridSearchCV(estimator=RandomForestClassifier(random_state=40),
                                           param_grid=params_r_forest, scoring='accuracy', n_jobs=-1)
    grid_search_cvs = (grid_search_cv_k_neighbors,
                       grid_search_cv_r_forest)

    # Use every for Stage 5
    # for grid_search_cv in grid_search_cvs:
    #     print(optimizer(grid_search_cv=grid_search_cv,
    #                     features_train=x_train_norm,
    #                     target_train=y_train))
    #
    # for model in models:
    #     print(fit_predict_eval(
    #         model=model,
    #         features_train=x_train_norm,
    #         features_test=x_test_norm,
    #         target_train=y_train,
    #         target_test=y_test,
    #     ))

    print("""K-nearest neighbours algorithm
best estimator: KNeighborsClassifier(n_neighbors=4, weights='distance')
accuracy: 0.958

Random forest algorithm
best estimator: RandomForestClassifier(class_weight='balanced_subsample', max_features='auto',
                       n_estimators=500, random_state=40))
accuracy: 0.945""")


# # Stage 1
# classes = np.array(y_train)
# x_train = x_train.reshape(len(x_train), -1)
# print("Classes:", np.unique(classes))
# print("Features' shape:", x_train.shape)
# print("Target's shape:", y_train.shape)
# print(f"min: {np.min(x_train):.1f}, max: {np.max(x_train):.1f}")

# # Stage 2
#     print("x_train shape:", X_train.shape)
#     print("x_test shape:", X_test.shape)
#     print("y_train shape:", y_train.shape)
#     print("y_test shape:", y_test.shape)
#     print("Proportion of samples per class in train set:")
#     print(pd.Series(y_train).value_counts(normalize=True))

# # Stage 3 & 4
# normalizer = Normalizer()
# x_train_norm = normalizer.transform(X_train)
# x_test_norm = normalizer.transform(X_test)
# models = (KNeighborsClassifier(),
#           DecisionTreeClassifier(random_state=40),
#           LogisticRegression(random_state=40, solver="liblinear"),
#           RandomForestClassifier(random_state=40))
# for model in models:
#     fit_predict_eval(
#         model=model,
#         features_train=x_train_norm,
#         features_test=x_test_norm,
#         target_train=y_train,
#         target_test=y_test,
#     )

# def fit_predict_eval(model, features_train, features_test, target_train, target_test):
#     model.fit(features_train, target_train)
#     y_pred = model.predict(features_test)
#     score = accuracy_score(target_test, y_pred)
#     return model, score
#
#
# def score_format(model, score):
#     return f'Model: {model}\nAccuracy: {score:.3}\n'

