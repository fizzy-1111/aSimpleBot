
## System Overview

- go through 3 module 

## preprocessing module
- prepare input for later use
- brief about input

## Tryon condition module
- take input from the prepocessing module to gen I^c and S^
- S^ is the segmatation of person wearing the cloth
- I^c is the deform of the input cloth to fit the person

## Generator architecture

- this module use GAN framework
- we start with generator architecture
- 3 components 
- Encoder to extract the feature pyramid from each encoder. the extracted features are fed into feature fusion blocks
- Feature Fusion Block to exchange info from extracted features
- Condition Aligning => to handle misalignment

## Encoder

- multiple layer
- Talk about input output
- talk about Cloth encoder extract feature from what
- Pose encoder extract feature from what
- flow path way from Pose, Seg path way from Cloth

## Feature Fusion Block
- Receive the flow path way and seg path way from previous block
- Get the extracted features from the corresponding encoder layer
- Refine each other to estimate the next flow pathway and seg

## Condition aligning
- get the last flowpath way and seg pathway
- From the flowpath way, seg pathway and clothing image, cloth mask => produce the segmentation map
- Use the segmentation map to deform the cloth to fit the person I^c

## Discriminator 

- Operate on multiple scale of the image
- Classify S and S^
- Each downscale image classified by a sub
- the sub produce a prediction map Y^i
- the final is the combination of all prediction map of each downscale img

## Training condition

- let D the dis, G the gen
- ground truth S and segmap S^

## Training condition 2

- cross entroypy loss - classify every pixel
- L1 loss - calculate absolute difference between S^c vs Sc
- VGG loss - calculate percepture difference between ...

## Training condition 3

- Loss TV - enforce smoothness between neighboring pixel
- Using LSGAN for main loss function

## Training condition 3

- the objective on the generator side is the combination of the above loss
- for the dis -> objective using LSGAN


## Try on image

------
# Notes

  
## Introduction 

- phải nói rõ là làm được những gì,  ví dụ chỗ nào thử chỗ nào ko thử
- cái mà làm khác những gì
- Về cái application , phải nó rõ là mấy phương pháp trước thiếu gì, cái mình làm là gì
- Hình vô thưởng vô phạt, không cite nguồn

## Related work
- phần related work thì nên để mô hình kiến trúc của mấy cái mô hình đó
- Thiếu hình

## Implementation

- Làm rõ 1 lần nữa, 1 cách chi tiết hơn là có gì khác
- Lý do tại sao lại nhắm vào module sau để sửa chữa

