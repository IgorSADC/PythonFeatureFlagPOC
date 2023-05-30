import sys
from typing import Any



class DisabledFeatureException(Exception):
    pass

def disabled_feature_mock(*args, **kwargs): 
    raise DisabledFeatureException()

class FeatureFlaggedModule: 
    '''
    This class will mock all the disabled features of a module so it returns a DisabledFeatureException in case of usage
    TODO: Allow alternative features/behaviours other than the disabled feature mock
    '''
    def  __init__(self, disabled_features) -> None:  
        module_names = set([f.__module__ for f in disabled_features])
        assert len(module_names) == 1
        module_name = module_names.pop()
        
        self.module = __import__(module_name)
        for disabled_feature in disabled_features:
            setattr(sys.modules[module_name], disabled_feature.__name__, disabled_feature_mock)  
    
