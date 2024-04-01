# This file was generated by liblab | https://liblab.com/

from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.upload_dataset_payload import UploadDatasetPayload
from ..models.new_dataset_response import NewDatasetResponse
from ..models.new_dataset_payload import NewDatasetPayload
from ..models.dataset_view_response import DatasetViewResponse
from ..models.dataset_list_response import DatasetListResponse
from ..models.add_data_payload import AddDataPayload


class DatasetService(BaseService):

    @cast_models
    def add_dataset_data(self, request_body: AddDataPayload, dataset_id: str):
        """Inserts data into a dataset

        :param request_body: The request body.
        :type request_body: AddDataPayload
        :param dataset_id: The unique identifier of the dataset.
        :type dataset_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(AddDataPayload).validate(request_body)
        Validator(str).validate(dataset_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/api/dataset/{{datasetId}}/addData",
                self.get_default_headers(),
            )
            .add_path("datasetId", dataset_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return response

    @cast_models
    def get_dataset_data(self, dataset_id: str) -> DatasetViewResponse:
        """Retrieve the details of a specific dataset by its Id.

        :param dataset_id: The unique identifier of the dataset.
        :type dataset_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successfully retrieved the dataset details.
        :rtype: DatasetViewResponse
        """

        Validator(str).validate(dataset_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/api/dataset/{{datasetId}}", self.get_default_headers()
            )
            .add_path("datasetId", dataset_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return DatasetViewResponse._unmap(response)

    @cast_models
    def list_datasets(self) -> List[DatasetListResponse]:
        """Retrieves a list of datasets and their total row counts

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Dataset retrieved
        :rtype: List[DatasetListResponse]
        """

        serialized_request = (
            Serializer(f"{self.base_url}/api/dataset/list", self.get_default_headers())
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return [DatasetListResponse._unmap(item) for item in response]

    @cast_models
    def initialize_dataset(self, request_body: NewDatasetPayload) -> NewDatasetResponse:
        """Initializes a new dataset.

        :param request_body: The request body.
        :type request_body: NewDatasetPayload
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successfully created a new dataset.
        :rtype: NewDatasetResponse
        """

        Validator(NewDatasetPayload).validate(request_body)

        serialized_request = (
            Serializer(f"{self.base_url}/api/dataset/new", self.get_default_headers())
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return NewDatasetResponse._unmap(response)

    @cast_models
    def upload_dataset(self, request_body: dict):
        """Uploads a dataset file and its associated data

        :param request_body: The request body.
        :type request_body: dict
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(dict).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url}/api/dataset/upload", self.get_default_headers()
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "multipart/form-data")
        )

        response = self.send_request(serialized_request)

        return response
