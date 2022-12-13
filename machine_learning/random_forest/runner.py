#https://www.analyticsvidhya.com/blog/2021/06/understanding-random-forest/?#
#https://towardsdatascience.com/understanding-random-forest-58381e0602d2
import os


import machine_learning.utils.data_loader
import machine_learning.utils.math
import machine_learning.utils.algorithm_results_plotter
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

relative_path_to_file = '../data/preprocessed_files/rbi/banks_posatm_summary.csv'
test_set_proportion = 0.4
number_of_simulations = 500
random_state = None
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, relative_path_to_file)
headers,X,y = machine_learning.utils.data_loader.get_features_labels(filename)
print(X.shape)
print(y.shape)
print(headers)
randomforest_classifier = RandomForestClassifier(random_state=random_state,n_jobs=-1,max_depth=3,n_estimators=4)

testing_f1_score = []
for i in range(number_of_simulations):
    X_train, X_test, y_train, y_test = machine_learning.utils.data_loader.split_data_to_traintest(X, y, test_size=test_set_proportion, random_state=random_state)
    randomforest_classifier.fit(X_train,y_train)
    y_pred = randomforest_classifier.predict(X_test)
    f1 = machine_learning.utils.math.F1_score(y_test,y_pred)
    testing_f1_score.append(f1)
print(len(testing_f1_score))
machine_learning.utils.algorithm_results_plotter.plot_curve(range(1,number_of_simulations+1),testing_f1_score,include_bar_graph=True)


# optional grid search execution

# params = {
#     'max_depth':[1,2,3],
#     'min_samples_leaf':[1,2,3,4],
#     'n_estimators':[1,2,3]
# }
# grid search model is used for tuning the hyper-parameters and finding the best combination.
# We need to run the same classifier on different hyper-parameters,
# and such a setting has been made easy through the gridsearch instance in sklearn.
# grid_search = GridSearchCV(estimator=randomforest_classifier,param_grid=params,cv=2,n_jobs=-1,verbose=1,scoring='accuracy')
# grid_search.fit(X_train,y_train)
# print(grid_search.best_score_)
# best_estimator = grid_search.best_estimator_
# print(best_estimator)

