# Copyright 2024 TBD Labs Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import TYPE_CHECKING

from latched.model_exporters.base import BaseModelExporter
from latched.model_wrappers.huggingface import HuggingFaceModelWrapper
from latched.utils.logging import setup_logger

logger = setup_logger(__name__)

if TYPE_CHECKING:
    from latched.model_wrappers.base import BaseModelWrapper


class OpenVINOExporter(BaseModelExporter):
    """
    Export the model to OpenVINO.
    """

    @classmethod
    def run(cls, model_wrapper: BaseModelWrapper, **kwargs) -> None:
        if isinstance(model_wrapper, HuggingFaceModelWrapper):
            from optimum.exporters.openvino import export_from_model

            output_name = kwargs.get("output_name", "ov_model")
            model_wrapper.original_model.eval()
            export_from_model(model_wrapper.original_model, output_name, patch_16bit_model=True)

            logger.info(f"Model successfully exported to {output_name}")
        else:
            raise NotImplementedError(f"Unsupported model wrapper: {type(model_wrapper)}")
