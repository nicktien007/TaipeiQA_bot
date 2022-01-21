# 台北QA Line bot

[投影片](https://docs.google.com/presentation/d/1hdI8dChMhUInzIPMmNeYSKldH5WrfXYl1RhpqKZeyM8/edit?usp=sharing)

[Dataset Link](https://github.com/p208p2002/taipei-QA-BERT/blob/master/Taipei_QA_new.txt)

[Train Model Colab Link](https://colab.research.google.com/drive/1PvUlWD5Evs1VlNVLh0M2XEKNvSNvgRzS?usp=sharing)


## introduction

該LINE BOT 調用finetune的 TaipeiQA Model API 進行 QA問答
https://huggingface.co/nicktien/TaipeiQA_v1



> 問一個問題，告訴你應該去哪個單位處理這些問題

![img](https://raw.githubusercontent.com/nicktien007/Nick.IMG_01/main/img/75SK5bfffPDQvzbEg05h2iF0UixCHNfoCHzPDInSccjsSOzyzkLxHXDSXLKhnGgkImrkwnrzt_HJaEb19g7bw5d-aT8ovA3cURiBjNmzC_CmFKZjrs-zc6QFZspIlx2Ayn_Zz5NujorJ.png)

Q：1張卡片可以借用幾台YouBike？

A：臺北市政府交通局



![image-20220107010822392](https://raw.githubusercontent.com/nicktien007/Nick.IMG_01/main/img/image-20220107010822392.png)





## Steps

### Step #1 Train Model

[Dataset](https://github.com/p208p2002/taipei-QA-BERT/blob/master/Taipei_QA_new.txt)

[Train Model Colab 連結](https://colab.research.google.com/drive/1PvUlWD5Evs1VlNVLh0M2XEKNvSNvgRzS?usp=sharing)



### Step #2 Model 上傳 Hugging face

https://huggingface.co/nicktien/TaipeiQA_v1

![image-20220118220921338](https://raw.githubusercontent.com/nicktien007/Nick.IMG_01/main/img/image-20220118220921338.png)



### Step #3 Git clone TaipeiQA_bot

```shell
git clone https://github.com/nicktien007/TaipeiQA_bot.git
```



佈署到[Heroku](https://dashboard.heroku.com/apps/taipeiqa-bot)

![image-20220118220935791](https://raw.githubusercontent.com/nicktien007/Nick.IMG_01/main/img/image-20220118220935791.png)

### Step #4 申請Line BOT

[LINE DEVELOPER PAGE](https://developers.line.biz/en/)



![image-20220118221042448](https://raw.githubusercontent.com/nicktien007/Nick.IMG_01/main/img/image-20220118221042448.png)

## Video

[![](https://raw.githubusercontent.com/nicktien007/Nick.IMG_01/main/img/image-20220118215200605.png)](https://www.youtube.com/watch?v=Jq16t74LAwc "")

## ref

- https://bit.ly/3ePFaA7

- https://bit.ly/3pVpGkt
- https://bit.ly/335kjq8
- https://bit.ly/3zrCZfA
