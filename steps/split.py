from pandas import DataFrame

def split_fn(train_df: DataFrame, validation_df: DataFrame, test_df: DataFrame) -> (DataFrame, DataFrame, DataFrame):
    """
    Perform additional processing on the split datasets.
    """

    return (train_df, validation_df, test_df)
