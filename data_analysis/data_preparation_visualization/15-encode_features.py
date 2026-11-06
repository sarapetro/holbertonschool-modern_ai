#!/usr/bin/env python3
"""Encode customer churn features for modeling."""

import pandas as pd
from sklearn import preprocessing


def encode_features(df):
    """Return encoded data and fitted target, binary, and tenure encoders."""
    df = df.copy()
    churn_encoder = preprocessing.LabelEncoder()
    df['Churn'] = churn_encoder.fit_transform(df['Churn'])

    binary_columns = [
        'Partner', 'Dependents', 'PaperlessBilling', 'SeniorCitizen'
    ]
    binary_encoder = preprocessing.OrdinalEncoder(
        categories=[['No', 'Yes']]
    )
    for column in binary_columns:
        df[column] = binary_encoder.fit_transform(
            df[[column]]
        ).ravel().astype(int)

    tenure_encoder = preprocessing.OrdinalEncoder()
    df['TenureGroup'] = tenure_encoder.fit_transform(
        df[['TenureGroup']]
    ).ravel().astype(int)

    one_hot_columns = ['Contract', 'PaymentMethod']
    one_hot_encoder = preprocessing.OneHotEncoder(drop='first')
    encoded_values = one_hot_encoder.fit_transform(df[one_hot_columns])
    encoded_columns = pd.DataFrame(
        encoded_values.toarray(),
        columns=one_hot_encoder.get_feature_names_out(one_hot_columns),
        index=df.index
    )
    df = pd.concat(
        [df.drop(columns=one_hot_columns), encoded_columns], axis=1
    )
    return df, churn_encoder, binary_encoder, tenure_encoder
