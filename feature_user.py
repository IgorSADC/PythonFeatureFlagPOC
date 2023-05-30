from feature import FeatureClass, some_disabled_feature, some_enabled_feature


def enabled_feature_user(): 
    return some_enabled_feature()

def disabled_feature_user():
    return some_disabled_feature()

def class_user(): 
    instance = FeatureClass()