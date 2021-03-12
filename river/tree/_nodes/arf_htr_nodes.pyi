from .arf_htc_nodes import BaseRandomLearningNode as BaseRandomLearningNode
from .htr_nodes import LearningNodeAdaptive as LearningNodeAdaptive, LearningNodeMean as LearningNodeMean, LearningNodeModel as LearningNodeModel
from typing import Any

class RandomLearningNodeMean(BaseRandomLearningNode, LearningNodeMean):
    def __init__(self, stats: Any, depth: Any, attr_obs: Any, attr_obs_params: Any, max_features: Any, seed: Any) -> None: ...

class RandomLearningNodeModel(BaseRandomLearningNode, LearningNodeModel):
    def __init__(self, stats: Any, depth: Any, attr_obs: Any, attr_obs_params: Any, max_features: Any, seed: Any, leaf_model: Any) -> None: ...

class RandomLearningNodeAdaptive(BaseRandomLearningNode, LearningNodeAdaptive):
    def __init__(self, stats: Any, depth: Any, attr_obs: Any, attr_obs_params: Any, max_features: Any, seed: Any, leaf_model: Any) -> None: ...
