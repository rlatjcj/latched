# Copyright 2024 TBD Labs Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import os
import torch
import torch.nn as nn
from latched.utils.logging import setup_logger

logger = setup_logger(__name__)


def get_size_of_model(model: nn.Module, label: str = ""):
    """Print the size of the model in MB or GB.

    Args:
        model (nn.Module): The model to get the size of.
        label (str): The label of the model. Defaults to "".
    """
    model.eval()
    torch.save(model.state_dict(), "temp.p")
    size = os.path.getsize("temp.p")
    logger.info(f"model: {label} \t Size (KB): {size / 1e3}")
    os.remove("temp.p")
    return size
