import pytest

from ff_module import DisabledFeatureException, FeatureFlaggedModule

from feature import FeatureClass, some_disabled_feature

disabled_features = [
    some_disabled_feature,
    FeatureClass
]

FeatureFlaggedModule(disabled_features)


def test_can_disable_a_function_feature(): 
    from feature_user import disabled_feature_user, enabled_feature_user
    
    #Assert an enabled function can be used
    enabled_feature_user()
    
    #Assert a disabled function cannot be used
    with pytest.raises(DisabledFeatureException):
        disabled_feature_user()
        
def test_can_disable_high_order_function(): pass
        
def test_can_disable_a_class(): 
    from feature_user import class_user

    #Assert a disabled class cannot be instantiated 
    with pytest.raises(DisabledFeatureException):
        class_user()
    
    
def test_can_disable_child_class(): pass

def test_can_disable_interface() : pass