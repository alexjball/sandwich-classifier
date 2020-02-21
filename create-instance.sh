#!/bin/bash

cd $(dirname $BASH_SOURCE)

[ -e .env ] && . create-instance.env

gcloud compute instances create $INSTANCE_NAME \
        --service-account=$SERVICE_ACCOUNT \
        --zone=$ZONE \
        --image-family=$IMAGE_FAMILY \
        --image-project=deeplearning-platform-release \
        --maintenance-policy=TERMINATE \
        --accelerator="type=$GPU_TYPE,count=1" \
        --machine-type=$INSTANCE_TYPE \
        --boot-disk-size=200GB \
        --metadata="install-nvidia-driver=True"

