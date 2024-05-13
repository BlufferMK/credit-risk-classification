# %%
# Import the modules
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# %% [markdown]
# ---

# %% [markdown]
# ## Split the Data into Training and Testing Sets

# %% [markdown]
# ### Step 1: Read the `lending_data.csv` data from the `Resources` folder into a Pandas DataFrame.

# %%
# Read the CSV file from the Resources folder into a Pandas DataFrame
df = pd.read_csv(Path("lending_data.csv"))

# Review the DataFrame
df.tail()

# %% [markdown]
# ### Step 2: Create the labels set (`y`)  from the “loan_status” column, and then create the features (`X`) DataFrame from the remaining columns.

# %%
# Separate the data into labels and features
# Separate the y variable, the labels
y = df["loan_status"]

# Separate the X variable, the features
X = df.drop("loan_status", axis=1)

# %%
# Review the y variable Series
y[:5]

# %%
# Review the X variable DataFrame
X[:5]

# %% [markdown]
# ### Step 3: Split the data into training and testing datasets by using `train_test_split`.

# %%
# Import the train_test_learn module
# from sklearn.model_selection import train_test_split  I put this at the head of the code

# Split the data using train_test_split
# Assign a random_state of 1 to the function
X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=1, stratify=y)

# %% [markdown]
# ---

# %% [markdown]
# ## Create a Logistic Regression Model with the Original Data

# %% [markdown]
# ###  Step 1: Fit a logistic regression model by using the training data (`X_train` and `y_train`).

# %%
# Import the LogisticRegression module from SKLearn
# from sklearn.linear_model import LogisticRegression      I put this at the head of the code

# Instantiate the Logistic Regression model
# Assign a random_state parameter of 1 to the model
classifier  = LogisticRegression(solver= 'lbfgs',random_state=1)

# Fit the model using training data
classifier.fit(X_train, y_train)

# %% [markdown]
# ### Step 2: Save the predictions on the testing data labels by using the testing feature data (`X_test`) and the fitted model.

# %%
# Make a prediction using the testing data
predictions = classifier.predict(X_test)

# %% [markdown]
# ### Step 3: Evaluate the model’s performance by doing the following:
# 
# * Generate a confusion matrix.
# 
# * Print the classification report.

# %%
# Generate a confusion matrix for the model
confusion_matrix(y_test,predictions)

# %%
# Print the classification report for the model
target_names = ["healthy loan","high risk loan"]
print(classification_report(y_test, predictions, target_names=target_names))

# %% [markdown]
# ### Step 4: Answer the following question.

# %% [markdown]
# **Question:** How well does the logistic regression model predict both the `0` (healthy loan) and `1` (high-risk loan) labels?
# 
# **Answer:**The model does a very good job of predicting healthy loans, predicting 99.5% of them correctly.  It does a reasonable job of predicting high-risk loans, predicting 87% of them correctly.  Another way of looking at it is to say that 99.8% of approved loans (predicted to be healthy) are healthy loans, with only 0.2% of approved loans being high risk.  This seems like a very reasonable model to use for predicting health of loans.

# %% [markdown]
# ---


