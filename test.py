import torch
from torchvision import transforms
import webdataset as wds
from itertools import islice

# url = "http://storage.googleapis.com/nvdata-openimages/openimages-train-000000.tar"
# url = f"pipe:curl -L -s {url} || true"
# url = "s3://roshanin-dev/webdataset/tinyimagenet.tar"
# url = f"pipe:aws s3 cp {url} - || true"

url = "s3://mansmane-dev/imagenet_web_dataset/train/imagenet-train-{000000..000554}.tar"
url = f"pipe:aws s3 cp {url} - || true"
dataset = wds.Dataset(url)
for i, sample in enumerate(dataset):
    for key, value in sample.items():
        print(key, repr(value)[:50])
    if i == 5:
        break

# for sample in islice(dataset, 0, 3):
#     for key, value in sample.items():
#         print(key, repr(value)[:50])
#     print()

dataloader = torch.utils.data.DataLoader(dataset, num_workers=1, batch_size=None)
for i in range(3):
    print(next(iter(dataloader)))
# images, targets = next(iter(dataloader))
# images.shape

x = []
for i in range(3):
    # print(next(iter(train_loader)))
    x.append(next(iter(train_loader)))