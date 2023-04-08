name: SQL
run-name: SQL Test
on: [push]
jobs:
  SQL-Test:
    runs-on: ubuntu-latest
    steps:

      - uses: actions/checkout@v2
      - uses: actions/setup-python@v1
      - uses: BSFishy/pip-action@v1
        with:
          packages: |
            coverage
            flask-mysqldb
      - name: Setup Database
        run: |
          sudo /etc/init.d/mysql start
          mysql -e 'CREATE DATABASE test;' -uroot -proot
          mysql -e 'USE test; CREATE TABLE Tag (ID int,tags varchar(255)) ;' -uroot -proot 
          mysql -e 'USE test; insert into Tag(tags,ID) values ("Python",90);' -uroot -proot 
          mysql -e 'USE test; insert into Tag(tags,ID) values ("C++",91);' -uroot -proot 
          mysql -e 'USE test; insert into Tag(tags,ID) values ("JavaScript",92);' -uroot -proot 
          mysql -e 'USE test; insert into Tag(tags,ID) values ("MySQL",93);' -uroot -proot 
          mysql -e 'USE test; insert into Tag(tags,ID) values ("Java",94);' -uroot -proot 
          mysql -e 'USE test; CREATE TABLE Answer (ID int PRIMARY KEY auto_increment, Owner_User_Id int ,Creation_Date datetime default NOW(),Parent_ID int,Score int default 0,Body TEXT) ;' -uroot -proot
          mysql -e 'USE test; insert into Answer(ID,Owner_user_Id,Creation_Date,Parent_Id,Score,Body) values (92,61,"2008-08-01 14:45:37",90,13,"Its Answer is too long therefore i am reducing its size");' -uroot -proot
          mysql -e 'USE test; insert into Answer(ID,Owner_user_Id,Creation_Date,Parent_Id,Score,Body) values (93,62,"2008-08-01 15:45:37",90,14,"Its Answer is too long therefore i am reducing its size to very small answer");' -uroot -proot
          mysql -e 'USE test; insert into Answer(ID,Owner_user_Id,Creation_Date,Parent_Id,Score,Body) values (94,61,"2008-08-01 16:45:37",91,13,"Its Answer is not too long sill im reducing its size");' -uroot -proot
          mysql -e 'USE test; insert into Answer(ID,Owner_user_Id,Creation_Date,Parent_Id,Score,Body) values (96,63,"2008-07-01 14:59:36",91,13,"Its Answer is very small still i am..");' -uroot -proot
          mysql -e 'USE test; insert into Answer(ID,Owner_user_Id,Creation_Date,Parent_Id,Score,Body) values (95,66,"2009-08-01 14:45:37",92,13,"Its long therefore i am reducing its size");' -uroot -proot
          mysql -e 'USE test; CREATE TABLE Question(ID int PRIMARY KEY auto_increment,Owner_User_Id int,Creation_Date datetime default NOW(),Score int default 0,title varchar(255),Body text);' -uroot -proot
          mysql -e 'USE test; insert into Question(ID,Owner_User_Id,Creation_Date,Score,title,Body) values(90,66,"2007-08-01 14:45:37",98,"SQL","Its body is about SQL")' -uroot -proot
          mysql -e 'USE test; insert into Question(ID,Owner_User_Id,Creation_Date,Score,title,Body) values(91,62,"2007-08-02 15:45:37",99,"Python","Its body is not about SQL but about python")' -uroot -proot
          mysql -e 'USE test; insert into Question(ID,Owner_User_Id,Creation_Date,Score,title,Body) values(92,61,"2007-04-01 09:45:37",79,"C++","Its body is about C++ and C# also")' -uroot -proot
          mysql -e 'USE test; insert into Question(ID,Owner_User_Id,Creation_Date,Score,title,Body) values(93,64,"2009-08-01 14:46:37",87,"Database in SQL","I have to write something about it as")' -uroot -proot
          mysql -e 'USE test; insert into Question(ID,Owner_User_Id,Creation_Date,Score,title,Body) values(94,63,"2010-08-01 15:45:37",123,"Double is too muvh ","Is body necessary for all part is")' -uroot -proot
          mysql -e 'USE test; CREATE TABLE User(ID int PRIMARY KEY auto_increment, Display_Name text, About_me text,Creation_Date datetime default NOW(),Last_access_time datetime default NOW(), Location text, reputation int default 0, up_votes int default 0, down_votes int default 0, profile_image_url varchar(1000) default "https://static.vecteezy.com/system/resources/previews/005/544/718/original/profile-icon-design-free-vector.jpg" , website_url text,password   varchar(1000) default "1234");' -uroot -proot
          mysql -e 'USE test; insert into User(ID,Display_Name,About_me,Creation_Date,Location,reputation,up_votes,down_votes,website_url) values (61,"Satyam","Something needs to be written there","2006-08-01 15:45:37","India",378,893,498,"www.gooogle.com");' -uroot -proot 
          mysql -e 'USE test; insert into User(ID,Display_Name,About_me,Creation_Date,Location,reputation,up_votes,down_votes,website_url) values (62,"Raghav","needs to be read there","2006-09-03 15:45:47","India,Delhi",37,8393,48,"www.facebook.com");' -uroot -proot 
          mysql -e 'USE test; insert into User(ID,Display_Name,About_me,Creation_Date,Location,reputation,up_votes,down_votes,website_url) values (63,"Jai","omthig ns o be riten here so write","2004-07-01 15:45:47","India,Hauz jhaus",378,83,8,"www.yahoo.com");' -uroot -proot 
          mysql -e 'USE test; insert into User(ID,Display_Name,About_me,Creation_Date,Location,reputation,up_votes,down_votes,website_url) values (64,"Zaurez","Soing needs to be wrn thee","2005-08-02 15:43:37","India,Mumbai",3,83,48,"www.ggle.com");' -uroot -proot 
          mysql -e 'USE test; insert into User(ID,Display_Name,About_me,Creation_Date,Location,reputation,up_votes,down_votes,website_url) values (66,"Satyam","Something needs to be written there","2006-08-01 15:45:37","India",378,893,498,"www.gooogle.com");' -uroot -proot 

      - name: Clean temp directory
        run: |
          python -m coverage run -m unittest
          python -m coverage report
        working-directory: ./