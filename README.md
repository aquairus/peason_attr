# my caffe net for pedestrian attribute

# stack

训练
train_vgg   wpal_net.sh  train_net.py                   wpal_net/train.py    layer
			             change weight&label			snapshot			cfg.NUM_ATTR=9
										               prototxt   			db


测试
test_vgg  test_net.py  wpal_net/test.py



#todo

attribute group

test  ok

recog


# attribute

model0 0~8    9
性别

1～3          
年龄16
年龄30
年龄45

4~6
体型微胖
体型标准
体型偏瘦

7~8              #skip this
角色顾客
角色制服

model1 9~14 6
发型光头
发型长发

头肩黑色头发

头肩戴帽

头肩眼镜

头肩围巾

model2 15~23  9

上衣衬衣
上衣毛衣
上衣马甲
上衣T恤
上衣棉服
上衣夹克
上衣西服
上衣卫衣
上衣短袖

model3 24~29  6

下衣长裤
下衣裙子
下衣短裙
下衣连衣裙
下衣牛仔裤
下衣包腿裤

30～34  5

鞋子类型皮鞋
鞋子类型运动鞋
鞋子类型靴子
鞋子类型布鞋
鞋子类型休闲鞋

model4 35~42    8
附属物双肩包
附属物单肩包
附属物手提包
附属物箱子
附属物塑料袋
附属物纸袋
附属物车
附属物其他


43~50       8
model5
行为打手机
行为交谈
行为聚集
行为抱东西
行为推东西
行为拉拽东西
行为夹带东西
行为拎东西

model6
51~54

正面
背面
面向左侧
面向右侧

55～58
左侧遮挡
右侧遮挡
上部遮挡
下部遮挡

59～62
遮挡类型环境物
遮挡类型附属物
遮挡类型目标
遮挡类型其他

model7
63~74         12

上衣颜色黑
上衣颜色白
上衣颜色灰
上衣颜色红
上衣颜色绿
上衣颜色蓝
上衣颜色黄
上衣颜色棕
上衣颜色紫
上衣颜色粉
上衣颜色橙
上衣颜色混色

model8
75~82     8
下衣颜色黑
下衣颜色白
下衣颜色灰
下衣颜色红
下衣颜色绿
下衣颜色蓝
下衣颜色黄
下衣颜色混色

model9
83~91     9
鞋子颜色黑
鞋子颜色白
鞋子颜色灰
鞋子颜色红
鞋子颜色绿
鞋子颜色蓝
鞋子颜色黄
鞋子颜色棕
鞋子颜色混色
