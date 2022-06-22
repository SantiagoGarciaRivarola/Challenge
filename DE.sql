INSERT INTO us_sec(name_alias,pass,create_time,status)
VALUES('Rodrigo','123rod',20220615,True),('Tincho','123tin',20220616,True),('Lucas','123luc',20211022,False),('Federico','123fed',20220618,True),('Manuel','123man',20220610,True);

INSERT INTO g_sec(id,name_gs,description_gs)
VALUES('Rodrigo','RGS','High security'),('Tincho','TGS','Medium security'),('Lucas','LGS','Low security'),('Federico','FGS','High security'),('Manuel','MGS','Low security');

INSERT INTO levelacc(idacc,nameacc)
VALUES('Rodrigo','Read'),('Tincho','Write'),('Federico','Administrator'),('Manuel','Owner');
