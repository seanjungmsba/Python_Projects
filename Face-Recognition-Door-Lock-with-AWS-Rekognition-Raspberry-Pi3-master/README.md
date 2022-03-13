
## Hardware Requirements:

#### 1.Raspberry Pi (Any Version Will Work)

<img src="img/rpi.png">

#### 2.Raspberry Pi Camera (Also USB Webcam Can Be Used)

<img src="img/rpicam.jpg">

#### 3.Push Button

<img src="img/push.png">

#### 4.Electric Door Lock

<img src="img/edl.jpg" height="350">



## Software Dependencies:

*Python2*

*Boto3*
```python
pip install boto3
```

*Python3*

*Boto3*
```python
pip3 install boto3
```
## Step 1 : Create a AWS S3 Bucket in that bucket create folders with the name of the students and add their images atleat 5-10

## Step 2 : Go to IAM and create a new user and set access type to Programmatic access 

## Step 3 : Set permissions for S3 and Rekoognition to full access 

## Step 4 : Complete the process you will get Accesss Key ID & Secret Access Key Copy both and add it in train.py and main.py
*train.py*
```
s3_client = boto3.client(
    's3',
    aws_access_key_id='',# add the aws access key
    aws_secret_access_key=''# add the aws secret access key
    
)

collectionId='' #collection name

rek_client=boto3.client('rekognition',
                            aws_access_key_id='',# add the aws access key
                            aws_secret_access_key='',# add the aws secret access key
                            region_name='',)# add the region here

```
*recognition.py*
```
rek_client=boto3.client('rekognition',
                        aws_access_key_id='',# add the aws access key
                        aws_secret_access_key='',# add the aws secret access key
                        region_name='ap-south-1',)# add the region here
```

## Step 5 : Add the S3 Bucket Name & Folder to save the images on pi
*Both files* 
```
bucket = '' #S3 bucket name
```
*recognition.py*
```
directory = '' #folder name on your raspberry pi
```

## Run
*First Run Train.py File on RPI*
```
python train.py
```

*Run main.py File on RPI ,connect the booton with GPIO 26* 
```
python main.py
```
