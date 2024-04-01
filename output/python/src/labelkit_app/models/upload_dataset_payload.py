# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap(
    {
        "dataset_title": "datasetTitle",
        "ground_truth_column_index": "groundTruthColumnIndex",
        "blank_column_title": "blankColumnTitle",
    }
)
class DatasetData(BaseModel):
    """Object containing the dataset title, ground truth column index, and an optional blank column title

    :param dataset_title: The title of the dataset
    :type dataset_title: str
    :param ground_truth_column_index: Index of the ground truth column
    :type ground_truth_column_index: int
    :param blank_column_title: Title for an optional blank column, defaults to None
    :type blank_column_title: str, optional
    """

    def __init__(
        self,
        dataset_title: str,
        ground_truth_column_index: int,
        blank_column_title: str = None,
    ):
        self.dataset_title = dataset_title
        self.ground_truth_column_index = ground_truth_column_index
        if blank_column_title is not None:
            self.blank_column_title = blank_column_title


@JsonMap({"dataset_data": "datasetData"})
class UploadDatasetPayload(BaseModel):
    """UploadDatasetPayload

    :param dataset_data: Object containing the dataset title, ground truth column index, and an optional blank column title
    :type dataset_data: DatasetData
    :param file: The binary content of the dataset file
    :type file: str
    """

    def __init__(self, dataset_data: DatasetData, file: str):
        self.dataset_data = self._define_object(dataset_data, DatasetData)
        self.file = file
