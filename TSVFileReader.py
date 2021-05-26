#* 已知受体找配体


REQUIRED_KEY = [0, 1, 9, 10, 37, 38, 41, 42, 46, 47]
required = ['BindingDB Reactant_set_id', 'Ligand SMILES', 'IC50 (nM)', 'Kd (nM)', 'BindingDB Target Chain  Sequence', 'PDB ID(s) of Target Chain', 'UniProt (SwissProt) Primary ID of Target Chain', 'UniProt (SwissProt) Secondary ID(s) of Target Chain', 'UniProt (TrEMBL) Primary ID of Target Chain', 'UniProt (TrEMBL) Secondary ID(s) of Target Chain']
#REQUIRED_KEY = [0, 1]

#required = ['BindingDB Reactant_set_id', 'Ligand SMILES']


def comma2hyphen(s: str) -> str:
    if ',' in s:
        temp = s.split(',')
        return "-".join(temp)
    else:
        return s


def main(N: int, readFilePath: str, writeFilePath: str) -> None:
    """

    :param N: 51180568
    :param filepath: 写入文件的地址
    :return: 无返回值，写入文件
    """
    try:
        cnt = 0
        # N = 51180568
        with open(readFilePath, 'r', encoding='gbk') as fileObject:
            contentTitle = fileObject.readline().split('\t')
            for j in range(N):
                content = fileObject.readline().split('\t')
                for i in range(len(contentTitle)):
                    if i < len(content):
                        if content[i] != '':
                            line = []

                            for index in REQUIRED_KEY:
                                content[index] = comma2hyphen(content[index])
                                line.append(content[index])

                            print(line)
                            with open(writeFilePath, 'a') as writeFileObject:
                                for k in range(len(line)):
                                    if line[k].strip() == '':
                                        if k == len(line) - 1:
                                            writeFileObject.write('null')
                                        else:
                                            writeFileObject.write('null,')
                                    else:
                                        if k == len(line) - 1:
                                            writeFileObject.write(line[k].strip())
                                        else:
                                            writeFileObject.write(line[k].strip() + ",")
                                writeFileObject.write('\n')
                            writeFileObject.close()
    except Exception as errorMsg:
        print(errorMsg)
    finally:
        fileObject.close()


if __name__ == '__main__':
    main(1, 'BindingDB_All.tsv', 'data1.csv')
    #main(51180568, 'purchase.tsv', 'data2.csv')
