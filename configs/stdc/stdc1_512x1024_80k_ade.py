_base_ = [
    '../_base_/models/stdc.py', '../_base_/datasets/ade20k.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_80k.py'
]

checkpoint = 'https://download.openmmlab.com/mmsegmentation/v0.5/pretrain/stdc/stdc2_20220308-7dbd9127.pth'  # noqa

model = dict(
    backbone=dict(
        backbone_cfg=dict(
            init_cfg=dict(type='Pretrained', checkpoint=checkpoint))),
    decode_head=dict(num_classes=150))

lr_config = dict(warmup='linear', warmup_iters=1000)
data = dict(
    samples_per_gpu=12,
    workers_per_gpu=4,
)
