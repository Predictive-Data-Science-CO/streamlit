import streamlit as st
# Load libraries
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

st.markdown(""" 
            ## Model Selection
            - Predict iris flower species
            """)

# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)

# descriptions
st.text(dataset.describe())
# class distribution
st.text(dataset.groupby('class').size())

st.text("box and whisker plots")
fig, axes = plt.subplots(2, 2, figsize=(5, 3))
dataset.plot(kind='box', subplots=True, layout=(2, 2), sharex=False, sharey=False, ax=axes)
st.pyplot(fig)

st.text("histograms")
fig2, axes2 = plt.subplots(2, 2, figsize=(5, 3))
dataset.hist(sharex=False, sharey=False, ax=axes2)
st.pyplot(fig2)

st.text("scatter plot matrix")
fig3, ax3 = plt.subplots(figsize=(5, 5))
scatter_matrix(dataset, alpha=0.2, figsize=(5, 5), diagonal='kde', ax=ax3)
st.pyplot(fig3)

st.text("Split-out validation dataset")
array = dataset.to_numpy()
X = array[:,0:4]
y = array[:,4]
X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1)

st.text("Spot Check Algorithms")
models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))

st.text("evaluate each model in turn")
results = []
names = []
for name, model in models:
	kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
	cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
	results.append(cv_results)
	names.append(name)
	st.text('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))

# Display the plot in Streamlit	
st.text("Compare Algorithms")
fig4, ax4 = plt.subplots()
ax4.boxplot(results, labels=names)
ax4.set_title('Algorithm Comparison')

st.pyplot(fig4)

st.text("Make predictions on validation dataset")
model = SVC(gamma='auto')
model.fit(X_train, Y_train)
predictions = model.predict(X_validation)

st.text("Evaluate predictions")
st.text(accuracy_score(Y_validation, predictions))
st.text(confusion_matrix(Y_validation, predictions))
st.text(classification_report(Y_validation, predictions))
   



