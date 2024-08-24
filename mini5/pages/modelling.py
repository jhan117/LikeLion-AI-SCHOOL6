import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from catboost import CatBoostClassifier
from sklearn.model_selection import StratifiedKFold

from sklearn.model_selection import KFold, StratifiedKFold
from sklearn.metrics import log_loss

sns.set_theme()

st.markdown('### 모델링')
max_depth = st.slider('Select a range of < max_depth >',  0, 10, 8)
learning_rate = st.slider(
    'Select a range of < learning_rate >',  0.00, 1.00, 0.04)
n_estimators = st.slider('Select a range of < n_estimators >',  0, 3000, 10)


train_x = pd.read_csv("data/train_x.csv")
train_y = pd.read_csv("data/train_y.csv")
train = pd.read_csv("data/pre_train.csv")
test = pd.read_csv("data/pre_test.csv")

cat_models = {}


def column_index(df, cat_features):
    cols = df.columns.values
    sidx = np.argsort(cols)
    return sidx[np.searchsorted(cols, cat_features, sorter=sidx)]


def cat_kfold(max_depth, learning_rate, random_seed, n_estimators):

    folds = StratifiedKFold(n_splits=10, shuffle=True, random_state=55)
    outcomes = []
    sub = np.zeros((test.shape[0], 3))

    for seed in random_seed:
        for n_fold, (train_index, val_index) in enumerate(folds.split(train_x, train_y)):

            X_train, X_val = train_x.iloc[train_index], train_x.iloc[val_index]
            y_train, y_val = train_y.iloc[train_index], train_y.iloc[val_index]

            cat = CatBoostClassifier(n_estimators=n_estimators, max_depth=max_depth, random_seed=seed,
                                     learning_rate=learning_rate, bootstrap_type='Bernoulli')
            cat.fit(X_train, y_train,
                    eval_set=[(X_train, y_train), (X_val, y_val)],
                    early_stopping_rounds=50, cat_features=cat_features,
                    verbose=0)

            cat_models[n_fold] = cat

            predictions = cat.predict_proba(X_val)
            test_predictions = cat.predict_proba(test)

            logloss = log_loss(y_val, predictions)
            outcomes.append(logloss)

            sub += test_predictions

    mean_outcome = np.mean(outcomes)

    return mean_outcome


def plot_feature_importance(importance, names, model_type):

    feature_importance = np.array(importance)
    feature_names = np.array(names)

    data = {'feature_names': feature_names,
            'feature_importance': feature_importance}
    fi_df = pd.DataFrame(data)

    fi_df.sort_values(by=['feature_importance'], ascending=False, inplace=True)

    fig = plt.figure(figsize=(10, 8))

    sns.barplot(x=fi_df['feature_importance'], y=fi_df['feature_names'])

    plt.title(model_type + ' Feature Importance')
    plt.xlabel('Feature Importance')
    plt.ylabel('Feature Names')

    st.pyplot(fig)


cat_features = [f for f in train_x.columns if train_x[f].dtype == 'object']
cat_features_idx = column_index(train_x, cat_features)

if st.button('모델링 해보기'):
    st.write('n_estimators에 따라 소요 시간이 차이가 납니다. (5 - 15)분만 기다려주세요.')
    mean = cat_kfold(max_depth, learning_rate, [1042], n_estimators)
    st.write("Mean : ", mean)
    with st.expander('feature_importance 시각화'):
        plot_feature_importance(
            cat_models[0].get_feature_importance(), train_x.columns, 'CatBOOST')
