# Project2 😼🐶

tf를 사용하여 model을 만들고 그 model을 사용하여 웹 페이지를 만드는 것이 과제였습니다.
tf를 잘 다루지 못하여 이 부분에서는 기본적인 수준만 구현하였습니다. 

강아지상 고양이상을 판별하여 주는 model을 만들었습니다.
약 8000여개의 사진을 사용하였고, sigmoid를 사용하여 0과 1 2가지로 판별해주도록 하였습니다.
0.5초과면 강아지, 0.5이하면 고양이로 설정하였습니다.

각 분류된 내용을 통하여 강아지상 페이지, 고양이상 페이지으로 이동하도록 하였습니다.
JOIN -> LOGIN -> INDEX -> RESULT순으로 진행하겠습니다.


## ✍ stack
<img src="https://img.shields.io/badge/html-E34F26?style=for-the-badge&logo=html5&logoColor=white"> <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white"> <img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white"> <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"> <img src="https://img.shields.io/badge/jquery-0769AD?style=for-the-badge&logo=jquery&logoColor=white"> <img src="https://img.shields.io/badge/mongoDB-008000?style=for-the-badge&logo=mongoDB&logoColor=white"> <img 
src="https://img.shields.io/badge/flask-0769AD?style=for-the-badge&logo=flask&logoColor=white">




## 🌲file tree
![image](https://user-images.githubusercontent.com/79139076/149701119-764f804d-d361-4918-82c9-b5ca06aac838.png)



## JOIN
![image](https://user-images.githubusercontent.com/79139076/149701485-cdb2eada-7bb1-46e5-ae1e-6e057fa94443.png)

회원가입화면 입니다. 이메일, 이름, 비밀번호 세가지만을 이용하였습니다. 이메일과, 비밀번호는 JS에서 정규식을 사용하여 이메일에는 이메일 형식,
비밀번호에는 특수문자, 영문자, 숫자가 들어가도록 만들었습니다. 만약 유효한 값이 들어오지 않으면 아래와 같이 문구를 출력하도록 하였습니다.

![image](https://user-images.githubusercontent.com/79139076/149702182-0f9aeb9e-728c-46bc-acff-eac5c758c24d.png)

![image](https://user-images.githubusercontent.com/79139076/149702308-d3cf7766-4477-4d64-bd04-0e693a934eaa.png)

아이디가 존재하는지 유무를 확인하기 위해서 중복확인 버튼을 만들어주었습니다. 이 버튼을 누르면 ajax통신을 사용하여 email을 서버에 보내고 db에 존재 유무를 확인한 뒤
존재하면 response값으로 fail을 보내어 아래와 같은 문구를,

![image](https://user-images.githubusercontent.com/79139076/149702106-cd1d4be9-7348-4559-a491-054f5680dd33.png)

그렇지 않다면 아래와 문구를 출력합니다.

![image](https://user-images.githubusercontent.com/79139076/149702499-d6ca8b3e-9a6c-4a77-8675-a68eba6e9956.png)

마지막으로 같은 비밀번호가 적혔는지 확인하는 기능을 넣었습니다. 다르다면 아래와 같은 문구를 출력합니다.

![image](https://user-images.githubusercontent.com/79139076/149702689-18123e4e-63eb-4813-b508-3e8e253b96f0.png)

이 모든 것을 잘 통과하면 회원가입 버튼을 누르면 이 정보들을 가져가서 db에 저장합니다. 비밀번호 같은 경우에는 hash값을 사용하여
안전하게 보관하도록 하였습니다. 그리고 /login 화면으로 redirect하는 것 까지 설정해주었습니다.

## LOGIN
![image](https://user-images.githubusercontent.com/79139076/149702957-fa7d925f-4a68-4b51-be75-e2b4ad182112.png)

로그인 화면입니다. 방금 작성한 아이디를 통해서 로그인할 수 있고, OAUTH를 통해서 소셜로그인 하는 방법까지 구현해보았습니다.
github와 kakaotalk 2가지를 만들었습니다. 이 버튼을 누르면 정보를 sns상에 등록되어있는 정보를 바탕으로 회원가입을 자동으로 진행시키고 로그인까지 되도록 하였습니디.
만약 아이디와 비밀번호가 db상의 정보와 일치하지 않는다면 아래와 같은 문구를 출력하도록 하였습니다. 


![image](https://user-images.githubusercontent.com/79139076/149703991-6f32032d-b315-49d0-ab71-90958e4989ef.png)

![image](https://user-images.githubusercontent.com/79139076/149703402-7ffa1022-fb53-4f9c-883f-93760c1c159d.png)

정보가 잘 된다면 로그인을 시킵니다. 로그인을 시키면 서버가 기억할 수 있도록 토큰을 발행해줍니다.(jwt)
여기서 payload에는 email정보를 담아두어 이를 통해 user의 정보를 받아올 수 있습니다. 

로그인을 성공하면 url '/'에 접근할 수 있습니다. '/'에는 index.html을 렌더링합니다.
앞서 나올 /cat , /dog , / 등의 url에는 로그인이 되어있는 상태일 때만 들어갈 수 있도록 하였습니다.
반대로 /login, /join등의 url에는 로그인이 되어있지 않은 상태일 때만 들어갈 수 있도록 하였습니다.
decorater를 통해서 미들웨어를 구현해주었습니다.

## INDEX
로그인을 하면 아래와 같은 화면이 출력이 됩니다.

![image](https://user-images.githubusercontent.com/79139076/149703684-21b8200a-e6a8-482e-8e5c-70fba95d0e03.png)

사진 업로드 박스를 클릭하거나, 파일을 가져다 집어 넣으면 사진이 화면에 나옵니다. 

![image](https://user-images.githubusercontent.com/79139076/149704244-e1a7012d-590b-4d90-81ed-098f17a6bce8.png)

만약 웹캠으로 찍은 사진을 사용하고 싶다면 위의 카메라 전환 버튼을 누르면 됩니다.
누르면 '카메라 전환'이 사진 촬영으로 바뀌고, 사진 촬영을 누르면 아래와 같이 사진이 canvas에 그려집니다.
그리고 다시 촬영하고 싶다면 위의 '재촬영'버튼을 눌러주면 다시 웹캠이 나옵니다.
canvas에 그려진 그림을 dataUrl을 통해 base64로 인코딩을 하였고 이를 다시 atob를 사용하여 디코딩한 뒤
unit8array에 할당하여 블롭을 통해 서버로 보내도록 하였습니다.

![image](https://user-images.githubusercontent.com/79139076/149704493-1ed867dc-9eb2-4950-b516-699703f7aaaa.png)

다시 돌아와서 강아지 사진을 넣고 버튼을 클릭하면

![image](https://user-images.githubusercontent.com/79139076/149704244-e1a7012d-590b-4d90-81ed-098f17a6bce8.png)

/dog으로 이동시켜 아래와 같은 페이지를 출력하도록 합니다.

![image](https://user-images.githubusercontent.com/79139076/149705271-a3b05d2c-68a1-4200-95ff-5f676a893f58.png)

캡쳐에는 나오지 않았지만 두번 째 부분에는 iframe을 사용하여 youtube에서 재미난 영상을 가져와 넣었습니다.
아래의 연예인 사진에는 jquery를 사용한 slide를 구현하였습니다. settimeout을 사용하여 자동으로 사진이 넘어가도록 하였고,
화살표 버튼을 누르거나, 아래의 동그란 버튼을 누르면 해당 페이지로 이동하도록 하였고, 마우스를 올리면 사진이 넘어가지 않도록 하였습니다.
아래의 어떤 강아지 일까이 이부분역시 iframe을 통해 다른 사이트의 내용을 가져와 자신의 성격은 어떤 강아지에 해당하는 것인가를 보여주는 것입니다.
제일 아래의 강아지 버튼을 클릭하면 강아지상 연예인 월드컵 페이지로 이동하도록 하였습니다. 
반대로 고양이 사진을 넣으면 

/cat으로 이동하여 아래와 같은 화면을 보여줍니다.

![image](https://user-images.githubusercontent.com/79139076/149705845-29093421-98bb-4ee4-a1a6-90350ec992a7.png)

/dog의 사진과는 다르게 연예인의 이름을 클릭하면 그 연예인이 화면에 나오도록 구현하였습니다.

그리고 방명록 기능도 만들었습니다. 
글을 적으면 ajax를 통해 db에 저장이 되고 템플릿을 렌더링할 때 정보를 같이 보내줍니다.
따라서 그 정보를 for문이 돌면서 html을 생성해 나가는 방식을 사용하였습니다.

닉네임 옆에 무슨 상인지 적혀있는 것을 확인하실 수 있는데,
index에서 사진을 넣고 tf가 분석을 할 때 분석한 결과에 따라 db에 고양이상, 강아지상의 정보를 user에 담아주는 기능을 만들었습니다.
따라서 자동으로 자신이 글을 적으면 닉네임 옆에 무슨 상인지 표시해주는 기능을 만들었습니다.

맨 아래 역시 사진에는 나오지 않았지만, 자신이 고양이 상이라면 그 중에 어떤 고양이인지 확인할 수 있는 사이트를
iframe을 통해 가져와 실시간으로 확인할 수 있도록 하였습니다.



