import pandas as pd

def preprocess(radiant_heroes,dire_heroes):
    # initialize output value
    data_preprocessed = pd.DataFrame()

    # columns order used to train MLP
    heroes_id = ['1','10','100','101','102','103','104','105','106',
                 '107','108','109','11','110','111','112','113','114',
                 '119','12','120','121','123','126','128','129','13',
                 '135','14','15','16','17','18','19','2','20','21','22',
                 '23','25','26','27','28','29','3','30','31','32','33',
                 '34','35','36','37','38','39','4','40','41','42','43',
                 '44','45','46','47','48','49','5','50','51','52','53',
                 '54','55','56','57','58','59','6','60','61','62','63',
                 '64','65','66','67','68','69','7','70','71','72','73',
                 '74','75','76','77','78','79','8','80','81','82','83',
                 '84','85','86','87','88','89','9','90','91','92','93',
                 '94','95','96','97','98','99',]

    for id in heroes_id:
        data_preprocessed[id] = 0

    id_1 = radiant_heroes[0]
    id_2 = radiant_heroes[1]
    id_3 = radiant_heroes[2]
    id_4 = radiant_heroes[3]
    id_5 = radiant_heroes[4]
    id_6 = dire_heroes[0]
    id_7 = dire_heroes[1]
    id_8 = dire_heroes[2]
    id_9 = dire_heroes[3]
    id_10 = dire_heroes[4]

    data_preprocessed = data_preprocessed.append({str(id_1) : 1,
                                str(id_2) : 1,
                                str(id_3) : 1,
                                str(id_4) : 1,
                                str(id_5) : 1,
                                str(id_6) : -1,
                                str(id_7) : -1,
                                str(id_8) : -1,
                                str(id_9) : -1,
                                str(id_10) : -1} ,
                                ignore_index=True)

    data_preprocessed = data_preprocessed.fillna(0)
    data_preprocessed = data_preprocessed.astype(int)

    return data_preprocessed
