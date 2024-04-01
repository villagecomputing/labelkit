# This file was generated by liblab | https://liblab.com/

from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"dataset_name": "datasetName", "ground_truths": "groundTruths"})
class NewDatasetPayload(BaseModel):
    """NewDatasetPayload

    :param dataset_name: dataset_name
    :type dataset_name: str
    :param columns: columns
    :type columns: List[str]
    :param ground_truths: ground_truths, defaults to None
    :type ground_truths: List[str], optional
    """

    def __init__(
        self, dataset_name: str, columns: List[str], ground_truths: List[str] = None
    ):
        self.dataset_name = dataset_name
        self.columns = columns
        if ground_truths is not None:
            self.ground_truths = ground_truths
