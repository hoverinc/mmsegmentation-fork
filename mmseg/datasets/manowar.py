# Copyright (c) OpenMMLab. All rights reserved.
from .builder import DATASETS
from .custom import CustomDataset


@DATASETS.register_module()
class ManowarDataset(CustomDataset):
    CLASSES = ('wall', 'floor', 'cabinet', 'object', 'door', 'window', 'ceiling')

    PALETTE = [[174, 199, 232], [152, 223, 138], [31, 119, 180], [219, 219, 141],
               [214, 39, 40], [247, 182, 210], [78, 71, 183]]

    def __init__(self,
                 img_suffix='.jpg',
                 seg_map_suffix='.png',
                 ignore_index=255,
                 **kwargs):
        super(ManowarDataset, self).__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, ignore_index=ignore_index, **kwargs)