from pathlib import Path
import os
import pandas as pd

def export_large_id_json(df, saveloc):
    """
    Export the dataframe containing all of the nutrition ID information into one JSON file

    Keyword Arguments:
    df -- Pandas dataframe containing columns for ID, name, and units
    saveloc -- location to save JSON file to
    """

    df.to_json(saveloc, orient="records")


def export_individual_json(df, savedir):
    """
    Export the dataframe containing all of the nutrition ID information into individual JSON files for each nutrient ID

    Keyword Arguments:
    df -- Pandas dataframe containing columns for ID, name, and units
    saveloc -- location to save JSON file to
    """
    trim_df_noindex = df.drop(columns="id")

    for i in df.index:
        trim_df_noindex.loc[i].to_json(Path(savedir, "{}.json".format(df.loc[i]["id"])))


def main():
    food_nutrient_path = Path("fooddata/food_nutrient.csv")
    nutrient_path = Path("fooddata/nutrient.csv")

    ids_used = set()
    # ids_used = set(int(x) for x in ['1056', '1175', '1304', '1032', '1009', '1121', '2069', '1041', '1110', '1310', '1062', '1221', '1213', '1410', '1303', '1408', '1340', '1341', '1183', '2067', '1095', '2065', '1233', '1165', '2058', '1218', '1314', '1186', '1112', '2005', '1212', '1050', '2010', '1261', '2026', '1194', '1078', '1127', '1043', '1190', '1307', '2063', '1195', '1162', '1325', '2017', '1269', '2006', '2013', '1119', '1266', '2021', '1246', '2062', '1196', '2029', '1129', '1270', '1010', '1159', '1236', '1219', '1011', '1198', '1406', '1089', '1005', '1158', '1311', '2028', '1412', '1301', '1117', '1260', '1044', '1170', '1368', '1313', '1098', '1214', '1305', '2032', '1104', '2057', '1403', '1084', '2000', '1131', '1299', '1130', '1184', '1161', '1259', '1004', '1178', '1008', '2003', '1024', '1126', '1007', '1088', '1057', '1289', '1329', '1090', '1235', '1323', '1166', '2023', '2038', '1300', '2048', '1051', '1106', '2020', '1267', '1146', '1013', '1265', '1275', '2068', '1216', '1120', '1081', '1283', '1293', '1180', '1263', '2019', '1279', '1018', '1039', '1333', '1058', '2025', '1125', '1116', '2047', '1080', '1312', '1330', '1076', '2050', '1149', '1092', '1228', '1292', '1224', '1227', '1105', '1268', '1334', '1253', '2015', '1026', '2059', '1082', '1226', '2014', '2007', '1167', '1262', '1124', '1191', '1075', '1405', '1091', '1068', '1072', '1187', '1286', '1199', '1276', '1188', '2012', '1107', '2049', '1192', '2004', '1137', '1296', '1185', '1321', '1099', '1096', '1038', '1287', '1223', '1217', '1278', '1114', '1118', '1274', '1332', '2051', '1315', '1271', '1414', '1264', '1331', '1306', '1284', '1215', '2016', '1079', '2018', '1316', '1094', '1002', '1063', '1222', '1234', '1225', '2022', '1097', '2033', '2060', '1077', '1177', '1242', '1181', '1220', '1012', '1014', '1113', '1317', '1285', '1128', '1411', '1277', '2052', '1160', '1111', '1102', '1258', '1108', '1272', '2008', '1210', '1086', '1288', '1123', '1298', '1232', '1294', '1103', '1087', '1109', '1280', '1273', '1197', '1281', '2009', '1101', '2061', '1257', '1003', '1085', '1176', '2053', '1211', '1122', '1093', '1335', '1404', '1100', '2024', '1409'])
    with open(food_nutrient_path, "r") as fn_file:
        lines = fn_file.readlines()

        for line in lines[1:]:
            elems = line.replace("\"", "").replace("\n", "").split(",")
            ids_used.add(int(elems[2]))


    df = pd.read_csv(nutrient_path)
    trim_df = df[df["id"].isin(ids_used)]
    trim_df = trim_df.drop(columns=["rank", "nutrient_nbr"])

    if not Path("data").exists():
        os.mkdir("data")
        os.mkdir("data/nutrient")
    
    export_large_id_json(trim_df, Path("data/nutrition_full.json"))
    export_individual_json(trim_df, Path("data/nutrient"))


if __name__ == '__main__':
    main()