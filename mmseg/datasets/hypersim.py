# Copyright (c) OpenMMLab. All rights reserved.
from .builder import DATASETS
from .custom import CustomDataset


@DATASETS.register_module()
class HypersimDataset(CustomDataset):
    """Hypersim Semantic dataset.
    0: [174, 199, 232], # wall
    1: [152, 223, 138], # floor
    2: [31, 119, 180], # cabinet
    3: [219, 219, 141], # object
    4: [214, 39, 40], # door
    5: [247, 182, 210], # window
    6: [78, 71, 183], # ceiling
    Invalid / noise index as 255.
    """

    CLASSES = ('wall', 'floor', 'cabinet', 'object', 'door', 'window', 'ceiling')

    PALETTE = [[174, 199, 232], [152, 223, 138], [31, 119, 180], [219, 219, 141],
               [214, 39, 40], [247, 182, 210], [78, 71, 183]]

    def __init__(self,
                 img_suffix='.jpg',
                 seg_map_suffix='_gt.png',
                 ignore_index=255,
                 **kwargs):
        super(HypersimDataset, self).__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, ignore_index=ignore_index, **kwargs)