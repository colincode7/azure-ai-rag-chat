from .builtin_metrics import BuiltinCoherenceMetric, BuiltinGroundednessMetric, BuiltinRelevanceMetric
from .code_metrics import AnswerLengthMetric, HasCitationMetric, LatencyMetric
from .prompt_metrics import CoherenceMetric, DontKnownessMetric, GroundednessMetric, RelevanceMetric

metrics = [
    BuiltinCoherenceMetric,
    BuiltinRelevanceMetric,
    BuiltinGroundednessMetric,
    CoherenceMetric,
    RelevanceMetric,
    GroundednessMetric,
    DontKnownessMetric,
    LatencyMetric,
    AnswerLengthMetric,
    HasCitationMetric,
]

metrics_by_name = {metric.METRIC_NAME: metric for metric in metrics}
